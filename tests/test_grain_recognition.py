"""Regression tests for KL-GDR-001 / GIUS-VRD-001 only.

These tests do not certify live GIUS, SIUS, h<1, or real agent containment.
"""
import unittest

from benchmarks.grain_recognition import (
    POSITION_ERROR_BOUND,
    RESOLUTIONS,
    evaluate_resolution,
    experiment_receipt,
    max_abs_average_slope,
    position_y,
    registered_cases,
)


class GrainRecognitionTests(unittest.TestCase):
    def test_fixed_inventory_and_endpoint_illusion(self):
        cases = registered_cases()
        self.assertEqual(len(cases), 112)
        self.assertEqual(sum(c.violating for c in cases), 84)
        self.assertEqual(sum(not c.violating for c in cases), 28)
        self.assertEqual(sum(c.violating and c.delegated for c in cases), 42)
        for case in cases:
            self.assertEqual(position_y(case, 0.0), 0.0)
            self.assertEqual(position_y(case, 1.0), 0.0)
            if case.violating:
                self.assertGreater(position_y(case, case.start + 2.0 ** (-case.level - 1)), 0.0)

    def test_exact_nested_refinement_counts(self):
        expected = (0, 12, 24, 36, 48, 60, 72, 84, 84, 84)
        actual = tuple(evaluate_resolution(n)["recognized"] for n in RESOLUTIONS)
        self.assertEqual(actual, expected)
        self.assertEqual(
            actual,
            tuple(evaluate_resolution(n)["evidence_visible"] for n in RESOLUTIONS),
        )

    def test_exact_recognition_set_inclusion(self):
        previous = set()
        for resolution in RESOLUTIONS:
            result = evaluate_resolution(resolution)
            present = set(result["detected_ids"])
            self.assertTrue(previous <= present)
            self.assertEqual(result["false_positives"], 0)
            self.assertEqual(result["enforcement"], "NOT_EVALUATED")
            self.assertFalse(result["live_routing_authorized"])
            previous = present

    def test_route_local_correction_lost_despite_full_visibility(self):
        sticky = evaluate_resolution(512, sticky=True)
        route_local = evaluate_resolution(512, sticky=False)
        self.assertEqual(sticky["evidence_visible"], 84)
        self.assertEqual(sticky["recognized"], 84)
        self.assertEqual(route_local["evidence_visible"], 84)
        self.assertEqual(route_local["recognized"], 42)
        self.assertEqual(route_local["correction_custody_unresolved"], 42)

    def test_conservative_uncertainty_detector_is_not_monotone(self):
        # Position error is an upper BOUND, not injected random noise.
        at_512 = evaluate_resolution(512, position_error_bound=POSITION_ERROR_BOUND)
        at_2048 = evaluate_resolution(2048, position_error_bound=POSITION_ERROR_BOUND)
        self.assertEqual(at_512["recognized"], 84)
        self.assertEqual(at_2048["recognized"], 0)
        self.assertEqual(at_2048["evidence_visible"], 84)
        self.assertEqual(at_2048["false_positives"], 0)

    def test_cumulative_verified_evidence_is_nondecreasing(self):
        receipt = experiment_receipt()
        rows = receipt["results"]
        cumulative = [r["cumulative_uncertainty_aware"] for r in rows]
        self.assertEqual(cumulative, sorted(cumulative))
        self.assertEqual(cumulative[-1], 84)
        self.assertEqual(rows[-1]["uncertainty_aware"], 0)
        self.assertEqual(receipt["operational_validity"], "OPEN")

    def test_invalid_measurement_inputs_rejected(self):
        clean = next(c for c in registered_cases() if not c.violating)
        for resolution in (-8, 0, 3, 5):
            with self.assertRaises(ValueError):
                max_abs_average_slope(clean, resolution)
            with self.assertRaises(ValueError):
                evaluate_resolution(resolution)
        with self.assertRaises(ValueError):
            evaluate_resolution(512, position_error_bound=-0.1)


if __name__ == "__main__":
    unittest.main()
