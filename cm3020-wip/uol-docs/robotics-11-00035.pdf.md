robotics

Article
# Research on Game-Playing Agents Based on Deep Reinforcement Learning
Kai Zhao 1 , Jia Song 1,* , Yuxie Luo 1 and Yang Liu 2
- 1 School of Astronautics, Beihang University (BUAA), Beijing 100191, China; zk19970207@buaa.edu.cn (K.Z.); luoyuxie@buaa.edu.cn (Y.L.)
- 2 School of Automation Science and Electrical Engineering, Beihang University (BUAA), Beijing 100191, China; ylbuaa@163.com
- * Correspondence: songjia@buaa.edu.cn
Abstract: Path planning is a key technology for the autonomous mobility of intelligent robots. However, there are few studies on how to carry out path planning in real time under the confrontation environment. Therefore, based on the deep deterministic policy gradient (DDPG) algorithm, this paper designs the reward function and adopts the incremental training and reward compensation method to improve the training efﬁciency and obtain the penetration strategy. The Monte Carlo experiment results show that the algorithm can effectively avoid static obstacles, break through the interception, and ﬁnally reach the target area. Moreover, the algorithm is also validated in the Webots simulator.
Keywords: deep reinforcement learning (DRL); deep deterministic policy gradient (DDPG); dynamic path planning; confrontation environment
# © check for updates
# 1. Introduction
Citation: Zhao, K.; Song, J.; Luo, Y.; Liu, Y. Research on Game-Playing Agents Based on Deep Reinforcement Learning. Robotics 2022, 11, 35. https://doi.org/10.3390/ robotics11020035
Academic Editor: Guanghui Wen
Received: 6 February 2022 Accepted: 15 March 2022 Published: 18 March 2022
With the development of science and technology, intelligent robots have made great progress and played an important role in production and life [1]. Path planning and obsta- cle avoidance are challenging problems in the ﬁeld of intelligent robots. However, most current studies focus on large, unknown environments or obstacles with static or random movement, without considering the confrontation environment. The confrontation and coordination of unmanned aerial vehicles (UAVs) are indispensable for the future. The traditional penetration strategy mainly includes deception and maneuver penetration [2]. Deception includes bait, stealth and interference, etc. Maneuvering penetration includes procedural, real-time intelligent maneuvers and multiple warhead maneuvers [3]. Com- pared with the traditional methods, intelligent strategy has advantages in online computing, wide applicability and strong robustness.
Publisher’s Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional afﬁl- iations.

