# Q-learning


Q-learning (off-plicy TD control) [1]
```
Initialization: Initialize Q(s,a) for all state-action pairs and step size α∈(0,1]

for each episode do:
  Initialize S_0
  for each step S_t in cthe current episode do
    Select A_t using polict that is based on Q
    R_(t+1), S_(t+1) <- Env(S_t, A_t)
    Q(S_t, A_t) <- Q(S_t, A_t) + α[R_(t+1) + γmax_a Q(S_(t+1, a) - Q(S_t, A_t)]
   end
end
```

To run: Please go to the file location and from the command line execute the below command.


```python
python q_learning.py
```

---

Reference: https://deeplizard.com/learn/video/QK_PP_2KgGE

With changes done w.r.t the Q learning algorithm (it was not in line with the original Q-learning algorihtm) and changed how the exploration rate decays (made it simpler and intuitive)

Environment: https://gym.openai.com/envs/FrozenLake-v0/

---

[1] Zihan Ding, Yanhua Huang, Hang Yuan, and Hao Dong.  Intro-duction to reinforcement learning. In Hao Dong, Zihan Ding, andShanghang Zhang, editors,Deep Reinforcement Learning:  Funda-mentals,  Research and Applications, pages 47–123. Springer Sin-gapore, Singapore, 2020
