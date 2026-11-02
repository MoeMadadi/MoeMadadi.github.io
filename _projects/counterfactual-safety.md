---
layout: page
title: Counterfactual Safety Learning
description: Early-stage route-safety decisions from the robot's own images.
importance: 2
---

Early-stage work on route safety. The robot must proceed, reject the route, or inspect further. The decision uses the robot's own camera images, not an occupancy map.

Matched clear and blocked scenes can share the same visual history. A counterfactual check swaps the view that resolves the ambiguity between those scenes. After the swap, that view should no longer reveal which scene is which.
