1380
IEEE TRANSACTIONS ON SMART GRID, VOL. 12, NO. 2, MARCH 2021
# Mobility-Aware Charging Scheduling for Shared On-Demand Electric Vehicle Fleet Using Deep Reinforcement Learning
Yanchang Liang , Student Member, IEEE, Zhaohao Ding , Senior Member, IEEE, Tao Ding , Senior Member, IEEE, and Wei-Jen Lee , Fellow, IEEE
Abstract—With the emerging concept of sharing-economy, shared electric vehicles (EVs) are playing a more and more important role in future mobility-on-demand trafﬁc system. This article considers joint charging scheduling, order dispatching, and vehicle rebalancing for large-scale shared EV ﬂeet operator. To maximize the welfare of ﬂeet operator, we model the joint decision making as a partially observable Markov decision pro- cess (POMDP) and apply deep reinforcement learning (DRL) combined with binary linear programming (BLP) to develop a near-optimal solution. The neural network is used to evaluate the state value of EVs at different times, locations, and states of charge. Based on the state value, dynamic electricity prices and order information, the online scheduling is modeled as a BLP problem where the decision variables representing whether an EV will 1) take an order, 2) rebalance to a position, or 3) charge. We also propose a constrained rebalancing method to improve the exploration efﬁciency of training. Moreover, we provide a tabular method with proved convergence as a fallback option to demon- strate the near-optimal characteristics of the proposed approach. Simulation experiments with real-world data from Haikou City verify the effectiveness of the proposed method.
Index Terms—Electric vehicle, deep reinforcement learning, order dispatching, rebalancing, charging scheduling.
- MDP Markov decision process
- POMDP Partially observable Markov decision process
- REV Revenue-based method
- RL Reinforcement learning
- SOC State of charge
- TD Temporal-difference.
Sets and Indices
# Ag,t
- Action space in grid g at time step t
- G Set of grids {1, 2, . . . , G} indexed by g, h
- Set of grids equipped with chargers, Gch ⊆ G
- Ig,t Set of available EVs {1, 2, . . . , Ig,t} indexed by j in grid g at time step t
- Jg,t Set of available dispatches {1, 2, . . . , Jg,t} indexed by j in grid g at time step t
# J ch
# If
# g,t
# J or
# g,t
# J re
# g,t
Set of charging dispatches, J ch
# ⊆ Jg,t
# g,t
# Set of order dispatches, J or
# ⊆ Jg,t
# g,t
Set of rebalancing dispatches, J re
# ⊆ Jg,t
# g,t
# t
# Index for time steps.
# Parameters
NOMENCLATURE
Acronyms
# BLP
- Binary linear programming
- CR Constrained rebalancing
- DRL Deep reinforcement learning
EV Electric vehicle
# Ire
g→h,t Number of EVs rebalanced from g to h at time step t Iin-ch g,t Jor g,t Number of EVs being charged in g at time step t Number of order dispatches in g at time step t lj Nch g pch g,t por Destination of dispatch j Total number of chargers in grid g Charging price of grid g at time step t Price of order dispatch j.
Manuscript received April 10, 2020; revised August 1, 2020; accepted September 9, 2020. Date of publication September 21, 2020; date of cur- rent version February 26, 2021. This work was supported in part by the National Natural Science Foundation of China under Grant 51907063; in part by the Fundamental Research Funds for the Central Universities under Grant 2019MS054; and in part by the Support Program for the Excellent Talents in Beijing City under Grant X19048. Paper no. TSG-00531-2020. (Corresponding author: Zhaohao Ding.)
Yanchang Liang and Zhaohao Ding are with the School Electrical and Electronic Engineering, North China Electric Power University, Beijing 102206, China (e-mail: liangyancang@gmail.com; zhaohao.ding@ncepu.edu.cn). of
Tao Ding is with the Department of Electrical Engineering, Xi’an Jiaotong University, Xi’an 710049, China (e-mail: tding15@xjtu.edu.cn).
# j
Variables
- ag,t Joint action of all available EVs in g at time step t
- sg,t Joint state of all available EVs in g at time step t
- AE; Change in SOC during EV i execution dispatch j
- Ati Duration for EV i to complete dispatch j
- ai,t Action of EV i at time step t
- bij Binary decision variable (bij = 1 if EV i matches dispatch j, else 0)
Wei-Jen Lee is with the Energy Systems Research Center, University of Texas at Arlington, Arlington, TX 76019 USA (e-mail: wlee@uta.edu).
Color versions of one or more of the ﬁgures in this article are available online at https://ieeexplore.ieee.org.
- Ei,t SOC of EV i at time step t
- li,t Location of EV i at time step t
- Return of EV i following time step t
# Ri,t
Digital Object Identiﬁer 10.1109/TSG.2020.3025082
- ri,t Reward of EV i at time step t
1949-3053 © 2020 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: University of London: Online Library. Downloaded on December 28,2024 at 23:18:31 UTC from IEEE Xplore. Restrictions apply.
LIANG et al.: MOBILITY-AWARE CHARGING SCHEDULING FOR SHARED ON-DEMAND EV FLEET USING DRL
- rij Cumulative discounted reward during EV i exe-
- cution dispatch j
- si,t State of EV i at time step t
- sij State of EV i after completing dispatch j.
Functions
- π(s) Deterministic policy function
# V(s; θ )
- State value function approximated by the neural network with parameters θ .
# π (s)
# V i
# State value function of EV i under policy π .
makes RL more suitable for real-time scheduling of large- scale ﬂeet [8]. As a model-free method, the training process of RL is based on historical experience (e.g., historical order data [9]) without the need to model transportation networks. In addition, RL is a commonly used method for sequential decision-making problems, which can well balance the ﬂeet’s immediate and future revenue. For example, greedily matching vehicles with long-distance orders can receive high immediate gain at a single order dispatching stage, but it might jeopardize future revenue because of its long drive time and unpopular destination [10]. However, one of the basic concepts of RL— state value—can naturally evaluate the future revenue of the vehicle in a certain spatiotemporal state.
# I. INTRODUCTION
I N RECENT years, the advent of large-scale shared on- demand ride-hailing platforms such as Uber and Didi Chuxing has greatly transformed the way people travel. At the same time, electric vehicles (EVs) have received widespread attention due to their lower pollution emissions and lower energy costs compared to gasoline vehicles, but the limited range and availability of charging infrastructure has hin- dered the application of EVs in private mobility. However, in combination with shared mobility-on-demand technology, managing EVs in the form of a ﬂeet can ensure that there are sufﬁcient number of vehicles with adequate energy to sat- isfy customers’ travel demands through intelligent charging scheduling, order dispatching and vehicle rebalancing, thereby eliminating “range anxiety”. Moreover, the development of such shared mobility-on-demand ﬂeets in large cities also has positive effects on mitigating parking and trafﬁc congestion problems [1].
Recently, RL has been applied to order dispatch of ride- hailing platforms [8], [10]–[13]. In [8], a learning and planning method was proposed and successfully deployed in Didi Chuxing’s production system, where the ofﬂine learning step applies dynamic programming to update the state value stored in a table, and the online planning step uses the state value to compute real-time matching through the Kuhn-Munkres (KM) algorithm [14]. Since tabular methods are severely limited by the curse of dimensionality, Shi et al. [11] used neural networks to replace the tabular method in [8] to represent state value function. For the same purpose, Tang et al. [12] proposed a new neural network structure, Cerebellum Value Network, to represent the state value function. RL combined with neural networks is often called deep RL (DRL). To cap- ture dynamic demand-supply variations, mean ﬁeld DRL [15] was used to approximate the interaction between the vehicle and its surrounding area [13].
In this article, we consider the welfare maximization problem for a shared on-demand EV ﬂeet operator. In gen- eral, there are three main scheduling tasks for operating an EV ﬂeet, namely (i) order dispatching, i.e., to match the orders and vehicles in real time to directly deliver the service to the users, (ii) vehicle rebalancing, to reposition some idle vehi- cles to other locations, and (iii) charging scheduling, i.e., to determine the charging location and time for each EV. These three types of scheduling are closely related to each other, e.g., EVs can choose appropriate order dispatching or rebal- ancing to transfer to a location with greater demand to increase future revenue, or to a charging station with low electric- ity prices to reduce charging costs. Some recent work has jointly optimized different types of scheduling. Zhang et al. [2] proposed a model predictive control (MPC) approach that opti- mizes order dispatching and rebalancing of the ﬂeet subject to energy constraints. Duan et al. [3] optimized order dispatch- ing and rebalancing based on network ﬂow model. In addition, Tsao et al. [4] proposed a stochastic MPC algorithm focusing on vehicle rebalancing. These methods have shown promising results. However, the detailed transportation network model may result in scalability issue.
Recent years witnessed tremendous success in reinforce- ment learning (RL) in modeling computational challeng- ing decision-making problems [5]–[7] that were previously intractable. The computational overhead required by RL to solve the multi-agent resource management problem is usually much smaller than that of operations research methods, which
RL was also applied to ﬂeet rebalancing [16] and charging scheduling [17], [18]. Lin et al. [16] proposed a contextual multi-agent DRL framework for rebalancing large-scale ﬂeet. Vandael et al. [17] used RL to solve the charging scheduling problem of EV ﬂeet. Ding et al. [18] proposed a DRL- based EV charging strategy to maximize the proﬁt of the distribution system operators while satisfying all the physi- cal constraints. In addition, Wan et al. [19] applied DRL to optimize charging/discharging scheduling for private EV.
Few works [10], [11], [20] used RL method to jointly optimize different types of scheduling for EV ﬂeet. Jin et al. [10] optimized joint order dispatching and rebal- ancing, but due to the limited stability of the hierarchical DRL used, its application in the real world is very chal- lenging [10]. In addition, they did not consider charging scheduling. Shi et al. [11] considered charging scheduling while optimizing order dispatching, but they used a positive constant reward to guide EV charging, which could not reﬂect the impact of locational electricity prices on charging behavior. The adopted KM algorithm presents challenges on incorpo- rating constraints for charging behavior (e.g., the number of available chargers should be limited). In addition, they did not consider the rebalancing of EV ﬂeet. Turan et al. [20] used DRL to solve the joint routing, charging and pricing problem of EV ﬂeet, where the input of neural network is the state of entire study area, and the output is the scheduling result of all EVs. But the state and action space of such a completely cen- tralized scheduling would be immensely huge. For instance,
Authorized licensed use limited to: University of London: Online Library. Downloaded on December 28,2024 at 23:18:31 UTC from IEEE Xplore. Restrictions apply.
1381
1382
IEEE TRANSACTIONS ON SMART GRID, VOL. 12, NO. 2, MARCH 2021
when the study area is divided into 10 nodes and the state of charge (SOC) is discrete to 6 levels, the dimension of state space has reached 1240 [20].
In order to facilitate joint optimization of different types of scheduling decisions, we treat each rebalancing or charging behavior as an order and assign it to EVs in the form of dis- patch. The difference is that one order dispatch is assigned to at most one EV, but one rebalancing or charging dis- patch can be assigned to multiple EVs. For large-scale EV ﬂeet, the state and decision space of the joint optimization problem is huge and dynamically changing, and cannot be solved directly using existing DRL algorithms (e.g., DQN [5], DDPG [21], SAC [22]). To this end, we model the joint optimization problem as a partially observable Markov deci- sion process (POMDP) [23], in which we evaluate the state value of each EV rather than the entire area to reduce the state space (i.e., policy evaluation). In order to reduce the decision space, we divide the study area into hexagonal grids for decentralized scheduling. We argue that this scheduling problem is different from the conventional Markov decision process (MDP) in that the state transition can be determined in advance. With this feature, we transform the collabora- tive scheduling of EVs in each grid into a binary linear programming (BLP) problem (i.e., policy improvement). We interactively perform policy evaluation and policy improve- ment (a common form of RL) [24] to develop a near-optimal scheduling policy. In policy evaluation, we use techniques such as neural network approximation and empirical replay mechanisms to improve computational and data efﬁciency [5], but lose the theoretical guarantee of convergence. We thus provide a convergent tabular method as a fallback option. An experimental comparison with the tabular method demon- strates that the proposed method has achieved near-optimal performance.
Our major contributions are listed as follows:
- 1) We propose a joint optimization framework for a large-scale shared on-demand EV ﬂeet operator as a POMDP which simultaneously considers charging scheduling, order dispatching and vehicle rebalancing decisions.
- 2) We develop a solution method utilizing DRL combined with BLP to obtain a near-optimal scheduling policy. The proposed method is tested with city-scale real-world data to illustrate its effectiveness. We also provide a con- vergent tabular method as a fallback option and give a proof of its convergence.
- 3) We propose a constraint method for vehicle rebalancing to reduce the exploration space in DRL training process, which can also be used to improve the performance of conventional scheduling methods.
The rest of this article is organized as follows. We for- mulate the joint optimization problem as a POMDP in Section II. Section III describes the speciﬁc implementa- tion methods of policy improvement and policy evaluation. In Section IV, simulation experiments based on real-world data from Haikou City are used to verify the effectiveness of the proposed method. Finally, we conclude the paper in Section V.
Wi Charging Ev © dvailbie EV > Rebalance > Charge 5 (a)
Fig. 1. Illustration of joint order dispatching, rebalancing, and charging scheduling in grid g at time step t. (a) All available dispatches; (b) Dispatches assigned to EVs.
# II. A POMDP FORMULATION
This article considers joint order dispatching, vehicle rebal- ancing, and charging scheduling for shared on-demand EV ﬂeet operator. As shown in Fig. 1, the study area is divided into hexagonal grids, denoted as G = {1, 2, . . . , G}, and each grid can serve as a trip origin or destination. The hexagonal grid has been widely used for ﬂeet scheduling problems [10], [12], [16] and its advantages are discussed in [25], [26]. We perform scheduling for EV ﬂeet at a series of discrete time steps, t = 0, 1, . . . , T−1 (T is the termination time of episode). The objective of scheduling optimization is to maximize the operator’s proﬁt, i.e., to increase the total order revenue and reduce the total charging cost. We consider each EV as an agent and model the joint scheduling problem as a POMDP in a fully cooperative setting, where the major components are deﬁned as follows.
1) State: We maintain a set of available EVs (not in ser- vice or charging) for each grid g ∈ G, denoted as Ig,t = {1, 2, . . . , Ig,t}. For example, the available EVs set for grid g in Fig. 1 is Ig,t = {1, 2, 3}. Since EVs are moving and entering/exiting available status at any time, set Ig,t changes over time. For each available EV i ∈ Ig,t, its state variable si,t consists of the current time step t, its location li,t and SOC Ei,t, i.e., si,t = [t, li,t, Ei,t]. The location li,t is repre- sented by the index of the grid where EV i is located, i.e., li,t = g ∀i ∈ Ig,t. Note that when an EV is not avail- able, we ignore its state. In addition, we use the state vector sg,t = [si,t]i∈Ig,t to represent the states of all available EVs in grid g.
2) Action: To facilitate joint optimization, we model each rebalancing or charging decision as an order and assign it to EVs in the form of dispatch. Speciﬁcally, we maintain a time-varying available dispatch set Jg,t = {1, 2, . . . , Jg,t} for each grid g, which includes order set J or g,t, rebalancing set J re g,t, and charging set J ch g,t , i.e., Jg,t = J or ∪ J re ∪ J ch g,t . For g,t g,t example, the available dispatch set for grid g in Fig. 1 includes J or = {1, 2}, J re = {3, 4, 5, 6, 7, 8, 9}, and J ch = {10}. At g,t g,t g,t each time step t, a dispatch decision from set Jg,t will be assigned to EV i, and this action is represented as a vector ai,t = [bij]j∈Jg,t , where element bij is a binary variable (bij = 1 if EV i matches dispatch j, else 0). For example, in Fig. 1(b), the action of EV 3 matching dispatch 7 is denoted as a3,t = [0 0 0 0 0 0 1 0 0 0].
We utilize matrix ag,t = [bij]i∈Ig,t,j∈Jg,t to represent the joint action of all available EVs in grid g. For the example shown
Authorized licensed use limited to: University of London: Online Library. Downloaded on December 28,2024 at 23:18:31 UTC from IEEE Xplore. Restrictions apply.
LIANG et al.: MOBILITY-AWARE CHARGING SCHEDULING FOR SHARED ON-DEMAND EV FLEET USING DRL

