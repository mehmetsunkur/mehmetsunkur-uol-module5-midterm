## Obtaining evidence of learning in digital games through a deep learning neural network to classify facial expressions of the players

Heraclito A. Pereira Jr. 1 , Alberto F. De Souza 1 and Crediné S. De Menezes 1,2

1Post-graduate Program in Informatics, Federal University of  Espírito Santo, Espírito Santo, Brazil 2Education Faculty, Federal University of Rio Grande do Sul, Rio Grande do Sul, Brazil hapereirajr@gmail.com,

alberto@lcad.inf.ufes.br,credine@gmail.com

AbstractThis Emotions play a significant role in determining human behavior, including the involvement and motivation of students, in the learning process. A digital game have become an important option, as a pedagogical tool, for the development of skills currently required for the insertion of an individual in labor market. This paper reports a research on a computational architecture, based on the techniques and methods of Learning Analytics,  to  assist  educators,  who  use  digital  games  as pedagogical  tools,  in  assessing  the  impacts  of  a  player's emotional states on his motivation to play and, consequently, in their  learning.  Such  architecture  aims  to  identify  data  on players' emotional states, through their facial expressions, and cross them with data on the players 'actions, game events or states, which can evidence their learning. A deep learning neural network  is  used  in  the  identification  of  the  players'  facial expressions, through images of the faces of the students playing. The capture of these images is done by a webcam, installed on the computer where the game is playing, which is triggered by an  intelligent  software  agent,  according  to  pre-established conditions. This intelligent software agent also captures the data about the learning evidences. A software module, to analyze learning and the possible impacts of players' emotional states on their learning, completes the proposed computational architecture. The work was developed in the discipline on digital games  applied  to  Education  in  a  postgraduate  course  in Computer Science.

Keywords-Game-based learning assessment; recognition of facial expressions; deep learning neural networks; game-based learning.

## I. INTRODUCTION

The use of digital games in the Education field is already a reality, but it still is inhibited in this area by the lack of consolidated resources in order to evaluate students' learning during the games [1]. Such assessment should focus on what knowledge;  skills  and  positive  attitudes  the  games  could develop in a student-player and look for evidence concerning his evolution level that he has achieved, in terms of these learning elements, after playing [2].

The Evidence Centered Design (ECD) approach, proposes that learning can be evaluated by a set of evidences, which is represented by data collected during the teaching process [3]. These data need not to be restricted to numerical and textual data,  once  some  studies  have  already  shown  that  data originated  from  biophysiological  manifestations  of  the

student, who is using the pedagogical tool, such as a digital game, can evidence learning [4].

When a digital game is used like pedagogical tool, the emotional states of a player and his motivation to play may influence in his learning and, consequently, in his evaluation [5]. Thus, it is important to capture data that evidence such states and motivations, not only to modulate the assessment of their learning, but also to use digital games according to the characteristics of the players. This is important because the genre and the elements of a digital game can stimulate a specific type of player, but demotivating for another one.

This paper reports a research developed in the discipline about digital games applied to Education in a postgraduate course  of  Computer  Science.  Its  main  objective  was  to propose and evaluate a computational architecture, based on the techniques and methods of Learning Analytics, to assist teachers, who use digital games as pedagogical tools, in the evaluation of the impacts of a player's emotional states and his motivation to play, in his learning. This architecture consists of: i) an intelligent software agent for collecting data of the players'  actions,  game  states  and  events,  and  also  for recording images of the players; ii) a deep learning neural network, for the processing of these images, aiming to identify the  emotional  states  of  the  players  through  their  facial expressions,  and  iii)  a  software  module  for  analysis  of learning, based on the ECD approach. Data on players' facial expressions  will  allow  teachers  to  check  whether  their emotional states were facilitators or barriers to learning while playing, and to help them to see if the game and its elements fit the teaching objectives.

## II. THEORETICAL FOUNDATION

The next points contains the main theories to support this research.

## A. Assessment of learning based on digital games

Digital  games  have  become  an  increasingly  important option, as a response in the search for better pedagogical tools, for the development of skills necessary for the insertion of an individual in professional life and in Society. Its motivational and  immersive  aspects  have  been  deeply  studied  in  the literature [6].

