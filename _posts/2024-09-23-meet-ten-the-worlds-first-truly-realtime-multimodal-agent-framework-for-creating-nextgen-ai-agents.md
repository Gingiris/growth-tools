---
layout: post
title: "Meet TEN, the World's First Truly Real-time Multimodal Agent Framework for Creating Next-Gen AI Agents"
canonical_url: https://gingiris.github.io/growth-tools/blog/2024/09/2024-09-23-meet-ten-the-worlds-first-truly-realtime-multimodal-agent-framework-for-creating-nextgen-ai-agents/
image: "https://gingiris.github.io/growth-tools/assets/images/blog-devrel-dashboard.jpg"
date: 2024-09-23
description: "Ever since OpenAI demonstrated the real-time conversational capabilities of GPT-4o, it’s as if the movie ‘Her’ has come to life. Motivated by th"
tags: [python, ai, opensource, javascript]
faq:
  - q: "What is TEN (Realtime Extension Network)?"
    a: "TEN is an open-source multimodal AI agent framework designed for real-time, low-latency interactions. It enables developers to build AI agents that process voice, video, and text simultaneously with sub-200ms response times — making it suitable for voice assistants, live translation, and interactive AI applications."
  - q: "What makes TEN different from other AI agent frameworks?"
    a: "TEN's key differentiator is real-time multimodal processing. Unlike LangChain or AutoGPT which are primarily text-based and batch-oriented, TEN handles simultaneous audio, video, and text streams with latency optimized for live interaction. It's built for use cases where response time matters: live voice agents, real-time translation, interactive AI tutors."
  - q: "How do I get started with the TEN framework?"
    a: "TEN is open source on GitHub. To get started: clone the repository, follow the quickstart guide in the README to set up the environment, and run one of the provided example agents. The framework supports Python and C++ extensions, and integrates with major LLM providers including OpenAI, Anthropic, and local models."
---

Ever since OpenAI demonstrated the real-time conversational capabilities of GPT-4o, it’s as if the movie ‘Her’ has come to life. Motivated by the breakthrough user experience of new multimodal capabilities, developers are seeking ways to build real-time conversational AI agents. It is true that some open-source workflow builders currently offer options for easy-to-use orchestration, however, building multimodal AI agents is difficult as these agents not only require ultra-low latency but a deep understanding of technologies like chat, speech to text, text to speech, and real-time audio and video communications. There is also the added complexity of integrating all of these modules together to deliver human-like experience.

Fortunately, there is now an optimal framework for developers with the introduction of TEN (Transformative Extensions Network)(Github link:https://github.com/TEN-framework/TEN-Agent), the world’s first truly real-time multimodal agent framework that minimizes coding pain and enables developers to build next-gen AI applications from scratch.


## WHAT IS THE TEN FRAMEWORK？

The TEN Framework is an open-source framework that enables developers to quickly build real-time multimodal agents (voice, video, data stream, image and text), making it easy for developers to experiment, integrate large language models, and create reusable extensions. TEN can be used to build agents supporting use cases like voice chatbots, AI generated meeting minutes, language tutors, simultaneous translators, virtual companions, counseling and a lot more. Developers can leverage a diverse set of AI services and extensions and have the full flexibility to build, test and roll out the next-gen AI agents, which can think, listen, see, and interact as humans do in real-time.

You have likely heard a developer say something like “I want to build agents as quickly as possible” or enterprise developers say, “We ultimately need a solution that is scalable and extensible to grow with my business needs.” The TEN framework is the optimal choice for developers who want to quickly build real-time multi-modal AI agents for demonstrations today and who need a framework that can easily scale to support larger production deployments while providing the flexibility to add new capabilities or large language models via extensions.


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ikrjbiz2wpj9anwq3w2n.png)

## WHAT CAN YOU BUILD USING THE TEN FRAMEWORK?
With the Ten framework, you can build AI agents that can interact naturally and in real-time as humans do. Let’s take a quick look at an Agent demo powered by TEN.


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qclq8rvdarg0mup9vv1b.png)