Fig. 2. State transition process of each EV.
- j ∈ J re
- *j € J: In this article, staying in the current hexag- onal grid is modeled as a special kind of rebalancing. Therefore, the destination /; of rebalancing dispatch j is the current grid or an adjacent grid. The time steps required to complete the rebalancing dispatch (Afj;) can be calculated in real time based on traffic conditions. For simplicity, in this paper we set Az = 1 [10], [16]. The change in SOC AE; can also be calculated from the mileage (AEj < 0). Since rebalancing is not gainable or payable, we set rj = 0.
in Fig. 1(b),
⎡
⎤
⎡
⎤
ag,t = ⎣ a1,t a2,t ⎦ = ⎣ 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ⎦ (1) a3,t 0 0 0 0 0 0 1 0 0 0
The generation of joint action needs to meet certain dispatch constraints, which we will discuss in Section III-A. We denote the action space that satisﬁes the dispatch constraints as Ag,t. Note that unlike the standard MDP, the action space Ag,t changes over time as it is affected by available EVs and available dispatches.
3) Reward and Return: Reward ri,t is deﬁned as the rev- enue (cost is treated as negative revenue) obtained by EV i in time step t. Return Ri,t is deﬁned as the cumulative discounted rewards of EV i from time step t until the end of the episode:
Ri,t = ri,t + γ ri,t+1 + · · · + γ T−t−1ri,T−1 (2)
where γ ∈ [0, 1] is the discount factor that is used to trade
off the importance between immediate and future rewards.
As shown in Fig. 2, the number of time steps EV i takes to complete dispatch j, denoted as Az, may sometimes be greater than 1, i.e., EV i requires multiple time steps to reach the next state, which is also called semi-MDP [27]. Similar to the standard MDP, there is a recursive relationship between returns in adjacent states:
Rig = Tir 4 Yaaa be Fy İriş ay + V9 (rics kek yi Atty 7) — ryt OUR ary (3)
where ri; is the cumulative discounted reward during EV i execution dispatch j. For example, if EV i matches the dispatch J that starts at t= 1 and has a duration Az; = 3 (as shown in Fig. 2), then rj = ri,.1 + 77,2 +7723, and Rj.) = r+ y>Ria-
(3)
- j ∈ J ch
- .jE Ji The charging dispatch destination /; is still the current grid g. It is assumed that once each EV i is dis- patched to charge, it will not leave until it is fully charged. Therefore, the change in SOC AE; = 1 — E;,, and the charging duration At = [AE;;/Pcy]. The charging cost per time step is the product of the electricity price and the change in SOC. The cumulative discounted reward during charging is the inverse of the total charging cost:
t+Atj—1 rm=— Yo vp AE: (5) t=
where Pee is the dynamic charging price of grid g in time step T, which is assumed to be obtainable or predictable. AE; is the change in SOC of EV i in time step t, which is equal to the charging power Pcp if SOC Ej, is not greater than 1, ie., AE;; = min(Pen, | — Ej,r).
In short, each EV i whose state is sj, = [t, Ji, Ej,;] at time step £ will transition to state Sirk = Ut + Ati, ii, Eig + AEjl (abbreviated as sj) at time step ¢+ At after completing dispatch j, and obtain a cumulative discounted reward of rij during this period. Both the reward rj and the new state sj can be determined before dispatch j is executed.
5) Policy and State Value Function: From the perspective of EV ﬂeet operator, the goal of the joint optimization problem should be to maximize the expected return of the entire ﬂeet. However, the state and action space of scheduling all EVs completely centrally is too large [20]. A common solution is to use a partially observable setting that ignores the states of other EVs when scheduling for each EV [8], [11]. Considering that there are mutual constraints on the actions of EVs in a grid, e.g., the number of available orders and chargers is limited, we jointly schedule EVs in each grid to facilitate their cooperation. The scheduling objective for each grid can be formulated as
4) State Transition In the fleet operation platform, if EV i matches dispatch j, the relevant information—dispatch des- tination /;, dispatch duration Afjj, change in SOC AE, and reward r;—can be calculated before the dispatch is performed:
max π i∈Ig,t Eπ Ri,t|si,t = max π i∈Ig,t V i π si,t (6)
- » J © Jey: The destination /;, duration Af, price Pi" and mileage of order dispatch j can be obtained by the fleet operation platform. The change in SOC AEj can be cal- culated from the mileage (AEj < 0). For an order with a price of Pe and a duration of Azj, the reward equally allocated to each time step is Pe / Afij, and the cumulative discounted reward for this order is
where π is a deterministic policy that maps from the state of each grid to a joint scheduling action, i.e., ag,t = π(sg,t) ∀g ∈ G. The expected return when EV i starts in si,t and follows π thereafter, i.e., Eπ [Ri,t|si,t], is deﬁned as the value function of π (si,t). According to (3), the relationship state si,t, denoted as V i between the value functions of adjacent states (i.e., Bellman equation for semi-MDP [27]) is
# t+Atj—1
t+Atj—1 Ti — > t= or rt Pi A 4)
# τ =t
Vİ (Si) = Ex [Riclsie] = Ex [rg + Ri als) = Erlrij + yV4 (siyasi). (0)
# V i
Authorized licensed use limited to: University of London: Online Library. Downloaded on December 28,2024 at 23:18:31 UTC from IEEE Xplore. Restrictions apply.
1383
(7)
1384
IEEE TRANSACTIONS ON SMART GRID, VOL. 12, NO. 2, MARCH 2021
# III. SCHEDULING POLICY
Policy evaluation and policy improvement are performed interactively to develop a near-optimal scheduling policy. Policy evaluation refers to the computation of the value func- tions for a given policy. Policy improvement refers to the computation of an improved policy given the value function for that policy. We will elaborate the implementation of these two processes in the proposed scheduling problem. For simplicity, we omit the subscript t for all variables in this section.
Grid a Grid g (6)
Fig. 3. EVs rebalance from grid g to h. (a) Unconstrained rebalancing; (b) Constrained rebalancing.
# A. Policy Improvement With Binary Linear Programming
Policy improvement is done by making the policy greedy with respect to the current value function [24]. We can formu- late an improved greedy policy based on the sum of the state values of all available EVs in a grid:
(Sg) = arg max EL ry + yA4Vi (sy)|si,ai] (8a) agcAy icT, = argmax Y | rg -yüvi (si) | (8b) agcAy icL,
1’
The reason why (8a) is equal to (8b) is that the reward rj and the new state sj; obtained after taking the action a; are determinable in the current scheduling problem (Section II-D). In (8b), rj is the instant reward of EV i execution dispatch j, and Vİ (sj) reflects the future rewards of EV i after executing dispatch j to reach a new state. Therefore, Eq. (8b) aims to take the action that maximizes the sum of short-term and long-term rewards of all EVs. The reward of EVs after episode ends is not considered, so when sj is the termination state of episode (corresponding time step f+ Ary > T), vi (sij) = 0. Therefore, we rewrite (8b) as
⎛
⎡
⎤
⎞
(a =4) - (4) X > bi; < max | 0, — ş — iel, je Tg #8 (118
#8
where Eg. (11a) constrains each bi; to a binary variable: If dispatch j is assigned to EV i, then bj = 1, otherwise bj = 0. Eq. (11b) indicates that each EV must be assigned with one dispatch. Eq. (11c) indicates that each order dispatch is assigned to at most one EV. In (11d), Ne is the total number of chargers in grid g (Neb > > 0), and yi “ch is the number of EVs being charged in grid g. This means that the number of EVs dispatched to charge in grid g cannot be greater than the number of available chargers. In (1le), A AES represents the change in SOC during the journey from "grid J; to the nearest charger (ap < 0), which ensures that each EV has a sufficient charge level to reach the nearest charger after completing an order or rebalancing. Eq. (11f) is a constraint on the number of rebalanced EVs, which is used to reduce the action space to improve the efficiency of exploration in policy evaluation, which will be described in detail next.
n' (sg) = arg max X Yi (9) a.cAy ; ET,
where
Sij is terminal . . Sij is non-terminal yy a ; vive (5H),
(10)
We use dispatch constraints to represent action space Ag, and use binary variable bij to directly represent the choice of dispatch. Then Eq. (9) can be rewritten as a BLP problem with decision variable ag = [bij]i∈Ig,j∈Jg :
arg maxbij i∈Ig j∈Jg yijbij (11)
subject to:
bij ∈ {0, 1} ∀i ∈ Ig, ∀j ∈ Jg (11a)
# by
For the two grids g and h as shown in Fig. 3, the destination of rebalancing dispatch in grid g is the original grid g or the adjacent grid h. If grid h has more incoming orders than g for a period of time in the future, rebalancing EV i to h is more likely to obtain higher return than g (as the energy cost due to moving to an adjacent grid is relatively small compared with service revenue), i.e., V i π (sij)|lj=h > V i π (sij)|lj=g ∀i ∈ Ig. In addition, the rewards for all rebalancing dispatches are 0, i.e., rij|lj=h = rij|lj=g = 0. Therefore, according to (10) and (11), each EV (except assigned to an order or a charging dispatch) will be rebalanced to grid h to increase the objective function, which will make the order demand in grid g unsatisfactory (as shown in Fig. 3(a)). In addition, during the evaluation of value π (sij)|lj=h is sometimes larger function, some errors, such as V i π (sij)|lj=g, will make some than, and sometimes smaller than V i EVs repeatedly rebalance in the two grids, which results in a waste of energy.
bij = 1 ∀i ∈ Ig (11b)
# j∈Jg
bij ≤ 1 ∀j ∈ J or g i∈Ig (11c)
ieT,
bij ≤ Nch g − Iin-ch g i∈Ig j∈J ch g (11d)
bi (Ei + AEy + BEP) > O Vie Ty. Wi e Tg" UTE (Ile)
(11e)
To cope with this problem, we constrain the number of rebalanced EVs by balancing the demand-supply gap between adjacent grids. At time step t, the number of available EVs in grid g, h is denoted as Ig, Ih, and the number of , Jor order dispatches is denoted as Jor h , respectively. Then the g − Ig and Jor − Ih, demand-supply gap in these two grids is Jor g h respectively. Without any rebalancing between the two grids, we predict that the demand-supply gap in the two grids at time
Authorized licensed use limited to: University of London: Online Library. Downloaded on December 28,2024 at 23:18:31 UTC from IEEE Xplore. Restrictions apply.
LIANG et al.: MOBILITY-AWARE CHARGING SCHEDULING FOR SHARED ON-DEMAND EV FLEET USING DRL
step t + 1 will still be Jor − Ig and Jor − Ih. In order to sat- g h isfy more orders as a whole, we assume that after rebalancing Ire g→h EVs from g to h at time step t, the demand-supply gap between the two grids will be balanced at time step t + 1 (as shown in Fig. 3(b)):
Jor g − Ig − Ire g→h = Jor h − Ih + Ire g→h (12)
Then we have
Ire g→h = Jor h − Ih − 2 Jor g − Ig (13)
Note that when the demand-supply gap of grids g and h are both positive, Ire g→h may still be a positive number, but at this time, the best policy in grid g may be to let all EVs serve the orders, i.e., Ire g→h should be 0. Therefore, we do not consider Ire g→h obtained by (13) as the speciﬁc number of rebalanced EVs but the upper limit number. Since Ire g→h may also be a fraction or a negative number, we round it up and set it to not less than 0, and ﬁnally write it as the constraint form shown in (11f). Adding reasonable constraints to rebalancing in this way can eliminate unreasonable actions in the action space to improve the efﬁciency of exploration, which we call con- strained rebalancing (CR). Note that CR can also be applied to conventional scheduling policies.
Algorithm 1 shows the training process of neural network V(s; θ ). To improve the stability of training, one technique is to use a target network to calculate the TD target value [5]. During initialization, we create a copy of the neural network V(s; θ ), denoted as ˆV(s; ˆθ ). Network ˆV(s; ˆθ ) is called the tar- get network, and original network V(s; θ ) is called the online network. During the training process, the parameters θ of online network are updated every step, but the parameters ˆθ of target network are updated every C steps (making it equal to the current θ ). With the target network, TD target value can be calculated as:
rij,
. Tij, Sij is terminal Yü = | ryt ys ö). Sij is non-terminal (5)
Another technique used to stabilize training and also improve data efﬁciency is the experience replay mecha- nism [29]. Speciﬁcally, we maintain a replay buffer D of capacity D for the entire EV ﬂeet. After getting a dispatch assignment, each EV i will store transition (si, rij, sij) in the replay buffer D. At each step of training, we randomly choose M transitions from D to form a mini-batch M. With the mini- batch, we can calculate the loss function L(θ ), which is deﬁned as the mean square error (MSE) between the TD target value and the estimated state value V(si; θ ):
# B. Policy Evaluation With Neural Networks
L(θ ) = 1 M (si,rij,sij)∈M ˆyij − V(si; θ ) 2 (16)
Given an estimated value function ˜V(s) for policy π , the
process of policy evaluation is to change it to be more like the true value function Vπ (s) for policy π . Temporal-difference (TD) prediction [28] is a commonly used method for policy evaluation:
Wp) — V(si) + ary + yü (si) — Vs) (14)
where w is the step size. rij + yi Vsip — Wsp), called the TD error, is used to measure the difference between the esti- mated value of s; and the better estimated rj + AtjV (sip). rt AtyV (si) is also called TD target value. TD prediction bases its update in part on an existing estimate, so it is a bootstrapping method [24].
Generally speaking, the value function can be a look-up table that directly stores values of states. However, in the cur- rent scheduling problem, the tabular method will suffer from the curse of dimensionality because of too many time steps and grids. In addition, the continuous variable Ei also makes the tabular method difﬁcult to handle. To this end, we use neural networks to approximate the value function. Another problem is that the excessive number of EVs makes it difﬁ- cult for us to maintain a value function for each EV. In this article, we assume that all the EVs are homogeneous, which is a quite common case for shared on-demand EV ﬂeets [8], [11]. In this way, all those EVs have the same battery capacity, power consumption, and travel speed, so that they can share the same value function V(s; θ ) approximated by the neural network, where θ are the parameters of the neural network. We train the network V(s; θ ) to make it more like the true value function of a given policy.
The parameters θ are updated by gradient descent to minimize the loss function:
# θ ← θ − lr∇θ L(θ )
(17)
where lr is the learning rate. Since the parameters θ are contin- uously updated, the policy generated by the state value V(s; θ ) is also continuously updated, which means that the transitions stored in the replay buffer are not generated by the same pol- icy. This way in which the evaluated policy differs from the policy used to generate data is called off-policy learning.
Since continuous exploration is the key to making policy evaluation work [28], we apply e-greedy policy to generate scheduling actions during the training process: Each grid g performs random action (randomly generate action a, under constraints (11a)-(11f)) with probability e, and greedy action (get action a, by solving (11)) with probability 1 — e. The probability e decays from | to 0.1 in steps of Ae and then remains unchanged at 0.1. Note that when testing a trained neural network, we do not add any exploration but apply a completely greedy policy, i.e., e = 0.
Similar to most popular DRL algorithms (e.g., DQN, DDPG, SAC), the proposed method applies three elements to improve performance: function approximation (i.e., neural networks) for scalability and generalization, bootstrapping for computational and data efﬁciency [24], and off-policy learning for experience replay. However, combining these three ele- ments may lead to instability and divergence [30]. For this reason, we present a tabular method in the Appendix as a fallback option. The tabular method eschews function approx- imation and off-policy, so it is susceptible to the curse of
Authorized licensed use limited to: University of London: Online Library. Downloaded on December 28,2024 at 23:18:31 UTC from IEEE Xplore. Restrictions apply.
1385
1386
IEEE TRANSACTIONS ON SMART GRID, VOL. 12, NO. 2, MARCH 2021
Algorithm 1: Policy Evaluation With Neural Networks
Initialize e = 1; Initialize replay buffer D with a capacity of D; Initialize network V(s; 0) with random parameters 0; Initialize target network Ws; 6) with parameters 6 <6; for episode = | to number of episodes do Receive initial state s; for each EV i; for time step t= 0 to T—1 do foreach grid ge G do foreach EV i € TZ, do foreach dispatch j € Jz do Calculate AEj, rij, siz; | Calculate yi; according to (10); Draw a sample u from uniform distribution U(O, 1); if u < ¢ then Randomly generate ag = [DijlicT,.je J under constraints (11a)—(11f); else Get ag = [bijlicT, jeg, by solving (11); foreach bij e a, do if bj = 1 then Assign dispatch j to EV i; | Store transition (6;, rij, 5i) in D; if e > 0.1 thene—e— Ag; Randomly choose M transitions from D to forma mini-batch M; Calculate target value Yi; according to (15); Calculate loss function L(0) according to (16); Update parameters 06 — 0 — IrVgL(0); Every C steps reset dö 6;
dimensionality and data inefﬁciency, but it can theoretically converge to a near-optimal policy. We give the speciﬁc steps and convergence proofs of the tabular method in the Appendix. Fortunately, many experiments have shown that DRL algo- rithms like DQN and DDPG, which have no theoretical convergence guarantees, can learn near-optimal policies [31], [32]. We will show that the proposed method also achieves near-optimal performance in an experimental comparison with the convergent tabular method (Section IV-C).
# IV. CASE STUDY
A. Experimental Settings
The study area is the center of Haikou City as shown in Fig. 4, which is approximately divided into 133 hexag- onal grids. We assume that there are 20 grids equipped with chargers, which constitute three rechargeable areas (indicated by three different colors), denoted as Gch 1 {17, 46, 48, 65, 67, 80, 102}, Gch = {10, 12, 36, 51, 53, 56, 58} 2 and Gch = {89, 92, 105, 109, 112, 133}, respectively. All grids 3 in each charging area are set to have the same electricity = price. We appropriately scale the electricity price data of three

Fig. 4. The center of Haikou City divided into 133 hexagonal grids.
time step sare value location ) © one-hot Ni 4 neurons soc 4 eco <7 1 an © one-hot | i = ; Ni i! 128 neurons
Fig. 5. Neural network architecture for estimating state value.
different buses in PJM [33] to simulate charging electricity prices. We set the number of chargers in each rechargeable grid Nch g = 12, and the power of each charger Pch = 30kW. The total number of EVs is set to 800. The characteristics of EVs are modeled after Beiqi New Energy EU300 with a battery capacity of 45kWh and a range of 300km. The initial EV position is randomly placed, and the initial SOC bounded between 0.2 and 0.8 is sampled from N (0.5, 0.12) [19]. Each time step is set to 15 minutes, but higher accuracy can be used in actual scheduling. Considering that a charging behav- ior may affect the rewards for more than one day, we set each episode to one week, i.e., T = 672.
The data provided by Didi Chuxing [9] includes on-demand orders in the center area of Haikou City for 26 consecu- tive weeks (2017/05/01–2017/10/29). The order information includes order generation time, price, origin, destination and duration. We randomly select about 1.6 × 105 orders at a time from the dataset and compose an episode (a week) based on the order generation time (day of week, time of day). Notice that the random seeds used in the training phase and the testing phase are different. We set that each order will be cancelled if it is not serviced within half an hour after it is generated. Fig. 6 shows the cumulative order requests for the entire study area within a week. It can be seen that there is more demand for orders on the right side of the area. Combined with the distri- bution of chargeable areas, we can ﬁnd that Gch > Gch 2 3 in terms of order demand. Fig. 7 shows the change in order demand over time in the entire study area. It can be seen that 14:00–19:00 is the peak period of order demand > Gch 1 every day.
Authorized licensed use limited to: University of London: Online Library. Downloaded on December 28,2024 at 23:18:31 UTC from IEEE Xplore. Restrictions apply.
LIANG et al.: MOBILITY-AWARE CHARGING SCHEDULING FOR SHARED ON-DEMAND EV FLEET USING DRL

>. Proposed method ö —-Proposed method without CR. «-DRL-based order and charging dispatch 3 4 5 6 7 8 9 10 Episode
Fig. 6. Number of order requests for different locations during the week.
Fig. 8. Episodic average cumulative reward of EV ﬂeet over 6 different random seeds during training. Error bars are the 95% conﬁdence intervals.
0 96 192 288 384 480 576 672 t
Fig. 7. Number of order requests per time step in the study area.
g 400 a —Proposed | Proposed without CR E 300 -—DRL-based order and charging dispatch z —REV a — REV with rebalancing g ZU —REV with CR “3 100 5 0 96 192 288 384 480 576 672 t
The neural network used to approximate the state value function is shown in Fig. 5, which has 3 hidden layers with 128, 64, and 32 neurons respectively. We apply rectified linear unit (ReLU) [34] to each layer. At the input layer, the discrete state variables (i.e., time step t and location /;,,) are represented with one-hot encoding. The Adam optimizer [35] is used for learning the neural network parameters with a learning rate Ir = 0.001. The other hyperparameters during training are as follows: the number of episodes is 10, the capacity of replay buffer D = 5 x 10°, the discount factor y = 0.9, and the decay step size of the exploration probability Ag = 1.5 x 10-4,
Fig. 9. Average cumulative reward of EV ﬂeet over 6 different random seeds during testing.
- • DRL-based order and charging dispatch: This method is a state-of-the-art DRL-based EV ﬂeet scheduling algo- rithm [11]. The method was proposed without taking into account the fact that the number of chargers is limited, so in this article there will be a queue of EVs waiting for charging.
- • Proposed method without CR: The only difference from the proposed method is that we do not constrain the number of EVs rebalanced to other grids.
The BLP problem is written and solved in Python with Gurobi [36], and the neural networks are trained in Python with Pytorch [37], an open source deep learning platform. All experiments are carried out on a computer with a 10-core 3.70 GHz Intel Core i9-10900X processor and 32 GB of RAM.
- B. Performance Comparison
We veriﬁed the performance of proposed method by com- paring with several benchmark algorithms:
- • Revenue-based method (REV): This method is often used as a benchmark for order dispatching algorithms, meaning that orders with higher prices will be given pri- ority to get dispatched ﬁrst [10], [13]. In order to apply to the EV ﬂeet in this article, we set that each EV will be charged when there is no order in the current grid and there is a charger available, otherwise it will stay in the current grid.
- • REV with rebalancing: Based on REV, we set that when the current grid has no orders and no charger is avail- able, EV will move to the neighboring grid with a larger demand-supply gap.
- • REV with CR: Based on REV with rebalancing, we con- strain the number of EVs rebalanced to other grids as in (11f).
- • Proposed method: Our proposed model as detailed in Section III.
The training results of the three DRL-based methods are shown in Fig. 8. One can seen that the use of CR signiﬁcantly improves the efﬁciency of exploration (the performance of the initial episodes are improved) and increases the cumulative reward of ﬁnal convergence. In addition, the method with- out rebalancing (i.e., DRL-based order and charging dispatch) performed worse than the other two methods.
The test results of all methods are shown in Fig. 9. One can seen that the cumulative reward of proposed method is higher than other methods. In addition, the methods without rebalancing (REV, DRL-based order and charging dispatch) are relatively low, while the methods with CR (REV with CR, proposed method) are higher than the methods with conven- tional rebalancing (REV with rebalancing, proposed method without CR).
The one-day trajectory of an EV during the testing phase of different methods is shown in Fig. 10. The starting loca- tion for this EV is the lower left corner of the map where order demand is low. Under the proposed method (Fig. 10(a)), the EV is gradually shifted from the lower left corner to a higher demand area for more order revenue by performing a series of rebalancing dispatches. For the proposed method without CR (Fig. 10(b)), the EV can be rebalanced to areas
Authorized licensed use limited to: University of London: Online Library. Downloaded on December 28,2024 at 23:18:31 UTC from IEEE Xplore. Restrictions apply.
1387
1388
IEEE TRANSACTIONS ON SMART GRID, VOL. 12, NO. 2, MARCH 2021
— Order dispatch — Rebalancing dispatch 96> | Charging dispatch 72 ~ 48- 24 @
va aa 340 wv ze S$ -+-Proposed method Cumulative reward (k$) 320 Proposed method withont target network —-Proposed method without experience replay 1 2 3 4 5 6 7 8 9 10 Episode
Fig. 11. Impact of the target network and experience replay mechanism on the proposed method. Error bars are the 95% conﬁdence intervals across 6 random seeds.
€ 380 g = 360 z 2 2 340 z E320 ö 1 2 3 4 5 6 7 8 9 10 Episode
Fig. 12. Impact of the discount factor on the proposed method. Error bars are the 95% conﬁdence intervals across 6 random seeds.
lack of vehicle rebalancing prevents the EV from proactively shifting to high-demand areas for additional revenue.
# C. Stability of Training
This subsection analyzes the factors that affect the training stability of the proposed method, including the target network, experience replay mechanism, and discount factor. In addi- tion, comparison with a convergent tabular method is used to reﬂect the near-optimal performance achieved by the proposed method.
Fig. 11 shows the impact of the target network and experi- ence replay mechanism on the proposed method. The absence of experience replay signiﬁcantly reduces the average cumu- lative reward (by 7.05%), while absence of target network reduces it not so much (by 0.86%). The absence of any of these increases the conﬁdence interval, i.e., makes the training unstable.
Fig. 10. The one-day trajectory of an EV during the testing phase of different methods. (a) Proposed method; (b) Proposed method without CR; (c) REV with CR; (d) DRL-based order and charging dispatch.
Fig. 12 illustrates the impact of the discount factor γ on the performance of the proposed method. A low discount factor can cause agent to prioritize excessively immediate rewards and become myopic to future rewards [24]; however, targeting a high discount factor may lead to instability or divergence in the state value function estimates, yielding a poor quality policy [38]. Fig. 12 shows that when γ = 0.9, the proposed method achieves an effective tradeoff between the above two effects, converging to a more proﬁtable policy.
of high demand but sometimes the rebalancing is repeated between adjacent grids (black dashed circles), resulting in a waste of energy. For REV with CR (Fig. 10(c)), the EV can also be rebalanced to areas of high demand, but this process is circuitous due to the lack of guidance from the state value function (see Fig. 15 for state values at different locations). As for DRL-based order and charge dispatch (Fig. 10(d)), the
We compare the proposed method with the tabular method provided in the Appendix. In the tabular method set- i.e., Ei,t ∈ ting, we discretize the SOC into 11 levels, {0, 0.1, 0.2, . . . , 1}, and set the thresholds δ = 2.0 and δ = 1.5, respectively. The threshold δ determines the accu- racy of the policy evaluation. Fig. 13 shows the experimental results. It can be seen that the smaller the threshold δ, the
Authorized licensed use limited to: University of London: Online Library. Downloaded on December 28,2024 at 23:18:31 UTC from IEEE Xplore. Restrictions apply.
LIANG et al.: MOBILITY-AWARE CHARGING SCHEDULING FOR SHARED ON-DEMAND EV FLEET USING DRL
380 w Ss Proposed method +-Tabular method (6 = 2. / —-Tabular method (6 = 1.5) 1 10 20 30 40 50 Episode w Dsi Ss Cumulative reward (k$) we g s
Fig. 13. Episodic average cumulative reward of EV ﬂeet for the proposed method and tabular method. Error bars are the 95% conﬁdence intervals across 6 random seeds.
TABLE I COMPUTATIONAL TIME TO REACH CONVERGENCE OF THE PROPOSED METHOD AND THE TABULAR METHOD
—S$0C=0.8 —SOC=0.4 —SOC=0.05 vy ln nl Pe \ / ig Fron, N 0 x —+t = 60 (15:00) g t = 66 (17:30) 4 t = 76 (19:00) 5 ee a | oz n n 1 4 0 0.2 0.4 0.6 0.8 1 SOC (b)
Total time Number of Average time Method . . N (min) episodes o per episode (min) Proposed method 177.38 10 17.74 Tabular method (6 — 2.0) 321.29 30 10.71 Tabular method (6 — 1.5) o 575.82 50 11.52
Fig. 14. Change in state value of grid 55 over time and SOC. (a) Time; (b) SOC.
slower the convergence of the tabular method, but the higher the cumulative reward after convergence. In addition, the tab- ular method has a smaller conﬁdence interval, i.e., higher stability, but converges signiﬁcantly slower than the proposed method. Table I also shows that the total computational time required for the tabular method to reach convergence exceeds that of the proposed method. The slow convergence is due to the fact that the tabular method only updates one state value estimate per update, so EVs need to visit each state and try each action multiple times to get a good estimate. Therefore, the tabular method, although convergent, is computationally and data inefﬁcient and can be used as a fallback option in case the proposed method is not convergent. Fortunately, Fig. 13 shows that the proposed method converges well and outperforms the tabular method in terms of average cumula- tive rewards over 50 episodes. The tabular method has been proven to converge to a near-optimal policy (Appendix), which means that the proposed method also achieves a near-optimal performance.
(b)
Fig. 15. State value at different locations. (a) SOC = 0.8; (b) SOC = 0.05.
# D. State Value Analysis
We analyze the changes in state value over time, SOC, and location based on trained neural network. Fig. 14 shows the state value in grid 55 as a function of time and SOC. Fig. 14(a) reﬂects that the change in state value is similar every day: it is higher before the peak demand period and lower before the peak charge period (at about t = 96, i.e., 24:00). Figs. 14(a) and (b) both reﬂect a positive correlation between state value and SOC. In addition, comparing curve t = 60 (15:00) and curve t = 66 (17:30) in Fig. 14(b), it can be found that when SOC > 0.2, the state value is similar, but as SOC approaches 0, the downward trend of curve t = 66 (17:30) is more obvi- ous. This is because it is only 1.5 hours from 17:30 to the end of the peak demand (as shown in Fig. 7), so the EV with small SOC will lose this important order revenue because it needs to be charged ﬁrst.
We next analyze the state value in different locations. Fig. 15 shows the state value of two different SOCs at 08:00 on Thursday. It can be seen that when SOC = 0.8, the state value near the high-demand area is higher, but when SOC = 0.05, the rechargeable grids, especially the grids with lower elec- tricity prices (see Fig. 16(a) for charging prices), have higher state value.
- E. Impact of Different Electricity Pricing Mechanisms
We analyze the impact of four different electricity pricing mechanisms on charging behavior:
- • Price varies both with time and location. This is the default setting. As described in Section IV-A, the charg- ing price changes every time step and varies from one rechargeable area to another.
Authorized licensed use limited to: University of London: Online Library. Downloaded on December 28,2024 at 23:18:31 UTC from IEEE Xplore. Restrictions apply.
1389
1390
IEEE TRANSACTIONS ON SMART GRID, VOL. 12, NO. 2, MARCH 2021
250 Hs Number of charging EVs in Gi (BE Number of charging EVs in Gi 55 Number of charging EVs in Gö» 200 —Total number of available orders / 10 — Charging price in G# —Charging price in G3" Sharging price in Gj? 0 4 8 12 16 20 24 Hour (b) 150 Sİ bi 048 © & 100 ROJ İzi a 028 50 a 0 0 0 4 8 12 16 20 24 Hour (d)
Fig. 16. The variation in the number of charging EVs during a typical day for different pricing mechanisms. (a) Price varies both with time and location; (b) Price does not vary with time but with location; (c) Price varies with time but not with location; (d) Price varies neither with time nor with location.
also plotted the total number of available orders and the elec-
tricity price of each rechargeable area during this period. For prices that vary with time and location, Fig. 16(a) shows that in the early morning hours when electricity prices and demand are lower, there are more EVs charged, while in the after- noon and evening hours when electricity prices and demand are higher, fewer EVs are charged. In addition, it can be seen that the number of charging EVs in area Gch is generally the 1 largest. This shows that although area Gch is far from the 1 high-demand area, its lower electricity price still attracts a large number of EVs by choosing a series of movable dis- patches (order or rebalancing dispatch) to be recharged here. Comparing Figs. 16(a) and (b), it can be seen that the charg- ing behavior does not change much after the price change cycle becomes one day. This is because the impact of price and demand on charging behavior is similar. For example, the order demand and electricity price every afternoon are high, and any of these factors will hinder EV charging. Figs. 16(c) and (d) reﬂect that when the price of the entire area is the same, the number of EVs selected to charge in area Gch 1 greatly reduced, which is because area Gch 1 is far from the high- is demand area. In addition, Fig. 16(d) reﬂects that the charging distribution is no longer affected by price ﬂuctuations and the randomness is reduced.
# V. CONCLUSION
In this article, we model the joint optimization framework combining charging scheduling, order dispatching and vehi- cle rebalancing for large-scale shared on-demand EV ﬂeet operator as a POMDP, and develop a near-optimal solution method based on DRL and BLP. A simulation experiment based on city-scale real-world data from Haikou City shows that the overall proﬁt can be signiﬁcantly increased by coordi- nating those scheduling decisions and dynamically responding to order demand and charging prices, such as rebalancing EVs to high demand areas (or low electricity price areas) to increase order revenue (or reduce charging costs). In addition, the proposed constrained rebalancing method signif- icantly improves the exploration efﬁciency of training and can improve the performance of conventional policies. Moreover, we provide a tabular method with proved convergence as a fallback option to demonstrate the near-optimal characteristics of the proposed approach.
- • Price does not vary with time but with location. The new charging price is the average price of all time steps in one day.
- • Price varies with time but not with location. The new charging price is the average price for the entire study area.
Future work can be model the scheduling process in more detail: For order dispatching, we will consider that an EV can simultaneously carry multiple passengers with different des- tinations; for charging scheduling, we will consider that EVs can be discharged to the grid for participating power mar- ket. In addition, we will consider beneﬁts to participants other than EV ﬂeet operator, such as passenger waiting costs, to maximize social welfare.
- • Price varies neither with time nor with location. The new charging price is the average price of all time steps throughout the study area in one day.
# APPENDIX
# CONVERGENT TABULAR METHOD
The variation in the number of charging EVs during a typi- cal day for different pricing mechanisms is shown in Fig. 16. In order to analyze the distribution of charging behavior, we
We provide a tabular method for the EV ﬂeet scheduling problem as shown in Algorithm 2. Due to the use of tables, we have to discretize the continuous state variable SOC, which
Authorized licensed use limited to: University of London: Online Library. Downloaded on December 28,2024 at 23:18:31 UTC from IEEE Xplore. Restrictions apply.
LIANG et al.: MOBILITY-AWARE CHARGING SCHEDULING FOR SHARED ON-DEMAND EV FLEET USING DRL
1391
# Algorithm 2: Tabular Method for EV Fleet Scheduling
Algorithm EV Scheduling 1 For all se S, V(s) — 0, V’(s) — oo; 2 Policy Evaluation: For all s e S, N(s) — 0; while ||V’ — Vil.o > 5 do Vel; for time step t= 0 to T—1 do foreach a; € 7(s,) do Take action a;, observe rj and sjj; N(si) — N(si) + 1; V(si) — Vos) + yoy ly ty iV(sy) — Vis] 3 Policy Improvement: policy-stable — true; foreach s, € S, do old-action — 1 (Sg); (8g) — argmax,, Diez, [ij + yIV (sis if old-action # (sg) then policy-stable < false; if policy-stable then stop and return V and z else go to 2;
converges to zero with probability 1 (w.p.1) under the follow- ing assumptions: leftmargin=*
- 1) The state space is ﬁnite;
- 2) 0 ≤ αn(x) ≤ 1,
# αn(x) = ∞, and
# α2
(x) < ∞;
- 2) 0 < a(x) < 1,0, n(x) = 00, and X,, a2 (x) < 00;
# n
# n
# n
- 3) |ELFn@)|Falllw <vllOnllw +en, where y € (0, 1) and Cn converges to zero w.p.1;
4) var[Fn(x)|Fn] < KA + Onl?) with constant K > 0. Here F, denotes the filtration of an increasing sequence of o-fields including the history of processes; a, On, Fn € Fn and || - ||w is a weighted maximum norm [39].
Proof: See [40, Th. 1] and [41, Corollary 5] for detailed derivation.
Lemma 2: Let 7 and x’ be any pair of deterministic
policies such that, for all s ∈ SG,
x’ (s) = arg max E[r, + y Vz (8;41)|8, a] a
Then V, > Vx. Moreover if 7 is not optimal, strict inequality holds in this inequality for at least one state.
Proof: See [24].
For the policy evaluation in Algorithm 2, we deﬁne the n-th updated value of N(s) to be αn(s), then αn(s) = 1 1 n . We next prove that the policy evaluation is convergent:
# m
is often used in previous methods [1], [20]. In this way, the scheduling problem satisﬁes the deﬁnition of a ﬁnite MDP: the sets of states, actions, and rewards all have a ﬁnite number of elements. In addition, the tabular setting no longer relies on the experience replay mechanism, which is used to stabilize the training of neural networks but requires off-policy learning. Based on these, we will prove the convergence of the tabular method.
Theorem 1: For any ﬁnite MDP with a given policy π and the current estimated value function V(s), the policy evaluation algorithm given by
Vu (si) = Vals) + ns) [ry yü Va (si) — Vn(si)] (18)
converges to the true value function Vπ (s) w.p.1 provided αn(s) = 1 n and γ ∈ [0, 1).
Proof: We start by rewriting (18) as
Vn41(si) = (1 — pls) Vasi) + on(si) [rj + ¥*"Vn(sif)]
In order to facilitate the proof, we first describe the joint scheduling problem from the perspective of the entire fleet: At each time step t the EV fleet receives a global state s, € Sg, takes an action a; = aile, TI and receives a scalar reward =). Yer; Fiş, Where Tf denotes the set of all EVs (including available and unavailable EVs) in grid g.
We start from introducing the assumptions:
Assumption 1: Each state is visited inﬁnitely often.
Assumption 2: The state value function of the entire EV fleet V,,(s) equals the summation of the individual EVs’ state value functions, i.e., Vz(s) = >, Birş V (si).
To apply Lemma 1 we subtract V,(5) from both sides of the above equation. If we write ©,(s) = V,(s) — Vr(s) and Fy(s) = ry + y“Vn(si) — Vz (5), we have On41(s) = (1 = an(s))On(s) + On()Fn(s).
The harmonic series is a divergent infinite series, i.e., nel i = oo. Notice that since a,(s) = i < 1, y, An(s) = o requires that all states be visited infinitely often. 17, @2(s) = DD İS convergent with an exact sum of 7 [42],
6 [42].
The error reduction property of multi-step returns [24] guarantees that for any Af; > 1,
Assumption 3: All EVs are homogeneous, i.e., they have same the battery capacity, power consumption, and travel speed, so that they can share the same state value func- tion V(s).
Note that Assumptions 2 and 3 have been used to address the curse of dimensionality of dealing with the entire ﬂeet’s state domain [8], [11], [13]. We have also used these two assumptions in our proposed DRL-based method: Assumption 2 for formulating a decentralized scheduling pol- icy (Section II-E) and Assumption 3 for sharing the neural network (Section III-B).
max|E, [Fn(si)|si = sll = max| Ezlrij + yy, (sy)lsi > 8] — Vx (s)]| = yi maxl V, (5) — Ve (3)|
which means the multi-step look-ahead reward gives a smaller worst-case error in the estimation of the true value function. It is now immediate from the above formula that
ELF n(s)|Fallloo < ¥ "I Vn (8) — Vir (Yag < YİV) — Vela = Yl @nlloo
Our proof is also built upon the two lemmas as follows: Lemma 1: The random process {@,} defined in R as
On) = CL — Gn (X))On(®) + On (0) Fn)
Finally,
var[Fn(s)|Fn] = E (Fn(s) − E[Fn(s)])2|Fn
Authorized licensed use limited to: University of London: Online Library. Downloaded on December 28,2024 at 23:18:31 UTC from IEEE Xplore. Restrictions apply.
1392
IEEE TRANSACTIONS ON SMART GRID, VOL. 12, NO. 2, MARCH 2021
= B| (ri + yi Vn(sis) — Vz(5) = Elry + v4 Va(sig)] + Ve OZ) = Bİ (ry + v9 Vasi) — El + "Val si)]) IF] = varlrij yasi Arl
Noting that Assumption 1 is difﬁcult to implement in prac- tice, we use a small threshold δ, as shown in Algorithm 2, to determine the accuracy of policy evaluation. Therefore, Algorithm 2 converges to a near-optimal policy in practice.
# ACKNOWLEDGMENT
which, due to the fact that rij is bounded, clearly veriﬁes
The authors thanks for the support of data source from Didi Chuxing GAIA Initiative.
varlFy(s)|Fnl < K(1 + Nesli)
for some constant K.
Then, by Lemma 1, ©, converges to zero w.p.1, i.e., V,(s)
converges to Vπ (s) w.p.1.
We ﬁnally prove the convergence of Algorithm 2:
Theorem 2: Algorithm 2 converges to an optimal policy under Assumptions 1, 2, and 3.
# REFERENCES
- [1] F. Rossi, R. Iglesias, M. Alizadeh, and M. Pavone, “On the interaction between autonomous mobility-on-demand systems and the power network: Models and coordination algorithms,” IEEE Trans. Control Netw. Syst., vol. 7, no. 1, pp. 384–397, Jan. 2019.
- [2] R. Zhang, F. Rossi, and M. Pavone, “Model predictive control of autonomous mobility-on-demand systems,” in Proc. IEEE Int. Conf. Robot. Autom. (ICRA), 2016, pp. 1382–1389.
Proof: The goal of the joint optimization problem should be ﬁnding the optimal policy to maximize the expected total return of EV ﬂeet, i.e., state value Vπ (s). According to Lemma 2, maximizing E[rt + γ Vπ (st+1)|s, a] can achieve non-decreasing Vπ (s), and we decompose maxa E[rt + γ Vπ (st+1)|s, a] as follows:
E rt + γ Vπ (st+1)|s, a max a (19a)
= max E ri,t + γ Vπ si,t+1 a i∈I+ g g |si, ai (19b)
ri,t + γ Vπ = E si,t+1 max ag i∈I+ g g |si, ai (19c)
= = max X Eli + ¥ Vie (Sir41) 15%. ai] = XI Vit ty Va (si, ij) ieT, 8 ieT; (19d)
- [3] L. Duan, Y. Wei, J. Zhang, and Y. Xia, “Centralized and decentralized autonomous dispatching strategy for dynamic autonomous taxi opera- tion in hybrid request mode,” Transp. Res. C Emerg. Technol., vol. 111, pp. 397–420, Jan. 2020.
- [4] M. Tsao, R. Iglesias, and M. Pavone, “Stochastic model predictive con- trol for autonomous mobility on demand,” in Proc. IEEE 21st Int. Conf. Intell. Transport. Syst. (ITSC), 2018, pp. 3941–3948.
- [5] V. Mnih et al., “Human-level control through deep reinforcement learning,” Nature, vol. 518, no. 7540, pp. 529–533, 2015.
- [6] D. Silver et al., “Mastering the game of go with deep neural networks and tree search,” Nature, vol. 529, no. 7587, p. 484, 2016.
- [7] D. Silver et al., “Mastering the game of go without human knowledge,” Nature, vol. 550, no. 7676, pp. 354–359, 2017.
- [8] Z. Xu et al., “Large-scale order dispatch in on-demand ride-hailing plat- forms: A learning and planning approach,” in Proc. 24th ACM SIGKDD Int. Conf. Knowl. Disc. Data Min., 2018, pp. 905–913.
- [9] Data Source: Didi Chuxing GAIA Initiative. Accessed: Nov. 17, 2019. [Online]. Available: https://gaia.didichuxing.com
- [10] J. Jin et al., “CORIDE: Joint order dispatching and ﬂeet management for multi-scale ride-hailing platforms,” in Proc. 28th ACM Int. Conf. Inf. Knowl. Manag., 2019, pp. 1983–1992.
- [11] J. Shi, Y. Gao, W. Wang, N. Yu, and P. A. Ioannou, “Operating electric vehicle ﬂeet for ride-hailing services with reinforcement learn- ing,” IEEE Trans. Intell. Transp. Syst., early access, Oct. 21, 2019, doi: 10.1109/TITS.2019.2947408.
where i ∈ I−
where i e Z, denotes the set of unavailable EVs (in service or charging) in grid g. Based on Assumptions 2 and 3, we can rewrite (19a) as (19b). Since only available action for each EV i € Zz is to continue to execute its current dispatch, we can decompose (19c) into (19d), and only need to maximize the first item of (19d). For the same reason, deciding the action of EV i € TZ, at the next time step is equivalent to deciding which dispatch the EV will perform next, ice., maXa, Lier, Elri, 4 Vx (Sit+1)Ii, Gi] = maxa, Diez, Elrij + YİV Gsi)lsi, a. In the current scheduling problem, the reward rj and th new state sj obtained after taking action a; can be deter- mined in advance, which means that the expected value is sti equal to itself, ie., maxa, Diet, E[ry + yO V! (sipsi, ai] = maxa, ier, [rg VİVE Gi). ie I
- [12] X. Tang et al., “A deep value-network based approach for multi-driver order dispatching,” in Proc. 25th ACM SIGKDD Int. Conf. Knowl. Disc. Data Min., 2019, pp. 1780–1790.
- [13] M. Li et al., “Efﬁcient ridesharing order dispatching with mean ﬁeld multi-agent reinforcement learning,” in Proc. World Wide Web Conf., 2019, pp. 983–994.
- [14] J. Munkres, “Algorithms for the assignment and transportation prob- lems,” J. Soc. Ind. Appl. Math., vol. 5, no. 1, pp. 32–38, 1957.
- [15] Y. Yang, R. Luo, M. Li, M. Zhou, W. Zhang, and J. Wang, “Mean ﬁeld multi-agent reinforcement learning,” 2018. [Online]. Available: arXiv:1802.05438.
- [16] K. Lin, R. Zhao, Z. Xu, and J. Zhou, “Efﬁcient large-scale ﬂeet manage- ment via multi-agent deep reinforcement learning,” in Proc. 24th ACM SIGKDD Int. Conf. Knowl. Disc. Data Min., 2018, pp. 1774–1783.
- [17] S. Vandael, B. Claessens, D. Ernst, T. Holvoet, and G. Deconinck, “Reinforcement learning of heuristic EV ﬂeet charging in a day- ahead electricity market,” IEEE Trans. Smart Grid, vol. 6, no. 4, pp. 1795–1805, Mar. 2015.
In summary, maximizing Lier, [rig + yi vi 5, (Sij)] for each grid is equivalent to maximizing Elr, + yVx(s;+1)ls, al. According to Lemma 2, we can conclude that for all s € S, n'(s) = Vier, [rg + yöüvi (sil, then Vz > V,. Policy 2’ is guaranteed to be a strict improvement over 7 (unless 7 is already optimal). Because a finite MDP has only a finite num- ber of policies [24], Algorithm 2 must converge to an optimal policy in a finite number of iterations.
- [18] T. Ding, Z. Zeng, J. Bai, B. Qin, Y. Yang, and M. Shahidehpour, “Optimal electric vehicle charging strategy with Markov decision pro- cess and reinforcement learning technique,” IEEE Trans. Ind. Appl., vol. 56, no. 5, pp. 5811–5823, Sep./Oct. 2020.
- [19] Z. Wan, H. Li, H. He, and D. Prokhorov, “Model-free real-time EV charging scheduling based on deep reinforcement learning,” IEEE Trans. Smart Grid, vol. 10, no. 5, pp. 5246–5257, Nov. 2018.
- [20] B. Turan, R. Pedarsani, and M. Alizadeh, “Dynamic pricing and man- agement for electric autonomous mobility on demand systems using reinforcement learning,” 2019. [Online]. Available: arXiv:1909.06962.
- [21] T. P. Lillicrap et al., “Continuous control with deep reinforcement learning,” 2015. [Online]. Available: arXiv:1509.02971.
Authorized licensed use limited to: University of London: Online Library. Downloaded on December 28,2024 at 23:18:31 UTC from IEEE Xplore. Restrictions apply.
LIANG et al.: MOBILITY-AWARE CHARGING SCHEDULING FOR SHARED ON-DEMAND EV FLEET USING DRL
1393
- [22] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine, “Soft actor–critic: Off- policy maximum entropy deep reinforcement learning with a stochastic actor,” 2018. [Online]. Available: arXiv:1801.01290.
- [23] M. L. Littman, “Markov games as a framework for multi-agent rein- forcement learning,” in Proc. Mach. Learn., 1994, pp. 157–163.
- [24] R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction. Cambridge, MA, USA: MIT Press, 2018.
- [25] C. P. Birch, S. P. Oom, and J. A. Beecham, “Rectangular and hexagonal grids used for observation, experiment and simulation in ecology,” Ecol. Model., vol. 206, nos. 3–4, pp. 347–359, 2007.
- [26] J. Ke et al., “Hexagon-based convolutional neural network for supply- demand forecasting of ride-sourcing services,” IEEE Trans. Intell. Transp. Syst., vol. 20, no. 11, pp. 4160–4173, Dec. 2018.

Zhaohao Ding (Senior Member, IEEE) received the B.S. degree in electrical engineering and the B.A. degree in ﬁnance from Shandong University, Jinan, China, in 2010, and the Ph.D. degree in elec- trical engineering from the University of Texas at Arlington, Arlington, TX, USA, in 2015.
He is currently an Associate Professor with North China Electric Power University, Beijing, China. His research interests include power system planning and operation, power market, and electric transportation system.
- [27] R. S. Sutton, D. Precup, and S. Singh, “Between MDPS and semi- MDPS: A framework for temporal abstraction in reinforcement learn- ing,” Artif. Intell., vol. 112, nos. 1–2, pp. 181–211, 1999.
- [28] R. S. Sutton, “Learning to predict by the methods of temporal differ- ences,” Mach. Learn., vol. 3, no. 1, pp. 9–44, 1988.
- [29] L.-J. Lin, “Reinforcement learning for robots using neural networks,” Dept. School Comput. Sci., Carnegie–Mellon Univ., Pittsburgh, PA, USA, Rep. CMU-CS-93-103, 1993.
- [30] J. Tsitsiklis and B. Van Roy, “An analysis of temporal-difference learning with function approximationtechnical,” Lab. Inf. Decis. Syst., Massachusetts Inst. Technol., Rep. LIDS-P-2322, 1996.
- [31] Y. Liang, C. Guo, Z. Ding, and H. Hua, “Agent-based modeling in electricity market using deep deterministic policy gradient algo- rithm,” IEEE Trans. Power Syst., early access, Jun. 2, 2020, doi: 10.1109/TPWRS.2020.2999536.
- [32] H. Lee, M. Girnyk, and J. Jeong, “Deep reinforcement learning approach to MIMO precoding problem: Optimality and robustness,” 2020. [Online]. Available: arXiv:2006.16646.
- [33] PJM Market Data. Accessed: Nov. 25, 2019. [Online]. Available: https://www.pjm.com/
- [34] X. Glorot, A. Bordes, and Y. Bengio, “Deep sparse rectiﬁer neural networks,” in Proc. 14th Int. Conf. Artif. Intell. Stat., 2011, pp. 315–323.
- [35] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” in Proc. 3rd Int. Conf. Learn. Rep. (ICLR), San Diego, CA, USA, May 2015, p. 6.
- [36] (2019). Gurobi. [Online]. Available: https://www.gurobi.com/
- [37] A. Paszke et al., “Pytorch: An imperative style, high-performance deep learning library,” in Proc. Adv. Neural Inf. Process. Syst., 2019, pp. 8026–8037.
- [38] V. François-Lavet, R. Fonteneau, and D. Ernst, “How to discount deep reinforcement learning: Towards new dynamic strategies,” 2015. [Online]. Available: arXiv:1512.02011.
Tao Ding (Senior Member, IEEE) received the B.S.E.E. and M.S.E.E. degrees from Southeast University, Nanjing, China, in 2009 and 2012, respectively, and the Ph.D. degree from Tsinghua University, Beijing, China, in 2015. From 2013 to 2014, he was a Visiting Scholar with the Department of Electrical Engineering and Computer Science, University of Tennessee, Knoxville, TN, USA. He is currently an Associate Professor with the State Key Laboratory of Electrical Insulation and Power Equipment, School of Electrical Engineering, Xi’an Jiaotong University. He has published more than 60 technical papers and authored by “Springer Theses” recognizing outstanding Ph.D. research around the world and across the physical sciences—Power System Operation with Large Scale Stochastic Wind Power Integration. His current research interests include electricity markets, power system economics and optimization meth- ods, and power system planning and reliability evaluation. He received the Excellent Master and Doctoral Dissertation from Southeast University and Tsinghua University, and the Outstanding Graduate Award of Beijing City. He is an Editor of IEEE TRANSACTIONS ON POWER SYSTEMS, IET Generation, Transmission and Distribution, and CSEE Journal of Power and Energy Systems.
- [39] D. P. Bertsekas, “Weighted sup-norm contractions in dynamic pro- gramming: A review and some new applications,” Dept. Elect. Eng. Comput. Sci., Massachusetts Inst. Technol., Cambridge, MA, USA, Rep. LIDS-P-2884, 2012.
- [40] T. Jaakkola, M. I. Jordan, and S. P. Singh, “Convergence of stochastic iterative dynamic programming algorithms,” in Proc. Adv. Neural Inf. Process. Syst., 1994, pp. 703–710.
- [41] C. Szepesvári and M. L. Littman, “A uniﬁed analysis of value-function- based reinforcement-learning algorithms,” Neural Comput., vol. 11, no. 8, pp. 2017–2060, 1999.
- [42] T. M. Apostol, “A proof that Euler missed: Evaluating ζ (2) the easy way,” Math. Intell., vol. 5, no. 3, pp. 59–60, 1983.

Yanchang Liang (Student Member, IEEE) received the B.S. degree from the College of Electrical Engineering, North China Electric Power University, Baoding, China, in 2018. He is currently pursuing the M.S. degree with North China Electric Power University, Beijing, China.
His current research interests include control, optimization, reinforcement learning, with applica- tions to power systems, and electric transportation systems.

Wei-Jen Lee (Fellow, IEEE) received the B.S. and M.S. degrees in electrical engineering from National Taiwan University, Taipei, Taiwan, in 1978 and 1980, respectively, and the Ph.D. degree in elec- trical engineering from the University of Texas at Arlington, Arlington, TX, USA, in 1985. In 1986, he joined the University of Texas at Arlington, where he is currently a Professor with the Department of Electrical Engineering and the Director of the Energy Systems Research Center. He has been involved in research on power ﬂow, transient and
dynamic stability, voltage stability, short circuit, relay coordination, power quality analysis, renewable energy, and deregulation for utility companies. He is a registered Professional Engineer in the State of Texas.
Authorized licensed use limited to: University of London: Online Library. Downloaded on December 28,2024 at 23:18:31 UTC from IEEE Xplore. Restrictions apply.