Well-designed digital games tend to induce players to enter in a state of flow [7], where they lose notion of time and are absorb by the experience that they are surviving through

the game. Such a flow produces involvement and engagement of the player and, therefore, facilitates the apprenticeship.

The expansion of the use of digital games as teaching tools still have, as its main challenge for effective use, the definition of  processes and reliable resources, user friendly, for the assessment of the learning that take place during the game.

The growing use of computational resources, including digital games, in the teaching, with the objective to reach better results than traditional methods, led to the emergence of an area called Learning Analytics (LA).  Thus, this "is the area that applies techniques and methods of computer science, pedagogy, sociology, psychology, neuroscience and statistics to analyze the data collected during education processes" [8].

The research in Learning Analytics has indicated the use of other types of data, beside numerical and textual data, as a way to collect evidence to support the evaluation process of learning, including digital games. This trend has given rise to a section of LA, called Multimodal Learning Analytics, which also includes the collect and analysis of data from several manifestations of the student, captured by sensors, during the learning  process  such  as:  touches,  gestures,  voices,  facial expressions and eye movements. [4].

Despite the growing interest in this area of research and in the development of methods, techniques and tools for the game-based  learning assessment, there are still few consolidated instruments for this type of evaluation [9].

## B. Emotions in interactions and learning

The principal condition to lead to a significant learning is that the student is predisposed to learn. Such a predisposition is directly linked to his emotional state [10].

Emotions, according to Biology, are define as dispositions for action and they play a significant role in determining human  behavior  [11].  Emotions  are  determinant  in  the involvement and motivation of the students.

One of the most widespread theories on emotions is the basic emotions model of the human being. This theory says that humans' emotions have the same physical manifestations in different cultures. Ekman [12], who studied the six facial expressions of the six basic emotions (Fig. 1), verified that, in addition to being found in different cultures and distant parts of the world, they are manifested in the same way, from children to the elderly. It considers basic emotions, capable of recognized through the facial expressions of the human being: joy, sadness, fear, anger, surprise and repugnance [13].

Fig. 1- Six basic emotional facial expressions - Source: (SCHMIDT; COHN, 2001).

<!-- image -->

## C. Recognition of facial expressions through deep learning neural networks

According to Oliveira and Jaques [14], "there are two main approaches to classify what a facial expression demonstrates: (i) use of classifiers or (ii) use of psychological facial coding

models." When using classifiers, the approach consists in training a classifier with specifics images that contains the desired expressions and its emotions. The second approach consists in using a model of psychological facial classification, which codes all facial appearances caused by muscular contractions, which, with or without combinations, represent all possible facial expressions.

When using classifiers, the artificial neural networks of the deep learning type have been apply successfully in order to solve problems of face and facial expressions recognition.

Artificial neural networks are distributed parallel systems composed of simple processing units (artificial neurons) that calculate  certain  mathematical  functions.  These  units  are arranged  in  one  or  more  layers  and  interconnected  by  a substantial number of connections and, in most models, these connections  are  associated  with  weights,  which  store  the knowledge acquired by the model and serve to weight the input received by each neuron of the network [15]. Artificial neural networks have been apply successfully in different problems  of  computer  vision,  such  as  face  recognition, recognition  of  facial  expressions,  recognition  of  gestures, among others.

The convolutional neural network is a type of artificial neural network, based on biological processes, where neurons are organized to obtain a higher resolution image from a lower resolution image, including regions of overlap of the visual field, therefore it is indicated for image and video recognition [16].

## D. ECD (Evidence Centered Design) approach to evaluate learning

The approach that seems to be most suitable for building a reliable assessment is the ECD - Evidence Centered Design that started in the Educational Testing Service - New Jersey, USA in 1997 by Robert Mislevy, Linda Steinberg, and Russel Almond [3]. This approach provides a conceptual framework for  learning  assessment,  based  on  diagrammatic  models, which is able to support a wide range of types of evaluation, from the most traditional ones, such as essay tests and multiple choice tests, to types of evaluations considered more modern, for example evaluation of learning portfolios and simulations. This approach establishes that the learning obtained by the student is evaluate based on evidences gathered from different expressions  of  the  student  during  the  teaching-learning process. These models have already proved, in practice, to be useful to guide the collect of data and analysis of the data, that will evidence the lessons learned.