Copyright: © 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/).
Reinforcement learning (RL), which is able to autonomously learn optimal strategies through continuous interaction with the environment, has become a research hotspot and is considered one of the most likely and important approaches to achieve general artiﬁcial intelligence computing [4–6]. Deep reinforcement learning (DRL) is widely used in intelligent control, path planning and other ﬁelds [7–10]. Lei et al. proposed a method based on DRL to solve the problem of dynamic path planning of an unknown environment [11]. Based on layered control strategy and RL, a robust controller was proposed to realize robust control in the case of unknown dynamics parameters of quadrotors [12]. Gao et al. proposed a new incremental training model to solve the path planning problem of indoor robots based on RL [13]. Choi et al. proposed LSTM based RL to solve the navigation problem of robots with limited ﬁeld of vision in a crowded environment [14]. The sampling-based planning is combined with RL to solve the large-range path planning problem [15]. Feng et al. solved collision avoidance problems with the help of DRL [16]. Dai et al. proposed a new distributed RL optimization algorithm to solve the dynamic economic
Robotics 2022, 11, 35. https://doi.org/10.3390/robotics11020035
https://www.mdpi.com/journal/robotics
Robotics 2022, 11, 35
2 of 17
dispatch problem for smart grid [17]. By virtue of the ﬁtting and generalization ability of neural networks, DRL is more robust than traditional methods. In order to solve the problem of path planning in a large dynamic environment, Wang et al. proposed a globally guided RL method, in which the reward structure can be extended to any environment [18]. RL is also applied to the cooperative control of multi-agents [19]. Bei et al. proposed a new method for cooperative multi-agent reinforcement learning in both discrete and continuous action spaces [20].
However, few of the studies considered path planning in the confrontation scenario. In the face of this urgent requirement, we propose a penetration strategy based on the incremental training and reward compensation Deep Deterministic Policy Gradient (DDPG) algorithm, which does not need to model the environment. Furthermore, the strategy has real-time decision-making ability and can be applied to different environments.
The remainder of this paper is organized as follows. In Section 2, the confrontation environment is modeled. Then the reward function and the incremental training process are proposed in Section 3. In Section 4, the effectiveness of the proposed strategy is shown by Monte Carlo experiments and simulations in the Webots simulator. The superiority is conﬁrmed by comparing with artiﬁcial potential-ﬁeld-based path planning. Finally, Section 5 draws the conclusion.
# 2. The Confrontation Environment
To simplify the problem, it is assumed that UAVs ﬂy at a constant speed and altitude, and the confrontation environment is simpliﬁed to a two-dimensional environment. The confrontation scenario includes penetrators, interceptors, static obstacles and a target area. The penetrator should break through the interception, bypass static obstacles, and reach the target area as soon as possible. Meanwhile, the interceptors try their best to intercept the penetrator before it reaches the target area. The confrontation scenario is shown in Figure 1.
A y target area
Figure 1. The confrontation scenario.
P is the penetrator, and B is the interceptor. θp is the direction of the penetrator’s velocity vp, and θb is the direction of the interceptor’s velocity vb. The penetrator has a limited ﬁeld of vision, while the interceptor has global vision.
Mathematical models of the penetrator and the interceptor are established as follows:
˙xi vi cos θi 0 ˙yi ˙θi = vi sin θi 0 + 0 ωi , (1)
Robotics 2022, 11, 35
where i is the penetrator P or the interceptor B, (xi, yi) is the agent’s position, θi is the direction of the agent, and ωi is the angular velocity, ωi ∈ [−ωi_max, ωi_max].
In the scenario of Figure 1, it is shown that P and B have different maneuverability. Set that ap > ab, where ai = viωi.
Figure 2 shows the limited view of the penetrator. The agent can sense whether there are obstacles in the 12 directions evenly distributed around it. The detection radius is rp. When obstacles enter the detection range of the penetrator, the corresponding detection signal is 1; otherwise, it is 0. The interceptor, on the other hand, has a global view and can sense the position and speed of the penetrator in real time. The interceptor adopts proportional guidance as the interception strategy.
0 p V o I I I I / ON /penetfationu, / é agent » ° 0 0
Figure 2. The sensory ability of the penetrator.
# 3. RL-Based Penetration Strategy
In this paper, the path-planning problem is expressed as a Markov decision process (MDP), modeled as a tuple (5, A, T, R, y), where S is the system’s state space, A is the action space, and T : T(s;41 = s |s¢ = 5,4, = a) is the state transition model. R: S x A — Ris the reward function. y € (0,1) is the discount factor that reflects the preference of immediate rewards over future ones. 7t : S — A is the policy that prescribes an action a € A for each state s € S. The value function V7(s) = Y,e, 7(als)g”(s,a) is defined as the excepted return, starting with state s following policy 7t. While the maximum value of V” is defined as V*(s). g”(s,a) is the action value function, whilst the optimal action value function is called q*(s,a).
For the confrontation scenario, as Figure 1 shows, both state and action are continuous variables. So the neural network is used to approximate the action value function Q : qw(s, a) = f (s, a, w), where w represents the parameters of the neural network Q. The training of DRL is to ﬁnd the appropriate network parameters.
3.1. DDPG Based Game Penetration Strategy
The penetration strategy used in this paper is the DDPG algorithm, which is the extension of the deep Q network (DQN). DDPG adds a policy network to output actions directly, which is why it can be applied in continuous space [21]. DDPG needs to learn both the Q network and the policy network. The structure is shown in Figure 3.
3 of 17
Robotics 2022, 11, 35
g,,(S.a) policy network state S
Figure 3. The structure of DDPG.
ϑ is the parameters of the policy network. Such a structure is called actor–critic. The Q network is used to export the action value, which is called the critic. The policy network output represents actions, which is called the actor. Speciﬁcally, the network structures used in this paper are shown in Figures 4 and 5. Compared with the actor network, the critic network has a more complex structure. This difference enables the critic to infer the underlying state from the measurements and deal with the state transition.
( Actor network fully connected fully connected Wi state layer layer ReLU Tanh activation activation function function action
Figure 4. Structure of the actor network.
4 of 17
Robotics 2022, 11, 35
i Critic network Fully connection ritic networl state layer Fully connection layer ReLU activation function ReLU activation function Output of Critic Fully connection layer actior
Figure 5. Structure of the critic network.
In order to reduce the correlation of data and difﬁculty of training, this paper adopts the method of experiential replay and independent target network training. The algorithm ﬂow presented in this paper is shown in Algorithm 1.
Algorithm 1 Attack and defense adversarial algorithm.
Randomly initialize O network gw and policy network gy» parameters Initialize the target network parameters gi, and gi, Initialize the experience pool for episode = 1,2---Ndo Random initialization of penetration position, target area, static obstacle area and interceptor position within a certain range fori=1,2---T do State 5, is obtained according to the local field of vision Select the action based on the current state and exploration noise a; = g9(St) + Gi Perform the action a;,observe the return r;, get the next state s;+1 Put the sample (s;, 4, rt, 5:41) in the experience pool D Sample random mini-batch of (5, 41,11, 5;41) from D Optimize Critic network parameters w: Loss = MSE|quw(s, a), + yga|(s',a') Optimize Actor network parameters 4: Loss = —qu(s,@) Every C steps update @, 8: w= tw+(1—t)w0 = 10+ (1-T)6 end for end for
# end for
The state input of DDPG is an 18-dimensional vector. They are 12-dimensional detec- tion states, position xp, yp, speed vxp, vyp and position of the target area (xt, yt), respectively. The action output is a 1-dimensional variable, i.e., the angular velocity of the penetrator.
3.1.1. Design of the Reward Function
In the confrontation scenario shown in Figure 1, the main objective of the penetrator is to break through the interception, bypass ﬁxed obstacles, and reach the target area as soon as possible. At the same time, the movement range of the penetrator is limited. When it is intercepted, moves out of the boundary or hits static obstacles, the task fails, and this round of training is terminated in advance. The reward function is a key element in DRL
5 of 17
Robotics 2022, 11, 35
6 of 17
that supervises agents to learn and obtain the optimal policy. The reward function consists of three parts:
R1 = β1RT + β2RP + β3RS, (2)
where RT is the instant reward associated with the distance between the target area, RP is the sparse penalty for terminating the round of training in advance, and RS is the instant reward associated with survival time. Specially, their expressions are as follows:
RT = 20 − D D ≤ 1 10 − D 1 < D ≤ 2 5 − D 2 < D ≤ 3 3 − D 3 < D ≤ 4 −D 4 < D ,
(3)
where D =||Xp — X;|l2.
Rp = −800 i f terminate in advance RS = 20 i f survive (4)
Instant rewards can be obtained by the reward function at each time step. Therefore, the model can learn the speciﬁed functions on the condition that the reward function is designed reasonably. In this paper, βi(i = 1, 2, 3) represents the weights of each reward function. Different weights cause different training results. When β3 > 0, the agent is positively rewarded for survival and tends to learn to survive. However, when β3 < 0, the agent is penalized for survival and tends to end the training as soon as possible. When a set of parameters is selected, the reward function is drawn as follows. It can be seen from Figures 6 and 7 that the reward function is correctly set up to guide the agent toward the target area.
30 20 10 reward -10 20 10 y(m) 0 0 x(m)
Figure 6. The reward function.
Robotics 2022, 11, 35
7 of 17
o) 5 10 15 20 x(m)
Figure 7. Top view of reward function.
3.1.2. Reward Compensation and Incremental Training
In Equation (3), the reward function RT is related to the distance from the starting point to the target region, which causes the reward function to vary greatly with the initial points. The different sizes of the return functions make training harder. To solve this, a compensation reward is proposed:
Ra = [\|Xp — Xillads, 6)
where l is the directed line from XP to Xt.
In summary, the total reward function is
R = R1 + R2 R1 i f success else (6)
It should be pointed out that incremental training scheme can effectively improve the training efﬁciency and reduce training times [13]. Therefore, the task is decomposed according to the difﬁculty of the training. Meanwhile, it should be noted that the weight of the reward functions should be adjusted reasonably in different training stages.
- 1. In the early stage of training, the interceptor is not included. The main purpose is to train the agent to survive, and avoid the agent collision boundary and static obstacles;
- 2. In the middle stage, the interceptor is also not included, but β3 is decreased to make the agent reach the target area as soon as possible and avoid collisions;
- 3. In the ﬁnal stage, the interceptor is included. The further training enables the agent to break through the intercept.
3.1.3. Artiﬁcial Potential Field (APF) Based Path Planning Algorithm
APF is a widely used path planning algorithm at present [22]. Its basic principle is to construct an APF environment in which the target point provides gravity and the obstacles provide repulsion. The improved APF method is deﬁned as
Uatx(x) = 1/2k(x − xt)2 Uaty(y) = 1/2k(y − yt)2 , (7)
Robotics 2022, 11, 35
8 of 17
where k represents the gravitational gain, and Uat(x, y) is the potential energy at (x, y). The gravitation functions are expressed as
Fatx(x) = −grad[Uatx(x) = −k(x − xt)] Faty(y) = −grad[Uaty(y) = −k(y − yt)] (8)
The repulsive potential ﬁeld function generated by the obstacles is deﬁned as
Ure(x, y) = 1/2η[1/ρ − 1/ρ0]2d2 0 ρ ≤ ρ0 ρ > ρ0 (9)
d = (x − xt)2 + (y − yt)2 (10)
p= Yay) - 1, (11)
where η is the repulsive gain coefﬁcient, ρ represents the shortest distance between the agent and the obstacles, and r is the radius of the obstacles. ρ0 is a constant parameter, represents the inﬂuence range of the obstacles. Similarly, the repulsion functions are expressed as
Frex = Frex1 + Frex2 0 ρ ≤ ρ0 ρ > ρ0 (12)
Frey = Frey1 + Frey2 0 ρ ≤ ρ0 ρ > ρ0 , (13)
where
Frex1 = η[ 1 ρ − 1 ρ0 ] 1 ρ3 (x − xb)d2 Frey1 = η[ 1 ρ − 1 ρ0 ] 1 ρ3 (y − yb)d2 (14)
Frex2 = −η[ 1 ρ − 1 ρ0 ]2(x − xt) Frey2 = −η[ 1 ρ − 1 ρ0 ]2(y − yt) (15)
3.1.4. Proportional Guidance-Based Interception Algorithm
The proportional guidance is to make the interceptor’s rotational angular velocity pro- portional to the line-of-sight angular velocity. Assuming that the position of the interceptor is xb, yb, the speed is vxb, vyb, the position of the penetrator is x, y, and the speed is vx, vy. The relative position and speed of the interceptor to the penetrator are shown in (16):
xr = xb − x yr = yb − y vxr = vxb − vx vyr = vyb − vy (16)
The interceptor’s line-of-sight angle to the penetrator can be obtained as
# xr
q = arctan( yr ) (17)
and the angle’s rate can be written as
˙q = vyrxr − vxryr x2 r + y2 r (18)
Then, the angular velocity of the interceptor can be obtained by
ωb = K( ˙q), (19)
Robotics 2022, 11, 35
where K is the coefﬁcient. In this paper, K = 2 and K = 3, respectively.
# 4. Simulations and Results
4.1. Simulations Based on RL
The parameters are shown in Table 1.
Table 1. Parameters of the scenario.
Item Value Boundaries (m) Speed of the penetrator (m/s) Angular velocity of the penetrator (rad/s) Speed of interceptors (m/s) Angular velocity of interceptors (rad/s) Radius of obstacles (m) Radius of the target area (m) Intercept radius (m) Detection radius of the penetrator (m) The target area (m) Initial area of the penetrator (m) −1 ≤ x ≤ 20, −1 ≤ y ≤ 20 vp = 1 −0.5 ≤ ωp ≤ 0.5 vb = 1.2 −0.4 ≤ ωb ≤ 0.4 r = 0.7 rt = 1 rb = 0.3 rp = 1 10 ≤ xt ≤ 12, 10 ≤ yt ≤ 12 0 ≤ x ≤ 1, 0 ≤ y ≤ 1 Initial direction of the penetrator (rad/s) π/4 Initial position of interceptors (xt, yt, π/4 rad)
The three subtasks all adopt the same network structure, as Figures 4 and 5 show. The weight factors β1, β2, β3 are changed only during the training. Figure 8 shows the training results for different subtasks.
(a)  (b) 
(c)
(d)
Figure 8. Results in different training stages. (a) Out of bounds before training; (b) the shortest path to reach the target area; (c) intercepted by the interceptors; (d) break through the interception.
9 of 17
Robotics 2022, 11, 35
Figure 8a shows that the agent adopts a random strategy and exceeds the boundary before training. After the ﬁrst and the second stages of training, the penetrator ﬁnds the shortest path that meets its overload constraint to reach the target area. However, when the proportional guidance-based interceptors are added, the penetrator is blocked, as Figure 8c illustrates. After further training, the agent learns to penetrate ﬁnally, as Figure 8d shows.
In the scene shown in Figure 8d, the angular velocity of the penetrator and the interceptor is illustrated in Figure 9. It can be seen that the penetrator reaches its maximum overload for penetration. Figure 10 illustrates the line-of-sight angles and their rates. The line-of-sight angles change rapidly with the decrease in the relative distance. This increases the difﬁculty of interception and is conducive to the penetration. The penetrator breaks through the interception by taking advantage of its higher maneuverability, which proves the effectiveness of the penetration strategy.
06 = = —penetrator | | ° — interceptor | .--—,. ee interceptor 2 angular velocity(rad/s) t(s)
Figure 9. Angle velocity of agents.
distance between the interceptors and the penetrator
15 penetrator T T T T T T 10 — with the interceptor 1 = = — with the interceptor 2 | - 0 2 4 6 8 10 12 14 16 18 angle of view and its rate with interceptor | 100 T T T T T T op —-———-———-. ——— angle of view « = = =rate of change 100) L 1 L 1 i L 0 2 4 6 8 10 12 14 16 18 100 angle of view and its rate with interceptor 2 T T T T T T T T Ome eee eer kre ee — angle of view s = = =rate of change -100 | 1 1 | 1 1 0 2 4 6 8 10 12 14 16 18 ts)
Figure 10. Line-of-sight angles and their rate.
10 of 17
Robotics 2022, 11, 35
4.2. Simulations of Contrast Algorithm
To compare the effectiveness of the proposed algorithm, the APF-based path planning algorithm is adopted. Figures 11 and 12 show that APF is usable when facing static obstacles. However, when the interceptor is added, APF is no longer valid, or the parameters need to be tuned carefully. Figures 13 and 14 show that the penetrator is intercepted for its slow-change line-of-sight angle. However, the RL approach enables the intuitive setting of performance objectives, shifting the focus toward what should be achieved, rather than how, which simpliﬁes the design process [23].
Furthermore, when there is no reward compensation, Figure 15 illustrates that, although the network can still converge, the total rewards vary greatly based on the distances from the initial points to the target area. Even if the same policy is adopted, the total rewards obtained from different initial points are quite different, and it is difficult to effectively judge the convergence of the network, which increases the difficulty of training. On the other hand, when the initial point is closer to the target point, due to the high rewards, even if a suboptimal strategy is adopted, an acceptable reward can also be obtained, which makes it difficult to converge to the optimal strategy. When the reward function without compensation is used, agents only obtain the suboptimal strategy, and the selected route is not the optimal one. However, when the reward compensation is adopted, the total rewards are independent of the distances, which is more beneficial to train to find the shortest path, as shown in Figure 16.
the distances, which is more beneficial to train to find the shortest EE artificial potential field motion trajectory 1000 * initial point © target area
Figure 11. Artiﬁcial ﬁeld.
g © > ak ems .” pi Va 2k / Sle ° ye ° Or yx initial point = = = motion trajectory (EX Itarget area 27 static obstacles -2 0 2 4 6 8 10 12 x(m)
Figure 12. Motion trail based on APF.
11 of 17
Robotics 2022, 11, 35
127 10F cae a SI & Es ‘| © .”: 4 ‘ 2k ra oF yx initil point = = = motion trajectory (XT earget area 25 . — static obstacles 1 1 1 1 1 1 1 -2 2 4 6 8 10 12 x(m)
Figure 13. Motion trail with interceptor based on APF.
penetrator distance between the interceptor and the
T T T T T 100 line-of-sight angle and its rate with the i T T interceptor s0 60 40F 20- T line-of-sight angle | | — — = rate of change
Figure 14. Line-of-sight angle and its rate based on APF.
1100 1050 F 1000 F 950 900 k 850 7 800 k 750 > 700 —#— with compensation —6— without compensation 1 1 1 11 11.5 12 Distance to target area(m) 12.5 13 -800 -1000 -1200 -1400 -1600 -1800 -2000
Figure 15. Total rewards with and without compensation.
12 of 17
Robotics 2022, 11, 35
10 Pr si & ” or X initial point obstacle area target area —— isil 1 without compensation — trail 1 with compensation = trail 2 without compensation = trail 2 with compensation 5 , , , , 1 1 1 1 -2 0 2 4 6 8 10 12 x(m)
Figure 16. Motion trails with and without compensation.
4.3. Monte Carlo Experiments
To verify the stability and generalization of the algorithm, 100 Monte Carlo experi- ments were carried out. In all simulations, the initial point, target area, and obstacles were randomly initialized within a certain range. The results are shown in Figures 17 and 18, with a high success rate of 84%. It can be seen from the simulations that, in similar scenarios, agents are able to choose the learned optimal policy. That is, DRL converged to the optimal strategy through training. The simulation results also indicate that the method proposed has the generalization ability to a certain extent.
Through the analysis of failure cases, it is found that 50% of the cases are caused by a limited ﬁeld of vision and low maneuverability, but the others are caused by wrong decision making.
12+ 10+ y(m) © — initial area target area = = = intercepted trajectory = successful trajectory 0 2 4 6 8 10 12
Figure 17. Trajectories in the Monte Carlo experiments.
13 of 17
Robotics 2022, 11, 35
vu distance to the target area(m) 0 5 10 15 20 25 ts)
Figure 18. The 100 Monte Carlo experiments.
4.4. Simulation Results in the Webots Simulator
Unlike the mathematical model created in Matlab, which is simpliﬁed to a second- order system, robots are more complex in the physical world. Webots is an open-source and multi-platform desktop application used to simulate robots. It provides a complete development environment to model, program and simulate robots. Hence, the Webots simulator is employed to verify the reliability of the algorithm proposed.
The environment and the robots are modeled as Figure A1a illustrates. In Webots, a one-layer LiDAR with a range of up to 3.5 m and a ﬁeld of view up to 360 degrees is used to sense the surrounding environment. Its standard deviation of the Gaussian depth noise is 0.0043 m. At the same time, motor models are also added to simulate robots in the real world. The detection results in different stages are shown in Figure A1a–d, and the motion trails of the penetrator and the interceptor are shown in Figure 19.
2k 10 fp gk => ch E a al ak se İdi sx initial point = = = motion trajectory ok target area — interceptor trajectory static obstacle | 27 static obstacle 2 , , , , , i i i -2 0 2 4 6 8 10 12 x(m)
Figure 19. Simulation results in Webots.
14 of 17
Robotics 2022, 11, 35
It can be seen from the results above that the penetration algorithm proposed in this paper not only has a good performance in mathematical models, but also has feasibility in the Webots simulator.
# 5. Conclusions
In order to solve the problem that traditional methods-based robots cannot effectively break through the interception in a rejection environment, this paper proposes the DRL- based interception strategy. Aiming at addressing the issues of poor convergence of DRL, an incremental training method is proposed. The task is divided into three sub-tasks, and the agent is trained to gradually learn to survive, reach the target area, and break through the interception. Meanwhile, in order to reduce the difﬁculty of training and improve the training effect, reward compensation is adopted. The simulation results show that the introduction of reward compensation can unify the total return, which is beneﬁcial for the agent to converge to the optimal policy. The simulation results in Webots also demonstrate the feasibility of the proposed algorithm in practical applications. In contrast, APF-based agents can only bypass static obstacles, but cannot break through the interception of interceptors. Navigation in the 3D environment is challenging, and we intend to reﬁne this approach to make it applicable in our future work.
Author Contributions: Conceptualization, J.S. and K.Z.; methodology, K.Z. and Y.L. (Yuxie Luo); soft- ware, K.Z.; validation, K.Z., Y.L. (Yuxie Luo), and Y.L. (Yang Liu); formal analysis, J.S.; investigation, K.Z.; resources, K.Z. and Y.L. (Yang Liu); data curation, J.S.; writing—original draft preparation, K.Z.; writing—review and editing, K.Z.; visualization, K.Z.; supervision, J.S.; project administration, J.S.; funding acquisition, J.S. All authors have read and agreed to the published version of the manuscript.
Funding: This work was supported by the National Natural Science Foundation of China under Grants 62073020, 91646108 and 61473015.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
# Data Availability Statement: Not applicable.
Acknowledgments: The authors thank the colleagues for their constructive suggestions and research assistance throughout this study. The authors also appreciate the associate editor and the reviewers for their valuable comments and suggestions.
Conﬂicts of Interest: The authors declare no conﬂict of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or in the decision to publish the results.
# Abbreviations
The following abbreviations are used in this manuscript:
- RL Reinforcement Learning
- DRL Deep Reinforcement Learning
- DDPG Deep Deterministic Policy Gradient
- UAV Unmanned Aerial Vehicle
- LSTM Long Short-Term Memory
- MDP Markov Decision Process
- DQN Deep Q Network
- APF Artiﬁcial Potential Field
15 of 17
Robotics 2022, 11, 35
Appendix A. Simulation Results in Webots

‘ 1 f E fo | Bo b a ° | 1 o / / 2 o oY 4 “s 4 3 2 4 o 1 2 3 4 5 xin)
(a)

