#!/usr/bin/env python

import os
import numpy as np
import gym
import matplotlib.pyplot as plt
from stable_baselines3 import PPO

from util import Evaluate

os.chdir("../environment/")
env = gym.make("reference_environment_direct_deployment:reference-environment-direct-deployment-v0")
os.chdir("../local_agent_training_and_evaluation/")

### Evaluate RL agents model_0 to model_39
trained_models = 40
episodes_per_model = 1000
mean_rewards = []
for i in range(trained_models):
    agent = PPO.load("MODEL_"+str(i))
    evaluate = Evaluate(env, agent)
    seeds = evaluate.read_seeds(fname="seeds.csv")
    mean_reward = evaluate.RL_agent(seeds) # Add your agent to the Evaluate class and call it here e.g. evaluate.my_agent(seeds)
    mean_rewards.append(mean_reward)
print('Mean rewards for RL agents:',mean_rewards)

### Plot learning curve
plt.plot(mean_rewards)
plt.xlabel("training time ("+str(trained_models)+" models with "+str(episodes_per_model)+" episodes each")
plt.ylabel("reward")
plt.title("learning curve")
plt.savefig("learning curve.png")

