---
layout: default
title: Computer Vision
parent: Courses
nav_order: 2
---

# Why Computer Vision?

It’s really straightforward. I’ve always dreamed of making a robot that can understand and interact with the world around it. Since I watched movies like The Iron Giant, Robots, and I, Robot, I became fascinated by robots that develop thinking and some form of consciousness, and that are able to understand their environment.

In Robots, the interaction is mostly between robots, and in some sense it’s a bit dystopian if we think about it carefully. On the other hand, The Iron Giant and I, Robot show robots interacting with humans and trying to improve their world, while also exposing social and ethical problems. What really caught my attention was not the story itself, but the idea that I want to make something like that real, and ideally within our lifetime.

That’s where computer vision comes in. It is one of the key components for building intelligent robots. At least for now, we cannot create robots with human eyes, so instead we need to build robots with cameras and computers that try to replicate, or approximate how we perceive the world or maybe invent a way that computers fully understand our world with another language.

In my opinion, even with all the recent advances in perception, we are still very far from building fully autonomous robots. One of the real bottlenecks lies in computer vision algorithms (There are other bottlenecks in robotics, is a big field). With large vision models, we can already understand a lot, and with modern action or policy models we can even control robots accordingly. However, the real issue is inference time and computational cost.

For comparison, the human brain consumes around 20 W, while processing vision, reasoning, and decision-making all at once. In contrast, current vision models require 100–500 W just for inference. And that’s only perception, the robot still needs to move, plan, and make further decisions. This problem becomes even more critical when we consider real-time operation.

If we talk about inference time, humans can recognize and understand all visual information almost without errors in about 100 ms, while machines can take 500 ms or more, especially when running large models or using limited computational resources (for example, free tiers of ChatGPT, Gemini, etc.) some of them are for the edge (My research and goal) but are fast but not too much accurate sometimes. To make autonomous robots a reality, we need inference that is fast, accurate, and energy-efficient, and that is exactly where the problem lies.

This challenge is my main motivation to research and learn more about computer vision.

For now I am following  the course Introduction to Computer Vision by MIT. Later on, I will continue with papers and more advanced topics, included a glance of my research.

## Resources

-Foundations of Computer Vision by  Antonio Torralba, Phillip Isola, and William Freeman. (My opinion, is the best for  really introductory level, do not need too much background knowledge to fully understand the material)

-Computer Vision: Algorithms and Applications by Richard Szeliski(Good for intermediate level towards advanced level, you must understand linear algebra for this book)