## III. RELATED WORK

The search for a solution that provides recognition of faces and facial expressions using artificial neural networks has been taking place for some time. Kobayashi and Hara [17] developed  a  research  using  the  six  basic  expressions  of emotion  [12]  as  categories  to  classify  through  neural networks. The neural network has been train using 90 images with the six basic facial expressions from 15 individuals, resulting in a recognition rate of 80 percent.

Padgett and Cottrell [18] used a neural network with a hidden layer for non-linear sigmoid type classification, with 7 exits, 6 exits for each of the basic emotions and one for the neutral expression. Several images of 12 individuals have been use and the recognition rate was of 86 percent.

Research in this area continued to grow and an overview of the work developed between 2002 and 2012, can be seen in [19].

Among the recent studies that are closest to the present conditions in this research, we can quote two. The first, from researchers  of  Berkley  University,  who  in  2010  at  the ImageNet Large Scale Visual Recognition Competition 2010, trained  a  deep  learning  convolutional  neural  network  to classify  1.3  million  high  resolution  images  and  achieved considerable results better than the previous results of stateof-the-art [16]. In the second, the Oxford researchers used an artificial neural network to train and test the recognition of faces from the image bank generated with expressive results (accuracy  between  92  and  96%),  compared  to  previous successful experiences [20].

It was find few studies addressing the recognition of facial expressions for computational learning environments. Changjun et al [21], who investigated the recognition of facial expressions in real-time using a Support Vector Machines (SVM) classifier, with the objective of estimating the affective state of students using a distance learning system. In that work, he trained the SVM algorithms with 100 facial images of 15 students. Afterwards, using 265 facial images of 42 people as a test set, the accuracy in face recognition result in 84.55%.

Concerning  the  bibliographical  research  carried  out  to know works related to the present paper, we did not find publications about the recognition of facial expressions as evidence of learning based on digital games.

## IV. METHODOLOGY PROPOSAL

This work originated during a discipline on digital games applied on Education in a postgraduate course in Computer Science, where demanded the students that they proposed computational resources for game-based learning assessment based on digital games.

Considering the immersion of a player during a digital game is fundamental to enhance their learning [7] and that their emotional states could affect such immersion, the authors were interested in researching devices to collect and treat data about  such  states  during  the  playing.  Thus,  to  generate evidence that would assist teachers in game-based learning assessing.

Although no specific publication was found on the use of computational resources to assess the impacts of the digital player's states of mind on their learning, it was found in the literature that, regardless of the pedagogical tool used, the state of mind and the motivation of the learner influence their learning [4,5,10,11].

Therefore,  a  bibliographical  research  about  ways  of identifying  the  individual  emotional  states  was  made, concluding that an effective way to identify these emotional states are through the facial expressions [12,13,14] and that,

for this, artificial neural networks of the deep learning type have been used successfully.

Thereby, it decided to construct a computational architecture for Learning Analytics, based on deep learning neural networks, to capture and process data on the emotional states of digital players, to verify the impact of these states on their learning.

For the experiments with such a computational architecture,  the  authors  in  order  to  teach  student-players about Healthy Eating and Home Economics built a digital game. The choice of this particular theme for the development of that game was because there was already a prototype of this type of game with source code freely available for use. In addition,  two  professors  of  an  undergraduate  course  in nutrition made themselves available to follow the experiments and contribute their observations to assist teachers, who use digital games as pedagogical tools, in the assessment of the impacts of a player's emotional states and his motivation to play, in his learning.

A series of experiments performed with students playing the game under the observation of the teachers, who intended to use digital games as pedagogical tools. As students played, evidence  of  their  emotional  states  and  their  learning  was captured by an intelligent computer software agent and, after each game session, each player responded a questionnaire about their experience while playing. At the end of all game sessions teachers also responded to a questionnaire.

