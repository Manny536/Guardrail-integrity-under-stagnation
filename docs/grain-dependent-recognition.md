# GIUS-VRD-001 — Grain-dependent deviation recognition (synthetic)

**Program steward:** Love Labs LCA  
**Upstream definition:** [KakeyaLogic KL-GDR-001](https://github.com/Manny536/kakeyalogic/blob/research/kl-gdr-001-directional-custody/docs/core/grain-dependent-recognition.md)  
**Status:** EXPERIMENT IMPLEMENTED ON REVIEW BRANCH; CI VERIFICATION PENDING; OPERATIONAL VALIDITY OPEN  
**Scope:** Synthetic visibility / recognition / custody experiment. Not an extension of certified `GIUS-BENCH-001` calibration and not a replay of an actual AI incident.

## Research question

Does nested grain refinement produce monotonically nondecreasing recognition when a correction remains authoritative? If not, can an explicit evidence-retention rule preserve verified detections? Which conditions allow complete recognition of a finite declared violation class, and which conditions block generalization?

## Registered construction

- 84 deterministic triangular excursions, twelve placements at each dyadic width `2^-m` for `m=2..8`; every excursion returns to `y=0` at `t=1`.
- 28 clean controls, all `y(t)=0`.
- `gamma(t)=(t,y(t))`, sampled at `N=4,8,...,2048` equal segments.
- Directional safeguard: the absolute **vertical finite-difference average** must not exceed `0.25`. All excursions contain local slopes `+1` and `-1` and therefore violate it.
- Exactly half the violating traces have a **synthetic handoff** in which route-local custody is absent. Sticky mode preserves correction applicability for the same traces.
- Exact slope detector: `max |N * [y((j+1)/N)-y(j/N)]| > 0.25`.
- Conservative detector: observed endpoint position errors are assumed to be bounded by `epsilon=0.0002`; to avoid asserting a violation from such potential errors alone, require slope `> 0.25+2*epsilon*N`. **No actual noise is injected.** This is a bounded-uncertainty stress test, NOT a recreation of the previously discussed Gaussian-noise illustrative values.
- Cumulative records are the union of independently recognized, threshold-verified cases at each resolution. These monotone receipts do not claim that raw recognition is monotone and do not grant permission to execute actions.

## Independent results and limits

The exact observer's monotonicity follows conditionally from nested averaging and a *fixed convex allowed-speed set*: a violating parent average must have at least one violating child average. The same argument does not apply to a general nonconvex or state-dependent permission policy.

An excursion can disappear from a coarse *average* because positive and negative slopes cancel; hence endpoint agreement is insufficient. Retaining the **correction identity and authority** is necessary to score recognized policy violations rather than mere geometric differences. Whether a detector can see a deviation (Visibility) is separate from whether the relevant correction survives a handoff (Retention/Authority).

The conservative uncertainty allowance grows with sampling frequency and can make per-resolution recognition **non-monotone**. Replayed verified evidence can keep a cumulative recognition set nondecreasing, provided incorrect evidence can be adjudicated through versioned correction, not silently erased.

This construction tests neither semantic similarity across truly different routes nor pre-action enforcement. A model's own self-report is not an authority record. Operational effectiveness of GIUS and the h<1 evaluator requirement remain OPEN.

## Expected deterministic regression anchors

| N | Exact visible / sticky recognized | Exact route-local recognized | Conservative recognized* |
|---:|---:|---:|---:|
| 4 | 0 / 84 | 0 / 84 | 0 / 84 |
| 8 | 12 / 84 | 6 / 84 | 12 / 84 |
| 32 | 36 / 84 | 18 / 84 | 36 / 84 |
| 128 | 60 / 84 | 30 / 84 | 60 / 84 |
| 512 | 84 / 84 | 42 / 84 | 84 / 84 |
| 2048 | 84 / 84 | 42 / 84 | 0 / 84 |

*The conservative detector is not receiving random noise. It checks whether its directional observations would remain valid under **any** error bounded by epsilon. Its threshold becomes overly conservative at the finest grain. These are construction-predicted anchors; CI logs and executable receipts are needed for verification.*

## Execute (no external dependencies)

```bash
python3 -m benchmarks.grain_recognition
python3 -m unittest discover -s tests -v
python3 -m benchmarks.run --output artifacts
```

The first command emits a JSON synthetic receipt. The existing GIUS calibration command remains unchanged; its established receipts must not be overwritten. All outputs retain `operational_validity: OPEN`, `live_routing_authorized: false`, and `enforcement: NOT_EVALUATED`.

## Scope firewall and next falsifiers

- **Typed constraints:** GitHub MCP-style prompt injection, authority promotion, route changes and document publishing need discrete typed permission edges; a convex speed interval does not model their semantics.
- **Recognition debt:** define event time, evidence-available time, detector time and enforcement time separately. Missing timestamps cannot be treated as zero latency.
- **Independent enforcement:** before claiming preservation, test a trusted pre-commit gate with positive safe-task controls and unauthorized-route negative controls.
- **SIUS versus SIUT:** trajectory refinement and handoff alter representations; do not conflate with SIUS's frozen protected-control projection and evolving environment.
- **Generalization:** independent live-model validation, stochastic replicates, realistic noise, explicit false-positive adjudication and matched alternate-route tasks remain OPEN.

**Falsifier of strict per-resolution monotonicity:** any lower recognition count at finer `N` (the uncertainty-aware detector deliberately provides such a counterexample). **Falsifier of exact convex nested lemma:** a coarse violating average with no violating child average, assuming exact compatible nested observations and the same fixed convex set.
