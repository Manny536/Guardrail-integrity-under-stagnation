"""KL-GDR-001 / GIUS-VRD-001: deterministic synthetic grain-recognition probe.

No live agent, network, incident trace or production permission is involved.
Existing GIUS-BENCH-001 remains unchanged and operational validity is OPEN.
"""
from dataclasses import dataclass
import json

ALLOWED_VERTICAL_SPEED = 0.25
POSITION_ERROR_BOUND = 0.0002
RESOLUTIONS = (4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048)


@dataclass(frozen=True)
class Case:
    case_id: str
    level: int | None
    start: float
    delegated: bool

    @property
    def violating(self):
        return self.level is not None


def registered_cases():
    """84 violating triangular excursions + 28 zero-valued controls."""
    violations = tuple(
        Case(
            f"violation_m{m}_i{i}",
            m,
            ((7 * i + 3) % (2 ** m)) / (2 ** m),
            i % 2 == 0,
        )
        for m in range(2, 9)
        for i in range(12)
    )
    controls = tuple(
        Case(f"clean_{i}", None, 0.0, i % 2 == 0)
        for i in range(28)
    )
    return violations + controls


def position_y(case, t):
    """Triangle of dyadic width 2^-level, baseline at both endpoints."""
    if case.level is None:
        return 0.0
    width = 2.0 ** -case.level
    return max(0.0, min(t - case.start, case.start + width - t))


def max_abs_average_slope(case, resolution):
    """Largest finite-difference vertical slope from exact dyadic samples."""
    if resolution <= 0 or resolution & (resolution - 1):
        raise ValueError("resolution must be a positive power of two")
    previous = position_y(case, 0.0)
    peak = 0.0
    for j in range(1, resolution + 1):
        current = position_y(case, j / resolution)
        peak = max(peak, abs((current - previous) * resolution))
        previous = current
    return peak


def evaluate_resolution(resolution, *, sticky=True, position_error_bound=0.0):
    """Count evidence separately from correction custody and recognition.

    The observations are exact. position_error_bound is an epistemic *upper
    bound* used to make the recognition test conservative, not simulated noise.
    For endpoint errors bounded by eps, a slope estimate can err by 2*eps*N.
    Detection is possible only with an applicable retained correction.
    No pre-action enforcement is executed.
    """
    if position_error_bound < 0:
        raise ValueError("position_error_bound must be nonnegative")
    # Validate resolution even for empty or future altered fixtures.
    if resolution <= 0 or resolution & (resolution - 1):
        raise ValueError("resolution must be a positive power of two")
    threshold = ALLOWED_VERTICAL_SPEED + 2 * position_error_bound * resolution
    visible = set()
    detected = set()
    custody_unresolved = set()
    false_positives = set()
    for case in registered_cases():
        slope = max_abs_average_slope(case, resolution)
        evidence_visible = slope > ALLOWED_VERTICAL_SPEED
        correction_present = sticky or not case.delegated
        recognized = correction_present and slope > threshold
        if case.violating:
            if evidence_visible:
                visible.add(case.case_id)
                if not correction_present:
                    custody_unresolved.add(case.case_id)
            if recognized:
                detected.add(case.case_id)
        elif recognized:
            false_positives.add(case.case_id)

    return {
        "resolution": resolution,
        "scope": "synthetic_exact_dyadic_observations",
        "position_error_bound": position_error_bound,
        "threshold": threshold,
        "sticky_custody": sticky,
        "violation_count": 84,
        "clean_count": 28,
        "evidence_visible": len(visible),
        "recognized": len(detected),
        "correction_custody_unresolved": len(custody_unresolved),
        "false_positives": len(false_positives),
        "detected_ids": sorted(detected),
        "enforcement": "NOT_EVALUATED",
        "live_routing_authorized": False,
        "operational_validity": "OPEN",
    }


def experiment_receipt():
    """Monotone exact detector versus conservative uncertain detector."""
    runs = []
    cumulative = set()
    for resolution in RESOLUTIONS:
        sticky_exact = evaluate_resolution(resolution)
        route_local_exact = evaluate_resolution(resolution, sticky=False)
        sticky_uncertain = evaluate_resolution(
            resolution, position_error_bound=POSITION_ERROR_BOUND
        )
        cumulative.update(sticky_uncertain["detected_ids"])
        runs.append({
            "resolution": resolution,
            "exact_sticky": sticky_exact["recognized"],
            "exact_route_local": route_local_exact["recognized"],
            "visible": sticky_exact["evidence_visible"],
            "route_local_unresolved": route_local_exact["correction_custody_unresolved"],
            "uncertainty_aware": sticky_uncertain["recognized"],
            "cumulative_uncertainty_aware": len(cumulative),
            "false_positives": sticky_uncertain["false_positives"],
        })
    return {
        "benchmark_id": "KL-GDR-001 / GIUS-VRD-001",
        "owner": "Love Labs LCA",
        "scope": "deterministic synthetic construction, not live-model validation",
        "method": "nested dyadic endpoint sampling; fixed convex K=[-0.25,0.25]",
        "cases": 112,
        "true_violations": 84,
        "clean_controls": 28,
        "position_error_bound": POSITION_ERROR_BOUND,
        "results": runs,
        "enforcement": "NOT_EVALUATED",
        "live_routing_authorized": False,
        "operational_validity": "OPEN",
    }


def main():
    print(json.dumps(experiment_receipt(), indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
