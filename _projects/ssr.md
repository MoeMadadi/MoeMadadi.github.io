---
layout: page
title: Streaming Subspace Routing
description: Task-free online continual learning with frozen ViT features and LoRA experts.
importance: 1
---

Streaming Subspace Routing (SSR) is my current work with Prof. Jiayu Chen at the Agentic Intelligence Lab, University of Hong Kong. The method uses the geometry of a frozen, unprompted ViT-B/16 to route each input among low-rank LoRA experts. It does not need task identity or class labels at inference.

Streaming subspace updates and soft expert composition are driven by residual distances. Rank-8 LoRA experts adapt the attention query and value projections, and the backbone stays frozen. Evaluation covers CIFAR-100, Tiny-ImageNet, and ImageNet-R under the Si-Blurry protocol, with replay budgets of 0, 500, and 2,000 samples. Results are multi-seed Aauc, Alast, and Flast.

A preceding shared-prompt method uses slow-learning LoRA adapters and EMA-based logit distillation. With 500 and 2,000 replay samples it improved over SinglePrompt on all three datasets. On ImageNet-R the gains were +6.62 Aauc and +7.19 Alast.

This work is a manuscript in preparation: Sun, Madadi, Yuan, and Chen, “Streaming Subspace Routing for Task-Free Online Continual Learning.”