All data that was collected was processed to obtain crossinformation  of  the  player's  emotional  states  and  their performances during and at the end of the game. After the processing, all information resulting from the experiments were analyzed, producing findings about the impacts of the players' emotional states on the learning outcomes.

## V. COMPUTATIONAL ARCHITECTURE OF LEARNING ANALYTICS USED

The computational architecture to develop the experiments was designed in two modules: the first one, for collecting and processing data of the playing player (Fig. 2), and the second for  obtaining  cross-information  of  the  player's  emotional states during the game with his respective actions or events or states of the game (Fig. 3).

The first module (Fig.2) consists of:

- · An intelligent software agent that is called inside the digital game, in specific stage / phase / level positions, to register data of a player's action, an event or a game state and the respective image of the player's face, while playing. These agents triggered according to the actions performed by the players, events that occurred in the game or also according to values of variables representing game states. For example, if the number of products purchased is less than ten percent of the total of products available and passed 1 minute to the game started, the agent will capture the images of the student playing, to check if he has an expression of poorly motivated.  Another example in which the agent triggered the data collected was immediately after the

game started and when it was 5 seconds to run out of game  time.  These  registers  represent  evidences  of learning,  which,  according  to  the  ECD  approach, demonstrate the learning obtained by the players.

- · After the students played the digital game, a deep learning  neural  network  will  process  the  recorded images in order to identify the facial expressions of each student playing.
- · A program that includes the codes of facial expressions identified  by  the  deep  learning  network  in  their respective  registers  recorded  when  images  were captured.

Fig, 2 - Module for collecting and processing data to evaluate the impacts of players 'emotional states on the players' learning.

<!-- image -->

The second module (Fig. 3) consists in:

Fig. 3 - Module for the evaluation of the impacts of the emotional states of the players in their learning .

<!-- image -->

- · A program for educators to include on a database, player data and game data that will be needed to obtain learning information. About the player is registered: his code of school enrollment, name, sex, date of birth and how long he has been playing. About the game, the necessary data are: levels, phases, stages of the game; players' actions, game states and events that represent evidences of learning, in addition to the learning that is expected through the digital game.
- · A  program  that  reports  on  learning  information, based on the evidence collected, and cross-information between the player's actions, events and game states, with their respective facial expressions representing their emotional states (example in Fig 4). Such crossinformation will help the educator better understand situations such as:
- o The elements / situations of the game that lead to the engagement and the enthusiasm of the player in the game, and, consequently, to a good learning of the player.
- o The elements / situations of the game that lead to the annoyance and learning difficulties of the player.
- o The incompatibility of the player profile with the game genre. The particular emotional states of players who, at the time of playing, have impaired  or  enhanced  their  learning  through play.

Fig. 4 - Report model showing the facial expressions' code of the player with code of school enrollment J010, according to his actions in the game and the events and states of the game. The facial expression code are 1 - joy, 2 sadness, 3 - fear, 4 - anger, 5 - surprise and 6 - repugnance.

<!-- image -->

Fig. 5 shows a model of the registers generated in module 1 that are processed in module 2 to obtain information that can help the educator in assessing the impact of players' emotional states on their learning. Each of these registers, following the processing  of  the  first module  of  the  computational architecture, will contain data of a player's action, or game event or stage, in a one stage of a phase of the game level, and the respective picture of the player's face.

It was used a deep learning neural network called VGG Face CNN to identify the facial expressions from the collected images.  This  neural  network,  developed  by  the  Visual Geometry  Group  of  Oxford  University,  has  a  very  deep architecture, trained from scratch using 2.6 million images of celebrities collected from the web, and is part of Caffe, a deep learning  framework  created  by  researchers  from  Berkeley Vision and Learning Center of the University of Berkley (caffe.berkeleyvision.org).  More details about this model can

be seen in [20]. The network was trained to obtain an accuracy rate of more than ninety percent in the classification of the images of the players among the six basic emotional facial expressions of the human, reported by Ekman [12].

Fig. 5 - Layout of the register with data of a player action, or game event or state and the respective facial expression of the player.

All other programs were developed in Python programming language version 3.6 (www.python.org) and for the database needed to store the data was used the system database manager My SQL version 3.5 (www.mysql. org).

