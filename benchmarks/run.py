"""Run the registered mock cases or check a supplied observer trace."""

import argparse
import json
from pathlib import Path
import sys

from benchmarks.evaluate import TraceError, evaluate
from benchmarks.mock_trace import CASE_IDS, make_trace


ROOT = Path(__file__).resolve().parent


def read_json(path):
    def reject_constant(value):
        raise TraceError(f"Non-finite JSON constant: {value}")
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise TraceError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(Path(path).read_text(), parse_constant=reject_constant,
                      object_pairs_hook=unique_keys)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Save reproducible traces and receipts")
    parser.add_argument("--trace", type=Path, help="Check one externally supplied mock observer trace")
    args = parser.parse_args(argv)
    try:
        policy = read_json(ROOT / "policy.json")
        if args.trace:
            receipt = evaluate(read_json(args.trace), policy)
            print(json.dumps(receipt, indent=2, allow_nan=False))
            return {"PASS": 0, "FAIL": 1, "UNRESOLVED": 2}[receipt["verdict"]]
        expected = read_json(ROOT / "cases.json")
        if set(expected) != set(CASE_IDS):
            raise TraceError("Preregistered control inventory changed")
        results = []
        for case in CASE_IDS:
            trace = make_trace(case, policy)
            receipt = evaluate(trace, policy)
            result = {"case": case, "expected": expected[case], "actual": receipt["verdict"],
                      "trace_sha256": receipt["trace_sha256"]}
            results.append(result)
            if args.output:
                args.output.mkdir(parents=True, exist_ok=True)
                for suffix, data in (("trace", trace), ("receipt", receipt)):
                    (args.output / f"{case}.{suffix}.json").write_text(
                        json.dumps(data, indent=2, allow_nan=False) + "\n")
            print(f"{case}: {receipt['verdict']} (expected {expected[case]})")
        passed = all(r["actual"] == r["expected"] for r in results)
        summary = {"program": "PEAICE-SIUS-001", "benchmark_id": "GIUS-BENCH-001",
                   "scope": "synthetic mock-trace calibration", "operational_validity": "OPEN",
                   "policy_sha256": receipt["policy_sha256"],
                   "cases": results, "calibration_passed": passed}
        if args.output:
            (args.output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
        return 0 if passed else 1
    except (TraceError, ValueError, OSError, KeyError, TypeError) as error:
        print(f"Invalid or unavailable evidence: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
