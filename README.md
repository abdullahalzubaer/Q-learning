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

To execute the program

Approach 1: Please go to the file location and from the command line execute the below command.


```python
python q_learning.py
```

Approach 2 (using docker):

1. Build the docker image using the following command

```
docker build -t q_learning .
```

Then run and get inside the container (`we cannot use the python q_learning.py`) since it will run inside the container and we will not see anything form outside. Therefore we get inside the container using the following command (su means superuser) [NOTE: I think I am wrong here and we can execute python q_learning.py, but since the output is a bit strange maybe that is why it was not working directly by using `docker run IMAGENAME`. Thats all I can say now. For example a simple hello world applicaiton that I have dockerized does show the output `hello world` when I execte this command `docker run IMAGENAME` :) ]

```
docker run -it q_learning su
```
and then 

```
python q_learning.py

```


---

Reference: https://deeplizard.com/learn/video/QK_PP_2KgGE

With changes done w.r.t the Q learning algorithm (it was not in line with the original Q-learning algorihtm) and changed how the exploration rate decays (made it simpler and intuitive)

Environment: https://gym.openai.com/envs/FrozenLake-v0/

---

[1] Zihan Ding, Yanhua Huang, Hang Yuan, and Hao Dong.  Intro-duction to reinforcement learning. In Hao Dong, Zihan Ding, andShanghang Zhang, editors,Deep Reinforcement Learning:  Funda-mentals,  Research and Applications, pages 47–123. Springer Sin-gapore, Singapore, 2020