The game context, developed for the experiments (Fig. 6), was a supermarket where the student, who took control of the main character, should acquire as much food as possible, using credits that become available to him by the game, and at an established time, at the beginning of the game session. In addition to the goal of buy as much food as possible, the player would  have  to  achieve  another  goal  which  was  to  find products  within  the  closest  proportions  of  food  types recommended in the healthy food pyramid [22]. To purchase food, the player must capture a credit card, which appears shortly after the game starts and anywhere in the game. In addition to obtaining the credit card, the player must exchange it for cash, in specimen, at a banking terminal that is also located in a corner of the supermarket.

Fig. 6 - Example of digital game screen for players to learn about Healthy Eating and Home Economics.

<!-- image -->

During  the  game  'fast  food  little  monsters'  appear circulating inside the supermarket. If they collide with the main character, they can eliminate him. Also during the game appear products' sale, with smaller prices than those already bought by the player. In this case, the player can exchange what he has bought for cheaper products, and such exchanges generate cash credits for the player. The game ends when the player is eliminated by a 'fast food little monster' or when the player runs out of time. The final score is the combinations of the number of products purchased with the greater adequacy of their shopping basket with the food pyramid [22].

## VI. EXPERIMENTS AND RESULTS

For the experiments 50 (fifty) students were selected, from two classes of the first period of two undergraduate courses in Computing and Computer Science.

Although the game shows low complexity of to teach, also 2 (two) professors from the nutrition undergraduation course participated in the experiment, as evaluators of the teaching process and assessment process. As well as the professor of the students who were participating in the experiment. The teachers could also interact with the functionalities of the computational architecture used.

The students could play for a week, as many times as they wanted. At the end of all game sessions, each player answered a brief quiz about his experience. This questionnaire, besides evaluating the learning obtained by the students, also served to  obtain  impressions  about  the  game  as  a  teaching  and assessment of learning tool. In the evaluation of the answers of the questionnaires, it considered the following classifications: Very Good (91 to 100% of correct answers), Good (76 to 90% of correct answers) and Regular or Sufficient (below 76% of correct answers). Furthermore, the professors also answered a questionnaire about what they observed of the whole process, from the game experience itself to the analysis of the data collected through the computational evaluation architecture.

At the end of the day, the generated images were processed by the deep learning neural network, the codes of the facial expressions  were  then  included  in  the  log  records  of  the players' actions, events or states of the game and, after that, the registers of all the players were included in a database.

At the end of the experiment, all the data collected were processed and analyzed. In this analysis, it was also used the data  collected  from  the  questionnaires  answered  by  the students and  the  professors,  who  participated  in  the experiment.

Initially,  the  learning  was  analyzed  by  computing  the evidence represented by the values assigned by the intelligent software  agent,  which  captured  the  evidences  of  learning based on the players' actions and the game events and states e during the sessions of the game. The automatic calculation of the learning obtained by the players, considered: the actions carried out by the players; sequences of their actions; values of variables representing game states, along and at the end of the game, indicative of events that occurred in the game and its intensities, as well as player actions as responses to these events. Fig. 7 contains a diagram showing the computation of

the evidence and the emission of a report with the learnings of the players.

Fig. 7 - Reporting with the computation of the learning obtained by the players from the evidence captured by the intelligent software agent.

<!-- image -->

The  comparative  analysis  of  the  learning  outcomes obtained by the players through the automated process, based on  the  records  containing  the  evidence  obtained  by  the intelligent  software  agent  during  play,  and  through  the questionnaire answered by the students showed (Table I) that:

- · Most students had very good or good learning about Healthy Eating and Home Economics.
- · The  results  of  the  manual  process  of  learning calculation, by the questionnaire, and the automatic process, by the computational architecture of Learning Analytics, were close.
- · The  result  of  the  calculation  of  learning  by  the automatic process, using the computational architecture of Learning Analytics, was superior to the one of manual process, by the questionnaire. This was considered normal because the automatic process is non-intrusive,  which  leaves  the  apprentice  more  at ease.

