# [Literature Review 1] Deep Learning on the NVIDIA Jetson Platform

The learning-phase implementations stay on kNN. This review looks at what
changes when models move to an embedded GPU — the same heterogeneous-compute
theme as RA4 and PA4, at the scale of deployed deep models rather than a
leave-one-out distance matrix.

Read: [A Survey on Optimized Implementation of Deep Learning Models on the NVIDIA Jetson Platform](https://doi.org/10.1145/3299874)

(If the DOI is gated, the same survey is widely indexed as Mittal, *ACM
J. Emerg. Technol. Comput. Syst.*, 2019; ResearchGate also hosts an
author PDF.)

Answer the following in `learning/LR1/AI_Jetson_Survey.md`. Label answers
1–4 with the question prompts.

1. Describe the objective, background, and methodology of the paper. About
   3–5 sentences.

2. Provide 1–2 conclusions the authors propose. Each conclusion should be
   about 2–3 sentences.

3. Find one additional article that supports or refutes a claim in the
   survey. Cite it in IEEE format.

4. Connect the paper to the classifier you have been building. Which
   constraints (memory, power, batch vs stream, CPU vs GPU, latency) would
   change how you evaluate or ship the kNN from PA1–PA5? Would the online
   window model or the batch leave-one-out model be the more realistic
   fit on a Jetson-class device, and why?

## Acceptance criteria

`learning/LR1/AI_Jetson_Survey.md` exists and answers all four questions.
