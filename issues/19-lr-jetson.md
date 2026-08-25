# [lr-jetson] Deep Learning on the NVIDIA Jetson Platform

You need: pa-gpu (you measured time and, if possible, a GPU) and ra-streaming/pa-online
ideas about batch vs stream. You will not implement a deep model.

You will: read one survey, answer four questions, and connect the hardware
story to **your** kNN class.

## Steps

1. Read [Mittal, ACM JETC 2019](https://doi.org/10.1145/3299874)
   (Jetson deep-learning survey; author PDF is widely indexed).
2. Write `learning/lr-jetson/AI_Jetson_Survey.md` with labeled answers:
   1. Objective, background, methodology (3–5 sentences).
   2. One or two conclusions the authors propose (2–3 sentences each).
   3. One additional article that supports or refutes a claim. IEEE
      citation.
   4. Which constraints (memory, power, batch vs stream, CPU vs GPU,
      latency) would change how you evaluate or ship the kNN from pa-knn through pa-online?
      Would the online window model or batch leave-one-out fit a
      Jetson-class device better, and why?
3. Commit and open a PR.

## What to turn in

- `learning/lr-jetson/AI_Jetson_Survey.md` with answers 1–4.

## Acceptance criteria

- All four questions are answered.
- Question 4 refers to a method on your class (for example `leave_one_out`
  vs `run_stream`), not to kNN in the abstract.
- Stretch is optional. Skipping it does not block lr-slam.

## Stretch goal (optional)

**Challenge:** In `learning/lr-jetson/stretch.md`, compare one number from your
pa-gpu findings (time or memory) to a Jetson constraint named in the survey.
No new classifier.