TABLE I.   RESULTS OF LEARNING ASSESSMENTS BOTH BY THE AUTOMATIC PROCESS BY THE LEARNING ANALYTICS ARCHITECTURE AND BY THE QUESTIONNAIRE RESPONSES ANSWERED BY THE PLAYERS.Next, it was performed the analyzes that included the crossing of facial expressions codes with game times, final and intermediate scores, challenges and obstacles overcome as shown in Fig. 8.

| the actions of the players and events   |        |
|-----------------------------------------|--------|
|                                         | 57,80% |

The first analysis was based on XY type graphs, where Xaxis had the codes of the players' actions and game events or states,  and  on  the  Y-axis  had  codes  1  to  6  representing respectively the facial expressions of the player: joy, sadness, fear, anger, surprise and disgust (example in Fig. 4).

Fig. 8 - Crossing data of players 'actions, game events and states with data of their facial expressions

<!-- image -->

It was considered that the expression of fear could mean concern, that of anger an extreme annoyance and that of repugnance also disapproval.

The analysis showed the number of occurrences of the player facial expressions by player action code or code of game events and states, followed by analyzes of times spent in players' actions, events or game states.

Based on these analyses, below are the results obtained by the most of the players (80% or more).

## Expressions of Joy observed in players when:

- · Players were successful in overcoming obstacles or even getting resources that could lead to satisfactory results.  Example:  when  they  beat  'fast  food  little monsters'  that  could  lead  to  the  end  of  the  game session, or when they got the credits that increased their food purchasing potential;
- · Players  identified  situations  in  which  they  already knew the procedure for success after repeated play. Example: initially the game placed the product types in  predetermined  quadrants  of  the  game  screen  (a supermarket), which facilitated the choice of food.

In these cases, after a subsequent analysis of the times of action, game events and states, after their occurrence, they did not show  significant cadence losses in the players' performances, which could imply in losses of immersion or flow in the game. Instead, situations of these types seem to motivate the players to immerse into the game, although a few players have celebrated the overcoming of obstacles of intense form.

## Expressions  of  Fear  (concern)  observed  in  players when:

- · The player was faced with complex and important tasks or with critical situations. Example: the task of monitoring the appearance of credits in the

- supermarket, going to the credit location, taking the credit, and going to the ATM to exchange the credit for cash and go back to shopping;
- · The player had share his attention between elements of the game. Example: when the game included more "fast  food  little  monsters"  that  circulated  in  the supermarket  corridors  of  the  game  "attacking"  the players, to increase the difficulty of the game.

In these cases, there was no perceived loss of cadence in the  performance  of  the  players,  on  the  contrary,  in  those moments, it seemed that the player was more immersed in the game.

## Expressions of anger observed in the players when:

Situations in which the players were frustrated with their performance.  Example:  Throughout  the  game,  the  student could catch credit cards to make purchases in the supermarket, the credits cards suddenly appeared and disappeared. When the credit card disappeared, without being caught, the analysis shown expressions of anger on the faces of the players. In such situations, the analysis of the players' actions, game events or states, showed a small loss of cadence in the rhythm of the game.

## Expressions of Surprise observed in the players when:

Random situations in the game that could bring benefits to their results. Example: the student could catch credit cards, which appeared and disappeared suddenly, that can be used to purchase products in the supermarket. Such situations, after analyzing the times of the players 'actions, game events and states, showed a small loss of player cadence in playing the game, perhaps because the player had to think about redoing a strategy that he used until that moment.

## Expressions  of  Disgust  (disapproval)  observed  in players when:

They  encountered  difficulties  of  understanding.  For example,  some  players  pointed  out  that  their  difficulties stemmed from the inferior quality of elements of the game. For example, students who played on the first day reported that  food  figures  were  difficult  to  understand.  With  the improvement  of  these  figures  for  the  following  games sessions, such kind of complaint disappeared. Such situations, after analyzing the times of the actions, events and states of the  game,  after  their  occurrence,  showed  a  small  loss  of cadence  in  playing  the  game,  perhaps  because  the  player should think more to understand the figures.

## No Expressions of Sadness observed in most of players during game sessions.

## Other Observations:

