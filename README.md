# Thai free self-instruct dataset 🥩
<a><img src="https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99" alt="Star Badge"/></a>
<a href="https://github.com/pavaris-pm/thai-free-self-instruct/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/pavaris-pm/thai-free-self-instruct?color=BC4E99"></a>
<a href="https://github.com/pavaris-pm/thai-free-self-instruct/blob/master/LICENSE"><img src="https://img.shields.io/github/license/pavaris-pm/thai-free-self-instruct?color=BC4E99" alt="License Badge"/></a>

This repository contains a script that enables the retrieval of a self-instruct dataset from ChatGPT website directly without incurring costs by calling an external OpenAPI. While it is not as effective as using an API, this solution provides an alternative method to obtain the dataset. Please note that the script requires some user action to function properly.

## Utilization of self-instruct dataset in LLM 🥓
![self-instruct pipeline](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88f7c2ca-5592-423d-b551-9794e325bafc_2218x1004.png)

## Background 👩‍🍳
ChatGPT is a powerful language model that can generate human-like responses given a prompt. To enhance its capabilities, it is often trained on large datasets, including self-instructed dialogues. These dialogues are crucial for training the model to engage in interactive conversations.

- According to the promising result of thai self-instruct dataset updated from `OpenThaiGPT (fine-tuning team)`: 
 [อัพเดท! จากทีม Finetune (8 Apr)](https://openthaigpt.aieat.or.th/previous-events/finetune-8-apr), they also publish the prompt that was used to retrieve self-instruct dataset from LLM like GPT-3 or even GPT-4 which is more interesting to use for dataset retrieval.

- Typically, obtaining a self-instruct dataset involves calling an external OpenAPI, which incurs costs per query. This repository offers a solution to retrieve the dataset for free, albeit with some manual intervention.

## Prerequisites 🚩
To use the self-instruct dataset retrieval script, since it was written in python, ensure you have the following prerequisites installed:
- Library
    - `pyautogui`
    - `pyperclip`
- Operating System (OS) - currently supported [updated at Jul 9th 2023]
    - `Windows`
 
## Usage & Demo 🎮
To run a script, follow these steps below. always note that this script is the prototype version, we still need some manual action.
In our case, `you just need to copy an output from OpenAI generation by yourself`. You can follow the demo below and act accordingly
```
git clone https://github.com/pavaris-pm/thai-free-self-instruct.git
```
then, execute `run_thai_self_instruct.py` script to get thai-self-instruct dataset
```
python run_thai_self_instruct.py
```

 ### Big thanks to `OpenThaiGPT` for determination of research and open-source contribution for Thai Language Modelling task ✨
 
 ![self-instruct pipeline](https://avatars.githubusercontent.com/u/126307330?s=280&v=4)
