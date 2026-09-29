---
layout: about
title: about
permalink: /
subtitle: Research Assistant at HKU · Continual Learning & Robot Learning

profile:
  align: right
  image: Profgit.PNG
  image_circular: false # crops the image to make it circular
  more_info: >
    <p>Agentic Intelligence Lab</p>
    <p>University of Hong Kong</p>
    <p><a href="mailto:mohammadmadadi2001@gmail.com">mohammadmadadi2001@gmail.com</a></p>

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: false # includes a list of news items
  scrollable: false # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

I am a research assistant in the [Agentic Intelligence Lab](https://agentic-intelligence-lab.org/) at the University of Hong Kong, working remotely with [Prof. Jiayu Chen](https://agentic-intelligence-lab.org/members/jiayu-chen.html). My research is on **continual learning** and **robot learning**: how a model can keep adapting when the task stream has no identity labels, and how robot policies can be adapted across manipulation tasks without forgetting earlier ones.

My current method, **Streaming Subspace Routing (SSR)**, uses the geometry of a frozen, unprompted ViT-B/16 to route each input among low-rank LoRA experts. Routing does not need task identity or class labels at inference. Rank-8 LoRA experts adapt the attention query and value projections while the backbone stays frozen. I evaluate SSR on CIFAR-100, Tiny-ImageNet, and ImageNet-R under the Si-Blurry protocol, with replay budgets of 0, 500, and 2,000 samples, and report multi-seed Aauc, Alast, and Flast. A preceding shared-prompt method, with slow-learning LoRA adapters and EMA logit distillation, improved over SinglePrompt on all three datasets at the 500- and 2,000-sample replay settings. On ImageNet-R the gains were +6.62 Aauc and +7.19 Alast.

On the robotics side, I have been studying continual robot learning for BEHAVIOR-1K household manipulation in OmniGibson and Isaac Sim, including how to design the task stream and how to learn from demonstrations. I have also been looking at continual diffusion policies on the Lift, Can, and Square tasks in Robomimic, with attention to specialization, forward transfer, and distillation between stages.

I received my B.Sc. in Mechanical Engineering from **Sharif University of Technology** (GPA 17.66/20; First Class Honours). I ranked 9th in the Robotics and Control division and 24th overall among 147 students. Before HKU, I compared PPO, TD3, and SAC for Franka Panda assistive-arm motion planning with Prof. Mohammad Taghi Ahmadian, and I studied workplace ergonomics and spinal loading with Prof. Navid Arjmand.

**Research interests:** robotics and autonomous systems, embodied AI, continual learning, robot learning, reinforcement learning, and motion planning.