TEN Agent is a server-side agent demo that connects to multiple extensions to enable real-time audio and video interactions with support for RAG (Retrieval-Augmented Generation) accessing and leveraging local documentation to provide answers. Developers can easily modify prompts and other configuration parameters to suit their needs. Check it out now! You will be impressed with the AI agent that you can create in less than 10 minutes!

## Of course, you can build your own agents locally with the TEN Framework.

For more complex use cases the TEN Framework allows developers to build their own AI agents with plug-and-play extensions from third parties in the community, integrate one or more LLMs, and manage the data flow between them using a built-in extension management tool called TEN Manager. Developers can also design the workflow using the Graph Designer which provides a simple drag-and-drop interface (shown below).


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/godwsuhj1fne39qk0w1v.png)

## WHY USE THE TEN FRAMEWORK?

The future of gen-AI is expected to rapidly shift toward voice and video as the primary and most natural interface for communication, with RTE (real-time engagement) becoming standard in most applications. During this shift, we’ve observed limitations in existing AI agent platforms.

For instance, some platforms, while effective for quickly developing multimodal agents, are limited to only Python, which restricts their potential for building more complex applications and scaling to broader use cases. Similarly, other platforms may have limited support for audio and video features, further constraining their versatility.

TEN is built to enable developers to create real-time multi-modal AI agents faster and more easily：

**Truly real-time multimodal with ultra-low latency.** TEN supports voice, video, data streams, images and text and it works perfectly in those use cases with voice or video interactions like real-time translation. Beyond that, the interaction (such as data transmission) between different extensions is optimized to streamline end-to-end development and performance.

**Ubiquitous support and customizable extensions.** Unlike other workflow builders with limited multi-modal and programming language support, the TEN Framework supports Golang, C++ and Python with Node.js coming up next. Plus, TEN also enables development across all major platforms including Windows, Mac, Linux and Mobile. All extensions are modular in structure with full flexibility across multiple languages. Extension developers are more than welcome to connect their services to the framework and the community.

**Real-time responsiveness with real-time state management.** By prioritizing immediate responsiveness, dynamic workflows, and synchronized data, agents built using the TEN Framework deliver more interactive, human-like AI experiences, including in multi-user cases. Using TEN, developers have a framework that delivers low latency, synchronization, adaptive media quality, concurrent user support, network resilience and more.

**Support Edge & Cloud simultaneously.** With the TEN Framework, extensions deployed across both edge and cloud environments can be seamlessly combined to create a wide range of applications. For privacy-sensitive edge deployments, smaller models can use local computing power to lower the overall cost and reduce latency, while cloud-based large language models can be integrated to achieve an optimal balance of cost and performance.

**Lightning-Fast building experience and developer-friendly.**The Intuitive visual interface and drag-and-drop components make it simple for developers to get started. For those who have more complex requirements, TEN’s flexible architecture and open APIs provide a robust platform for building custom extensions as well. In addition, TEN welcomes ideas and contributions to the community.

## With TEN as your AI agent framework, the only limit is your imagination.

Access the TEN Agent repo and build your first agent today! If you have fun building and exploring, be sure to [star the repo HERE](https://github.com/TEN-framework/TEN-Agent).


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2na55qple422cav899su.png)

If you are interested in knowing more about the TEN Framework, please access our website www.theten.ai to stay tuned for any future changes or releases. We are more than happy to hear your comments, ideas, and feedback! Please also join our community group on [Discord](https://discord.gg/VnPftUzAMJ).


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d03qqjvsp48brohjwie1.png)

You can also find us on

Discord: https://discord.gg/VnPftUzAMJ

X: https://x.com/TenFramework

Medium: https://ten-framework.medium.com/

Reddit: https://www.reddit.com/r/TenFramework/

Email: developer@theten.ai

Enjoy the TEN Framework and make your real-time multimodal agent come to life！