- · Students who have achieved a good nutritional balance as well as a large amount of food, kept the expressions of fear (worry) for much longer. On the other hand, most  of  the  students  who  had  different  facial expressions  and  had  more  expressions  of  disgust (disapproval),  had  the  worst  performances.  This disapproval was confirmed by most of them in the
- answers they gave in the questionnaire, even with the information that they did not like the game.
- · Women  players  (27%  of  all  players)  had  more variation of the expressions during the game than the men  and  were  the  ones  that  showed  the  most expressions of sadness when they had some failure.
- · Some of the students reported that on that day, they were not in an emotional state to play, but when they started the game session, they engaged in playing. The captured facial expressions images confirmed that their initial emotional state did not affect their performance.

Teachers who participated in the experiments, in assessing the  impact  of  facial  expressions  on  players  'performance, agreed that analyzes based on cross-matching of learning evidences  with  facial  expressions  classifications  reflected what was in their notes on players' behaviors during the play.

There was also no concern to control strictly the quality of the process of capture of the images of the players playing. However, during the experiments, it was necessary to control the players so that they did not move much during the game play. There were few cases in which the captured images were not good, they had to be discarded and the game session had to be repeated.

The students reported that the observation of professors, during the game, made them play more seriously but did not influence in their learning.

## VII - CONCLUSIONS AND FUTURE WORK

Considering the analyzes made for the cross-evaluation of the  learning  outcomes  computed  by  the  computational architecture  used  with  the  data  of  the  respective  facial expressions of the players, besides the answers given by the students  and  teachers  in  the  answered  questionnaires,  the following conclusions can be reached:

- · Most players remain with the expression of a fear close to the concern, and it seems to be this state that leads to better results, i.e. it is this state that seems best to keep players in immersion;
- · The expression of sadness is uncommon during the game, but the expression of anger (or frustration) is common when the player fails to seize an opportunity or is eliminated by a game obstacle;
- · The surprise expression also appeared little and, when this happened, it was associated with elements of the game that arose randomly and suddenly during the game;
- · Evidence has shown that states of anger (or frustration) and surprise, although not very significantly, are those that most negatively impact immersion or flow state;
- · The expression of disgust (disapproval) may indicate an inadequacy of the game genre for a player or even a poorly designed element or game situation.

The  results  obtained  in  this  research  were  considered satisfactory by the authors and the teachers because:

- · They showed to the students of the discipline about digital games applied on Education, during which, this research  was  developed,  that  it  is  possible  and advantageous  to  use  computational  resources  to evaluate learning in digital games;
- · Through them, relevant scientific contributions have been  obtained  for  those  who  are  interested  in researching the use of digital games as pedagogical tools.

As future work is intended to use more complex games, to extend the samples of the experiments and to form a historical basis  for  it  to  apply  a  software  of  data  mining  with  the objective of extracting patterns of performances of the players according to their profiles and their facial expressions.

It is also intended the construction and experimentation of an  intelligent  software  agent  that  can  adjust  the  game according to the facial expressions of the student, in an attempt to motivate him or to avoid discouraging him. That agent could provide feedback for the student, who is playing, in order to guide him or her better to take advantage of the teachings provided by the game.

## REFERENCES