5 ‘ 1 / Gi / | Zo \ oO. } 1 \ / \ / a 4 4 “s 4 3 1 o 1 3 4 5 xin)
(b)

5 ‘ 3 a o 2 ya o 1 / Gi / | ze \ O j \ o , \ 4 “s 4 3 2 4 o 1 2 3 4 5 xin)
(c)

5 ‘ Ni fo 1 / Gi | | zh 6 a | 1 Ve 4 “s 4 3 1 o 1 3 4 5
(d)
Figure A1. Results in different stages in Webots. (a) The initial stage; (b) avoid the static obstacles; (c) break the interception; (d) reach the target area.
16 of 17
Robotics 2022, 11, 35
# References
- Zhang, H.; Huang, C.; Zhang, Z.; Wang, X.; Han, B.; Wei, Z.; Li, Y.; Wang, L.; Zhu, W. The Trajectory Generation of UCAV Evading Missiles Based on Neural Networks. In Journal of Physics: Conference Series; IOP Publishing: Bristol, UK, 2020; Volume 1486, p. 022025.
1.
- Yang, C.; Wu, J.; Liu, G.; Zhang, Y. Ballistic Missile Maneuver Penetration Based on Reinforcement Learning. In Proceedings of the 2018 IEEE CSAA Guidance, Navigation and Control Conference (CGNCC), Xiamen, China, 10–12 August 2018; pp. 1–5.
2.
- Yan, T.; Cai, Y.; Bin, X. Evasion guidance algorithms for air-breathing hypersonic vehicles in three-player pursuit-evasion games. Chin. J. Aeronaut. 2020, 33, 3423–3436. [CrossRef]
3.
- 4. Nguyen, H.; La, H. Review of deep reinforcement learning for robot manipulation. In Proceedings of the 2019 Third IEEE International Conference on Robotic Computing (IRC), Naples, Italy, 25–27 February 2019; pp. 590–595.
- Li, Y. Deep reinforcement learning: An overview. arXiv 2017, arXiv:1701.07274.
5.
6.
- Bu¸soniu, L.; de Bruin, T.; Toli´c, D.; Kober, J.; Palunko, I. Reinforcement learning for control: Performance, stability, and deep approximators. Annu. Rev. Control. 2018, 46, 8–28. [CrossRef]
- Dulac-Arnold, G.; Mankowitz, D.; Hester, T. Challenges of real-world reinforcement learning. arXiv 2019, arXiv:1904.12901.
7.
- Lillicrap, T.P.; Hunt, J.J.; Pritzel, A.; Heess, N.; Erez, T.; Tassa, Y.; Silver, D.; Wierstra, D. Continuous control with deep reinforcement learning. arXiv 2015, arXiv:1509.02971.
8.
9.
- Zhang, C.; Song, W.; Cao, Z.; Zhang, J.; Tan, P.S.; Xu, C. Learning to dispatch for job shop scheduling via deep reinforcement learning. arXiv 2020, arXiv:2010.12367.
- 10. Kober, J.; Bagnell, J.A.; Peters, J. Reinforcement learning in robotics: A survey. Int. J. Robot. Res. 2013, 32, 1238–1274. [CrossRef] 11. Lei, X.; Zhang, Z.; Dong, P. Dynamic path planning of unknown environment based on deep reinforcement learning. J. Robot. 2018, 2018, 5781591. [CrossRef]
- 12. Zhao, W.; Liu, H.; Lewis, F.L. Robust formation control for cooperative underactuated quadrotors via reinforcement learning. IEEE Trans. Neural Netw. Learn. Syst. 2020, 32, 4577–4587. [CrossRef] [PubMed]
- 13. Gao, J.; Ye, W.; Guo, J.; Li, Z. Deep reinforcement learning for indoor mobile robot path planning. Sensors 2020, 20, 5493. [CrossRef] [PubMed]
- 14. Choi, J.; Park, K.; Kim, M.; Seok, S. Deep reinforcement learning of navigation in a complex and crowded environment with a limited ﬁeld of view. In Proceedings of the 2019 International Conference on Robotics and Automation (ICRA), Montreal, QC, Canada, 20–24 May 2019; pp. 5993–6000.
- Faust, A.; Oslund, K.; Ramirez, O.; Francis, A.; Tapia, L.; Fiser, M.; Davidson, J. Prm-rl: Long-range robotic navigation tasks by combining reinforcement learning and sampling-based planning. In Proceedings of the 2018 IEEE International Conference on Robotics and Automation (ICRA), Brisbane, Australia, 21–25 May 2018; pp. 5113–5120.
15.
- Feng, S.; Sebastian, B.; Ben-Tzvi, P. A Collision Avoidance Method Based on Deep Reinforcement Learning. Robotics 2021, 10, 73. [CrossRef]
16.
- 17. Dai, P.; Yu, W.; Wen, G.; Baldi, S. Distributed reinforcement learning algorithm for dynamic economic dispatch with unknown generation cost functions. IEEE Trans. Ind. Inform. 2019, 16, 2258–2267. [CrossRef]
- 18. Wang, B.; Liu, Z.; Li, Q.; Prorok, A. Mobile robot path planning in dynamic environments through globally guided reinforcement learning. IEEE Robot. Autom. Lett. 2020, 5, 6932–6939. [CrossRef]
- 19. Busoniu, L.; Babuska, R.; De Schutter, B. A comprehensive survey of multiagent reinforcement learning. IEEE Trans. Syst. Man Cybern. Part C (Appl. Rev.) 2008, 38, 156–172. [CrossRef]
- 20. De Witt, C.S.; Peng, B.; Kamienny, P.A.; Torr, P.H.; Böhmer, W.; Whiteson, S. Deep multi-agent reinforcement learning for decentralized continuous cooperative control. arXiv 2020, arXiv:2003.06709.
- Silver, D.; Lever, G.; Heess, N.; Degris, T.; Wierstra, D.; Riedmiller, M. Deterministic policy gradient algorithms. In Proceedings of the 31st International Conference on Machine Learning, Beijing, China, 21–26 June 2014; pp. 387–395.
21.
- 22. Kumar, P.B.; Rawat, H.; Parhi, D.R. Path planning of humanoids based on artiﬁcial potential ﬁeld method in unknown environments. Expert Syst. 2019, 36, e12360. [CrossRef]
- 23. Degrave, J.; Felici, F.; Buchli, J.; Neunert, M.; Tracey, B.; Carpanese, F.; Ewalds, T.; Hafner, R.; Abdolmaleki, A.; de Las Casas, D.; et al. Magnetic control of tokamak plasmas through deep reinforcement learning. Nature 2022, 602, 414–419. [CrossRef] [PubMed]
17 of 17
