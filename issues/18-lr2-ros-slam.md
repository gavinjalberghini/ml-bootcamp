# [Literature Review 2] ROS, Jetson, and SLAM

You need: RA1 (problem types) and RA5 (drift). LR1 is useful but not
required.

You will: read the assigned robotics paper and say what kind of problem
SLAM is, using vocabulary you already have. You will not implement SLAM.

## Steps

1. Read [the assigned Measurement / ROS / Jetson SLAM paper](https://doi.org/10.1016/j.measurement.2019.03.027)
   (use library access if the publisher page is gated).
2. Write `learning/LR2/ROS_Jetson_SLAM.md` with labeled answers:
   1. Objective, background, methodology (3–5 sentences).
   2. One or two conclusions the authors propose (2–3 sentences each).
   3. One additional article that supports or refutes a claim. IEEE
      citation.
   4. Using RA1's language, what kind of problem is SLAM (classification,
      regression, something else)? Where would concept drift (RA5) appear
      for a robot that keeps running in a changing room? Which **ideas**
      from your kNN work transfer (sliding windows, per-class metrics, GPU
      distance work, cost of being wrong) — not the classifier itself?
3. Commit and open a PR.

## What to turn in

- `learning/LR2/ROS_Jetson_SLAM.md` with answers 1–4.

## Acceptance criteria

- All four questions are answered.
- Question 4 uses RA1 and RA5 terms and names at least one method from
  your assignments.
- Stretch is optional.

## Stretch goal (optional)

**Challenge:** In `learning/LR2/stretch.md`, pick one SLAM failure mode
from the paper and say whether your PA5 window, PA2 macro-F1, or PA9-style
cost would be the better *analogy* — not an implementation.