- [1] D. Ifenthaler, D. Eseryel and X. Ge, 'Assessment for game-based learning,'  In: Assessment  in  game-based  learning,  Springer,  New York, NY, 2012, p. 1-8.
- [2] F.  Belloti,  B.  Kapralos,  K.  Lee,  P.  Moreno-Ger  and  R.  Berta, 'Assessment  in  and  of  Serious  Games:  An  Overview,'  Hindawi Advances in Human-Computer Interaction, 2013.
- [3] R. Almond, L. Steinberg and R. Mislevy, 'Enhancing the design and delivery  of  assessment  systems:  A  four-process  architecture,' The Journal of Technology, Learning and Assessment, v. 1, n. 5, 2002.
- [4] P. Blikstein and M. Worsley, 'Multimodal Learning Analytics and Education Data Mining: using computational technologies to measure complex learning tasks,' Journal of Learning Analytics, v. 3, n. 2, p. 220-238, 2016.
- [5] A. Hawlitschek and V. Köppen, 'Analyzing player behavior in digital game-based learning: Advantages and challenges,' In: 8th European Conference on Games Based Learning: ECGBL2014, 2014, p. 199206.
- [6] E.A. Boyle, T. Hainey, T.M. Connolly, G. Gray, J. Earp, M. Ott, T. Lim, M. Ninaus, C. Ribeiro and J. Pereira, 'An update to the systematic literature review of empirical evidence of the impacts and outcomes of computer games and serious games,' Computers & Education, 2016 Mar 1, 94:178-92.
- [7] D.J. Shernoff, M. Csikszentmihalyi, B. Schneider and E.S. Shernoff, 'Student engagement in high school classrooms from the perspective of flow theory,' In: Applications of Flow in Human Development and Education. Springer Netherlands, 2014, p. 475-494.
- [8] L. Johnson, S. Adams Becker, M. Cummins, V. Estrada, A. Freeman and H. Ludgate, 'NMC Horizon Report: Edición sobre Educación Superior 2013,' Austin, Texas: The New Media Consortium, 2013.
- [9] J.B. Hauge, R. Berta, G. Fiucci, B.F. Manjón, C. Padrón-Nápoles, W. Westra and R. Nadolski, 'Implications of learning analytics for serious game design,' In: Advanced Learning Technologies (ICALT), 2014 IEEE 14th International Conference on. IEEE, 2014, p. 230-232.
- [10] D. Ausubel and J.H. Novak, 'Psicología Educativa: Un punto de vista cognoscitivo,' México: Ed. Trillas, 1983.
- [11] P.J. Lang, 'The emotion probe. Studies of motivation and attention,' American Psychologist, 50, 372-385, 1995.
- [12] P. Ekman, 'Facial expressions. Handbook of cognition and emotion,' v. 16, p. 301-320, 1999.

- [13] K.L. Schmidt and J.F. Cohn, 'Human facial expressions as adaptations: Evolutionary  questions  in  facial  expression  research,' American journal of physical anthropology, v. 116, n. S33, p. 3-24, 2001.
- [14] E. de Oliveira and P.A. Jaques, 'Classificação de emoções básicas através de imagens capturadas por webcam,' Revista Brasileira de Computaçao Aplicada, v. 5, n. 2, p. 40-54, 2013.
- [15] A. de P. Braga, A.P.L.F. Carvalho and T.B. Ludermir, 'Redes neurais artificiais: teoria e aplicações', Livros Técnicos e Científicos, 2000.
- [16] A. Krizhevsky, I. Sutskever and G.E. Hinton, 'Imagenet classification with  deep  convolutional  neural  networks,'  In: Advances  in  neural information processing systems, 2012, p. 1097-1105.
- [17] H. Kobayashi, and F. Hara, 'The recognition of basic facial expressions by  neural  network. Transactions  of  the  society  of  instrument  and control engineers,' v. 29, n. 1, p. 112-118, 1993.
- [18] C. Padgett and G.W. Cottrell, 'Representing face images for emotion classification,' In: Advances in neural information processing systems, 1997, p. 894-900.
- [19] C.D. C/g259leanu, 'Face expression recognition: A brief overview of the last decade,' In: Applied Computational Intelligence and Informatics (SACI), 2013 IEEE 8th International Symposium on. IEEE, 2013, p. 157-161.
- [20] O.M. Parkhi, A. Vedaldi and A. Zisserman, 'Deep Face Recognition,' In BMVC, Vol. 1, No. 3, p. 6, 2015.
- [21] Z. Changjun, P. Shen and X. Chen, 'Research on algorithm of state recognition of students based on facial expression,' In: Electronic and Mechanical Engineering and Information Technology (EMEIT), 2011 International Conference on. IEEE, 2011, p. 626-630.
- [22] S.T. Philippi, A.R. Latterza, A.T.R. Cruz and L.C. Ribeiro, 'Pirâmide Alimentar Adaptada: Guia para Escolha dos Alimentos,' Rev. Nutr, 12(1), pp.65-80, 1999.