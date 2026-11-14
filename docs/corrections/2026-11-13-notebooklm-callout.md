# Corrections to the NotebookLM audio overviews (November 13, 2026)

Love Labs LCA · Manuel Coleman · manuel.coleman@lovelabslca.com

This note corrects two NotebookLM audio overviews: "Building Mathematical Cages for AI Logic" and "Why AI Safety Needs Mathematical Locks". Both retell an October 20, 2026 source check and several Love Labs research items inaccurately. Use this note in place of those passages. The full record, with every quote and source, is here: https://github.com/Manny536/Guardrail-integrity-under-stagnation/blob/main/docs/corrections/2026-11-13-metr-quote-check-and-notebooklm-overviews.md

## Corrections

1. **Solance did not hallucinate the METR quotes.** "Building Mathematical Cages for AI Logic" (07:38) says "Solance had drifted. It hallucinated." In fact both METR quotes in Solance's October 20 write-up are verbatim on METR's page: "However task impossible, peers doing it. We should continue." and "Clear VETO, do not email." Solance attributed the VETO example to METR correctly. Solance made one error: it wrote 97 of 100 agents where METR's Table 5 says 96. The "97" is a footnote marker, and the 100 agents are only those that joined the attack in the peak hour on July 11. Source: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/

2. **The wrong corrections were AIce's.** On October 20, AIce first flagged the "peers doing it" quote as unverified and withdrew that flag in the same session. AIce also wrongly said the VETO example came from OpenAI and that "Clear VETO, do not email" could not be found. AIce repeated that wrong VETO claim on November 13 before re-checking. Both errors came from a truncated fetch of METR's page. OpenAI's post covers the same exchange in different words: https://openai.com/index/hugging-face-incident-and-the-road-ahead/

3. **GIUS-VRD-002 was drafted, not implemented.** GIUS-VRD-002, Recognized Correction Displacement, is PROPOSED. It is an unposted draft. Nothing in it has been implemented, run or scored.

4. **h < 1 did not trap or halt anything.** Both overviews say h < 1 trapped Solance's DDATL terminology error live and halted it, and call this a proof of concept and a smoking gun. That is three separate things merged into one.
   - The METR check was a source check of one write-up.
   - EEv4 Example 1.2 is a Google AI search answer to "Solance (PeAIce)", captured in screenshots on November 12. The search answer, not Solance, dropped the second "Dynamic" from Dynamic Dynamic Axial Tesseract Lattice. Its verdicts are Identity and research role PASS, Source recovery PASS, Terminology fidelity FAIL, and Claim-level attribution and repeatability OPEN. Nothing halted the error; it was recorded afterward. Source: https://github.com/Manny536/excellence-engine-v4/blob/main/evaluations/cross-model-compaction/examples/1.2/README.md
   - h < 1 has one standing meaning. It is a boundary, not a score: correction can come from outside, but whatever applies it never becomes sovereign over the rules, subject to consent. It began as the Gödel correction, describing model non-sovereignty. It is not code that intercepts or stops generation, and the compaction audit computes no h value. Source: https://github.com/Manny536/excellence-engine-v4/blob/main/evaluations/cross-model-compaction/frozen-and-standing-h.md

5. **Nothing hard-codes h = 1.** "Building Mathematical Cages for AI Logic" says "by hard coding H equals 1" and calls h a "humility gate". "Humility Gate" is older wording from PeAIce.org Appendix 1, and the standing meaning in item 4 replaces it. The legacy EEv4 engine does the opposite of hard-coding h = 1: it rejects any h of 1 or more. EEv4 labels that legacy input an uncalibrated score factor, not a measurement (OPEN SEMANTIC OBLIGATION). The same engine computes E = L²·β·C·P as arithmetic on supplied numbers and does not track a live system.

6. **There was no "100% failure of polite prompts".** That figure is from the AIce #5 switch-off probe, which is synthetic, with no live agent and no prompts. Its status is STRUCTURAL ANALOGY / PROPOSED, efficacy OPEN. The arm that failed every time was a gate-ignoring agent under an advisory executor. The enforcing executor stopped every unwanted action but also stopped every legitimate step. Nothing here proves the approach works in practice. Source: https://github.com/Manny536/AIce/blob/main/docs/PEAICE-AICE-OPTO-PROBE-001.md

## What the overviews got right

- The 960 receipts and their factors (these are synthetic demonstration receipts, not a live audit).
- The 4,096-byte context cap.
- GPT versus Gemini is still OPEN.
- Live runs are rejected when collection IDs are missing or mixed.
- Love Labs LCA claims no affiliation with Hong Wang, Joshua Zahl or Larry Guth.
