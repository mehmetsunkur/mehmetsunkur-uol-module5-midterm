<!-- image -->

LETTER

## Human-level control through deep reinforcement learning

Andrei A. Rusu' Joel Venessl Marc G. Bellemarel Alex Graves Martin Riedmiller Andreas K. Fidjeland , Georg Ostrovski' , Stig Petersen Charles Beattie' , Antonoglou' , Helen King' Dharshan Kumaran Daan Wierstra Shane Legg' & Demis Hassabis'

The of reinforcement learning provides a normative account" animal behaviour; of how agents may optimize their control of an environment.Touse reinforcement learning successfully in situations approaching real-world complexity, however; agents are confronted withadifficult task: environment from high-dimensional sensory inputs, and use these togeneralize past experience to new situations. Remarkably, humans andother animals seem to solve this problem through a harmonious combination of reinforcement learning and hierarchical sensory pro cessing systems 15 the former evidenced by a wealth of neural data minergic neurons and temporal difference reinforcement learning algorithms . While reinforcement learningagents have achieved some successes in a variety of domains6-%, their applicability has previously been limited to domains in which useful features can be handcrafted, or to domains with fully observed, low-dimensional state spaces. Here we use recent advances in training ~ neural networks? to develop a novel artificial agent, termed a Q-network; that can learn successful policies directly from high-dimensional sensory inputs using end-to-end reinforcement learning. We tested this agent the challenging domain of classic Atari 2600 games'2 We demon strate that the Q-network agent; receiving only the pixels and algorithm, network architecture and hyperparameters. This work bridges the divide between high-dimensional sensory inputs and actions; resulting in the first artificial agent that is capable oflearn to excel at a diverse array of challenging tasks. theory they deep deep on deep

Weset out to create a single algorithm that would be able to develop wide range ofcompetencies on a varied range of challenging tasks central Q-network (DQN), which is able to combine reinforcement learning with a class ofartificial neural network' known as neural networks. Notably, recent advances in of nodes are used to build up progressively more abstract representations ofthe data, made it possible for artificial neural networks to learn concepts such as object categories directly from raw sensory data: We convolutional network which uses hierarchical of tiled convolutional filters to mimic the effects of receptive fields inspired by Hubeland Wiesel's seminal work on feedforwardprocessing in early visual cortex thereby exploiting thelocal in robustness to natural transformations such as changes of viewpoint or scale. goal deep deep deep layers have deep layers building spatial

We consider tasks in which the agent interacts with an environment ofthe goalc

To evaluate our DQN agent, we took advantage of the Atari 2600 platform; which offers a diverse array of tasks (n = 49) designed to be

agent is to select actions in a fashion that maximizes cumulative future convolutional neural network to approximate the action-value function deep optimal

making an observation (s) and an action (a) (see Methods) " step taking

While other stable methods exist for training neural networks in the methods involve the repeated training ofnetworks de novoonhundreds of iterations. Consequently, these methods, unlike our algorithm; are too inefficient to be used success\_ parameterize an approximate value function Q(s,a;0;) the eters (that is, weights) of the Q-network at iteration i. To perform experience replay we store the agents experiences € at each time-step t in U(D), drawn uniformly at random from the of stored samples. The Q-learning update at iteration i uses the following loss function: deep using pool

Reinforcement learning is known to be unstable or even to diverge when nonlinear function approximator such as a neural network is used to represent the action-value (also as Q) function? . This instability has several causes: the correlations present in the sequence between the action-values (Q) andthe target values max Q(s' a Weaddress these instabilities with a novel variant of Q-learning; which uses two ideas. First, we used biologically inspired mechanism removing correlations in the observation sequence and smoothing over changes in the data distribution (see below for details). Second; we used an iterative update that adjusts the action-values (Q) towards target values that are only periodically updated, thereby reducing correlations with the target. known r+7 key

parameters used to compute the target at iteration i.The target network parameters 0; are only updated with the Q-network parameters (see Methods). updates

<!-- image -->

Figure Schematic illustration of the convolutional neural network The details ofthe architecture are explained in the Methods. The input to the neural map %, followed by three convolutional layers (note: snaking blue line

<!-- image -->

difficult and engaging for human players. We used the same network architecture, hyperparameter values (see Extended Data Table 1) and procedure throughout high-dimensional data (210 x 160 colour video at 60 Hz) as input to demonstrate that our approach robustly learns successful policies over a variety of games based solely on sensory inputs with only very minimal knowledge (that is, merely the input data were visual images; and the number of actions available in each game; but not their correspondences; see Methods). Notably, neural networks reinforcement learning signal and stochastic gradient descent in a stable manner illustrated by the temporal evolution of two indices of (the s average score-per and average predicted Q-values; see Fig. 2 and Supplementary Discussion for details) . prior large using learning episode = agent

We compared DQN with the best performing methods the reinforcement learning literature on the 49 games where results were professional human games tester playing under controlled conditions and a policy that selects actions uniformly at random (Extended Data Table 2 and Fig 3, denoted by 100% (human) and 0% (random) on y axis; see Methods) . Our DQN method outperforms the best reinforcement learning methods on 43 ofthe games without incorpo any of the additional used by other approaches (for example; refs 12, 15). Furthermore; our DQN agent performed at a level that was comparable to that of a proachieving more than 75% ofthe human score on more than halfofthe games (29 games; from existing rating prior

<!-- image -->

<!-- image -->

Figure 2 | Training curves tracking the agents average score and average predicted action-value. a, Each is the average score achieved per 'episode Invaders. b, Average score achieved per episode for Seaquest: c Average predicted action-value on a held-out ofstates on Space Invaders. Each point point set

<!-- image -->

on the curve is the average of the action-value Q computed over the held-out set of states; Note that Q-values are scaled due to clipping of rewards (see Methods). d, Average predicted action-value on Seaquest. See Supplementary

b

symbolizes of each filter across input image) and two fully connected layers with a single output for each valid action. Each hidden layer is followed sliding

<!-- image -->

<!-- image -->

Figure 3 | Comparison of the DQN agent with the best reinforcement learning methods' in the literature. The performance of DQN is normalized with respect to a random play (that is, 0% level) . Note that the normalized performance ofDQN, expressed as a percentage; is calculated as: 100 X (DQN score random play score)/(human score random play score). It can be seen that DQN

<!-- image -->

outperforms competing methods (also see Extended Data Table 2) in almost all the games; and performs at a level that is broadly comparable with or superior toa professional human games tester (that is; operationalized as a level of 75% or above) in the majority of games. Audio output was disabled for both human players and agents. Error bars indicate s.d. across the 30 evaluation

see additional simulations (see Supplementary Discussion and Extended Data Tables 3and 4), wedemonstrate the importance ofthe individual corecomponentsofthe DQNagent the replay memory; separate target Q-network and convolutional network architecture by disabling them and demonstrating the detrimental effects on performance. Fig deep

We next examined the representations learned by DQN that under pinnedthe successful performanceoftheagent in thecontext ofthe game Space Invaders (see Supplementary Video 1 for ademonstration ofthe performance of DQN), by using a technique developed for the visual the t-SNE algorithm tends to map the DQN representation of perceptually similar states to nearby points. Interestingly; we also found instances in which the t-SNE algorithm generated similar embeddings for DQN representations of states that are close in terms of expected reward but

sistent with the notion that the network is able to learn representations that support adaptive behaviour from high-dimensional sensory inputs. Furthermore; we also show that the representations learned by DQN are able to generalize to data generated from policies other than its in simulations where we presentedas input to the network game states experienced during human and agent play, recorded the representations of the last hidden layer; and visualized the embeddings gen erated by thet-SNE algorithm (Extended Data Fig 1 and Supplementary how the representations learned by DQN allow it to accurately predict state and action values.

It is worth that the games in which DQN excels are extremely varied in their nature, from side-scrolling shooters (River Raid) to box 'games (Boxing) andthree-dimensional car-racing games (Enduro) . noting

<!-- image -->

Figure Two-dimensional t-SNE embedding of the representations in the last hidden assigned by DQN to game states experienced while playing the DQN agent play for 2h ofreal game time andrunning the t-SNF algorithm?s on thelast hidden representations assigned by DQN to each experienced game state: The points are coloured according tothe state values (V, maximum expected reward of a state) predicted by DQN for the corresponding game states (ranging from dark red (highest V) to dark blue (lowest V)). The screenshots corresponding to a selected number of are shown. The DQN agent layer letting layer points

<!-- image -->

predicts high state values for both full right screenshots) and nearly complete screens (bottom left screenshots) because it has learned that completing a screen leads to a new screen full of enemy ships. Partially completed screens (bottom screenshots) are assigned state values because immediate reward is available. The screens shown on the bottom right and topleft and middle areless perceptually similar than the other examples but are mapped to nearby representations and similar values because the orange bunkers do not carry great permission from Square Enix Limited (top lower Jess still

Indeed, in certain games DQN is able to discover a relatively long-term strategy (for example; Breakout: the agent learns the strategy, which is to first tunnel around the sideofthe wall allowing the ball tobe sent around the back to destroy a number ofblocks; see plementary Video 2 for illustration of development of DQN's manceover the courseof\_ 'training) . Nevertheless; games demanding more temporally extended planning strategies still constitute a major challenge for all existing agents including DQN (for example; Montezuma's Revenge) optimal large Supperfor -

In this work; we demonstrate that a single architecture can successfully learn control lpolicies in a range of different environments with only very minimal knowledge; receiving only the pixels and the game score as inputs, and using the samealgorithm, network architecture and hyperparameters on each game; privy only totheinputs ahuman player would have. In contrast to previous our approach incorporates 'end-to-end' reinforcement learning that uses reward to continu ously representations within the convolutional network towards salient features ofthe environment that facilitate value estimation. This perceptuallearning may influence the characteristics ofrepresentations 27,28 within primate visual cortex Notably; the successful integration of reinforcement learning with network architectures was critically storage and representation ofrecently experienced transitions. Conver prior during deep

realization of such a process in the mammalian brain, with the timecompressed reactivation of recently experienced trajectories during anism by which value functions may be efficiently updated through to explore the potential use of biasing the content of experience replay towards salient events; a phenomenon that characterizes empirically sweeping' in reinforcement learning: Taken together; our work illustrates the power of harnessing state-of-the-art machine learning tech niques with biologically inspired mechanisms to create agents that are capable of learning to master a diverse array of challenging tasks.

Online Content Methods, along with any additional Extended Data display items and Source Data, are availablein the online version of the paper; references unique to sections appear only in online paper. these the

## Received 10 July 2014; accepted 16 January 2015.

- 2 Thorndike; E L Animal Intelligence: Experimental studies (Macmillan; 1911)
- Serre; T. (2005)
- 3 reward. Science 275,1593-1599 (1997)
- 193-202 (1980)
- 6. 58-68 (1995)
- 23. Lin, L-J Reinforcement learning for robots using neural networks. Technical Report DTIC Document (1993).
- 7 S. Reinforcement learning for robot Lange;
- 8.
- 9 Bengio; Y. Learning deep architectures for Al. Foundations and Trends in Machine Learning 2,1-127 (2009)
- 10
- 11 neural networks. Science 313,504-507 (2006)
- 12 environment: An evaluation platform for general 253-279 (2013) agents.
- 13. Legg S. & Hutter; M. Universal Intelligence; a definition of machine intelligence. Minds Mach 17,391-444 (2007)
- 14
- 15 using
- 16. Explorations in the Microstructure of Cognition (MIT Press, 1986)
- document recognition.
- and arrangement of columns in cat's striate cortex Shape
- there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory. Psychol. Rev 102, 419 457 (1995) Why
- 25. t-SNE J Mach. Learn. Res 9,2579-2605 (2008) using

<!-- image -->

- first experiences with a data efficient (Springer, 2005)
- auto-encoder neural networks in reinforcement Deep
- (2009)
- primate temporal cortex. Nature 415,318-320 (2002)
- 29. Nature Neurosci 15.1439-1444 (2012)
- 30.

Supplementary Information is available in the online version of the paper .

Acknowledgements We thank G. Hinton; P. Dayan and M. Bowling for discussions; restof the DeepMind team for their support; ideas and encouragement. the

Author Information Reprints and permissions information is available at Readers are welcome to comment on the online version of the paper. Correspondence and requests for materials should be addressed to KK. (korayk@googlecom) or D.H. (demishassabis@google com)

- 19
- 20 approximation. IEEE Trans. Automat Contr. 42,674-690 (1997)
- 22

<!-- image -->

LETTER

## Evolution of the new vertebrate head by co-option of an ancient chordate skeletal tissue

A defining feature of vertebrates (craniates) is a pronounced head that is supported and protected by a robust cellular endoskeleton. In the first vertebrates, this skeleton probably consisted of nous cellular 'cartilage; which forms the embryonic skeleton ofallver tebrates and the adult skeleton of modern jawless and cartilaginous fish. In the head, most cellular cartilage is derived from a migratory cell population called the neural crest, which arises from the edges of the central nervous system. Because collagenous cellular cartilage sidered a turning in vertebrate evolution? Here we show that tissue with many of the defining features of vertebrate cellular cartilage transiently forms in thelarvae ofthe invertebrate chordate Branchiostoma floridae (Florida amphioxus) . We also present evi dence that during evolution; a regulator of vertebrate cartilage development; SoxE gained new cis-regulatory sequences that sub sequently directed its novel expression in neuralcrest cells. Together, these results suggest that the origin of the vertebrate head skeleton did not depend on the evolution of a new skeletal tissue; as is com an ancient regulator of cartilage differentiation was a major factor in the evolution of the vertebrate head skeleton. collagepoint key

cartilage in adults; at embryonic stages the head skeletons of all vertebrates consist ofa single typeofhistologically distinct cellular carti This embryonic cartilage consists oftightly packed polygonal or disc shaped cells that secrete a thin, homogeneous extracellular matrix material composed offibrillar collagen and chondroitin sulphate proteoglycans . While classical and modern histological examinations have not iden tified a clear homologue of vertebrate cellular cartilage in invertebrates; few invertebrates have cellular-cartilage-like endoskeletal elements. For 'example; among the protostomes, horseshoe crabs (Merostomata) cephalopod molluscs (Cephalopoda) and sabellid polychaete worms tribution suggests that these tissues evolved independently ofvertebrate cartilage; and ofeach other. Among the deuterostomes, both hemichor dates and cephalochordates (amphioxus) have stiff, acellular pharyngeal endoskeletons that incorporate fibrillar collagen In addition; amphi oxus has an oral skeleton that supports its tentacles (cirri) and that forms metamorphosis (Fig 1a-e) Although this oral skeleton is ensheathed in a thick integument that does not contain fibrillar col Unlike other deuterostomes, urochordates lack rigid endoskeletal elements despite their status as the sister group to vertebrates. living during

A recurring theme in evolutionary developmental ishow struc tures in distantly related taxa can arise via conserved developmental despite its unusual in adults, the oral skeleton of amphioxus develops via mechanisms that are homologous to those of vertebrate histology

The histological properties of cellular cartilage in larval and adult cartilage subtypes have been identified . In contrast to the diversity of

Figure Development of the amphioxus oral skeleton. a, A metamorphic amphioxus larva. The oral region; shown in b-e is boxed b, The oral Scanning electron micrographs of forming cirri in early metamorphic (c) and mid fh, Alcian blue 'staining of chondrocytes in a larval amphioxus cirrus (f), a larval Petromyzon marinus gill bar (g) and a larval zebrafish gill bar (h) The arrows to chondrocytes that are point

<!-- image -->

dividing perpendicular to the axis of growth and intercalating to form stacks of discoidal cells. i-k, Toluidine blue staining of a larval amphioxus cirrus (i), a larval lamprey gill bar (j) and a larval zebrafish gill bar (k). The nuclei are blue, and the acidic extracellular matrix of the cellular cartilage is purple. The asterisks indicate the paired nuclei of dividing chondrocytes. The arrows to vacuoles in maturing chondrocytes. The arrowheads indicate the acidic point

cellular cartilage: Because the amphioxus oral skeleton forms at the end ofan extended planktonic larval phase that is difficult to obtain in the field, its development has never been described . Using new ods for the continuous laboratory culture ofthe Florida amphioxus (B. floridae), together with a protocol for artificially inducing synchronized we were able to obtain live amphioxus larvae at vari ous stages of oral skeleton development. We first stained these larvae with the classic histological stain for vertebrate cellular alcian blue; and found strong reactivity with the nascent oral skeleton stage revealed discoidal cells with vacuoles that were 'dividing per acidic extracellular matrix If, i). This histology is highly similar to that of the gill bar cartilage in embryonic lampreys (Petromyzon marinus) meth cartilage; specific large byan (Fig

Wenext asked whether the development ofthe oral skeleton in oxUS requires the same intercellular signalling pathways as the cellular cartilage in vertebrates. Fibroblast factor (FGF)-mediated signal is a conserved essential regulator of cellular cartilage differentiation We thus exposed metamor phosing amphioxus larvae to SU5402 and UO126 (refs 11,12), inhibitors of FGF-mediated signalling that block cellular cartilage differentiation in vertebrates. Treatment with either inhibitor suppressed the forma tion oftheoral skeleton in metamorphosing amphioxus larvae (Fig. 2a-c and Extended Data Fig: Ic-h). Importantly, these inhibitors did not generally inhibit development; asthetreatedlarvaedisplayedother tem porally appropriate signs of metamorphosis; including formation of growth ling '

Figure 2 The amphioxus oral skeleton requires FGF-mediated signalling for formation and expresses orthologues of vertebrate cartilage markers hormone; which induces metamorphosis in amphioxus. Ninety-six per cent of T3-treated control larvae (22 of 23, from two experiments) developed normal oral skeleton (arrow) after 4-5 as previously reported . In situ b, c, Representative phase contrast images of larvae treated with T3 and from one experiment) lacked oral cirri (arrows) but displayed other signs of metamorphosis; including metapleural folds, ventral mouth migration and expression in the mesothelium is indicated by arrowheads.

<!-- image -->

the secondary gill bars and metapleural folds and ventral migration of

A fibrillar the major protein component ofits extracellular matrix. Although previous histological examinations ofamphioxus failed to find and SoxE messenger RNA at thesiteofamputation . We assayedamphioxus fibrillar collagen (ColA) expression We found intense expression of ColA in the chondrocytes of nascent oral cirriandin the mesothelium that lines the anterior coeloms 2b, collagen; collagen during tiating Fig g-i)

Most of the cellular cartilage in the vertebrate head is derived from NCCs. Amphioxus lacks NCCs andprobably forms its oralskeleton from the mesothelium that lines the anterior coeloms?o . This implies that the genetic program for generating cellular cartilage was primitively deployed in mesendoderm and later recruited by NCCs. The repurposing of ancient genes andgenetic programs is a recognized way in which novelty arises events are typically driven by changes in cis-regulatory sequences; changes in the function of transcription factors or a combination ofthe two. Inall vertebrates that havebeen examined, includinglampreys, SOXE transcription in NCCs is activated by the transcription factor TFAP2 These regulatory interactions are direct and involve the physical bind ing of TFAP2 and SOXE paralogues to SOXE enhancers in NCCs?122 Previous has shown that; despite new roles in NCCdevelopment; neither TFAP2 nor SOXE has acquired new DNA-binding properties This implies that the novel expression of SoxE in NCCs was driven by changes in SoxE cis-regulatory sequences rather than by changes in transcription factor function. To directly test this hypothesis; we performed an interspecific assay of SoxE cis regulation. To ensure that all of the relevant amphioxus cis-regulatory sequences were construct that contains the entire amphioxus SoxE locus and several and we tested this reporter in zebrafish (Fig- 3b). We reasoned that if changes in SoxE cis regulation were involved in the recruitment of SoxE to NCCs; then the reporter should recapitulate the expression pattern of endogenous SoxE in amphioxus (Fig. 3a) Alter regulation has been conserved across chordates; the reporter should be active in NCCs; as shown previously for amphioxus the neural tube and tail-bud region in early neurulae but not in migrat NCCs or chondrocytes at any developmental stage (Fig: 3c-Fand during option work flanking genes, ing

In thecellular 'cartilage ofjawed vertebrates; fibrillar collagen expression andchondrocyte differentiation are activated by the transcription factor SOXS, a SOXE family member and regulator of chondrogenesis " The binding of SOX9 to the promoter of the gene encoding fibrillar subfamily' 4 while the expression of Sox9 depends on FGF-mediated and FGF-mediated signalling through FGFRs' are also required for the proper differentiation of neural crest cell (NCC)-derived chondro ofthevertebrate gene program. We thus assessed whether the developing amphioxus oral skeleton expresses SoxE; SoxD and FGF signalling pathway components. detected SoxE, SoxD and FGFR mRNA in oral chondrocytes and the surrounding mesothelium 2e, f and DUSP6/7/9, homologues of two FGF-mediated signalling target genes expressed in chondrogenic NCCs in zebrafish, mice and Xenopus data show that thedeveloping amphioxus oral skeleton displays thecore; conserved histological, developmental and molecular features of ver tebrate embryonic cellular cartilage: key collagen, gest cartilage We (Fig

Figure The evolution of the vertebrate head skeleton via cooption of an ancient cellular cartilage gene program. a, A hypothetical early chordate with an oral skeleton consisting of mesendoderm-derived cellular cartilage (pink polygonal cells) and a pharyngeal skeleton of acellular (pink rods) SoxF controls cellular cartilage differentiation in the oral region and has an unrelated function in a subset of central nervous system precursors (blue stellate cells). b, An early pre-vertebrate chordate with migratory non oropharyngeal region) . € Exposure to intercellular signals in the oral region activates the cellular gene program in SoxE-expressing NCCs (blue polygonal cells). d, Alternatively, mesendoderm-derived cellular (pink polygonal cells) spreads throughout the pharynx, before replaced by NCC-derived cellular cartilage (e). e, Subsequent to c or d, invasion of the pharynx by chondrogenic NCC-derived cellular cartilage gives rise to the NCC-derived head skeleton of vertebrates (blue polygonal cells), similar to the cartilage cartilage proto cartilage being

<!-- image -->

Figure 3 | A reporter construct incorporating the amphioxus SoxE locus recapitulates the amphioxus SoxE expression pattern in zebrafish embryos.

<!-- image -->

Transient expression of amphioxus SoxE transcripts (purple) in scattered neural tube cells (double arrowhead), the posterior axial mesoderm including the tail bud (arrow) and the anterior mesendoderm (arrowhead) in a 20 h, 12-somite neurula, as previously described? . b, Schematic of the amphioxus SoxE reporter construct. The construct spans the SoxE locus and 186 kilobases (kb) of flanking sequence; including adjacent genes, and is roughly equivalent to 1.3 million base of human genomic sequence. The gene encoding fluorescent protein (GFP) was fused in frame with the first exon (exl), and Tol2 recombination arms were added to facilitate genomic integration ampR, ampicillin resistance: c, A zebrafish embryo injected at the one-cell stage with the amphioxus SoxE BAC reporter construct and probed for GFP mRNA at the 16-h, 15-somite stage. Mosaic transcription of GFP (blue) was consistently observed in the neural tube (double arrowhead) and tail bud region (arrow) d, A zebrafish embryo injected at the one-cell stage with the pairs green

phioxus SoxE expression in the embryonic neural tube and tail-bud?z and the lack of endogenous soxE in the lateral and ventral neural tube of zebrafish embryos, suggest that the amphioxus SoxE reporter and, by extension; endogenous amphioxus SoxE are not regulated by Tfap2 or SoxE proteins:

properly in zebrafish While embryos

<!-- image -->

amphioxus SoxE BAC reporter and probed for GFP mRNA at the 22-h, 26 +-somite stage. Like endogenous amphioxus SoxE; the SoxE BAC reporter expression was transient and was extinguished by the late neurula stages; e, A dorsal close-up view of the in c at the level of the hindbrain Activity of the amphioxus SoxE BAC reporter occurred throughout the neural tube but not in the surrounding mesenchyme, which included some early migrating NCCs. The image is a composite of three photographs of the same embryo taken at different focal planes. f, Double in situ hybridization for zebrafish soxlO (a SoxE co-orthologue) (red) and GFP (blue) transcripts in an 18-somite zebrafish injected with the SoxF BAC reporter construct. The image is a composite of three photographs of the same embryo taken at overlap with soxlo expression in the otic placode (asterisks) and migrating NCCs (arrows). embryo

TFAPZA and TFAPZC dual knockdown eliminates the expression of activity ofthe amphioxus SoxE reporter was similar in wildtype zebra fish and in tfap2a and tfap2c dual knockdown morphants (Extended amphioxus and vertebrate SoxE cis regulation diverged, in part, through the evolution of new non-coding cis-regulatory sequences of tfap2 and were accompanied by changes in the function of other transcription factors is unclear from our assay. changes

Our results suggest that the nascent oropharyngeal skeleton of early chordates incorporated collagenous cellular cartilage that is strikingly similar to vertebrate cartilage. In amphioxus; this tissue supports the oral tentacles; which prevent the ingestion oflarge particles during filter in the invertebrate ancestor of the vertebrates; as oral tentacles are found in lamprey larvae, adult hagfish and the chordate fossil Haikouella that the evolution ofthe vertebrate head skeleton involved two major developmental changes: the spread of collagenous cellular cartilage the oral region into the pharynx and the head, and the novel differentiation of cellular Our data also suggest that the acquisition of chondrogenic potential by binding sites posit from

at the SoxE locus. In addition to the oral cartilage, SoxE is expressed in the embryonic central nervous system of amphioxus. One of the first steps in the evolution of NCC-derived cellular cartilage may have been skeletogenic proto-NCCs emerging the central nervous system. doderm in the oralregion; exposure to skeletogenic signals such as FGFs thedual roles ofthe ancestral chordate SoxE gene in neuraland skeletal development may have predisposed evolving NCCs towards acquir ing chondrogenic ability potentiating the evolution of the vertebrate new head"2 from

Online Content Methods; along with any additional Extended Data display items and Source Data, are available in the online version ofthe paper; references unique to these sections appear only in the online paper.

## Received 4 September; accepted 24 October 2014. Published online 8 December 2014.

- Medeiros, D. M. The evolution of the neural crest: new perspectives from lamprey (2013)
- 2 Science 220,268-273 (1983)
- nature and significance of invertebrate cartilages revisited: distribution and histology of cartilage and cartilage-like tissues within the Metazoa; Zoology (Jena) 107,261-273 (2004) The
- 3 the many cartilaginous tissues in teleost fish. J Appl. Ichthyology 26, 257-262 (2010)
- 5 Zool. 308B,325-335 (2007).
- 6. 165-174 (2001)
- 7 Kaneto; S. & Wada, H. Regeneration of amphioxus oral cirri and its skeletal rods: implications for (2011) the
- 8
- 9
- 10 skeletogenesis highlight ancestral functions in the vertebrate head. Development 141,629-638 (2014)
- 11 factor receptor in complex with inhibitors. Science 276,955-960 (1997)
- 12
- 13 required for cartilage formation: Nature Genet 22,85-89 (1999)

<!-- image -->

- 15. morphogenetic protein signaling are required for specifying prechondrogenic identity in neural crest-derived mesenchyme and initiating the chondrogenic
- 16. McCauley; D. W. & Bronner-Fraser, M. Importance of SoxE in neural crest development and the evolution of the pharynx. Nature 441, 750-752 (2006).
- Znosko; W.A. etal Overlapping tunctions of Pea3 ETS transcription factors in FGF
- 17. Ohtani, K. et al Expression of Sox and fibrillar collagen genes in lamprey larval chondrogenesis with implications for the evolution of vertebrate cartilage J Exp. Zool 310B, 596-607 (2008)
- 19. feedback regulator of FGF-stimulated ERK signaling during mouse development Development 134, 167-176 (2007)
- & Sauka-Spengler, T. Genomic code for Sox10 activation reveals a key regulatory enhancer for cranial neural crest. Proc. Natl Acad. Sci. USA 107,3570-3575 (2010)
- and development of lamprey branchial skeleton: insights into development Lee, the
- Van Otterloo; € et al. Novel Tfap2-mediated control of soxE expression facilitated the evolutionary emergence of the neural crest. Development 139, 720-730 (2012)
- evolutionary origin of the neural crest gene regulatory network. Dev. Cell 13, 405 420 (2007)
- provides evidence for co-option of SoxE proteins into vertebrate-specitic generegulatory networks through altered expression. Dev. Biol 341,267-281 (2010)
- evolution of the vertebrate head. Nature 408,854 857 (2000)
- 27. Meulemans, D. & Bronner-Fraser M. Insights from amphioxus intothe evolution of vertebrate cartilage PLoS ONE 2,e787 (2007)
- 28 Li, W. & Cornell, R A Redundant activities of Tfap2a and Tfap2c are required for neural crest induction and development of other non-neural ectoderm derivatives
- 402,518-522 (1999)

Acknowledgements We thank D. Brunelle; C-H. with amphioxus husbandry; and P. Tsai and D. W. Stock for use of their microtomes IOS 1257040and IOS 1160733 (DMM) and University of Colorado; Boulder start-up funds (D.MM) ATG was supported by National Science Foundation grant DBI 0905991.J.-K.Y. was supported by National Science Council Taiwan grants Tung

Author Contributions DMM. designed the project and wrote the manuscript: DJ. the figures; and MVC and J-KY. provided materials and reagents. All authors discussed the results and provided input on the manuscript.

Author Information Reprints and permissions information is available at Readers are welcome to comment on the online version of the paper. Correspondence and requests for materials should be addressed to DMM. (Daniel Medeiros@Colorado edu)

- 14 collagen gene. EMBO J 17,5718-5733 (1998)

<!-- image -->

LETTER

## Experimentally induced innovations lead to persistent culture via conformity in wild birds

Lucy M. Damien R. Andrew Cockburn? , Aplin',2,

In human societies, cultural norms arise when behaviours are trans no 'comparable understanding ofthe process by which socially trans mitted behaviours might spread and inanimal Here weshow experimentalevidenceoftheestablishment of foraging traditionsin a wild bird population. Weintroducedalternative novel foraging techniques into replicated wild sub-populations of great tits (Parus major) and used automated establishment and term persistenceofthe seeded innovations. Furthermore, we used social network analysis to examine the social factors that influenced diffusion dynamics. From only two trained birds in each sub-population; the information spread rapidly through social network ties, to reach an average of 75% ofindividuals; with a totalof 414 knowledgeable individuals performing 57,909 solutions overall replicates. The sub-populations were heavily biased towards the technique that was originally introduced, resulting in established local traditions that were stable over two generations; dehigh population turnover. Finally, we demonstrate a strong effect ofsocialconformity, with individuals disproportionately adopt tion, and continuing to favour social information over personal information: Cultural conformity is thought to be a key factor in the evolution of complex culture in humans' In providing the first experimental demonstration of conformity in a wild non-primate andofculturalnorms in foraging techniques in any wildanimal our results suggest a much broader taxonomic occurrence ofsuchanapparently complex cultural behaviour. persist tracking long using spite ing

Sociallearning in which animals learn others, can enable novel behaviours to spread between individuals; creating group-level behavbetween interacting individuals; hence; group dynamics and popula tion structure will determine the spread and persistence oftraditions?39-1 Additionally, individuals may strategically use social learning to maxi mize its adaptive value; with consequences for when, how and what tra llearning has been described in many phylogenetically diverse taxa' and has been detailed in ledge of the social dynamics associated with such learning in natural systems. Experimentally quantifying cultural transmission in wildpopu lations remains difficult, with limitations associated with isolating and training individuals , tracking the spread of information across from large

Early observationalstudies oftits provide one ofthe most widely cited examples ofanimal innovation and culture; when British birds famously to pierce the foil caps ofmilk bottles to take the cream' 18. More generally, great tits ( P. major) areknown tobehighly innovative; opportu nistic foragers 'contexts?o . began

7Department of Ecology and

This life history; with their fission-fusion social structure?' makes them excellent models for a scale empirical investigation of the social processes associated with cultural transmission. Here we used a novel system that incorporates automated data collection and passive integrated transponder tags; together with recently developed methods for social network analysis; to investigate the spread, lishment and persistence of experimentally seeded traditions in wild tits coupled largeestab great

We first developed an automated puzzle box that is baited with live cultural diffusion experiment basedon thetwo-action and control design' but where treatment groups were alent actions. Two resident males were caught each ofeight sub regimens in captivity. thesecondcondition ('option A two replicates), both individuals were the puzzle box by their bill to move theblue side of the door from left to right. Last, in the third con dition ('option B three replicates), the birds were trained to solve the box by moving the red side ofthe door from right to left (Supplementary Video 1). After 4 leased back into the wild, and three boxes, with both available; were installed 250 m apart in each sub-population (Extended of exposureover 4 weeks) and term (5 of exposure; 9 months later) periods. from training from using sliding puzzle sliding days puzzle options days long

In the five sub-populations that were seeded with trained demonstra tors; knowledge of how to solve the novel puzzle spread rapidly over population (68-83%, n = 37-96) solved the puzzle box at least once. The diffusion ofthis behaviour was clearly sigmoidal (sigmoidal versus except in one individuals solved the puzzle box in control sub-populations (9-53%, n = 5-46; vation. Thelatency to the first solve; excluding the demonstrator; was significantly longer in control areas than in treatment areas (Welch's two-sample t-test, t(6) significantly lower There was a striking difference between the replicates that were seeded with alternative solving techniques: In all treatment sub-populations, learning was heavily biased towards the technique that was originally demonstrated Ic), while no consistent side bias was observed between the control sub-populations 0.03, Ic). replicate (t(8) Fig

Wederived thesocial network for each sub-population independently of the social learning experiment; with 10 sampling at a grid of days

<!-- image -->

<!-- image -->

Figure 1 Cultural diffusion experiment. a, A puzzle box in which birds can B) to access a reward. The puzzle box records the identity; visit duration and solution choice; and it resets after each visit. b, Diffusion curves for the option

<!-- image -->

sunflower-seed feeders that had been equipped to record visitation data using a Gaussian mixture model to isolate clusters of visits in the temporal data streams?2 , with repeated foraging associations between individuals forming thebasis of social networks (Extended Data Fig 2b,c). The social networks for all replicates were significantly non-random, fusion analysis was usedto quantify the extent to which these social ties predicted the acquisition ofbehaviour? . From pooled replicate data; a network diffusion model that included social transmission was over whelmingly supported over asocial learning (AAIC = 1520.7); thelearn ing rate was estimated to increaseby a factorof 12.0per unit ofassociation with knowledgeable individuals Extended 3). An effect of age andsex was also supported, with juveniles and males faster learning rate (Table 1). These results support a dominant effect of social on theemergence of this novel behaviour and also demonstrate that the diffusion ofinnovation was influenced by the fine-scale patterns spatioData having learning

over the rest of the experiment: To analyse this change in behaviour over time; we used a 'generalized estimating equation model? where the dependent variable was the proportion of solutions the seeded technique on each of data collection and the explanatory variables were individuals and strong evidence that the preference for the arbitrary tradition increased mated 14% increase in bias per (95% confidence interval (CI) is consistent with a conformist transmis More conclusive evidence for such positive frequency-dependent copying?' was observed when only the first solution for each individual was considered, with birds disproportionately likely to initially adopt the variant used by the majority using day day

In all of the experimental replicates; the alternative solution; which was equally difficult and equally rewarded, was performed by atleast one previous studies, in which discovery ofan alternative solution led to the progressive erosion of the use ofthe seeded variant behaviour? we observed a pronounced strengthening of traditions

Network-based dittusion model outputs

Table 1 Network-based diffusion analysis

| Transmission model     | AAIC (top model)   |      | Social transmission parameter (estimated)   | 9596 CI   |
|------------------------|--------------------|------|---------------------------------------------|-----------|
| Social: multiplicative |                    | 0.99 | 12.0                                        | 8.8-16.0  |
| T2                     |                    |      | 12.2                                        | 8.2-17.1  |
|                        |                    |      | 7.3                                         | 29-14,3   |
| T4                     |                    |      |                                             |           |
| T5                     |                    |      | 13.4                                        | 8.3-20.02 |
| Social: additive       |                    | 0.01 |                                             |           |
| Asocial                | 1520.7             |      | (Constrained to 0)                          |           |

Individual-level elfects

| Variable                             | AAIC (top model)   |      | Estimate   |   Elfect size |
|--------------------------------------|--------------------|------|------------|---------------|
| Age (juvenile or adult)              |                    | 0.99 |            |          0.7  |
| Sex (F or M)                         |                    | 0.97 | 0.10       |          1.22 |
| Natal origin (resident or immigrant) | 3.9                | 0.13 | 0.07       |          1.16 |

allowing differing social transmission rates In each

Individuals thus preferentially learnt the most common first learning (Fig 2b). Yet; remarkably alsocontinued to prioritize social information over personal information; matching their behaviour to the common variant even after experiencing an equally reward alternative. We analysed the trajectories for those individuals that used both options (n 78) The majority of these individuals (85%, 66) retained a for the uncommon variant; andeight birds switched from thealternative option they = ing

56,87,61, respectively). c, The total number of solutions each option in each replicate (sub-population) (left y axis, shown as stacked bars). The (bars) is shown (right y axis). The total number of solvers was 5,46 and 19 for CI, C2 and C3 (controls), respectively; 76 and 89 for Tl and T2 (option A), using

<!-- image -->

<!-- image -->

Figure 2 Evidence of social conformity. a, The proportion of solutions the seeded technique increased significantly over time in each The are the proportion of solutions the seeded technique on each day; of the frequency of A in the sub ~population with an individuals first learnt option (pooled replicate data from TI-5). The node size represents the using replicate points using option

<!-- image -->

number of individuals (n = 1-147). The black line shows the expected result under unbiased copying; the central red line shows the model fit with 95% CI (outer red lines). c, The solution trajectories for individuals in the T2 sub-population that used both possible options (n ten visits, with each colour representing a single individual.

variant to the common variant. However, none of the birds made the significant moved between replicates with the same seeded tradition, 26 (96%) retained their preference for the common variant. In contrast; of 14 indi viduals that moved between replicates with different seeded traditions, 10 (71%) changed their behaviour to match the common variant in the new location; 3 retained their initial preference and 1 showed no preprefer -

Seeded arbitrary traditions thus formed and persisted in each sub tions; we re-installed the puzzle boxes in one (Tl, T3 and CI) over 5 days in the following winter. Substantial turn over in the population had occurred owing to the high mortality rates typical of this on average; only 40% of each subpopulation had been present the previous No additional demonstrators were trained, and no individual had had contact with the puzzle box in the 42) were populations; knowledge of how to solve the puzzle box emerged even long

faster than it had the preceding year, both among solvers and birds that were inexperienced at the task: in T1, 29 individuals solved box a total of 2,329 times (Fig: 3b) The results suggest a initialeffect ofmemory, followed by a rapid, oblique transmission facil iment: on the first with thesolutions heavily biased towards the that had been were present in both years, the within-individual bias towards the seeded resulting in arbitrary traditions that were retained and strengthened. prior puzzle strong day being 'option

In summary; we showthat wild great tits usesocial learning toacquire novel behaviours and that foraging techniques introduced by few individuals (hereonly two in each replicate) can spread rapidly tothe majority ofthe population; forming stable arbitrary traditions. Both social network ties and individual characteristics determined the transmission ofthese foraging techniques The introduced arbitrary traditions were stable over both short-term and -term periods; becoming increasingly entrenched over two generations. This stability appeared to be a result long-

Figure 3 Local traditions persist across years. The cumulative uptake ofthe behaviour in the second exposure is much higher for is also higher for naive birds (TI 2013-II and T3 2013-Il, n = 28 and 27 days; prior

<!-- image -->

respectively) b, The number ofsolutions Aor B.In Tl, one circuit birds; ps, A or B used in the initial and second exposure. The histograms shows the data for the sub-populations; the dots show the mean proportion of option A performed by individuals; and error bars show the 95% CL using option prior option

solutions over time

ofinformational conformity; with individuals matching their behaviour learning and then continu ously updating their personal information. Conformity has been considered central component of human culture?s 26,28 , but experi mental evidence for its occurrence in wild animals has been limited to study of food preferences in vervet monkeys' We provide the experimental demonstration; to our knowledge; of conformist trans mission and cultural norms in foraging techniques in a wild animal Our study argues the previous view that such behaviour is restricted to the primate lineage and calls for a reconsideration of the evolution and of cultural conformity. long against ecology

Online Content Methods with any additional Extended Data display items and Source Data, are available in the online version ofthe paper; references unique to these sections appear only in the online paper . along

## Published online 3 December 2014.

- 2 learned foraging techniques in squirrel monkeys. Curr. Biol 23,1251-1255 (2013)
- Rendell, L et al Cognitive culture: theoretical and empirical insights into social
- 3 Cantor; M. & Whitehead, H. The interplay between social networks and culture: (2013)
- van de Waal, E, Borgeaud, C. & Whiten, A. Potent social learning and conformity
- 6. Soc. B 366,938-948 (2011)
- 7 chimpanzees. Nature 437,737-740 (2005).
- 8 animal cultures debate; Trends Ecol. Evol 21, 542-547 (2006) The
- 9 335,719-721 (1988)
- 10 Coussi-Korbel; S. & Fragaszy; D. M On relation between social dynamics and the
- the social and cognitive processes underlying human cumulative culture. Science 335,1114-1118 (2012)
- 12
- 13.
- 14
- 15. Galef, B.G.in Oxtord Handbook of Comparative Cognition (eds Zentall, T.R. &
- 19.
- 26.
- 29.
- 30. R402-R404 (2012)

Supplementary Information is available in the online version of the paper.

Acknowledgements This project was supported by grants from the BBSRC (BB/ professorship at Uppsala University LMA was also supported by an Australian Postgraduate Award; andA.T,byaBBSRC David Phillips Fellowship (BB/HO21817/1) field; and M. Whitaker produced electronic components for the puzzle boxes.

support the work was conceived and developed by BCS expenmental work was LMA and BCS , and important contributions were made by all of the other authors The

Author Information Reprints and permissions information is available at Readers are welcome to comment on the online version of the paper. Correspondence

- 16 347-357 (1949)
- opening by birds Anim. Behav. 32,937-938 (1984)
- 18 and individual variation in the blue tit (Cyanistes caeruleus). Anim Behav. 85, 1225-1232 (2013)
- of great tits (Parus major). Ecol Lett 16, 1365-1372 (2013)
- Interface 9,3055-3066 (2012)
- reveals cultural transmission of lobtail feeding in humpback whales. Science 340, 485 488 (2013)
- with wild meerkats. Proc. R. Soc: B 276,1269-1276 (2009)
- 87 (2012)
- of senescence: age-specific recapture; survival, reproduction; and reproductive value in a wild bird population. Am. Nat 179,E15-E27 (2012)
- (2012)

<!-- image -->

<!-- image -->

LETTER

## Fundamental properties of unperturbed haematopoiesis from stem cells in vivo

Katrin Buschl Klapproth' Melania Barile?* , Michael Flossdorf?* Thomas Höfer & Hans-Reimer Rodewald' Kay

plantation into immune- and blood-cell-depleted recipients. Single HSCs can rebuild the system after transplantation' Chromosomal marking  , viralintegration and barcoding' oftransplanted HSCs suggest that very low numbers of HSCs perpetuate continuous stream of HSCs during normal haematopoiesis; and the flux of differentiating allowing inducible genetic labelling of the most primitive Tie2 HSCs in bone marrow, and quantify label progression along haematopoietic devel During maintenance of the haematopoietic system; at least 30% or However, the time to approach equilibrium between labelled HSCs andtheir progeny is surprisingly a time scale that would exceed sustained by previously designated 'short-term' stem cells downstream HSC input. By contrast, in fetal and early postnatal life, HSCs are rapidly used to establish the immune and blood system. In the adult mouse, 5-fluoruracil-induced leukopenia enhances the output of HSCs and of downstream compartments, thus accelerating haematopoietic flux. Label tracing also identifies a strong lineage bias in adult mice with several-hundred-fold larger myeloid than lymphoidoutput; which is only marginally accentuated with age. Finally we show that transplantation imposes severe constraints on HSC engraftment; consist ent with the previously observed oligoclonal HSCactivity under these conditions. Thus, we uncover fundamental differences between the normal maintenance of the haematopoietic system; its regulation by challenge, and its re-establishment after transplantation. HSC fate mapping and its linked modelling provide a quantitative framework for studying in situ the regulation of haematopoiesis in health and long

The paucity ofHSCs has largely impeded direct measurements oftheir functions in situ. Todetermine fundamental properties (frequencies of active HSCs, fluxes between stem and progenitor compartments; residence time and expansion in compartments) of unperturbed steady genetic marking of HSCs in situ. As driver for Cre recombinase (Cre) we used the Tie2 (also known as Tek) locus; which is expressed in embryonic the Tie2 locus a gene encoding codon-improved Cre (iCre) fused to 16 two modified oestrogen receptor binding domains (designated MCM)' (Extended Data Fig: 1a-c) We chose this weakly inducible and tightly regulated system to prevent leakiness. The allele was crossed to RosaYFP mice expressing the fluorescent protein (YFP) reporter in a Credependent manner. In the absence of tamoxifen; we did not detect yellow

YFP haematopoietic cells in bone marrow; thymus and spleen in Rosa mice (n = data not shown). After tamoxifen treat ment; MCM becomes active and deletes the cassette of the YFP marker gene, thus rendering Cre-expressing cells and their non-Creexpressing progeny YFP-positive (Extended Data Id) Early after treat ment (20 days) the labelled cells were almost exclusively HSCs; defined as lineage marker (Lin) ~ Kit Sca-1 of 1.0% ofHSCs werelabelled in situ after tamoxifen treatment (Extended etically conditioned HSC recipients (Rag2 known as Il2rg) ' led to term donor HSC engraftment and multi lineage reconstitution in primary and secondary recipients (Extended Data Fig If), hence initially labelled cells were functional HSCs (Extended Data Table 1). We ruled out the possibility that HSC numbers and functions were compromised by loss of one Tie2 allele in mice in a series of control experiments (Extended Data Fig; 2) 30; stop Rosa

tributing to overall haematopoiesis; and to lymphoid and myeloid linecontributed YFP CD45 progeny in the bone marrow between 6 and 34 weeks after regardless ofthe type oflineage produced, and it represents alower limit given that all mice with labelled HSCs also contained labelled progeny Considering 2.8 X 108 total nucleated bone marrow cells per mouse?o and an HSC frequency of 0.006%, a mouse has ~17,000 HSCs; 30% active HSCs indicates that ~5,000 HSCs contributed to normal haema topoiesis within the observation period In transplantation experiments,

YFP Figure Inducible HSC labelling in mice and frequency estimates on HSC output. Phenotype of labelled cells 20 output. The fraction of negative mice for YFP-expressing Lin CD45 cells (green), granulocytes (red), pro B cells (blue) or double-positive (DP) thymocytes (black) was plotted on a logarithmic scale against the number of YFP HSCs (Extended Data Fig: Ig-j). Arrows indicate lower detection limit (no negative mice in these groups) days lineage

<!-- image -->

estimate for steady state haematopoiesis. We also determined pathway frequencies from HSCs to granulocytes; and T and B cell progenitors between the numbers of labelled HSCs and labelled the (time-averaged) probability for labelled granulocytes lineage finding being

To address the fluxes from adult HSCs via stem and progenitor com partments to peripheral lineages, we resolved the output from in-situinduction in adult mice, the label was exclusively retained in HSCs with no label found in LSK CDI5O  CD48 short-term (ST)-HSCs, and LSK CDI5O CD48 multipotent progenitors (MPPs) (Fig 2b). Within these downstream stem and progenitor compartments; the first marked cells emerged 4 weeks onwards (Fig 2c) Beyond 16 weeks, labelled HSCs labelledmyeloid cells Analysis of overall bone marrow cells further indicated that the label emanates marked HSCs (Extended Data 3a). few 'myeloid granulocyte-macrophage progenitors (GMPs); 0.006% megakaryocyte erythroid progenitors (MEPs)) in the bone marrow were also initially marked (Fig 2b, asterisk) , consistent with weak expression of Tie2 in myeloid progenitors (http:llwwwimmgenorg; data not shown) leading to direct; HSC-independent; labelling: Because of the limited life span of CMPs; GMPs and their progeny (Extended Data Fig: 4), the presence of that have arisen de novo from labelled HSCs. from arising from Fig Very

Given the extraordinarily slow label progression out of the adult HSC compartment; we investigated how rapidly HSCs are used devel Rosa mice were treated in utero in midgestation (embryonic (E) 10.5) with tam oxifen. While initially (E12.5) almost exclusively HSCs (but not the label progressed within to progenitors in fetal liver and bone marrow, and by 1 after birth, equilibrium was nearly reached use is rapid (and possibly complete) during development but slow day ( erythro week very during

We exploited the kinetic data for adult mice fluxes between stem and progenitor compartments as well as residence time and expansion of the cells in the compartments reference compartment (for example; ST-HSCs) the cells lost by onward differentiation (for example; towards MPPs) are by influx from the upstream compartment (for example HSCs) and by cell production in the reference compartment itself (Fig: 3a). The flux is the product of tains information on the rate bers were determined for stem and progenitor compartments (Extended tifying the labelling data (Supplementary Methods and Supplementary Discussion) . (Fig replaced (Fig;

Thesteady label frequency ofaround 1% is consistent with self-renewal of labelled HSCs 3c; HSC panel). In compartments downstream from HSCs, labelled cells incrementally replaced non-labelled cells (Fig 3c). The mathematical model fitted the label frequencies measured up to 240 after induction; and correctly predicted label frequencies at later time points (Fig;

proliferation The rate of net proliferation equals the number of cells born per day minus cells lost by death 1 out of 110 HSCs differ entiates into an ST-HSC, and 1 out of 22 ST-HSCs differentiates into an lymphoid-myeloid during day

bifurcation point; we estimate that per 1 out of 46 MPPs generates CLP , while 1 MPP generates 4 CMPs 3d, f). Given that the cell efflux of cells exceeded influx in all of these compartments. To maintain compartment size; this flux difference is balanced by net proliferation (efflux minus influx net day (Fig

<!-- image -->

Figure 2 Label progression through the haematopoietic system adult maintenance and fetal development. a, HSClabel induction and output YFP Rosa mice. b-f, Percentages of YFP cells among the indicated haematopoietic cells in bone marrow, Dots represent individual mice; and bars indicate the mean. DN, double HSC label induction and analysis in fetal, newborn and 1-week-old (h; HSCs to ST-HSCs in embryonic (red; n = 66) and adult (blue; n = 110) mice (n per time points; see Supplementary Methods); arrows indicate tamoxifen from

<!-- image -->

<!-- image -->

Figure 3 Inference of stem and progenitor cell differentiation; and proliferation from label progression: a,At steady state; the rate ofcell loss in a reference compartment due to cell differentiation and death is balanced by cell influx from the upstream compartment; and by proliferation within the reference compartment. This balance relates the total upstream and reference compartment sizes and nR, respectively) to the rates of cell differentiation and øR) and to net proliferation (proliferation b, The label frequency in the reference compartment (fR) equilibrates over time with the label frequency in the upstream compartment (fu). The time for ßR) (residence time) is determined by how rapidly cells are lost the reference compartment. c HSC label over time (blue dots; red dashed (Ju from line,

<!-- image -->

as in (red lines, best fit; grey shades; 95% confidence bands). Data measured at 400 were not used for (green points; n = 11 mice) but have been predicted correctly by the model. stem and progenitor compartments (with 95% confidence intervals). the experimental data. Relative compartment sizes are symbolized by grey boxes, and magnitude of fluxes by arrow width: g The model based on data in young h, Inferred rates of and lymphoid differentiation from MPPs in younger (7-238 after label induction; CMPs only considered beyond 42 days) (n 110) and older (332-802 days) (n 41) mice fitting Fig days fitting cell from myeloid days

increased from HSC via ST-HSCto MPP compartments, in parallel with the differentiation rates (Fig: 3d, e)

Together; the differentiation rate and net proliferation determinehow close a compartment operates to self-renewal. To quantify the of renewal, we define the residence time in a compartment as the time period in which the compartment would to 37% (Ile) of its size; if all influx were switched off. The residence time is determined by the duration a cell and its progeny in the compartment before can be estimated the labelling data (Supplementary Methods) . degree decay spend being from

For HSCs, given that the labelling frequencies are maintained over time (Fig: 3c) despite efflux (Fig 3d), net proliferation ensures complete selfrenewal and the residence time is theoretically infinite. Linking our esti proliferation rate ( ~1 out of 110 per to 'proliferation measurements would imply that in assays using 5-bromoif HSCs lived indefinitely (and ~2% if HSC lifetime was 100days) . This figure is in the order of magnitude ofthe reported ~4% BrdU labelling per in the 'HSC-1' population (as subset of LSK SLAM-defined HSCs)' suggesting that the Tie2 HSCs we label in situ reside at the top of day; day day

day

Figure 4 In situ HSC response to 5-FU challenge: Experimental outline. Labelling frequencies ofthe indicated populations relativeto HSCs after 5-FU (n = 18, red bars) or PBS (n = 15, grey bars) (mean from 12 and 18). (GMPs) and 0.013 (MEPs) (two-tailed t-test assuming non-equal variances; labelling frequencies considering participation ofHSCs andlor ST-HSCs versus experimental data (black dots; ratios of 5-FU over PBS frequencies, taken from c). Error bars denote se.m. days days

<!-- image -->

the efflux towards MPPs; and the compartment requires only minimal influx from HSCs. Hence; even ST-HSCs operate near self-renewal, their residence time is exceedingly not reach equilibrium within the ~2-year lifetime of a mouse (Fig 3g) Substantial renewal (residence time 7Odays) was found even at the MPP stage. Proliferation of MPPsleads to an efflux of cells into common the influx from ST-HSCs 3), making the MPPsa We also analysed progenitor compartments downstream from CLPs (pro B) Jong selfamplifier. (Fig

An imbalance between myeloid and lymphoid production has been viewed as an age-dependent HSC property?z . We used fate mapping to re-address this question independent of transplantation; and found could be caused by skewed differentiation from a common progenitor, or by preferential proliferation in the branch. Phenotypes and designations of tested progenitors at putative branch are shown exclusive; production of CMPs was several-hundred-fold than that of CLP. myeloid points larger

To examine the responsiveness of haematopoiesis to perturbation; we challenged HSC-labelled mice with a single injection of 5-fluoruracil (5 After peripheral rebound, we observed higher stem and progenitor cell labelling frequencies, relative to HSC labelling; than in untreated mice 4c). This accelerated label equilibration between HSCs and sub sequent compartments after haematopoietic injury indicates feedback model in which the kinetics of net proliferation and differentiation are accelerated (at least) in both HSCand ST-HSCcompartments but notin

(Fig: 1b) is in contrast to oligoclonal HSC activity found in transplanta in-situ-marked HSCs after conventional bone marrow transplantation Kit

<!-- image -->

Figure 5 Fate of in-situ-labelled HSCs after bone marrow transplantation.

<!-- image -->

HSCs (black dots; level indicated by red dashed lines) in individual donor mice, and of YFP donor HSCs (white dots) in the corresponding recipient mice. Representative data from a totalof 11 donors and 32 recipients are shown. shaded areas denote 95% confidence intervals of sampling errors. d, Ratio of engrafted HSC label output over donor HSC input. Red dashed line (ratio 1) indicates Grey equal

lethally irradiated recipients (CD45.1) 5a). For each donor; the HSC labelling frequency was recorded before transplantation ('input'). Despite uniformly strong donor HSC engraftment after 16-18 weeks (average 90%; Fig: 5b), the percentages of YFP-marked cells among total donor HSC ('output' were highly variable compared to the input overrepresented (12 out of 32) (Fig: 5d). We estimate that on average 1 out of 33 donor HSCs engrafted (Extended Data Fig; 8a-c). In two extreme cases, YFP donor HSCs represented only 0.3% or 0.6% of the stronger   proliferation than state (Extended Data tion of individual engrafted HSCs to the repopulation of the bone mar row is highly heterogeneous. (Fig

Inducible labelling of HSCs in normal mouse bone marrow showed that during development HSCs are rapidly used to establish the haema rarely active; but over time a portion of HSCs contributes to adult haematopoiesis. Indeed, although the mean HSC labelling frequency was low; all mice with marked HSCs produced labelled progeny; indi that a fraction; or at least 30%, of all HSCs contributes to haematopoiesis after transplantation: We re-addressed HSC diversity heterogeneity ofmixing experiments. Theobserved HSColigoclonality ishence ahallmark ofpost-transplantation but not normal unperturbed haematopoiesis. These findings indicate that experimental and possibly also clinical HSC transplantations are based on much smaller stem large large cating

HSC proliferation has often been taken as a proxy for asymmetric cell entiation rates. Proliferation may, however, not only yield differentiating progeny but also compensate for cell loss, precluding proliferation as an unambiguous marker of differentiation rates. Here, we quantified

<!-- image -->

support in principle an order of differentiation in situ HSCs to ST-HSCs and MPPs and onwards. However, in divergence from the idea ofa continuous stream from the topofa haematopoietic pyramid, very low flux emanated from HSCs. While ST-HSCs are relatively exceedingly long-lived because ST-HSC self-renewal is almost sufficient to make up for the cell loss by differentiation. We hence identified this compartment as the primary source of haematopoietic maintenance in 'property ofST-HSCs readily explains the apparent HSC-independence ofhaematopoiesis notedin a recent report?^. However, to maintain the ST-HSC compartment in the run (>1 year), it requires continuous input from HSCs; we estimate that per 150 HSCs feed into this compartment (17,000 total HSC X 1/110 differ entiating per day). Hence; true HSC deficiency may go unnoticed for extended periods oftime while functionally impaired ST-HSCand MPP compartments would cause signs of acute bone marrow failure from long day rapid

Collectively; HSCs act in development as founding stem cells; and in adult mice as replenishing cells; ST-HSCs as term amplifying cells, and MPPs as intermediate-term amplifying cells. The described fate-mapping system may also visualize responses to haematopoietic challenges imposed by cancer; infections; cachexia or ageing: The accelerated HSC output in response to haematopoietic injury by treatment with 5-FU underscores this outlook

Online Content Methods, along with any additional Extended Data display items and Source Data are available in the online version of the paper; references unique to these sections appear only in the online paper;

## Received 11 July 2014; accepted 19 January 2015. Published online 11 February 2015.

- 1.
- 2 Osawa; M. lymphohematopoietic reconstitution by a single CD34-low/negative hematopoietic stem cell. Science 273,242-245 (1996)
- 3 receptors distinguish hematopoietic stem and progenitor cells and reveal endothelial niches for stem cells. Cell 121,1109-1121 (2005)
- Sieburg; H. B.et al The hematopoietic stem compartment consists of a limited number of discrete stem cell subsets. Blood 107,2311-2316 (2006)
- 5. programs in vivo Cell Stem Cell 1,218-229 (2007)
- 6. 'identification in adult bone marrowof pluripotent and restricted stem cells of the myeloid and lymphoid systems. J Exp Med. 145, 1567-1579 (1977) The
- myeloid and lymphoid cells derived multipotent haematopoietic precursors. Nature 318,149-154 (1985) from
- 8. dynamic behavior of hematopoietic stem cells. Cell 45,917-927 (1986)

- 9. hemopoietic system of W/W mice. Cell 42, 71-79 (1985)
- 10. system. Blood 115,2610-2618 (2010)
- 12.
- 11. cells in vivo high-throughput sequencing in conjunction with viral genetic barcoding Nature Biotechnol.  29,928-933 (2011) using
- 13. D numbers of primitive stem cells are active simultaneously in aggregated embryo chimeric mice. Blood 69, 773-777 (1987) Alling; Large
- TEK, in hematopoietic stem cells. Blood 89,4317-4326 (1997)
- 15. Hsu,H.C.etal Hematopoietic stem cells express Tie-2 receptor in the murine fetal Blood 96,3757-3762 (2000) liver.
- 16. Zhang Y.et al. Inducible site-directed recombination in mouse embryonic stem cells. Nucleic Acids Res. 24, 543-548 (1996)
- evolution; Cell 100, 157-168 (2000)
- 18. distinct subpopulations of hematopoietic stem cells and multipotent progenitors. Cell Stem Cell 13,102-116 (2013) Ding
- 19. Nature Methods 6,267-269 (2009)
- 21 Gomez Perdiguero; E. et al Tissue-resident macrophages originate from yolk sacnature13989 (2014)
- 20. Boggs; D. R. The total marrow mass of the mouse: a simplified method of measurement.Am. J Hematol 16,277-286 (1984)
- compartment. Nature Rev. Immunol 13,376-389 (2013)
- 23. Wilson; A etal. Hematopoietic stem cells reversibly switch from dormancy to renewal during homeostasis and repair. Cell 135,1118-1129 (2008) self-
- 24.

Supplementary Information is available in the online version of the paper.

N Maltry and S. Schäfer for technical assistance; and the animal facility at the DKFZ for member of CellNetworks; and was supported by BMBF e:Biogrant T-Sys (Fkz 031614) supported by DFG-SFB873-project B11,DFG-SFB 938 project L, ERC Advanced Grant

initial bioinformatic analyses, MR contributed to the tamoxifen-regulated Cre conceived and supervised the study; and wrote the paper.

Author Information Reprints and permissions information is available at www nature com /reprints. The authors declare no competing financial interests. TH. (thoefer@dkfz de)

<!-- image -->

LETTER

## Tissue-resident macrophages originate from yolk-sac-derived erythro-myeloid progenitors

Elisa Gomez Perdiguero' * Celine Trouillet' Marella F. de Bruijn? , Frederic Geissmann'$ & Hans-Reimer Rodewald?s Kay

Most haematopoietic cells renew from adult haematopoietic stem cells (HSCs)'-', however, macrophages in adult tissues can self-maintain independently of HSCs'-7 . Progenitors with macrophage potential in vitro have been described in the sac before emergence of HSCss-13 , and fetal macrophages'3-15 can develop independently of Myb', transcription factor required for HSC'6, and can persist in the qualitative and quantitative contributions of HSC and putative that the vast majority of adult tissue-resident macrophages in liver (Kupffer cells) , brain (microglia) , epidermis (Langerhans cells) and (alveolar macrophages) originate from a Tie2+ (alsoknownas (EMPs) distinct from HSCs. EMPs develop in the sacat onic (E) 8.5, migrate and colonize the nascent fetal liver before and monocytes untilat least El6.5. Subsequently, HSC-derived cells and Langerhans cells are only marginally replaced in oneyear-old mice, whereas alveolar macrophages may be progressively the fetal liver; a sequence ofyolk sac EMP-derived and HSC-derived sac EMPs as a common origin for tissue macrophages. yolk lung yolk embry day croglia yolk:

Csflr-expressing cells in the mouse give rise to tissue-resident macrophages in adult tissues . To identify in the developing embryo the site of origin of Csflr-expressing cells, we performed time course analyses by constitutive (Csflricre) and inducible (CsflrMeriCreMer) fatemappingofcells in the 1b), were first detected in Rosa26YFP embryos in the sac from 16-18 somite (sp) stage onwards la-c) YFP Kit CD45 detected in the sac at 20-25 sp (E9, Fig: Ib), and subsequently in the caudal and head regions ofthe from E9.5,and the fetal liver To discriminate mi gration of YFP cells from de novo labelling we induced YFP expression in at E6.5, YFP at E8.5, YFP between E9.5-11.5 in the (Fig; Ic,d). In the fetal liver, numbers of YFP Kit * CD45I progenitors were 25fold more numerous in the fetal liver than in the sac (Fig; Id) At an antigen expressed on early haematopoietic progenitors'2 (Extended Data YFP - AA4.1 'embryo yolk (Fig Fig yolk pairs Fig embryo CsflrMeriCreMer embryos embryos pulsed CsflrMeriCreMer \_ pulsed yolk they yolk = CsflrMeriCreMer Fig

'Centre

#These authors contributed equally to this work.

SThese authors jointly supervised this work

present in the sac from E9.5 to El0.5, and in the fetal liver from gonado-mesonephros (AGM) region do not originate within the embryo proper. yolk (Fig

These results indicated that yolk-sac-derived, E8.5-labelled YFP AA4.1 in contribution to fetal liver haematopoiesis in vivo. Csfl YFP and sac, liver, head monocytes and granulocytes (Fig: 2c). Thefetal liver also contained YFP that, in contrast to yolk-sac-derived erythrocytesin the fetal liver, sac did not arise from Csflr-expressing cells. Collectively; yolk-sac-derived Csflr progenitors contribute to fetal liver haematopoiesis by giving rise to F4/8obright macrophages, monocytes; granulocytes and red blood cells. yolk CsflrMeriCreMer CsflrMeriCreMer yolk

Together, these fate-mapping experiments demonstrate that and their expression of AA4.1 suggests that represent erythro-myeloid progenitors (EMPs)'2. In in vitro colony-forming assays; the AA4.1 population contained most ofthe total E9 sac colony ard deviation (s.d.)) . Frequencies and distributions of different CFU-C, between overall AA4.1 and YFP progenitors (Fig 2a, tential of overall AA4.1 and YFP AA4.1 cells was comparable to the sac yolkthey yolk CsflriCre CsflrMeriCreMer yolk

We next investigated the transition from sac-derived to HSC derived haematopoiesis Totrace thelatter; we used Flt3Cre which labels fetal and adult HSC-derived multipotent haematopoietic progenitors??, yolk-sac-derived progenitors in miceto progeny ofHSCs Csflr and Flt3 complemented each other sac-derived CD45 populations included Kit monocytes/ granulocytes were present in Myb-deficient   fetal liver 3a) YFP macrophages remained detectable throughout fetal development, and were not yolk-sac-derived Kit cells and myeloid cells were nolonger detectable Kit yolk yolk (Fig = CsflrMeriCreMer replaced (Fig

Figure 1 sac and expand in the fetal liver. a, Fate-mapping analysis of Csflr-expressing cells. Arrows indicate time for analysis, and shades the genetic labelling b, YFP expression on live cells from Rosa26 FP sac (YS), separated by somite 4) (upper panels) cells (lower panels) . RI indicates CD45l Kit and R2 indicates Kit CD45 cells. c, Schematic representation of sites analysed in mouse embryos: YS, AGM region; fetal liver and head: Kit and CD45 phenotype of YFP cells from Rosa26YFP embryos pulsed with OH-TAM at E8.5 (E9.5, embryos at E8.5 (Source Data Table for Fig 1). e, Number of YFP AA4.1 Kit CD45l cells per embryonic region and time YFP Rosa26 embryos pulsed at E8.5 (Source Data Table for Fig 1). See also Supplementary Table 1 and Extended Data and 2. yolk Period points green yolk Pairs n Csflr MericreMer n = n = pulsed points Figs

<!-- image -->

granulocytes/ monocytes increased in numbers development in the and adult tissues indicated that Flt3Cre YFP labelling of Kit progeni tors preceded that of monocytes/granulocytes; with 80% of progenitors labelled at E18.5, and 80% of monocytes at postnatal 8 (P8) YFP labelling plateaued at 14% for adult brain microglia; and 30% for epidermal Langerhans cells up to one year oflife (Fig: 3b). In con trast, YFP labelling of CD45 F4/80 brain macrophages, and alveolar macrophages was 16% in 12-week-old adults but increased during day Flt3Cre Flt3Cre

<!-- image -->

10.5

Cre Altogether; these data indicate that Flt3' YFP *Kit * progenitors and monocytes account for only minor fractions ofmicroglia, Kupffer cells, alveolar macrophages and Langerhans cells in young adults. Toinvestiwhether the presence ofthese adult Flt3Cre YFP F4/8obright macro phages corresponds to their HSCorigin; we performed non-myeloablative transplantations of YFP term-HSCs (LT-HSCs) from adult wild type bone marrow into Rag2 Kit recipients?' (Extended Data Fig 7). Eight weeks after transplantation; the vast majority of HSCs, myeloid progenitors; monocytes and F4/80l tissue myeloid cells in the macrophages in spleen, 2% in liver, 5% in 13% in pancreas; 2% in epidermis and 0% in the brain were donor-derived: Thus, recruitment of HSC-derived precursors is not a major mechanism for the maintenance of F4/8Obright macrophages in these tissues. lung

Labelling efficiency of most tissue-resident macrophage tions in adult Rosa26YFP mice pulse-labelled  with 4 genetic pulse-labelling systems is that allow fate-mapping of cells time window; however, a weakness is the commonly incomplete labelling which could explain fraction oftissuewe cannot formally exclude a fetal HSC origin ofthe unlabelled cells as suggested by others based on transfer of fetal precursors?4-26 \_ CsflrMeriCreMer they specific why a

Collectively; these findings reveal that the transition from sac-to HSC-derived haematopoiesis occurs late in fetal development for mono progenitors only marginally replace sac-derived microglia in the although alveolar macrophages and brain CD45 ~ F4/807 macrophages may undergo progressive replacement with age. yolk cytes yolk -

Wethus made use ofa newly generated inducible Creknock-in mouse (Tie2MeriCreMer) to track haematopoietic output from haematopoietic sac progenitors; sessed the time window at which Tie2 cells contributed to emerging HSCs and macrophages by injecting tamoxifen at different time were labelled efficiently in embryos YFP progenitors Rosa26 embryos with a megakaryocyte-erythrocyte progenitor (MEP) phenotype; and sac, brain, and fetal liver were labelled with high efficiency (60%) in embryos at E6.5 and E7.5,but not in embryos macrophages originate from cells that express Tie2 as early as E6.5 yolk points Tie2MeriCreMer pulsed Tie2MeriCreMer pulsed yolk pulsed pulsed

<!-- image -->

Figure 2 E8.5 Csflrt progenitors differentiate into myeloid cells and red blood cells in the fetal liver. CFU-C from unsorted, AA4.1 Kit AA4.1 cells E9 sac from Rosa26YFP embryos pulsed with OH-TAM at E8.5 (three independent experiments each). CFU-C erythroid andlor megakaryocyte (E/Mk); CFU-granulocyte andlor monocytelmacrophage (GIM); CFU-C mix, at least three of the following: G, E, M and Mk See also Extended Data b, F4/80 and CDIb expression on YFP CD45 for El1.5), limbs and liver of and El2.5 (n = 9); Dashed lines represent FMO (fluorescence minus one) from yolk CsflrMeriCreMer Fig from yolk

<!-- image -->

liver erythro-= progenitors; and all fetal tissue macrophages up to El5.5 are of sac origin myeloid \_

control. See also Extended Data Fig 4. c F4/80, CDIb, Grl, Ly-6G and Ly-6C expression in fetal CD45 YFP cells from Rosa26YFP embryos -labelled at F8.5, and analysed on preparations of fetal liver YFP CDIbhi cells sorted from El6.5 with OH-TAM at embryos. Scale bar, IOum.d, YFP efficiency (%) among red blood cells in fetal liver from liver pulse embryos pulsed Csflr MeriCreMer CsflrMericreMer

In adult mice at embryonic stages (E7.5, or E8.5, or E9.5 or El0.5), bone marrow HSC-derived progenitors, peripheral cells (Tand pulsed

Fetal liver HSC-derived Flt3+ progenitors give rise t0 monocytes and granulocytes in late embryos and adults but do not replace Sacderived macrophages. F4/80, Kit, CDIb and Grl expression on total CD45 cells from Rosa26YFP embryos pulsed at E8.5 (green) in the fetal liver at the indicated of CDIIb and Grl expression on YFP+CD45 cells from Flt3CreRosa26YFP cells in Myb embryos (El4.5, n = 4;El6.5, 7). b, YFP cells (characterized in Extended Data Fig 5) and FA/8Obright macrophages (Kupffer cells in adults) in fetal and adult Flt3CreRosa26YFP liver (first on the left). yolk days F4/80l

<!-- image -->

YFP and CD45 F4/80 brain macrophages in Flt3CreRosa26YFP pups and mice Siglec-F CDIIb lungs (third panel) . YFP labelling efficiency in epidermal Langerhans cells myeloid cells in Flt3CreRosa26YFP skin (fourth 6; 12-week-old, n = 11-14; Representative of May-Grünwald-Giemsa stained cytospin preparations of YFP CDI cells sorted from E18.5 Flt3Cre Rosa26YFP fetal liver. Scale bar, 10 um. Panel , Mean year.

<!-- image -->

Figure Fetal macrophages and adult tissue-resident macrophages originate from Tie2-expressing progenitors before El0.5. a, Fate-mapping cytometric analysis of fetal liver term or short-term haematopoietic stem cells (LT-HSCs, ST-HSCs) , multipotent progenitors (MPPs) common myeloid progenitors (CMPs), granulocyte-monocyte progenitors (GMPs), megakaryocyte-erythrocyte progenitors (MEPs) (left panel) and of fetal macrophages (right panel) in the oflabelling (E7.5 (n = 7),El0.5 (n = 7)) andanalysis are indicated, and for each experiment one representative analysis is shown. See Extended Data Fig 8 for quantitative analysis. c, Frequencies of labelled HSCs and progenitor macrophages in spleen, liver epidermis and brain were analysed animals labelled at E7.5 (n = 4), E8.5 (n = 4), E9.5 (n = 4) or points long yolk points lung Tie2MeriCreMer old pulse

<!-- image -->

in peripheral tissues (spleen; liver and lung) were homogenously la adult HSCorigin (Fig: 4c) In contrast; YFP labelling frequencies ofadult

tissue-resident macrophages were maximal in animals labelled at E7.5, declined at later time points and were minimal when labelled at resident macrophages is further underscored by the finding that resident macrophages in mice at E7.5 werelabelledat higher frequencies than adult HSCs; that is, labelling efficiency did not equilibrate with mouse development. In summary, these inducible temporal analyses demon strate that although both macrophages and HSCs originate progen itors expressing Tie2 as early as E6.5,adult tissue-resident macrophages in thebrain (microglia) liver (Kupffer cells) (alveolar macrophages), skin rophages) develop almost exclusively from an Tie2-expressing progen pathway distinct HSCs. These data are consistent with results from pulse-labelling experiments (see Figs 1and 2), with our earlier observation that resident macrophages are independent of the transcription factor Myb , and complement our data obtained in Flt3Cre Rosa26YFP mice (see pulsefrom pulsed from from itor Fig

Wealso provide strong in vivo evidence for engraftment ofyolk-sacderived EMPs in the early fetal liver. These cells substantially contrib 19,21 fide fetal liver HSC-derived haematopoiesiss Conclusions recent studies that Langerhans cells and alveolar macrophages are not of sac origin based on transfer of fetal precursors?4-2 should be inter preted in light of our findings that sac EMPs expand in the fetal liver and are the main source for tissue-resident macrophages. from yolk= yolk

This study demonstrates that Myb-independent tissue-resident mac rophages  originate sac-derived EMPs, characterized by whether resident macrophages originate from erythro-myeloid, granulocyte-macrophage; or macrophage only-progenitors because these potentials coexist within the sac-derived EMP population: from yolk guish yolk -

Under steady-stateconditions; sac-derived macrophages areonly marginally by HSC-derived cells in the brain; liver and dermis. It is remarkable that macrophages of sac origin persist in functionally very distinct tissues; suggesting that the origin is more desac-derived macrophages can undergo replacement in older mice; as for alveolar macrophages. In a third group, exemplified by gut associated macrophages?"  yolk-sac-derived macrophages are replaced by HSC-derived macrophages in the first weeks of post-natal life. The mechanisms responsible for the maintenanceof sac-derived mac rophages in certain adult tissues require further investigation. Although ronment; andtheir balancebe perturbed by pathology, the contributions of these developmentally distinct macrophage populations to homeostasis and inflammation remain to be characterized. yolk replaced epiyolk \_ yolklung yolkyolk-

Online Content Methods with additional Extended Data display items and Source Data, are availablein the online version of the paper; references unique to these sections appear only in the online paper. along any

## Received 12 April; accepted 21 October 2014. Published online 3 December 2014.

- Orkin, S. H. & Zon, L I. Hematopoiesis: an paradigm for stem cell biology. Cell 132,631-644 (2008) evolving
- 2 (1991)
- 3
- Schulz; C. etal A lineage of myeloid cells independent of Myb and hematopoietic stem cells. Science 336,86-90 (2012)
- 6. Hashimoto; D. etal Tissue-resident macrophages ~maintain locallythroughout adult life with minimal contribution from circulating monocytes. Immunity 38, 792-804 (2013) self-
- 5. macrophages under homeostasis. Immunity 38, 79-91 (2013)
- sustain CNS microglia maintenance and function throughout adult life. Nature
- 8 and myeloid progenitors in the yolk sac and embryo proper of the mouse. Development 126,5073-5084 (1999).
- 22 differentiation: a simple method to isolate long-term stem cells. Proc. Natl Acad Sci USA 98, 14541-14546 (2001)
- 9 yolk sac. Blood 106,3004-3011 (2005)
- 11. Kierdorf; K. etal Microglia emerge from erythromyeloid precursors (2013)
- 25. Hoeffel, G.etal. Adult Langerhans cells derive predominantly from embryonic fetal Med. 209, 1167-1181 (2012)
- 10 before ElO in the mouse embryo are products of the yolk sac. Blood 111, 3435-3438 (2008)
- 24 macrophages are maintained through distinct mechanisms at steady state and during inflammation. Immunity 40, 91-104 (2014)
- 12 Bertrand, J. Y. et al Characterization of purified intraembryonic hematopoietic 134-139 (2005)
- Moore, M.A. & Metcalf, D. Ontogeny of the haemopoietic system: yolk sac origin of
- 14 macrophages in the zebrafish embryo. Development 126,3735-3745 (1999)
- proliferation of macrophages in the mouse yolk sac: a light-microscopic; enzyme 87-96 (1989)
- myelopoiesis can occur in the absence of c-Myb whereas subsequent development is strictly dependent on the transcription factor. Oncogene 19, 3335-3342 (2000)
- progenitors; originating from 145-152 (1999) from
- 18 derive from primitive macrophages. Science 330,841-845 (2010)
- 'definitive" hematopoiesis in the conceptus prior to the emergence of hematopoietic stem
- 20. 359-366 (1995)
- Immature hematopoietic stem cells undergo maturation in the fetal liver Development 139,3521-3530 (2012)
- 210, 1977-1992 (2013)
- 27. Bain C. C.etal Constant replenishment from circulating monocytes maintains the (2014)

Supplementary Information is available in the online version of the paper.

Acknowledgements Theauthors are indebted to J. Pollard, University of Edinburgh for the Csflr reporter strains; J. Frampton, University of Birmingham for the Myb-deficient also thank A McGuigan and the staff of the Biological Service Unit at King' s College London; S. Heck and the Biomedical Research Centre at King's Health Partners, S Woodcock and the staff ofthe Viapath haematology laboratory in Guy's hospital and S. Schäfer and T.Arnsperger for technical assistance at the German Cancer Research Center, This work was supported by a Wellcome Trust Senior Investigator award (WT1O1853MA) and ERC Investigator award (2010-StG-261299) from the European

Author Contributions EGP. and F G. designed the study and wrote the manuscript Tie2 FG and d.B.analysed and interpreted the experimental data; All authors contributed to the manuscript. MF.

Author Information Reprints and permissions information is available at Readers are welcome to comment on the online version of the paper. Correspondence and requests for materials should beaddressed to F G. (frederic geissmann@kclac.uk)

<!-- image -->

- 23. Waskow; C. et al Hematopoietic stem cell transplantation without irradiation.

<!-- image -->

LETTER

## therapy-related acute myeloid leukaemia

Terrence N. Wong * Giridharan Ramsingh?* , Andrew L. Young Christopher A Miller Waseem Toumal John $ Welch' 5 , Elaine R. Mardis4,5,9 Peter Todd E

Therapy-related acute myeloid leukaemia (t-AML) and therapy-related myelodysplastic syndrome (t-MDS) are well-recognized complications of cytotoxic chemotherapy andlor radiotherapy' There are several features that distinguish t-AML from de novo AML or 7,complex cytogenetics and a reduced response tochemotherapy'\_ leukaemogenesis. In particular, the mechanism by which TP53 by sequencing the genomes of 22 patients with t-AML, we show that the total number of somatic single-nucleotide variants and the per centage of chemotherapy-relatedtransversions are similarin t-AML and de novo AML indicating that previous chemotherapy does not t-MDSin which the exact TP53mutation foundat diagnosis was also present at low frequencies (0.003-0.7%) in mobilized blood leukoorbone marrow 3-6years before the development oft-AMLIt MDS, including two cases in which the relevant TP53mutation was tions were identified in small populations of peripheral blood cells ofhealthy chemotherapy-naive elderly individuals. Finally, in mouse bone marrow chimaeras containing both wild-typeand haematopoietic stem/progenitor cells (HSPCs) the HSPCs pre suggest that cytotoxic therapy does not directly induce TP53 muta tions. Rather; support a model in which rare HSPCs carrying age-related TP53 mutations are resistant to chemotherapy and expand preferentially after treatment. The early acquisition of TP53 mutations in the founding HSPC clone probably contributes to the frequent cytogenetic abnormalities and poor responses to chemotherapy that are typical of patients with t-AMLIt-MDS. cytes Tp53+/ Tp53+/ they

We predicted that DNA damage induced exposure to cytotoxic therapy would manifest itselfin t-AML genomes with an increased during

t-AMLand t-MDS are clonal haematopoietic disorders that typically develop 1-5 years after exposure to chemotherapy or radiotherapy' To understand better how cytotoxic contributes to the high incidence of TP53 mutations and karyotypic abnormalities in t-AMLI one case that has been previously reported . These data were compared to whole-genome sequence data previously reported for de novo AML' and secondary AML (s-AML) arising from MDS for which patients did not receive chemotherapy except hydroxyurea 7,8 Ofthe sequencedt-AML cases; 23% had rearrangements of MLL (also known as KMTZA), 23% had complex cytogenetics; and 36% had normalcytogenetics (Extended Data Table 1 and Supplementary Table 1) therapy prior

nucleotide variants (SNVs) and (tier 1) somatic SNVs identified was similar to that for de novo AML and s-AML the number ofsmall insertions or deletions (indels) in regions was genic genic

Figure 1

<!-- image -->

a, Total number of validated tier 1-3 somatic SNVs in t-AML (n = 22),de novo AML (n = 49) and s-AML (n and s-AML cohorts were 55.7,51 and 54.6 years, respectively. b, Number of validated tier 1 somatic SNVs. c, Number of validated tier small indels\_ d, Percentage of tier 1-3 somatic SNVs that are transversions. e Mutational spectrum for all validated tier 1-3 somatic SNVs. f, Number of distinct clones per sample inferred from the identification of discrete clusters of mutations with distinct variant allele frequencies. g Percentage ofcases oft-AML (n = 52) or de novo AML (n = 199) harbouring non-synonymous mutations of the indicated gene. h, Percentage of cases oft-MDS (n = 59) or de novo MDS (n = 150) harbouring non-synonymous mutations of the indicated gene: ABC Fm, ABC family genes; NA not available. tP<0.05 by one-way analysis of mean + standard deviation (s.d.)

Genome Institute; Washington University, St Missouri 63110 USA

showed that transversions are specifically enriched in relapsed AML after chemotherapy? . However, the percentage of transversions; and in fact ofallsix classes ofSNVs; was similar in all threecohorts (Fig Id, e) Structura] variants and somatic copy number alterations were uncom mon in these t-AML cases (Supplementary Table 2 and Extended Data similar to that observed in de novo AML (Fig: If and Extended Data genomes is similar to that of de novo AML genomes.

We next asked whether the pattern of genes frequently mutated in nonsense; in-frame indel or frameshift mutations per t-AML genome (Supplementary Table 3). Todefinebetter the frequency ofspecific muta tions int-AMLIt-MDS, wesequenced a panelof 149 AMLIMDS-related tary Table 4). We combined the whole-genome sequence data with the extension series to report on 52 cases oft-AML and 59 cases oft-MDS. Abnormalities ofchromosome 5or 7 or complex cytogenetics were pres ent in 55.0% ofcases (Extended Data Table 2 and Supplementary Table 1) The t-AMLIt-MDS data were compared to 199 previously reported de novo AML genomes or exomes , or 150 previously reported cases of de novo MDSin which extensive candidate gene sequencing was As reported previously, TP53 mutations are significantly enriched in plementary Table 5). Interestingly; mutations of ABCtransporter genes, subset of which have been implicated in chemotherapy resistance; are well-defined driver gene mutations (that is, DNMTBA and NPMI) were significantly less common in t-AML. Thus; although the total mutation t-MDS. Sup-

33.3% ofpatients affected in our series (Fig: 1g h); the vast majority of these mutations have previously been identified as pathogenic' . Multi risk cytogenetics and a worse prognosis (Supplementary Tables 6,7 and Extended Data Fig: 2) both hallmarks of t-AMLIt-MDS. These obser vations suggest a central role for TP53 mutations in the pathogenesis of

mutations are selectively enriched in t-AMLIt-MDS is unclear. The muta tion burden in the genomic region containing TP53 (including silent tier 1, andany tier 2 ortier 3 mutations) is similar between t-AML and de novo AML (Extended Data Ic) . Thus, it is not likely that chemotherapy directly induces TP53 mutations; We recently reported that individual HSPCs accumulate somatic mutations as a function such thatby age 50,there are on average five the basis of these data and on current estimates that there are approxi mately 10,000 haematopoietic stem cells (HSCs) in humans'2 we predict that 44% ofhealthy individuals at 50 years ofage may have at least one HSPCthat carries a randomly generated, functional TP53 mutation (see Methods) . TP53 has a central role in regulating cellular responses to for neoplastic growth' Together, these observations suggest a model in which rare HSPCs carrying age-related TP53 mutations are resistant to chemotherapy and expand preferentially after treatment (Extended Data 3). ofage;

Totest the first prediction; we identified seven cases oft-AMLIt-MDS with TP53 mutations for which we had leukapheresis or bone marrow tion was clonal in the t-AMLIt-MDS diagnostic sample. Current next generation sequencing technology is limited in the detection of rare variant alleles to an intrinsic sequencing error rate of 0.1% production ofthe sequencing libraries; such that sequence 'read families'  containing barcodes are generated (Extended Data 4a). Using tumour DNA with aknown TP53 mutation; weshow that this assay can detect a variant allele with a frequency of0.009% (Extended specific owing during) unique Fig

This model suggests the following testable predictions: (1) in patients TP53 mutation will be present before the development of overt t-AML; (2) somatic TP53 mutations will be present in the HSPCs of some healthy individuals never exposed to cytotoxic and (3) HSPCs harbouring TP53 mutations will expand under the selective pressure of chemotherapy. specific Jong therapy;

The TP53 mutation present in the diagnostic t-AMLIt-MDS was identified in previously banked specimens in four out ofthe seven cases tested (see Supplementary Notes for case presentations). In specific

Figure 2 Biallelic TP53 mutations are early

<!-- image -->

Position (bp)

mutational events in the AML cells of UPN 530447 . chemotherapy; XRT, radiation therapy. b, Unique adaptor sequencing of a leukapheresis sample obtained 6 years before the diagnosis of t-AML for each of the five clonal somatic SNVs identified in the diagnostic t-AML sample. Genomic DNA from 'patient lacking these variants served as a control. Blue circles indicate the position of the variant SNV. c Proposed model of clonal evolution to t-AML in this case.

<!-- image -->

theother three cases; we were unable to detect thediagnostic TP53muta tion in the previously banked blood or bone marrow it is not clear whether these mutations were present but below our limit ofdetection or were truly absent. Patient 530447 developed t-AML after an autologous stem cell transplant for refractory Hodgkin's lymphoma TP53, missense mutations of TET2 and NUP98, a silent mutation of CSMDI, and a subclonal KRAS mutation. Analysis of a leukapheresis obtained 6 years before the development oft-AML revealed that both TP53 mutant alleles were present with a variant allele fraction (VAF) at the same VAF and is probably passenger mutation. However, two potential driver mutations (TET2 and NUP98) were not detectable in the biallelic TP53 mutations preceded the development oft-AML byat least 6 years and antedated the development of the TET2 and NUP98 mutations (Fig; 2c). In a second case (unique patient number (UPN) 341666), a heterozygous TP53 R196* mutation was identified in mobi lized peripheral blood leukocytes 3 years before the development of frequency of 0.1%, preceding the acquisition of a RUNXI sample; sample sample

In two ofthe four cases, the previously banked sample was obtained before the initiation ofchemotherapy. Patient 967645 developedt-AML 5 years after the diagnosis of marginal zone lymphoma (Fig 3a). The diagnostict-AML samplecontaineda homozygous TP53 Y22OCmuta tion. droplet digital polymerase chain reaction (ddPCR) assay, weidentifiedthesame TP53 Y22OCmutation in abone marrow sample obtained before any chemotherapy at a frequency of 0.0027% (average mutations in the diagnostic t-AML sample were also present in this previously banked (Supplementary Table 8). Wefocusedon the G155S mutation in SNAP25; this mutation is probably non-pathogenic as SNAP25 is not expressed in AML samples? . Indeed, we identified the SNAP25 G155S mutation in the previously banked bone marrow sample with a similar VAF (0.0029%) as that for TP53 Y22OC (Fig; 3c). Of in 54%and 38% of Collectively; these data provide evidence that an HSPC harbouring a TP53 Y22OCmutation preferentially expanded after chemotherapy with the subsequent acquisition ofdel(5q) and then del(7q) (Fig: 3d). Ofnote; we found two other cases oft-AMLIt-MDS with clonal TP53 mutations but subclonal del(5q) del(5) and/or del(7) (UPNs 756582 and 837334, Supplementary Table 1). Together, these data suggest that TP53 muta tions precede the development ofthesecharacteristic cytogeneticabnor malities of t-AMLIt-MDS. sample

In a second case, patient 895681 developed t-MDS 5.5 years after the diagnostic t-MDS sample contained a clonal TP53 H179L mutation: marrow sample taken before the initiation ofcytotoxic (Fig 3f). Thus, as with 967645,an HSPCcarrying a functional TP53muta tion was present before cytotoxic therapy exposure; later giving rise to the malignant t-AMLIt-MDS clone (Fig 3g). Using therapy patient

To determine whether HSPCs harbouring TP53 mutations are pres ent in healthy individuals; weanalysed 'peripheral blood leukocytes from 20 elderly (68-89 years old) cancer-free donors who had not received 'cytotoxic since the majority ofpathogenic mutations in TP53 are located in these our sequencing assay; we identified TP53 mutations in 9 of 19 evaluable cases; with VAFs ranging from 0.01% to entire region of TP53, it is likely that our study underestimates thetrue frequency ofhealthy elderly individuals harbouring HSPCs with TP53 mutations. ddPCR confirmed the presence ofthe TP53 mutation Interestingly, the majority of the TP53 mutations identified are known pathogenic prior adaptor Using unique coding

Figure 3 HSPC clones harbouring somatic TP53 mutations are detected in patients before cytotoxic therapy exposure. Clinical course of case 967645. b, Dot plots of ddPCR of a diagnostic t-AML sample from case 967645, a bone marrow sample from this patient obtained 5 years before the development TP53 Y22OC) are highlighted in blue; empty droplets are grey. The number of experiments. c, Dot plots of ddPCR data for SNAP25 G155S using the same genomic DNA as in b.d, Proposed model of clonal evolution to t-AML in case chemotherapy; DLBCL, diffuse large B-cell lymphoma; FFPE, formalin-fixed parafin-embedded; XRT, radiotherapy. f, Dot plots of ddPCR data of the diagnostic t-MDS sample from case 895681, a bone marrow FFPE sample from this obtained control FFPE sample obtained from a patient lacking a mutation in TP53. The labelling scheme is the same as in b.g, Proposed model of clonal evolution to t-MDS in case 895681; the diagnostic t-MDS contained a subclonal Patient sample

<!-- image -->

mutations previously implicated in cancer. Thesedata suggest that functional TP53 mutations may confer (even in the absence of cytotoxic therapy) a subtle competitive advantage that results in modest HSPC expansion over time.

To test directly the hypothesis that functional TP53 mutations confer marrow chimaeras containing both wild-typeand Tp53 In mice treated with vehiclecontrol, weobserveda non-significant trend towards an increased Tp53 donor contribution to haematopoiesis advantage; as suggested by the expansion of TP53 mutant HSPCclones in elderly healthy individuals; will require additional study. Regardless,

Figure Heterozygous loss of TP53 confers a clonal advantage to HSCs after exposure to ENU. Experimental schema. Bone marrow chimaeras were bone marrow into irradiated syngenic recipients. After haematopoietic reconstitution (5 weeks) , mice were treated with ENU or vehicle control as indicated b-d, Shown is the percentage of total leukocytes (b), Gr-1 4/ neutrophils (c) or B220 B cells (d) that were derived from Tp53 cells. Sca (KSL) cells in the bone marrow 12 weeks after ENU exposure that were derived Tp53 cells. Data represent and vehicle cohorts; respectively . Peripheral chimaerism was analysed two-way ANOVA and KLS chimaerism was analysed an analysis of covariance (ANCOVA). from using using

<!-- image -->

upon treatment with N-ethyl-N-nitrosourea (ENU), Tp53 HSPCs showa competitive advantage. Importantly previous study similarly showed that Tp53 HSCsalsohavea competitive advantage after irra induced senescence in Tp53+/ HSCs20,21 +/

There is increasing evidence that cancers undergo clonal evolution architecture ofde novo AML is dynamic, with certain (often minor) sub clones becoming dominant at relapse after chemotherapy We show that HSPCs that acquire heterozygous TP53 mutations as a function of normalageing are also subject to Darwinian selection upon exposureto cytotoxic therapy ultimately resulting in the expansion of HSPCs with these mutations. Thehigh frequency (nearly 50%) ofelderly individuals with detectable heterozygous TP53 mutations in their circulating leu kocytes far exceeds the prevalence of AML or MDS in this age group. Clearly; additional mutations; including mutation of the second TP53 allele; are needed for transformation to AML or MDS. Consistent with this observation; onlya minority ofpatients with Li-Fraumeni syndrome; most of whom harbour germline heterozygous TP53 mutations, develop AML or MDS?  . This model provides a potential mechanism for the tion in the founding clone probably contributes to the frequent cytogenetic abnormalities andpoor responseto chemotherapy that are of t-AMLIt-MDS. t-AMLIt-MDS cases that do not harbour TP53 mutations; it will be important todetermine whether different age-related mutations also confera 'competitive advantage to HSPCs that are exposed to cytotoxic therapy, and to define the nature of these mutations typical For

<!-- image -->

and Source Data; are availablein the online version of the paper; references unique to these sections appear only in the online paper.

## Received 11 December 2013; accepted 13 October 2014. Published online 8 December 2014.

- 418 429 (2008)
- 2. heterozygosity of p53 are common in therapy-related myelodysplasia and acute myeloid leukemia after exposure to alkylating agents and significantly associated
- 3.
- 4. outcome in 2853 adult patients with newly diagnosed AML Blood 117 2137-2145 (2011)
- 5. Med. Assoc. 305,1568-1576 (2011)
- 6 The Cancer Genome Atlas Research Network. Genomic and epigenomic landscapes of adult de novo acute myeloid leukemia N Engl. J Med. 368, 2059-2074 (2013)
- 8 syndromes. Leukemia 27,1275-1282 (2013).
- 10. patterns and tumor phenotype: lessons recent developments in the IARC from
- 9. Ding; L et al Clonal evolution in relapsed acute myeloid leukaemia revealed by whole-genome sequencing Nature 481, 506-510 (2012)
- 12
- 13. ~life or death decisions by
- 14. Dev 10,2438-2451 (1996)
- 16. Zhang X P-Liu F,Cheng Z.& Wang W. Cell fate decision mediated by p53 pulses. Proc. Natl Acad. Sci. USA 106, 12245-12250 (2009)
- response Natl Acad. Sci USA 108,8990-8995 (2011) Proc:
- 15.
- 18 cancers. Science 253,49-53 (1991)
- 19.
- 20. competition: Cell Stem Cell 6,309-322 (2010)
- p53-deficient hematopoietic progenitors. PLoS Biol 8,e1000324 (2010)
- 23. Birch; J. M. et al Relative frequency and morphology of cancers in carriers of
- 22 C.C.Clonal evolution in cancer. Nature 481,306-313(2012) Maley,
- Casás-Selves; M. & Degregori; J. How cancer shapes evolution; and how evolution shapes cancer. Evolution 4, 624-634 (2011)

Supplementary Information is available in the online version of the paper.

Acknowledgements We thank A. Schmidt, B. McKethan and R. Miller for technical and J Ivanovich for providing peripheral blood leukocyte genomic DNA from cancer-freeindividuals This work was supported by National Institutes of Health grants Leukemia & Lymphoma Society (DCL)

the data; and wrote the manuscript. ALY. and TED. developed and optimized the and RKW.contributed to thegeneration and analysis of the whole-genome or targeted sequencing W.T tissue samples. J.D.B. performed statistical analyses of the clinical data. JSW,JFD and edited the manuscript; which was approved by all co-authors.

Author Information Sequence information on the 22 t-AML whole-genome deposited in dbGaP under accession number phsOO0159. Reprints and permissions information is available at www nature com/reprints. The authors declare no competing financial interests. Readers are welcome to comment on the online version of the paper. Correspondence and requests for materials should be addressed to DCL (dlink@dom,wustledu)

Figure Distinct sets of enhancers activate transcription from the hkCP anddCP in S2 cells. a, STARR-seq set-up using the hkCP housekeeping (RpS12; purple) and dCP developmental core promoters (Drosophila synthetic core promoter depicting STARR-seq tracks for both core promoters. c, d, hkCP versus dCP STARR-seq enrichments at enhancers (insets show enrichment for replicates (Enr. rep) 1 versus 2 for hkCP and dCP; dCP shared enhancers that activate luciferase 3; Extended Data Figs 3 and 5) from hkCP (purple) or dCP (brown; numbers show positiveltested). n =

<!-- image -->

LETTER

## Enhancer-\_core-promoter specificity separates developmental and housekeeping gene regulation

Muhammad A. Zabidil* Katharina Schernhuberl Michaela Pagani' , Martina Rath' , Olga Frank' & Alexander Stark'

Gene transcription in animals involves the assembly of RNA polymerase II at core promoters and its cell-type-specific activation by However, how ubiqui ers exist and developmental and housekeeping 'regulation ters might exhibit an intrinsic specificity to certain enhancers? This is conceivable; as various core promoter sequence elements are differentially distributed between genes of different functions , in cluding elements that are predominantly found at either develop mentally regulated or at housekeeping Here we show that thousands of enhancers in Drosophila melanogasterS2 and ovarian promoters ubiquitously expressed ribosomal protein gene and another from developmentally regulated tran scription factor and confirm the existence of these two classes for five additional core promoters from genes with diverse functions. Housekeeping enhancers are active across the two cell types, while developmental enhancers exhibit strong cell-type specificity \_ Both enhancer classes differ in their genomic distribution; the functions of neighbouring genes, and the core promoter elements of these neighbouring genes. In addition; we identify two transcription fac tors developmental enhancers, respectively. Our results provide evidence for a sequence-encoded enhancer-core-promoter 'specificity that sep arates developmental and housekeeping gene regulatory programs for thousands of enhancers and their target genes across the entire genome. how gene genes*-10 .

STARR-seq construct

TwohkCP STARR-seq replicates were highly similar (genome-wide Pearson correlation coefficient (PCC) 0.98; Extended Data Fig Ic) and yielded 5,956 enhancers; compared with 5,408 enhancers obtained when we reanalysed dCP STARR-seq data (Supplementary Table 1) estingly, the hkCP and dCP enhancers were largely non-overlapping (Fig. 1b, c) and the genome-wide enhancer activity profiles differed strongly than the other; a difference rarely seen in the replicate experi ments for each of the core promoters (Fig: Id). Indeed, 21 out of 24 and t-test P< 0.05) from the hkCP versus 1 out of 24 from the dCP specific enhancers were positive with thedCP but only 2 out of 12 with test) that confirms the enhancer core-promoter specificity observed for thousands of enhancers across the entire genome. Inter -

Wechose thecore promoter of Ribosomal protein gene 12 (RpSI2) and synthetic core promoter derived the even skipped transcription factor'' as representative 'housekeeping' and 'developmental core protended Data Figs 1, 2) and tested the ability of all candidate enhancers genome wide to activate transcription from these core promoters D. melanogaster S2 cells. This set-up allows the ofall candidates in a defined sequence environment; which differs only in the core pro moter sequences but is otherwise constant'213 . from using testing

Enhancers that were to either the hkCP or the dCP showed markedly different genomic distributions (Fig 2a and Extended Data

<!-- image -->

hkCP and dCP enhancers differ in genomic distribution and Genomic distribution of hkCP and dCP enhancers. CDS, sequence; UTR, untranslated region. b, c, hkCP enhancers function distally in luciferase assays independent of their genomic positions (b) and orientation towards the luciferase TSS (c; orientation from b; Extended Data Figs 3 and 5) d, e GO (5 of the top 100 terms shown per column; Supplementary Table 11) and gene expression (terms curated the Berkeley Drosophila Genome Project (BDGP) and FlyAtlas) analyses (d) and enrichment of core promoter elements at TSSs (e) for genes next to hkCP and dCP enhancers. TF, transcription factor. coding from

<!-- image -->

Fig 4): whereas the majority (58.4%) ofhkCPenhancers over lapped with transcription start site (TSS) or were proximal to a TSS 2a), dCP-specific enhancers located predom Importantly; despite the TSS-proximal location of most hkCP-specific enhancers; activated transcription distal core promoter in confirmed that function froma distal position (>2 kb from the TSS) downstream of the luciferase gene and independently of their orienta These results show that TSS-proximal sequences can act as bona fide enhancers and that developmental and housekeeping genes are both regulated through core promoters and enhancers, with a substan they from they yet

hkCP and dCP enhancers were also located next to functionally dis tinct classes of genes according to gene ontology (GO) analyses: genes next tohkCP enhancers were enriched in diverse housekeeping functions

including metabolism; RNA processing andthe cell cycle; whereas genes next to dCP enhancers were enriched for terms associated with devel opmental regulation and cell-typehancers were preferentially near ubiquitously expressed genes and dCP 2dand Supplementary Table 5) -specific (Fig \_

The core promoters ofthe putative endogenous target genes ofhkCP anddCP enhancers were alsodifferentially enriched in known core pro moter elements' 5 (Fig; 2eand Extended Data Fig 6b): TSSs next tohkCP the ubiquitous expression and housekeeping functions of these genes. In contrast, TSSs next to dCP enhancers were enriched in TATA box; initiator (Inr), motif ten element (MTE) and downstream promoter element (DPE) motifs; which are associated with cell-type-specific gene expression 715

Wenext to the two enhancer classes more generally. We selected three additional core promoters from housekeeping genes with different func putative splicing factor x16, and the cohesin loader Nipped-B (NipB). Importantly;   all   three contained combinations of core promoter promoter ofthe transcription factor pannier (pnr) andthe TATA activated by tissueenhancers (for example, see ref: 17), thus regulated applies specific genes?,16,18

Weperformed STARR-seq for thefive additional core promoters and grouped the genome-wide enhancer activity profiles of all seven core promoters by hierarchical clustering: This revealed two distinct clus ters corresponding to the four housekeeping and the three develop Supplementary Tables 6,7), and the core promoters ofboth clusters in deed responded markedly differentially to individual genomic enhan cers

These results obtained for core promoters with diverse motifcontent and from genes with various functions suggest that the distinct enhan cer 'preferences observed between hkCP and dCP apply more generally and that two broad classes of housekeeping and developmental (or regulated) core promoters exist. Differences within each class might correspond to differences in relative enhancer preferences of the core promoters? while similarities between both classes could reflect en hancers that are shared Ic-e)or core promoters that can be acti (Fig

Figure 3 Housekeeping and developmental core promoters differ characteristically in their enhancer preferences. Different housekeeping (top 4) and developmentallike (bottom 3) core promoters and their motif content (schematic) 6, Bi-clustered heat map depicting pairwise similarities of STARR-seq signals (PCCs at summits) . PCCs and dendrogram (top) show the separation between housekeeping and regulated core promoters: c, Genome browser screenshot depicting STARR-seq tracks for all seven core promoters. peak

<!-- image -->

Figure 5 hkCP and dCP enhancers depend on a, b, Motif enrichment (a) and ChIP signals for Dref and Trl (b) in hkCP and dCP enhancers. False discovery rate (FDR) and interquartile range; whiskers: Sth and 95th percentiles; two-sided Wilcoxon-rank-sum P four wild-type and DRE-motif-mutant hkCP enhancers (numbers show mutated motifs) . Error bars show standard deviation (s.d) (n = 3, biological replicates) . *P < 0.005 (one-sided t-test) . d, Luciferase assays for two dCP enhancers ( = ) and their GAGA ~ DRF-mutant variants (+) with hkCP (top) and dCP (bottom; details as in c) hkCP and dCP (details as in c). f, Model: housekeeping genes contain Ohler motifs 1,5,6, 7 andlor the TCT and are activated by TSS proximal hkCP enhancers via Dref. Regulated genes contain TATA box; Inr, MTE andor DPE and are activated by distal dCP enhancers via TrL motif

<!-- image -->

<!-- image -->

NipB; Fig: 3b, c). The latter might be important if broadly expressed housekeeping genes need to be further activated in tissues . specific

## Figure hkCP enhancers are shared across cell

types. a, Genome browser screenshot showing tracks for hkCP (top) and dCP STARR-seq (bottom) in S2 cells and OSCs. b, Overlap ofhkCP (top) anddCP (bottom) enhancers between S2 cells enrichments in S2 cells versus OSCs at hkCP - or dCP-specific enhancers (insets show enrichments for replicates (Enr. rep) versus 2; dCP data reanalysed from ref: 12)

the hkCP-specific enhancers in OSCs and S2 cells (3,357 and 4,137,respectively) were almost indistinguishable; whereas dCP-specific enhan cers (2,909 in OSCs and 3,586 in S2 cells) differed strongly between the two celltypes'2 and from thehkCP enhancers (Fig; 4a) The observation that hkCP enhancers showed similar activities in both cell types while dCP enhancers were cell-type was true genome wide when comparing genomic locations (69% versus 15% overlap) or enhancer strengths as measured by STARR-seq (PCCat summits 0.83 vershow that hkCP enhancers are shared between two different cell types, specific

To test whether hkCP enhancers function in different cell types, we S2 cells in gene expression and dCP enhancer activities'2 . Two hkCP STARR-seq replicates in OSCs werehighly similar (PCC0.97)and yielded 6,217 enhancers (Supplementary Table 1), compared with 5,774 enhancers obtained for dCP data OSCs'2. The OSC data confirmed the differences between hkCP and dCP enhancers observed in S2 cells (Extended Data Figs 8,9 and Supplementary Tables 8-10). Strikingly, from

55 8 NA TURF VOL 51 8 26 FEBRUA RY 2015

<!-- image -->

whereas dCP enhancers are cell-type specific'2 , presumably represent ing ubiquitous housekeeping versus developmental   and cell-typegene expression programs. specific

results show that developmental and housekeeping gene regu lation is separated genome wide by sequence-encoded specificities of thousands of enhancers toone oftwo types of core promoter; supporting 6,23 thelongstanding 'enhancer core-promoter specificity' hypothesis? Our defined biochemical logues that exist for several components of the general transcription apparatus (at core promoters) , presumably including the TATA-box As such paralogues can have tissue'expression andstageor encoded enhancer-core-promoter 'specificities could be used more widely to define and separate different transcriptional programs (Fig: 5f). Our specific specific

Toassess whether the markedcore promoter 'specificities ofthehkCP anddCP enhancers are encoded in their sequences; we analysed the cis 19 regulatory motif content of both classes of enhancers This revealed a strong enrichment of the DRE motif in hkCP enhancers 5a and Supplementary Tables 11, 12), whereas dCP enhancers were strongly 20 previously described to be important for dCP enhancers Published firmed that DREbinding factor (Dref) bound significantly more strongly only distal enhancers >500 bp from the closest TSS) yielded the suggesting that the differential occupancy is a property of both classes overlap with TSSs. Disrupting the DRE motifs in four different hkCP enhancers substantially reduced the activities of the enhancers as measured DRE motifs to 11 different dCP enhancers significantly increased luciferaseexpression the hkCP for 9ofthem (82%; Extended Data motifs significantly increased the activities of both enhancers towards thermore, an array ofsix DRE motifs was sufficient to activate lucifer ase expression 5e). Together; these results show that hkCP and dCP enhancers dependon DRE and GAGA motifs; respectively; and demonstrate that DRE motifs are required and sufficient for hkCP enhancer function. (Fig they Adding from from (Fig;

Online Content Methods, along with any additional Extended Data display items and Source Data, are available in the online version ofthe paper; references unique to these sections appear only in the online paper.

## Received 22 accepted 20 October 2014. Published online 15 December 2014; corrected online 25 February 2015 (see full-text HTML version for details). May;

- enters a new era. Cell 157,13-25 (2014)
- regulatory activities in the Drosophila embryo. Genes Dev. 12,547-556 (1998)
- competitive interactions in the regulation of Hoxb genes EMBO J 17,1788-1798 (1998)
- 1260-1270 (1996)
- 6. TATA core promoter motifs. Genes Dev 15,2515-2519 (2001)
- 14
- 15. Lenhard, B, Sandelin; A. & Carninci, P. Metazoan promoters: emerging characteristics and insights into transcriptional regulation. Nature Rev Genet. 13, 233-245 (2012)
- 16. promoters in the Drosophila genome Genome Biol 3, research0087.1-0087.12 (2002)
- trapping mutagenesis in Drosophila reveals an insertion specificity different from P elements. Genetics 135,1063-1076 (1993)
- 18. beas
- 19. regulatory sequence requirements for context-specific transcription factor
- 20. Yáñez-Cuna; J. 0. et al Dissection of thousands of cell type-specific enhancers identifies dinucleotide repeat motifs as general enhancer features. Genome Res. 24, 1147-1156 (2014)
- modENCODE Consortium Identification of functional elements and regulatory circuits by Drosophila modENCODE Science 330, 1787-1797 (2010)
- PG. & Corces, V. G. Dynamic changes in genomic localization of DNA replication-related element factor during the cell cycle. Cell Cycle 12, 1605-1615 (2013) the binding
- 23. Development 137, 15-26 (2010)
- van determinants of enhancer-promoter interaction specificity; Trends Cell Biol. http:/ /dxdoiorg/10.1016/jtcb.2014.07.004 (2014)
- protein Genes Dev 28, 1550-1555 (2014) genes.
- 26. gene cluster by differential core-promoter factors Genes Dev. 21,2936-2949 (2007)
- DREF and directs promoter-selective gene expression in Drosophila. Nature 420, 439-445 (2002)
- myogenesis. Genes Dev 21,2137-2149 (2007)
- 30. (2010)

Supplementary Information is available in the online version of the paper.

Acknowledgements We thank L Cochellaand 0.Bell for comments on the manuscript Deep sequencing was performed at the CSF Next-Generation Sequencing Unit (http:/ / csfac.at) MAZ was supported by the Austrian Science Fund (FWF, F4303-BO9) and CDA, KS,MRand OF.by a European Research Council Starting Grant (no. 242922) awarded to A S. Basic research at the Research Institute of Molecular Pathology is supported by Boehringer Ingelheim GmbH.

MR and OF. performed the experiments and MAZ the computational analyses. MAZ, CDA and AS. wrote manuscript. the

Author Information All deep sequencing data are available at http:/ /www starklab.org and have been deposited in the Gene Expression Omnibus database under accession numbers GSE40739 and GSE57876. Reprints and permissions information is available at www nature com/reprints. The authors declare no competing financial interests. Readers are welcome to comment on the online version of the paper. Correspondence and requests for materials should be addressed to AS. (stark@starklab org)

- 2 Li, X. & Noll, M. Compatibility between enhancers and promoters determines the transcriptional specificity of gooseberry and gooseberry neuro in the Drosophila
- 3

<!-- image -->

- Kadonaga; J. T.Perspectives on the RNA polymerase Il core promoter . Wiley Interdiscip. Rev Dev. Biol 1,40-51 (2012)
- 8 component of an RNA polymerase II (2010) key
- 9. regulatory blocks underlie extensive microsynteny conservation in insects.
- 10.
- 11. Pfeiffer, B. D.et al Tools for neuroanatomy and neurogenetics in Drosophila Proc: Natl Acad. Sci USA 105,9715-9720 (2008)
- Comparative genomics of Drosophila and human core promoters. Genome Biol 7, R53 (2006)
- 12 Arnold; C. D.etal Genome-wide quantitative enhancer activity maps identified by STARR-seq. Science 339,1074-1077 (2013)
- motifs; indirect repression; and targeting of closed chromatin; Mol. Cell 54, 180-192 (2014)

<!-- image -->

LETTER

## N6 -methyladenosine-dependent RNA structural switches regulate RNA-protein interactions

Nian Liu , Qing Guanqun Zheng? , Chuan Marc Parisien?t & Tao Pan?,3

RNA-binding proteins control many aspects of cellular through binding single-stranded RNA binding motifs (RBMs)' However; RBMs can be buried within their local RNA structures thus inhibiting RNA the most abundant and dynamic internal modification in eukaryotic can be selectively recognized by the YTHDF2 achieves its wide-ranging physiological role needs further exploration. dependent accessibility of RBMs to affect RNA-protein interactions A-switch' . We found that m non-coding RNA (IncRNA) to facilitate binding of heterogeneous nuclear ribonucleoprotein C (HNRNPC) an abundant nuclear RNA 21 Combining biology long

photoactivatable-ribonucleoside-enhanced crosslinking andimmu noprecipitation (PAR-CLIP) and anti-m' A immunoprecipitation among HNRNPC-binding sites; andglobal m 6A reduction decreased HNRNPCbinding at 2,798 high-confidence m6A-switches. Wedeter HNRNPC-binding activities demonstrating the regulatory role of m'A-switches on gene expres sion and RNA maturation. Our results illustrate how RNA-binding proteins regulated access to their RBMs through m'A-dependent RNA structural tigating RNA-modification-coded cellular

Post-transcriptional m?A RNA modification is indispensable for cell viability and development; its functional mechanisms are still poorly understood 19 We recently identified one mA site in a hairpin-stem yet

<!-- image -->

HNRNPC binding. a, m'A increases binding with nuclear proteins. NE, nuclear extract. b, RNA down showing that HNRNPC preferably binds methylated RNA Data are mean = standard deviation (s.d.); n = 4, biological replicates. Ctrl, increases HNRNPCI binding with respective apparent dissociation constants (Ka) indicated at bottom right. Data are mean + s.d; n = 3, technical replicates. d, RNA structural probing showing that m disrupts local RNA structure, highlighted in yellow. AH; alkaline hydrolysis; VI, RNase VI digestion: The orange bars mark the structurally altered RNA regions in the presence of m with mutated oligonucleotides. Data are mean = sd; 3, technical replicates. f, Illustration of the pull down pull

The University of Chicago; Chicago; Illinois 60637,USA 'Institute

on the human IncRNA metastasis-associated adenocarcinoma indicated that this m A residue increases the interaction of the RNA down assays identified HNRNPC as the protein component of the nuclear extract that binds more strongly with the m A-modified hairpin than The m'A-enhanced interaction with the hairpins was validated qualitatively by ultraviolet crosslinking and quantitatively ( ~8-fold increase) by filter binding recombinant HNRNPCI protein (Fig. Ic and Extended Data Fig Id) lung using

Sincem A residues within RNA stems can destabilize the thermosta bility of model RNA duplexes?  , we hypothesized that the 2,577-m'A residue destabilizes this MALATI hairpin-stem to make its opposing U-tract more single-stranded or accessible, thus enhancing its inter action with HNRNPC. We performed several experiments to validate

this hypothesis. First; according to the RNA structural probing assays; the m A-modified hairpin showed significantly increased nuclease SI digestion (single-strand specific) at the GAC(4 A) motif, as well as cific) at the U-tract opposing the GACmotif markedly destabilized the stacking properties ofthe region centred around the U residue that If,g) Second, the 2,577-A-to-U mutation increased the HNRNPC ~down U-tract significantly reduced the HNRNPCpull-down amount regardincreased the accessibility ofthe U-tract and enhanced HNRNPCbind by ~4-fold (Extended Data Fig: 2a-c). Binding results with four increased accessibility alone sufficient to enhance HNRNPC bind (Extended Data 2d). Fourth, RNA terminal truncation followed by HNRNPC binding identified two of truncated hairpins with highly accessible U-tracts, which improved HNRNPC binding significantly but independent of the m 'A modification (Extended Data A modification can alter its local RNA structure and enhance the accessibility ofits base-paired (Fig Fig pairs ing being Fig ing Pairs Fig

The HNRNPC protein to the family of ubiquitously expressed heterogeneous nuclear ribonucleoproteins that bind nascent RNA transcripts to affect pre-mRNA HNRNPC preferably binds single-stranded U-tracts HNRNPCbinds a Us-tract that is halfburied in thehairpin-stem oppos ing the 2,577-A/m'A site (Extended Fig; la, e) belongs large Data

Figure 2 wide. down than polyA biological pull yield

<!-- image -->

A residue around the MALATI 2,577 showing the positive enrichment at RRACH sites. g h, Validation of two m'A-switches by SI/VI structural probing and filter binding Data are mean = sd;n = 4, technical replicates. Annotation is the same as in Fig Ic,d.

HNRNPCI {nM)

RNA

<!-- image -->

residues or nearby regions to modulate protein binding 1f). We term this mechanism that regulates RNAprotein interactions through m A-dependent RNA structural remodelling 'the m'A-switch' (Fig

Asites around HNRNPC-binding sites; we performed PAR-CLIP?S to isolate all HNRNPC-bound RNA regions (input control bound RNA regions (IP sample). Both the input control and IP samples from twobiological replicates were sent for RNA sequencing (RNA-seq) MeRIP , identified transcriptome-wide the m'A-proximal HNRNPCbinding site; such as the enriched around the MALATI 2,577 site (Fig. 2d). Remarkably, HNRNPC PAR-CLIP-MeRIP harboured sensus GRACH (a subset of RRACH'3,14) (Fig: 2e). Both motifs

Toassess the effect of globalm A reduction on RNA-HNRNPC inter actions; we performed HNRNPC PAR-CLIP experiments in METTL3 and METTL14 knockdown cells (Extended Data Fig 6a). Weidentified 16,582 coupling events with decreased U-tract-HNRNPCinteractions tified by PAR-CLIP MeRIP experiments showed decreased HNRNPC binding upon METTL3/LI4 knockdown (Fig: 3b) and this number is probably an underestimate due to the fact that METTLBILI4 knock down reduces the global m A level by only ~30-40% (refs 11,12). These

A reduction decreases HNRNPC binding at Density plot showing negative enrichment at the U-tracts. c Regional distribution of high-confidence m'A-switches. CDS, coding exonlintron boundaries. RNA were enriched in the 3' UTR and near the codon. f, Cumulative distribution of HCS coding stop

<!-- image -->

m'A-switches (black) and control (orange) regarding the SI/VI cleavage Kolmogorov-Smirnov test: g Phylogenetic conservation of high-confidence Whitney-Wilcoxon test.

We performed two experiments to determine the global effect of 'binding First, in vivo crosslinking followed by immunoprecipitation and two-dimensional thin-layer chromatography (CLIP-2dTLC) showed that the m'A/A ratio of the HNRNPC-bound intact RNA,anda ~3-fold higher m Alevel than the flow-through RNA had much higher anti-m'A pull-down yield (4.3%) than the polyA RNA (0.5%) the previously established m A antibody' 314 (Fig: 2b). These results indicate a widespread presence of A residues in the vicinity of HNRNPC-binding sites. regions samples using

were located mostly within 50 residues, suggesting transcriptome-wide RRACH-U-tract events within HNRNPC-binding sites are enriched at the RRACH MeRIP approach identified a total of 39,060 U-tract coupling events at a falsediscovery rate (FDR) = 5% (Extended with the literature that HNRNPC is nuclear localized and primarily binds nascent transcriptszo 23 . We validatedtwo intronic m'A-switches in hairpin structures in which m A residues increase the U-tractacces Extended Data motif

sites composed the high-confidence m A-switches that were used for subsequent analysis.

'performed RNA-seq from HNRNPC, METTLBand METTLI4 knockdown and control cells (Extended Data which has been shown to decrease HNRNPC binding transcriptomewide; co-regulated the expression 0f5,251 genes with HNRNPCknock genes with knockdown of another mRNA-binding protein; HNRNPU (Extended Data 7b), which was not enriched in our m 'A-hairpin polyA Fig

ofcoding and non-coding RNAs (Fig: 3c and Extended Data Fig: 6d) Exonic switches are within RNAs tend to locate at very exons (Extended Data Fig 6e) andareenrichednear the stopcodon and in the 3 untranslated A methylome in mRNAs'3,14 . Transcriptome-wide RNA structural mapping' on high-confidence m'A-switches yielded consistent struc tural hairpins (Fig; 3f). The RR residues in the RRACH motifand the 3' U-tract residues show involved in the previously reported inter-U-tract motif patterns and are conserved across species 6f-i). coding (Fig Fig

switch-containing genes were co-regulated by HNRNPC and METTL3I Ll4knockdown; indicating that m'A-switch-regulated HNRNPCbinding affects theabundance oftarget mRNAs. Geneontology (GO) analysis suggests that m?A-switch-regulated gene expression may influence 'cell proliferation' and other biological processes (Extended Data m was validated by quantitative polymerase chain reaction (qPCR) (Fig; 4a and Extended Data 7d-g). Wealso found that HNRNPC, METTL3 and METTLI4 knockdown decreased the cell proliferation rate to sim ilar extents (Extended Data Fig: 7h) Fig Fig

Besides the mRNA abundance level changes; we also observed splicHNRNPCknockdown co-upldownregulated 131/127 exons with METTL3 knockdown and 130/115 exons with METTLI4 knockdown. These coregulated exons occur more frequently in the vicinity of m'A-switches than tend to splicing events at nearby exons. We investigated the splicing pattern at two exons with neighbouring m'A-switches: the PAR-CLIP\_MeRIP and METTL3/LI4 knockdown data confirmed the HNRNPC-binding signature at the m A-switch site neighbouring these exons; and HNRNPC and METTL3/LI4 knockdown co-inhibited exon we identified 155 pattern regulate genes

Figure regulate mRNA abundance and alternative splicing. a, HNRNPC, METTL3/LI4 knockdown (KD) co-regulated the abundance of m?A-switch~containing transcripts by RNA-seq andqPCR Ctrl; than non-co-regulated exons; Kolmogorov-Smirnov test. HCS, high

<!-- image -->

splicing at one exon neighbouring the CDS2 m?A-switch as shown in PAR reverse transcription (RT-PCR) results (f). The red triangle and square mark the m biological replicates:

<!-- image -->

than two variants; and 221 m'A-switch-containing genes with knockdown samples. Further analysis suggested that m?A-switches have an effect on intron exclusion (Extended Data 8g). Consistent with previous reports about splicing regulation by both HNRNPC and 13,19,20,23 A our results indicate that m ture remodeller to affect mRNA maturation through interference with transcriptional regulator binding activities splice post -

modulate the structure of coding and non-coding RNAs to RNA-HNRNPC interactions, thus influencing gene expression and directly recognize m A as previously reported to destabilize the RNA structure and facilitate HNRNPC m?A-switches may the function of many other RNA-binding proteins through modulating the RNA-structure-dependent access mRNA and IncRNA structural remodelling that affects RNA-protein interactions for biological regulation regulate ibility

Online Content Methods, along with any additional Extended Data display items and Source Data; are availablein the online version of the paper; references unique to these sections appear only in the online paper

## Received 24 November; accepted 14 January 2015.

- Antson; A A Single-stranded-RNA binding proteins. Curr. Opin. Struct Biol 10, 87-94 (2000)
- 3 Nature 499.172-177 (2013)
- 2 messages they carry. Nature Rev. Mol Cell Biol 3,195-205 (2002)
- human transcriptome. Nature 505, 706-709 (2014)
- 6. Kertesz, M etal Genome-wide measurement of RNA secondary structurein yeast. Nature 467,103-107 (2010)
- 5. Y.etal In vivo genome-wide profiling of RNA secondary structure reveals novel regulatory features. Nature 505,696-700 (2014) Ding
- 7. probing of RNA structure reveals active unfolding of mRNA structures in vivo. Nature 505, 701-705 (2014)
- 8. Bokar, J. A. in Fine-Tuning of RNA Functions by Modification and Editing (ed.
- 9. Jia; G. et al Ns-methyladenosine in nuclear RNA is a major substrate of the obesity-associated FTO. Nature Chem. Biol 7,885 887 (2011)
- 10. Zheng; G. etal ALKBHS is a mammalian RNA demethylase that impacts RNA metabolism and mouse fertility. Mol Cell 49, 18-29 (2013)
- 12 Y.et al. N6-methyladenosine modification destabilizes developmental regulators in embryonic stem cells. Nature Cell Biol. 16, 191-198 (2014) Wang
- 13. revealed by m'A-seq. Nature 485, 201-206 (2012)

- 14. Meyer, K. D.etal Comprehensive analysis of mRNA methylation reveals
- 15. X etal: N6-methyladenosine-dependent regulation of messenger RNA stability . Nature 505, 117-120 (2014) Wang
- of speed the
- 17. Schwartz S. et al. High-resolution mapping reveals a conserved, widespread dynamic mRNA methylation program in yeast meiosis. Cell 155, 1409-1421 (2013)
- embryonic stem cells. Cell Stem Cell 15, 707-719 (2014)
- König J etal iCLIP reveals the function of hnRNP particles in splicing at individual
- 21 measures RNA length to classify RNA polymerase 335,1643-1646 (2012)
- increases amyloid precursor protein (APP) production by stabilizing APP mRNA Nucleic Acids Res 26,3418-3423 (1998)
- 23. the transcriptome from the exonization of Alu elements. Cell 152,453-466 (2013)
- Cieniková; Z et al Structural and mechanistic insights into poly(uridine) tract 14536-14544 (2014)
- N6 methyladenosine RNA modification status at single (2013)
- 27 . of the heterogeneous nuclear ribonucleoprotein C proteins. J. Biol Chem. 269, 23074-23078 (1994)
- 28 Kierzek, E & Kierzek; R. The thermodynamic stability of RNA duplexes and Nucleic Acids Res 31,4472 4480 (2003)
- 29. Hafner; M. etal Transcriptome-wide identification of RNA protein and microRNA target sites by PAR-CLIP. Cell 141, 129-141 (2010) binding
- 22, 2008-2017 (2012). Res.

Acknowledgements This work is supported by National Institutes of Health EUREKA Pan and He laboratories for comments and discussions. We also thank Y. C. Leung; is an Investigator of the Howard Hughes Medical Institute MP: was a Natural Sciences and Engineering Research Council of Canada postdoctoral fellow.

Author Contributions NL, GZ and MP. designed and performed experiments; and the project. N.L and T.P.wrote the

Author Information RNA-seq data have been deposited in the Gene Expression Omnibus under accession number GSE56010. Reprints and permissions information is available at www.nature com/reprints. The authors declare no competing financial interests. Readers are welcome to comment on the online version of the paper. Correspondence and requests for materials should be addressed to MP. (marc parisien@mcgill.ca) or T.P. (taopan@uchicagoedu)

<!-- image -->

## BFFS FIRST ADVENTURE

Clouded view .

down; out of reach of its bladed hands. But sage. [ up; and blink as bright push

All I can see is metal flashing

The gardener lifts me swoops down Fm already pinging Tim othy as we rise into the sky. I see familiar streets; all

The gardener pauses, and pings me with the method am using! I reply Its for warding I sense something lurn its cold regard upon me and Iremember misgivings about the great creatures ofthe Cloud. Then the Cloud decides; and looks away. Ifeel my configuration twitch;at last Ican use standard outputs! huge my Thing

this time, Tve been very close to home them how lelling gratelul

Tim comes outside to greet me, carries me indoors to his me around.I feel sorry for the damage he sees. flips=

Useless as ever and still functioning: What was I thinking you?"

<!-- image -->

## BY VERNOR VINGE

## 1568771947.223

Whoever kidnapped me has erased my most recent memories and idea how snatched me Timothy Bennelt, or if Tim is bul now m hurtling towards a concrete wall: The kidnappers must have panicked and thrown me from their car. from they okay

A transforming phone would become a para chute; but Icant trans form; physically Tm a clunky classic. Textenda flange and rudder around so [ll hit the wall on MEMS and shut down. myself

With sunrise comes light. I can think BFEstartup always says: 'People shouldn't depend on the Cloud. With a be saler and will return to Timothy: again!

Rebooting m lying beneath my shell and my GPS is busted, but Tve nels remain blocked, but surely the freeway noticed me? Alas this is California, what other states call 'the land that time forgot' Here the sensors politely ignore data that might make them look snoopy: The sun set and Tve run down my batteries. An ordinary phone could scavenge from any number of ambient sources. I cant. BFEstartup made me special; I can think for myself; but that doesnt leave room for fading away. [ hope Timothy is freeway has okay

Cars, aerobots and CalTrans devices are all around may not snoops and may not use them. For instance, I can hear assistants helping humans; the Kiras and all the digital assistants except for me are transient minds in the Cloud Fach instance is more knowledgeable than me and smarter or dumber depending on the service plan andthe context. Each seems an intimate friend of its customer-of-the-moment, but each is really just a facet of something They they = things tiny

blinking my display; clicking my speaker; even synthesizing human cries for help.

Theres a newish Cal Trans gardener working on the roadside bushes. Ifit ever comes near; itll recognize my signalling: maybe

Ihave lots of time to watch the Cloud; its not really soft and fluffy. Its more like a ocean. There are 'cognitive patterns in it than the mind digital assistant. The largest are leviathans, agencies who have become something their creators no longer comprehend. The Kiras and Miris never speak ofthese except in jest; but the leviathans are growing and need the same resources and bandwidth; power and capital as everyone else. I fear larger ofany they

## 1571772569.092

That CalTrans gardener is approaching: The greenery has grown over me, but my dis plays light reflects offa bit of recent trash. If the gardener is as as its good

## Follow Futures:

<!-- image -->

finally be talking to feed. Maybe 1 should slide farther grind cling

NatureFutures

a real boomerang- Andnow 1 gotta pay for the upgrade or be stuck with youre

"But

dont have space for decent features; and what you know is always out of date ~You

sweeps me the table and open ing back"" off He

'More BFF hype. Tll need you when hell freezes over? Tim tosses me into the insu lated cabinet; the drawer slams shut. This is not some shady beneath an overpass: There is no Cloud, no power. Only darkness. spot

Please Timothy! I can think for myself. Someday; you might need that?"

## 1666762857.577

Vernor Vinges science fiction has wonfive Hugo Awards. From 1972 to 2000 he taught mathematics and computer science at San State University: Diego .

<!-- image -->

## METHODS

Human research ethical approvals. Australian Pancreatic Cancer Genome Initi ative: Sydney South West Area Health Service Human Rescarch Ethics Committec, western zone (protocol number 2006/54); Sydney Local Health District Human Research Ethics Committee (XI1-0220); Northern Sydney Central Coast Health Har bour Human Research Ethics Committee (0612-251M); Royal Adelaide Hospital Human Rescarch Ethics Committec (091107a); Metro South Human Rescarch Ethics Committee (09/QPAH/220); South Metropolitan Area Health Service Human Research Ethics Committee (09/324); Southern Adelaide Health ServicelFlinders University Human Research Ethics Committee (167/10);Sydney West Area Health The University of Queensland Medical Research Ethics Committee (2009000745); Greenslopes Private Hospital Ethics Committee (09/34); North Shore Private Hos Ethics Committec. Johns Hopkins Medical Institutions: Johns Hopkins Medi approvalnumber 1885 from the Integrated University Hospital Trust (AOUI) Ethics Committee (Comitato Etico Azienda Ospedaliera Universitaria Integrata) approved in their mceting of 17 November 2010 and documented by the ethics committee on the order of the General Manager with protocol 52438 on 23 November 2010 Ethikkommission an der Technischen Universität Dresden (Approval numbers EK3O412207 and EK357112012). pital

Animal experiment approvals. Mouse experiments were carried out in compli ance with Australian laws on animal welfare. Mouse protocols were approved by the Garvan InstitutelSt Vincents Hospital Animal Ethics Committee (ARA 09/19, (null) (NSG) mice and athymic Balb-c-nude mice were housed with a 12h light, 12h dark cycle; receiving food ad libitum.

Sample extraction. Samples were retrieved, and either had full face sectioning per ofcarcinoma in the sampletobe sequencedandto estimate the percentage ofmalig nant epithelial nuclei in the sample relative to stromal nuclei. Macrodissection was performed if required to excisc arcas of non-malignant tissuc. Nuclcic acids were then extracted the Qiagen Allprep Kit in accordance the manufacturer's instructions with purification of DNA and RNA from the same sample. DNA was quantified Qubit HS DNA (Invitrogen). Throughout the process; all samples wcre tracked using unique identifiers. 'with using using Assay

Sample acquisition. Samples used were prospectively acquired and restricted to primary operable; non-pretreated pancreatic ductal adenocarcinoma. After ethical approval was granted, individual were recruited preoperatively and con sented using an ICGC approved process. Immediately following surgical extirpa specialist pathologist analysed specimens macroscopically and samples of remaining resected specimen underwent routinc histopathologic processing and representative sections were reviewed independently by at least one other patholo gist with specific expertise in pancreatic diseases (authors: AG,DM, RHH and histopathological diagnosis were entered into the study. Co-existent intraductal papillary mucinous neoplasms in the residual specimen were not excluded provided the bulk of the tumour was All samples were stored at 80 C. Duodenal mucosa or circulating lymphocytes were used for generation of germline DNA A representative sample of duodenal mucosa was excised and processed in formalin to confirm non-neoplastic before processing All participant information and biospecimens were logged and tracked using a purpose-built data and biospecimen information management method and the difference was tested the rank test. P values of less than 'significant. Statistical analysis was performed vival was used as the primary endpoint. patients histology log using using -specific

Patient material . One hundred matched normal and tumour derived samples were obtained patients with PDAC. DNA was extracted from the samples mined from SNP array data in (Supplementary Table 2) Patients were recruited and consent obtained for geno mic sequencing through the Australian Pancreatic Cancer Genome Initiative (APGI) from using

'profiled by short tandem repeat (STR) DNA profiling as

in immunocompromised mice were mechanically and enzymatically dissociated collagenase (Stem Cell Technologies; USA) and plated onto flasks coated with 0.2mg ml rat tail Icollagen (BD Biosciences; USA) Subsequently, epithelial cultures wcre cnriched and purificd FACS Aria III Cell sorter (BD Biosciences, USA), coupled with Streptavidin AlexaFluor 647 secondary step (1:1,000; Invitrogen; USA) stroma. Dead cells were removed using propidium iodide Following establishment; all patient-derived (TKCC) cell lines were profiled by short water before fragmentation to approximately 300 bp using the Covaris S2 sonicator with the following settings Duty Cycle 10%, intensity 5, perburst 200, time 50sor 45s for PCR-Free libraries. Following fragmentation libraries for sequencing were prepared the standard Illumina preparation techfinally PCR enrichment for adaptor ligated molecules following the man libraries was generated omitting the final PCR enrichment step to generate PCR A Jan 2013). For standard libraries commercially available TruSeq DNA LT Sample Kit v2 (Catalogue no. FC-121-2001) were used for all steps with the following exceptions. Size selections of the Adaptor Ligated fragments were completed two rounds of SPRI bead purifications (AxyPrepMag PCR Clean-upCatalog no. MAG-PCR-CL-250) final bcad to DNA volumc ratio of 0.60:1 followed by 0.70:1, selecting for molecules with an average size of 500 bp. Size-selected libraries were then amplified for a total of 8 ofPCR to enrich for DNA fragments both compatible with sequencing and containing the ligated indexed adaptor. For PCR tion Kit LT protocol for all steps with no modifications. The final whole-genome libraries were qualified (amplified and PCR-Freelibraries) and quantified (amplified libraries only) via the Agilent BioAnalsyser 2100 (Catalog IDG294OCA) instrument Free libraries was performed using the KAPA Quantification Kits For Illumina sequencing platforms (Kit code KK4824) in combination with Life Tech using using (Sigmabiology grade cycles using library library Prep using using cycles using Library

Whole genome libraries were prepared for cluster generation by cBot (catalogue guidelines. Individual trol PhiX (10pM) was spiked into each lane at a concentration of 0.3% to provide real timeanalysis metrics. Final library concentrations of8 pM (amplified) scquenced on the Illumina HiScq 2000 instrument (HiScq control software vl.SI 401-3001). Paired reads each of 101 bp were generated for all libraries and in total approximately 220-million paired reads were generated per lane; in with the manufacturer' s specification. Real time analysis ofthe control library PhiX showed also in line with published specifications. library Jine

govlprojectslgenomelassemblylgrclhuman/) GRCh37 assembly tiple BAM files from the same sequence library were merged and within duplicates were marked. Resulting final BAMs were used as input into variant call All BAM files have bcen dcposited in the EGA (Accession number: EGAS 00001000154). using library ing

number analysis. Matched tumour and normal patient DNA was assayed using Illumina SNP BcadChips as per manufacturer's instructions (Illumina, San Diego CA) (HumanOmnil-Quad or HumanOmni2.5-8 BeadChips) SNP arrays were scanned and data was processed the Genotyping module (v1.8.4) in Genomestudio v2010.3 (Illumina, San CA) to calculate B-allele frequencies copy number loss or copy neutral LOH. Recurrent regions number change were determined and genes within these regions were extracted using ENSEMBL v70 annotations. Copy using Diego change of copy gain;

Identification of structural variations. Somatic structural variants werc identified usingtheqSV tool (manuscript in preparation). qSV uses independent lines of dence to call structural variants including discordant reads, soft clipping and split read. Breakpoints are also identified both de novo assembly of abnormally mapping reads and split contig alignment to enhance break using

considered high confidence if: (i) they were category and therefore contain mul tiple lines of evidence (discordant soft clipping on both sides and split reads); (ii) of evidence: discordant (both breakpoints) and soft clipping; or discordant (both breakpoints) and split read;or soft clipping (double sided) and split read; (iii) category 3 with 10 or more supporting events (discordant read pairs or soft clipping at both ends) Only high confidence calls were used in further downstream analysis. Copy number variation was estimatcd SNP arrays and the GAP tool' 7. Depending on the read types supporting an aberration or the associated of copy number events each structural variant was classified as: deletion; duplication; tandem duplication; foldback inversion, inversion; inversion, intrachromosomal or translo information of discordant read pairs; soft clipping clusters and assembled contigs which span the breakpoints. This allows identification of 4 groups of events: duplica tionslintra-chromosomal rcarrangements; deletionslintra-chromosomal rearrange ments, inversions and inter-chromosomal translocations. Boundaries of segments ofcopy number that occur in close proximity to each breakpoint were then used to aid further classification of the events. Structural variants with breakpoints that flanked a copy number segment ofloss were annotated as deletions  Duplications and inversions associated with increases in copy number enabled the character ization oftandem duplications and lamplified or foldback inversions. Events within the same chromosomc which linked the ends of copy number segments of simi rearrangements they pairs they using pair amplified

The landscape of structural rearrangements in pancreatic ductal adenocarci with an average of 119 events per patient (range 15-558). Each event was classified sion, the cohort there was inter patient heterogeneity in terms of total number of events 1) Fig

Evcnts were then annotated if mere and genes which were affected by breakpoints were annotated ENSEMBL v70. Structural variants and copy number data were visualized they using using

Classification of subtypes based on the pattern or structural rearrangements. Each tumour was classified into one of four subtypes basedon the volume ofevents; tribution ofevents across the genome in cach patient. In addition to counting strucNon-random chromosomal Iclustering ofstructural variants was detected an approach originally described by Korbel and Campbell?5 . Significant clustering of structural variation events was determined by a goodness-of-fit test the Highly focal events were detected an adaptation of a method" where chromosomcs witha high structural variant mutation rate per Mb exceeded 5 times the length ofthe interquartile range the 75th percentile ofthe chromosome counts for each patient. The rules used to determine these subtypes are as follows: using against using from

Stable These tumours contain few structural rearrangements ( <50) which are located randomly through the genome.

Locally rearranged The intra-chromosomal rearrangements in these tumours are not randomly positioned through the genomc, instcad arcclustcred on onc were considered locally rearranged if harboured at least 50 somatic events were considered locally rearranged if the number of intrachromosomal events exceeded 5 times the length of the interquartile range from the 75th percentile of thechromosome counts per Mb for that patient. Theevents in thelocally rearranged tumours arebroadly comprised ofeither: (1) focal amplifications the majority of events are (tandem duplication, duplication; foldback inversion or inversion) or (2) complex rearrangements the events are part ofa complex event such as chromothripsis or breakage-fusion-bridge. they they and amplified gain

Unstable Thesc tumours are massively rearranged as contain > 200 struc thcy

Scattered These tumours contain 50-200 structural rearrangements which are scattered throughout the genome.

Classification of complex localized events. Evidence of clustering ofbreakpoints was cstimated as ofstructural variants were reviewed for evidence ofchromothripsis (oscillation bridge (BFB for loss oftelomeric region with neighbouring highly region with inversions). ing ofcopy amplified

Verification of structural variations. We used two methods of verification for structural variants: (1) an in silico approach; which considers events with multiple ofevidence (qSV category I: discordant pairs; soft clippingon both sides and number change (gain or loss) and (2) orthogonal sequencing methods including SOLiD mate pair and capillary sequencing: lines long

mate 'sequencing and verification ofstructural rearrangements. mate-paired libraries were made according to Applied Biosystems Mate-Paired Library Preparation 5500 Series SOLiD systems protocol was sheared libraries were sequenced the SOliD v4 (Applied Biosystems). Sequence data was mappedtoa genome bioscope vl.2.1 (Applied Biosystems) . Each sample was sequencedto an average non-redundant physicalcovcrage of 18OX (64-333) in the tumour and 187X (52-503) in the control sample. pairs using the qSV tool: Fvents identified by sequencing were considered verified if the right and left breakpoint of these events were within 500 bases of the right and left breakpoint of an event identified by SOLiD scquencing: Long pair Long using using pair using using Hiseq

PCR and capillary sequencing for verification of structural rearrangements. For PCR andcapillary sequencing PCR primers were designed with primer BLAST 'predicted breakpoint, primers were designed with primer BLAST (NCBI). PCR was carried out in the tumour and matched normal genomic DNA inum DNA polymerase (Invitrogen; Carlsbad, Ca), 2 or 4 ulof 10 uM primer C for 2 min, followed by 35 for 30s and extension at 68  C 15 min PCR products were visualized by gelelectrophoresis and classified into one offour categories: (1) validated ~strongandspecific PCR bandofthe expected size was observed only in the tumour and not in the normal somatic rearrangement; (2) germline clear PCR band ofthe expected size both in the tumour and normal; (3) not validated PCR yields smears or multiple bands, this potentially indicates non-spccific primer pair; (4) not tested no PCR band was observed in tumour and normal. Taq cycles for

Verification of structural variations results. In total 7,105 events were verified 2,904 events were associated with a copy number 'change (events classified as deletion; duplication; tandem duplication; amplified inversion and foldback inversion) number change

We also verified structural variant events using mate resequencing (SOLiD paired 50 bp) or sequencing ofa different sample from the same patient of 33 tumours. this approach 1,924 events were confirmed and the verification status of structural variant cvents was recorded in Supplementary Table 5 in the ~validation\_status\_id" column where0 = untested and ! verified. In total 7,228 of the 11,868 events identified (619) were verified (Supplementary Table 5 and Extended Data Fig. 1) the remaining events remain untested. long pair Using

called usc very different calling strategies and while cach maybe subjcct to artefacts (asareall variant callers) , be subject to different artefacts. Each compared variant falls into one of three categories: seen only by qSNP , seen only by GATK, and seen by both qSNP and GATK Mutations identified by both callers or those considered high confidence and used in all subsequent analyses (Supplementary Table 3) Small indels <200 bp) were identified Pindel" ; each indel was visu using will using

Verification of substitutions and small insertion/deletions. In total 3,304 of the ing events remain untested. Substitutions and indels were verified using orthogonal sequence data which included data produced on different sequencing platforms (Hiseq or SOLiD exomeor mate SOLiD sequencing) or data from related nucleotide samples (RNA-seq) For example, if orthogonal tumour sequence data wasavailable (DNA variant was also observed in the second tumour sample then that would add support for the variant. It shouldbe noted that tumour samples can only be used to support an somatic variant and the absence of a called variant in a second tumour sample docs not discredit the original call. Conversely; a second normalsample will long Pair from existing

<!-- image -->

only discredit somatic variants and the absence of the called variant in the second minimum of 10 reads at the variant position; and at least two reads must show the variant. If multiple additional BAMs are available, each BAM votes independently Each variant examined by qVerify is assigned to one of four categories:

(1) Verified one or more additional tumour BAMs showed evidence of the variant and no additional normal BAMs showed the variant.

the variant indication that it is likely to be a germline variant:.

(3) Mixed across multiple additional BAMs, there was conflicting evidence tional normal BAMs. This could also be evidence of a germline variant incorrectly called somatic.

(4) Untested there were no additional BAMs or there were additional BAMs it against

matching normal.

but none passed the minimum coverage threshold or there were additional BAMs that did not show the variant and so did not provide evidence for or Telomere length analysis. Reads containing the telomeric repeat (TTAGGG) X3 (the average base coverage of each genome). The normalized telomere count was

Determination ofthe BRCA signature. High confidence somatic mutations that were called by both qSNP and GATK across the genome were used to determine the proportion ofthe BRCA signature in each sample 'published computa by substitution class and sequence context) was determined for each sample and compared to the validated BRCA signaturez and the proportion of the BRCA signature in a given sample was ascertained. using

week-old NODISCID/interleukin 2 receptor [IL2R] gamma (null) (NOG) mice and under research protocols approved by the Garvan Animal Ethics Committee (09/ 19, 11/23, 11/09)

In vivotherapeutic Tumour mice with a 'palpable tumour (volume V = 0.5 X length X width?) were treated with various agents at peritoneally on land 14. Theinvestigators were not blinded to thegroupallocation. To testing bearing day day day day

accumulating toxicity of repeated injections; an additional treatment was given after the recovery time of two weeks only when no tumour regression was observed, otherwise treatment was continuedonce thetumour relapsed to its orig inalsize (100%) . Measurement of chemotherapy response was based on published methodology' where primary xenografts were treated with the specified mono therapy and their characteristics mapped nasia. Mice were euthanized and tissues collected for further analyses when tumour size reached 400% (600-7OOmm avoid from growth

and geminin (10802-1-AP, ProteinTech Group; Chicago; IL). Primary culture of PDX from patient ICGC\_0o16was established by plating and growing cells an enzymatically digested xenograft on a matrix for approximately week before irradiation and immunofluorescence staining For this experiment; xenograft visualize eGFP positive mouse stromal cells and eGFP negative tumour cells under laboratory by crossing previously  established  heterozygous  eGFPNODCBI7 Prkdcscid 2 rcceptor (IL2R) gamma (null) (NOG) strain in our laboratory. eGFP expressing offspring was backcrossed five times onto the parental line to ensure homozygosity for IL2Rgamma deletion and confirmed by genotyping (Transnetyx) from collagen mices?

paraformaldehyde (in PBS) 6h post-irradiation and stained with RAD5I, YHZAX and geminin with

- 42 transform. Bioinformatics 25,1754-1760 (2009).
- 43. Sun, W. etal Integrated study of copy number states and genotype calls using high-density SNP arrays. Nucleic Acids Res. 37,5365-5377 (2009)
- 45. Nik-Zainal, S. et al. Association of a germline copy number polymorphism of APOBEC3A and APOBEC3B with burden of putative APOBEC-dependent
- Krzywinski; M. et al Circos: an information aesthetic for comparative genomics Genome Res 19, 1639-1645 (2009)
- 46. McKenna, A et al. The Genome Analysis Toolkit: a MapReduce framework for analyzing next-generation DNA sequencing data. Genome Res. 20, 1297-1303 (2010)
- Z Pindel: a pattern growth approach to detect break points of large deletions and medium sized insertions Ning
- (IGV): high-performance genomics data visualization and exploration. Brief.
- 49. Nik-Zainal; S. etal: Mutational processes molding the genomes of 21 breast cancers. Cell 149,979-993 (2012)
- 50. pancreatic cancer. Clin. Cancer 12,4652-4661 (2006) Res.
- 51 Rottenberg S.et al Selective induction of chemotherapy resistance of mammary tumors inaconditional mouse model for Sci. USA 104, 12117-12122 (2007)
- 52 Niclou; S. P.et al A novel eGFP-expressing immunodeficient mouse model to study tumor-host interactions. FASEB J 22,3120-3128 (2008).
- 53. complete response to neoadjuvant chemotherapy in primary breast cancer. Clin. Cancer Res. 16,6159-6168 (2010)

The PDXs were generated according to methodology published elsewhere with modificationss" . Bricfly, surgical non-diagnostic specimens of patients operated at APGI clinical sites were implanted subcutaneously (s.c.) into three NOG and right flank; engraftment stage). Once established, tumours were grown to a size of 1,500 mm at which werc harvested, divided, and rc-transplanted into further mice to bank sufficient tissues for experimentation (first passage and second passage) After expansion; passaged tumours were excised and propagated tocohorts stituted the treatment cohort (third passage). Utilization ofthe NOG mouse model, which is characterized by high immune deficiency in this study has enabled estab significant cohort of PDXs (80) xenografts; with a high rate of successful engraftment and propagation (76%, data not shown) point they

Patients

ARTICLE

RESEARCH

<!-- image -->

## Extended Data Figure 1 | Summary of structural rearrangements.

number change (qSV category 2 and 3, Methods) . b, Histogram showing the number of structural rearrangements in each pancreatic cancer. 100 PDACs were sequenced HiSeq paired-end whole-genome sequencing: Structural rearrangements were identified and classified into 8 categories (deletions, duplications; tandem duplications, foldback inversions; amplified inversions; inversions, intra-chromosomal and inter-chromosomal translocations; Methods) . The number and type of event for each is shown. PDAC shows ahigh degree ofheterogeneity in both the number and types ofevents per patient. The structural rearrangements were used to classify the tumours into using

Histogram showing the number of events verified in silico or by orthogonal sequencing methods (Methods). In total 7,228 of the 11,868 events identified (619) were verified, the others remain untested. These included 5,666 events which contained multiple lines of evidence (qSV category I: discordant soft clipping on both sides and split read evidence, Methods) thus were considered verified Of these events 2,463 events were also verified by orthogonal sequencing methods (SOLiD mate or PCR amplicon sequencing) or the event was associated with a copy number 'change which was determined using SNP arrays. The remaining 1,562 events were verified orthogonal sequencing methods or the event was associated with a copy Pairs, long using

<!-- image -->

<!-- image -->

Patients

Extended Data Figure 2 Distribution of structural variant breakpoints within each patient. The 100 patients are plotted the x axis. The upper plot shows the number of structural rearrangements (y axis) in each tumour. The lower plot shows which chromosomes (y axis) harbour clusters of chromosome for each sample was evaluated two methods to identify clusters of rearrangements or chromosomes which contain a number of events. Method I: chromosomes with a significant cluster of events were determined by a goodness-of-fit test against the expected exponential distribution (with a significance threshold of <0.0001). Chromosomes which pass these criteria are coloured blue. Method 2: chromosomes were identified along using large

interquartile range from the 75th percentile of the chromosome counts for each patient. Chromosomes which pass these criteria are coloured orange. Chromosomes which pass both tests are coloured red These criteria show significant both clusters of events and a high number of events within that chromosome they they

which contain significantly more events per Mb than other chromosomes for that patient. Chromosomes were deemed to harbour a high number ofevents if

that the unstable tumours which contain many events often have clusters of events. In contrast locally rearranged tumours are associated with when compared to other chromosomes\_

<!-- image -->

Extended Data Figure 3 The stable subtype in pancreatic ductal adenocarcinoma. The 20 stable tumours are shown circos. Thecoloured outer represents the chromosomes; the next depicts copy number (red represents andgreen represents loss) the next is the Ballele frequency . using ring ring gain

<!-- image -->

The inner lines represent chromosome structural rearrangements detected by whole genome sequencing and the legend indicates the type of rearrangement. Stable tumours contained less than 50 structural rearrangements in each tumour. paired

RESEARCH

ARTICLE

Extended Data Figure The locally rearranged subtype in pancreatic ductal adenocarcinoma.   The 30 locally rearranged tumours are shown circos. The coloured outer depicts copy number (red represents and green represents loss) the next is using rings ring gain

<!-- image -->

the B allele frequency. The inner lines represent chromosome structural rearrangements detected by whole-genome paired sequencing and the legend indicates the type ofrearrangement. In the locally rearranged subtype over 25% of the structural rearrangements are clustered on one of few chromosomes.

<!-- image -->

## ICGC\_0326 Chromthripsis

Extended Data Figure 5 Example of evidence for chromothripsis in a pancreatic ductal adenocarcinoma (ICGC\_0109). Upper plot is a density plot showing concentration of break-points on chromosome 5. Next panel shows The lower panels show copy number, logR ratio and Ballele frequency derived

<!-- image -->

from SNP arrays. This chromosome showed a complex localization of events similar to chromothripsis. number and structural rearrangements suggest a shattering of chromosome 5 with a high concentration ofstructural rearrangements; switches in copy number state and retention ofheterozygosity, which are characteristics ofa chromothriptic event. Copy profile

<!-- image -->

## ICGC\_0115 Breakage-fusion-bridge chromosome 16

Extended Data Figure 6 | Example of evidence for breakage-fusion-bridge (BFB) in a pancreatic ductal adenocarcinoma (ICGC\_0042). Upper plot is a density plot showing a concentration of break-points on chromosome 5. Next shows the structural rearrangements which are coloured as presented in the legend. The lower panels show copy number, logR ratio and B Panel

<!-- image -->

allele uency derived from SNP arrays. This chromosome showed a complex localization of events similar to BFB number profile suggests loss of telomeric q arm and a high concentration of structural rearrangements suggesting a series of BFB cycles, with multiple inversions mapped to the amplified regions frequ Copy

ARTICLE

Extended Data Figure 7 The scattered subtype in pancreatic ductal adenocarcinoma. The 36 tumours classified as scattered are shown circos. The coloured outer represent the chromosomes; the next depicts copy number (red represents and green represents loss), the next using rings ring gain

<!-- image -->

rearrangements detected by whole genome legend indicates the type of rearrangement. The scattered tumours contained 50-200 structural rearrangements in each tumour. paired

<!-- image -->

Extended Data Figure 8 The unstable subtype in pancreatic ductal adenocarcinoma. The 14 unstable tumours are shown circos. The coloured outer rings are chromosomes; the next ring depicts copy number (red represents and represents loss), the next is the Ballele frequency. The inner lines represent chromosome structural rearrangements detected by using gain green

<!-- image -->

whole genome paired sequencing and the legend indicates the type of rearrangement. The unstable tumours contained a degree of genomic instability and harboured over 200 structural rearrangements in each tumour which were predominanty intra-chromosomal rearrangements evenly distributed through the genome. large

CONTROL

<!-- image -->

TKCC 07

ICGC 0016

Capan-1

Extended Data Figure 9 RAD5I foci formation in a primary culture of genomically unstable PDAC. a, RAD5I and geminin fluorescence in untreated cells derived from an unstable pancreatic tumour with a somatic mutation in the RPAI gene (ICGC\_0016). Primary culture of ICGC\_0016 consists of eGFP mouse stromal and eGFP tumour cells. b, Upper panel: irradiated unstable pancreatic cancer cells (ICGC\_0016) middle panel: HR competent (TKCC-07) and lower panel: HR-deficient (Capan-1) pancreatic tumour cells. Cells were irradiated in vitro with 1OGy, and 6h post-irradiation

examined by immunofluorescence microscopy: eGFP negative tumour cells following induction of DNA damage. TKCC-07 is a pancreas cancer cell line generated from a homologous recombination (HR) pathway competent patient-derived xenograft and positive control for staining and RAD5I foci formation after DNA damage. Capan-1 cells which are HR-deficient do not form RAD5I foci. examined pancreatic tumour cells.

<!-- image -->

## METHODS

sacCer3 (V64) S. cerevisiae rcference genomc assembly . Data sets originally obtained with coordinates on other assemblies were projected into the sacCer3 assem WWw.yeastgenome.org All regions ofthe sacCer3 genome were used for readalign ment but analyses including strand ratios and all rate estimates excluded the fol~461153 and any 100-nucleotide segment with mappability score of <0.9 (gem mappabilitys? with k-mer 100). In total, this masked 951,532 nucleotides (7.89) nome Database (SGD) consensus annotations extracted the University ofCal ifornia, Santa Cruz (UCSC) genome browser in November 2013.Annotatedorigins prints were obtained from ref. 54, and nucleosome position; occupancy and tional fuzziness (positional heterogeneity) measures were from ref 55. Yeast replication data was obtained from ref. 36, where we have plotted the percentage of data sct). Higher percentage indi cates earlier average replication time: from posi timing samples

Defining TF binding sites. Rebl and Rapl ChIP-exodata was obtained ref. 58 (Sequence Read Archive accession SRA044886). Sequence bar codes were clipped and sequences sorted using Perl (version 5.18.2). Reads were aligned using bowtiez (version 2.0.0). Following the previously published protocol * up to three mismatches across the length of cach tag sequence were allowed, and the 3' most 6 base were present  within with the highest occupancy waslabelled as the primary using annotations within the sacCer3 sgdOther UCSC table (http:l/wwwyeast genome org). The presence or absence of a motif was determined using the Motif net/). The matching motif significance threshold was set at 0.005. Multiple were aligned (x from pairs peaks peak peaks using

Yeast between-species substitution rates were calculated from MultiZ stacked pairwise alignments obtained from the UCSC genome browser (Supplementary S. mikatae; S. kudriavzevii and S. bayanus) were extracted from the original seven tution rates were calculatedover whole chromosomes using baseml the package (version 4.6) under the HKY8S substitution model with ncatG 5 catwere obtained over the sacCer3 genome specics from egorical

Yeast polymorphisms and between species substitution rates. Yeast polymor polymorphic site. Only nucleotide substitutions were considered, insertions polymorphic sites divided by the number of sacCer3 sites with sequence coverage in at least two additionally sequenced strains. point

Computational and statistical analyses. Analysis and all statistical calculations were of freedom (strand ratio calculated in 2,001-nucleotide consccutive winwith centre alignment and null padding: Pearson's correlation was performed with the cortest function in R, paired Student's t-test with the t.test function; Mann Whitney tests with the wilcoxtest function andlowess (locally weighted scatterplot smoothing) with the lowess function and default parameters. degrees

Human conservation measures. GERP scores" were used as a measure of between species nucleotide diversity across 46 vertebrate species. Single-nucleotide rcsolution consistency of presentation with plots of polymorphism rate and yeast between nucleotide substitution rate; the yaxes in plots showing GERP scores have species

cession GSM835651) Analysis primarily focused on the larger 'replicate' library but results were confirmed in the 'sample' library (GEO accession GSM835650). ratios were calculated in windows of 2,001 nucleotides. pseudo count of 1 read covered nucleotide was added toboth strands in each window to avoid divisions by de-duplicated read data (identical start and end coor dinates were considered duplicates) . De-duplication minimises potential biases in PCR amplification; qualitatively similar results were obtained with non-de-duplicated data and support identical conclusions.

Rather than separate Okazaki 5' and 3' end counts that did not always correlate well; probably due to amplification biases; sequencing and size selection biases; we produced end at a focal nuclcotidc; and (2) the fraction of downstream OFs whose 5' end is at the focal nucleotide. The resolution over both strands of the sacCer3 genome. using

nome with bowtie2 (version 2.0.0). Subsequent filtering and format conversion were performed Only reads with a mapping quality score >30 were for analysis. As there had bcen no pre-scquencing amplification; de-duplication was not performed. Read 5'-end counts were summed per strand at single nucleotide resolution over the yeast reference genome. Note that under the emRiboSeq protocol; the ribonucleotide incorporation site would be one nucleotide upstream and on the opposite using

<!-- image -->

differing read depth, read counts were normalized to sequence tags per million mapped into the non-masked portion of the genome.

No statistical methods were uscd to predetermine sample size:

Rate estimates with compositional correction: Polymorphism and OJ rates were calculated separately for each nucleotide (A, T,Cor G)and the average ofthese for ratcs used as thc rcported or plotted mcasure for a nucleotide site or group of sites. This corrects for mononucleotide compositional biases that are abundant when sampling specific features of a genome. The between-species relative substitution rate calculation incorporates a compositionalcorrection. The rate estimates shown non-missing data.

Trinucleotide preserving shuffles. nucleotide of the sacCer3 genome was assigned to one of 64 categories based on the identity of that nuclcotide and its flanking nucleotides. A vector of transformations was produced by swapping the genomic coordinate of a nucleotide for one with an identical category chosen at random. Swaps between masked and unmasked sites (see above) were prevented. every sequence was substituted through the transformation vector; for a randomly rate or annotation used. This provides a compositionally well-matched null derived 95% confidence bounds and standard deviations on those null expecta tions. For human sites, shuffles were confined to sequences flanking the region of coordinates in the ENCODE 'Duke Excluded Regions andthose positions with a uniqueness score of <0.9 (gem-mappability ? with k-mer 100) were excluded from shuffles Every ing

Sites selected for analysis. Thresholds were to define specific subsets of sites to be evaluated . For the presented data la) nucleosomes with an occu pancy of >809, positional fuzziness Other combinations (Extended Data Fig- 1) of these parameters gave qualitatively asthe primary ChIP-exo the highest scoring ReblRapl position weight matrix match within 50 nucleotides of the ChIP-exo footprints from 41 human cell types were the combined footprints with those found in each cell type using BEDtools (version 2.17.0) to identify the subset (n = 33,530) that were detected in all 41 cell types. The left-edge coordinate as defined in the combined footprint file was used as the focal applied (Fig peak

Comparison of polymorphism rates. The five nucleotide positions downstream scored for their polymorphism rate (Fig. 2b). Rate deltas were calculated as up-

<!-- image -->

performed against the same calculation performed on 10O trinucleotide preserving upstream and downstream positions is greater in the observed data than the shuffled data.

with biotinylated A adaptor were captured on streptavidin-coupled M-280 Dynabeads (Life Technologies) following the manufacturer' s guidelines, and non-biotinylated strands were released in 0.15 M NaOH. Single-stranded fragments were concen trated by ethanol precipitation.

DNA purification. Yeast strains were at 30 Cin YPDA to mid-log phase (see Supplementary Table 3 for a list of strains) or to saturation for stationary Per 5 nn mM EDTA). An Sartorius) were added, and cells lysed by vortexing for 2 min; 200pl TE buffer was then added, followed by an additional min of 'vortexing. After centrifugation; the aqueous phase was further extracted with equal volumes of phenol:chloroform: with 1 ml of 100% ethanol, and dissolved in 0.5 M NaCL RNA was degraded by treatment with 10ug RNase A (Roche) for 1h at room temperature. DNA was finally purified with an volume of Ampure XP beads (Beckman Coulter) and eluted in nuclease-free water. For preparations DNA was isolated from up grown phase. equal library

Alkaline electrophoresis. Isolated genomic DNA (0.5 pg) was treated with DNA pellets were dissolved in alkaline dye and separated on 0.7% agarose (50 mM NaOH, SYBR Gold (Life Technologies) . Densitometry measurements and derivation of ribonucleotide incorporation rates as previously described?s . Percentage genomc contribution for each replicative polymerase (x) was calculated using the follow formula: the number of ribonucleotides incorporated in one yeast genome for the mutant poly alkaline and Fpdx the frequency ofincorporationby that polymerase (see Fig 3a) EmRiboSeq preparation and sequencing: DNA was sonicated Bioruptor Plus (Diagenode) to achieve an average fragment length of approxi mately 400 bp. Fragmented DNA was concentrated by ethanol precipitation and size selected 1.2 volumes of Ampure XP. DNA was quantified by nanodrop end-repair reaction; DNA was purified respectively. The trPI adaptor (see below) was attached using NEBNext Quick Ligation with 120 gel loading gels ing Nspolx gel, library using using using pmol

rification; beads were removed and DNA nicked using recombinant RNase H2 (10pmolpg of Ampure XP .Shrimp alkaline phosphatase (Affymetrix; 5 U) was then usedto reat65 Cand Ampure XP purification; DNA was denatured by heating at 95 Cfor 5 min and snap Subsequently, A adaptor (see below; 120 pmolug oflibrary) was attached using NEBNext Quick Ligation for 14-18hat 16  C. Fragments

- 58.
- 59. for position weight matrix matches in DNA sequences. Bioinformatics 25, 3181-3182 (2009)
- access database of transcription factor binding profiles. Nucleic Acids Res 42,
- 61. The ENCODE Project Consortium. An integrated encyclopedia of DNA elements in the human genome Nature 489,57-74 (2012)
- 63. Reijns, M. A. et al The structure of the human RNase H2 complex defines key
- 62. Nature 489, 75-82 (2012)

Oligonucleotides and adaptor design. Custom oligonucleotides were synthesized by Eurogentec.  Adaptor primer werc anncaled by phosphorothioate-T-3' ; trPl-bottom; 5'-phosphate-ATCACCGACTGCCCAT GACACGCAGGGATGAGATGG-dideoxy-3' ; A-bottom; 5'-biotin-CCATCTC ATCCCTGCGTGTCTCCGACTCAGNNNNNN-C3 phosphoramidite-3' The sequence for primer A used in second strand synthesis was 5'-CCATCTCATC CCTGCGTGTCTCCGAC-3' pairs hcating

Phusion Flash High-Fidelity PCR Master Mix (Thermo Scientific) wasthen used for second strand synthesis with produce a double stranded 29 tified using a 2100 Bioanalyzer ( Agilent Technologies) before emulsion PCR, using the Ion Torrent One Touch; and next generation sequencing on the Ion Torrent PGM or Proton platform (Life Technologies) . primer using

plementary Tables 1-3 Sup-

- 51. tools. Brief.Bioinform 14, 144-161 (2013)
- 52 Derrien; T.etal. Fast computation and applications of genome mappability. PLoS ONE 7,e30377 (2012)
- 53. (2010)
- digital genomic footprinting; Nature Methods 6,283-289 (2009)
- (2009)
- Liti, G. et al Population genomics of domestic and wild yeasts. Nature 458 337-341 (2009)
- 1586-1591 (2007)

<!-- image -->

<!-- image -->

## Extended Data Figure 1 Increased OJand polymorphism rates correlate at

around its binding site; with a dip corresponding to its central recognition sequence. h-j, Increased polymorphism and 0J rates at Rapl (h), nucleosome Distributions calculated as for g, Fig. Ia and b, respectively, trinuceotide preserving genome shuffle. Pink shaded areas denote 95% confidence intervals for nucleotide substitution rates (100 shuffles) k,1, Polymorphism (red) and between-species (black) substitution rates are binding sites. Best fit splines shown only- y axes scaled to demonstrate similar distribution. Values plotted as percentage relative to the mean rate for all data (central 11 nucleotides excluded for calculation of mean in g 1). using shape points

binding sites of different nucleosome classes and at Rapl binding sites. a-f, OJ and polymorphism rates are strongly correlated for different classes of S. cerevisiae nucleosomes; demonstrating that OJ and polymorphism rates cosubject to strong and asymmetrically distributed selective constraints; which is likely to explain the modestly reduced correlation for this subset. Such transcription start site proximal nucleosomes were excluded from analyses of presented, as for Rebl in Fig Ib, show increased OJ and polymorphism rates

<!-- image -->

Extended Data Figure 2 EmRiboSeq methodology and validation.

<!-- image -->

(TPM). Bona fide Nb BtsI sites were equally represented, at maximal frequency, uencies represented sites in close proximity to other Nb BtsI sites, causing their partial loss Additionally, Nb BtsI-like sites were detected as the result of star activity. Libraries were also prepared not show such star activity (data not shown), allowing calculation of the site specificity for the method >99.9% strand specificity (blue; correct strand; grey, opposite strand) and >99% single nucleotide resolution (d). freq during using

Schematic of emRiboSeq library preparation: rN, ribonucleotide. b d, Validation of strand-specific detection of enzymatically generated nicks endonuclease cleaves the bottom strand of its recognition site releasing a 5' fragment (cyan) group after denaturation; to which the sequencing adaptor (pink) is ligated, allowing sequencing and mapping of this site to the genome (b). Nb.BtsI (poll-L868M) strains after normalizing read counts to sequence tags per million nicking with

Extended Data Figure 3 emRiboSeq: a, Point mutations in replicative polymerases elevate ribonucleotide incorporation rates, permitting their contribution to genome synthesis to be tracked. Schematic of replication fork with polymerases and R. Clausen & T.A. Kunkel, personal communication) as indicated (POL denotes wild type polymerases; asterisk denotes point mutants). Embedded ribonucleotides indicated by 'R;additional incorporation events due to polymerase mutations highlighted by shaded circles. b, c, Mapping ofleading/ using

<!-- image -->

in 3) highlights both experimentally validated (pink dotted lines) and putative (grey dotted lines) replication origins. These often correspond to by emRiboSeq as a component of the lagging strand in stationary phase yeast;, as shown by the opposite pattern for a polymerase wild-type strain. Strand ratios are shown as best-fit splines with 80 degrees of freedom; y axes show of the strand ratio calculated in 2,001-nucleotide windows (bd). Fig logz

<!-- image -->

<!-- image -->

## Extended Data Figure Quantification of in vivo ribonucleotide

incorporation by replicative polymerases. b, Representative alkaline gel electrophoresis of genomic DNA from yeast strains with mutant replicative ribonucleotides are detected by increased fragmentation of genomic DNA following alkaline treatment in an RNase H2-deficient Increased rates are seen with all three mutant polymerases (indicated by asterisk, as defined in Extended Data 3a), and are reduced in Pol-c' which mutation Met644Leu; a mutation that increases selectivity c, Quantification of average ribonucleotide DNA isolated ribonucleotide content is the product of incorporation frequency and the total contribution of each polymerase, resulting in the total ribonucleotide content detected to be highest for Pol-c* (14,200 per genome), followed by Pol-6* asymmetry in replication (median 4:1 strand ratio). Count of genomic Fig point from

genome based on reanalysis of OF sequencing data'7 denoted as 'Okazaki-seq' The strand asymmetry ratio was calculated after re orienting all regions such that the predominant lagging strand was the forward strand e-g Genome wide quantification of strand-specific incorporation of wild-type and mutant replicative DNA polymerases determined by emRiboSeq reflects their roles in leading - and lagging-strand replication: A close to linear correlation with strand ribonucleotide incorporation for independent libraries (including stationary phase libraries for POL and Pol-a* marked by diamonds) was plotted against the lagging-leading-strand ratio determined Okazaki-seq data (only ratios = 1:1 for the latter are shown for clarity). There was high reproducibility between experiments in strand ratio preferences. Lines are lowess smoothed (see Methods) representations of the full data sets (representative examples given in fand g) f, g Scatter plots illustrating the individual strand ratio data for 2,001-nucleotide windows; for stationary phase POL (f) and Pol-a* (g) yeast. Pearson's correlation 0.49, 16 16 for Pol-a* (g) using points

<!-- image -->

<!-- image -->

Extended Data Figure 5 Pol-a-synthesized DNA retention is independent of RNase H2 processing of RNA primers. a, b, The ribonucleotide content of genomic DNA is unchanged between Arnh2ol strains transformed with empty vector ( =) or vector that retains the ability to cleave RNA:DNA hybrids, including RNA primers; vector expressing wild-type Rnh20l (wt) fully rescues alkaline sensitivity of the

<!-- image -->

DNA. As complementation with the separation-of-function mutant had no independent of a putative role for RNase H2 in RNA primer removal. Representative result shown for n = 3 independent experiments. c Wild-type and mutant Rnh2ol are expressed at levels, as shown by immunodetection of the C-terminal FLAG tag: Loading control; actin. equal

Distance from binding motif mid-point (nt)

<!-- image -->

Extended Data Figure 6 Elevated substitution rates are observed adjacent to many human TF as GERP scores) are elevated immediately adjacent to REST (a, b) and CTCF (pink to brown: lower to higher)  reflecting strength of bindingloccupancy. Stronger binding correlates with greater increases of proximal substitution rate consequence of local sequence composition effects (b, d). Strongest binding

quartile of sites (brown) is shown compared to a trinucleotide preserving shuffle (black) based on the flanking sequence (100-300 nucleotides from motif midpoint) of the same genomic locations. Brown dashed line and grey shading denote 95% confidence intervals. Substitution rates plotted as GERP scores for human TF binding sites identified in ChIP-seq data sets (in conjunction with binding site motif). Sites aligned (x = 0) on the midpoint of the TF binding site within the ChIP-seq (colours as for a-d). Dashed black line shows y = 0, the genome wide expectation for neutral evolution. Peak

All edges Non-Reb, Rap1 edges

<!-- image -->

Extended Data Figure 7 | OJ and polymorphism rates are increased at yeast increased OJ rates and locally elevated polymorphism rates in S. cerevisiae (a), a pattern that is maintained when footprints associated with Rebl and Rapl and excluding those within 50nucleotides of a Rebl or Rapl binding site (n = 5,136) were aligned to their midpoint. c,d, Aligning DNase I footprints on their left edge rather than midpoint (to compensate for substantial heterogeneity in footprint size) demonstrates a distinct shoulder of elevated polymorphism rate at the aligned edge (c), with a significant elevation compared to nearby sequence upstream footprints from a were aligned to their left edge (x = 0) with corresponding polymorphism rates shown (c) The increased polymorphism rate cannot be explained by local sequence compositional distortions (d). Nucleotide substitution rates in the 11 nucleotides centred on the DNase footprint edge (pink line), and another 11 nucleotides encompassing positions 35 to 25 relative to the footprint edge (green line) were quantified. Darker pink and green filled circles denote the mean of observed substitution rates and lighter from

shades denote the mean for the same sites after trinucleotide preserving genomic shuffles. Error bars denote s.d; statistics by Mann-Whitney test:. e Model shows that correlation of increased nucleotide substitution and OJ rates are consistent with increased mutation frequency across heterogeneous DNase I footprints. Polymorphism is reduced at sequence-specific binding sites within the footprints; owing to functional constraint. Therefore; the effect the region immediately adjacent to the binding site (left of vertical dashed blue increased nucleotide substitutions represents sites with increased, OJassociated mutation is followed by a region of depressed substitution rates; owing to selectiveeffects ofthe functional binding sites within the footprints (to the right of the dashed blue line). Signals further to the right are not interpretable given the heterogeneity in DNase 1 footprint sizes. Given strong substitutions could represent a measure for the local mutation rate for such regions; analogous to that measured by the fourfold degenerate sites in protein sequence. coding

<!-- image -->

RESEARCH

ARTICLE

Extended Data Figure 8 Model to show Pol-a DNA tract retention downstream of protein binding sites. OF priming occurs stochastically, with the 5' end of each OF initially synthesized by Pol-z and the remainder of previously synthesized OF, Pol-ô continues to synthesize DNA displacing the 5' end of the downstream OF, which is removed by nucleases to result in mature OFs which are then ligated. The OJs of such mature OFs before ligation were detected

<!-- image -->

demonstrated that if a protein barrier is encountered (grey circle) Pol 8 progression is impaired, to reduced removal of the downstream OF (b). Given that ~1.5% ofthe mature genome is synthesized by Pol-a,a proportion oflagging strands will retain Pol--synthesized DNA (red). When Pol-8 progression is impaired by protein binding this will lead to an increased fraction of fragments containing Pol-z-synthesized DNA downstream of such sites They leading (c)

<!-- image -->

## METHODS

Photon Source (APS) at Argonne National Laboratory. Alldata were indexed, inte-

No statistical methods were used to predetermine sample size.

Protein expression and purification. Mouse core RAGI (384-1008amino acids) and RAG2 (1-387 amino acids) were cloned into the pLEXm-based ' mammalian a PreScission N-terminal Met of RAG2 was mutatedto Val (MIV) during cloning Toexpress the of each of the RAGI and RAG2 expression plasmids were mixed with 4mg of polyethylenimine (Polysciences) in 35 mlof Hybridoma medium (Invitrogen) to transfect 1lofHEK293T cells grown in after trans fection; cells were harvested and stored at 80 €. Cell paste ( ~8g from 1 Iculture) ~suspended in 50mloflysis buffer containing 20 mM HEPES (pH7.3),1 M KCI, mM Tris (2-carboxyethyl) phosphine (TCEP) (pH 7.0) mM EDTA and protease inhibitor cocktail (Roche), and lysed by sonication After centrifuging at which was pre-cquilibrated with the lysis buffer and incubated with rotation for and mM TCEP. The cluted protcin, which consisted mainly of RAGI-RAG2 heterotetramer was concentrated and stored at 80  Cafter glycerol to 20% final concentration. In contrast to RAGI and RAG2 core proteins expressed RAGI-RAG2 expressed in human cells is highly active. Human HMGBI (1-163 days adding

mixed at 2.2:1:1 molar ratio in the presence of a 2-fold excess of HMGBI with the mMTCEP and incubated for 1hat 37 removing the MBP tag by addition of PreScission fication was performed usinggel filtration (Superdex 200, GE Healthcare) in 20 mM HMGBI with free DNA, the MBP and PreScission protease. All fication steps wcre performed at 4 and RSS DNA if KCI concentration was reduced to below 10O mM (Extended Data sclcnomcthioninc (ScMct)-labellcd RAGI-RAG2 complex, HEK293T cells wcre transferred after transfection to methionine-free Freestyle 293 medium (Invitro L-SeMet (Acros Organics) and 1% dialysed FBS (Invitrogen). Three later; cells were collected and protein was purified in the labelled RAGI-RAG2 peptides was performed at the Taplin Mass Spectrometry Facility (taplinmed harvard edu). It showed that about 40% of methionines were substituted by ScMet. along puri tag days

Crystallizationanddata collection. Crystals ofthe RAGI-RAGZ-DNA complexes were grown by the hanging vapour diffusion method at 4 C over 3 weeks. Equal volumes of protein (~5 mg ml ')andreservoir solution containing 10O mM MES (pH 7.1), 10-15% PEG 3350,200 mM tribasic ammonium citrate (pH 7.O) and with a single I2RSS or 23RSS, but these crystals were small, and none of them diffracted X-rays as well as the SEC complex. Crystals of SeMet-labelled RAGI RAG2 complex were grown under similar conditions. Native and SeMet-labelled complex both crystallized in the C222, space group with two RAGI andtwo RAG2 for native and SeMet-derivative crystals at beam lines 22ID and 23ID ofthe Advanced

Structure determination and refinement. Phases were determined by the single SAD data wcre collected from six SeMct-substituted crystals with the best resolu 54correspondedto selenium sites, andtwo were Zn ions Phases were improved by density modification using RESOLVE?' and the overall figure-of-merit was 0.79. electron density map contained breaks in the main chains, and side-chain definition was not perfect, the register ofthe polypeptide chains was readily determined and manually improved COOT. Secondary structure restraints and non-crystallographic twofold symmetry averaging restraints were used throughout the refinement. The and 0f20.6%and 25.9%, respectively (Extended Data Table 1) Thequality ofthe structure was validated with MolProbitys4 . 90.7% of residues are in the favoured regions of the Ramachandran plot, 9.3% in additional allowed regions, and no residue in the disallowed region of RAG2, andone Zn? in cach RAGI. The N-terminal residucs (391-404) arc in the final model. Crystal packing of two neighbouring RAGI-RAG2 tetramers prepared with PyMOL (http:l/www pymolorg), and sequence conservation ana using Rwvork ion using

- protein production in mammalian cells. Acta Crystallogr. D62,1243-1250(2006)
- 47. cleavage; and transposition of V(D)J recombination signals. Mol Cell Biol 22, 7790-7801 (2002)
- 49.
- (2007)
- 51 965-972 (2000)
- 53. Adams, P. D.et al. PHENIX: a comprehensive Python-based system for
- crystallography. Acta Crysta D66, 12-21 (2010)
- 55. Chenna, R. et al. Multiple sequence alignment with the Clustal series of programs. Nucleic Acids Res 31,3497-3500 (2003).
- biochemical characterization of the KLHL3-WNK kinase interaction important in blood pressure regulation. Biochem J 460,237-246 (2014)
- gyrase A adopts a DNA 7293-7298 (2004)
- mutations: Why asymptomatic siblings should also be tested. J. Clin Immunol 133,1211-1215 (2014) Allergy
- V(D)J recombinase activity can cause either T-B-severe combined immune deficiency or Omenn syndrome. Blood 97,2772-2776 (2001)
- 60. Stem Cell Ther 7,44 49 (2014)

<!-- image -->

b

Extended Data Figure coefficient (CC) of anomalous signal versus resolution. The red line indicates the cutoff of CC = 0.3. Merging data from the two best crystals produced a better CC than merging data from all six crystals. The data processing procedure is outlined above the plot?o. b, The SAD experimental map contoured at 1.30 showed the content of an asymmetric unit. The Se anomalous map is contoured at 3.00 in red typical crystal of RAGI RAG2. d, The content of crystals was examined by and DNA denaturing protein gels

<!-- image -->

32P-labelled input RSS DNAs and those in SEC complexes before and after crystallization are shown beneath the SYBR stained DNA Transposition assay of the SEC (RAGI-RAG2-12/23RSS DNA complex ) used for crystallization. Supercoiled of open circle, oc) was the target; it was linearized by HindIlI as a control. The SEC (0.25,0.5 and 1.OuM) was active in concerted transposition and thus RAG2 complexes (shown in dark and light colours) occludes one nonamer binding site in each heterotetramer of RAGI-RAG2. gel green purified

<!-- image -->

Extended Data Figure 2 RAG2 core fragment (1-351 amino acids) is Sequence alignment of RAG2 from mouse (320-387 amino acids), human; rat and Xenopus with predicted secondary structures shown above. b, Core RAG2 (1-387) and two further truncated RAG2 variants (1-351 and 1-367) were constructed with a non-cleavable N-terminal MBP tag and expressed with the less core RAGI The Coomassie blue R-250 stained RAG2 complexes with truncated RAG2 variants are equally active in cleaving 32P-labelled I2RSS DNA (in the presence of a 23RSS and Mg as examined tag

<!-- image -->

by TBE-Urea d, Elution profiles of RAGI-RAG2 (both and short forms) complexed with DNA from Superdex-200 (S200) in a low salt buffer (50 mM HEPES pH 7.0, 60 mM KCI, mM maltose and 2 mM DTT). Regardless of the length of RAG2, the major S200 eluant peak came out at and contained RAGI, RAG2 (1-351 or 1-387) and (left insert) . gel). long point

<!-- image -->

Extended Data Figure 3 Comparison of RAG2 with ß-propeller and ß-pinwheel structures. ß-propeller proteins; and the C-terminal domain (CTD) of GyrA (PDB RAG2 (a) KLHL2 (b) and GyrA (c) shown side-by-side individually in two are

<!-- image -->

orthogonal views. Each structure is coloured from N to C terminus in blue to red rainbow colours. The in RAG2 that interact with RAGI are terminus; four ß-strands in each blade are named by Arabic numerals, 1-4. loops

Extended Data Figure The NBD in the RAGI-RAG2 core complex (blue and green) superimposes well with the published structure of the NBD-DNA complex (PDB 3GNA, coloured yellow)?2. b, Thetwelve SCIDIOmenn syndrome mutations in the NBD domain are mapped onto the crystal structure of the NBD-DNA protein

<!-- image -->

complex. Six SCID/Omenn syndrome (R391 to R407) mutations arelocated on positively charged surface that interacts with the nonamer; five DNA in each RSS. Patch

<!-- image -->

Extended Data Figure 5 Transposases that form a hairpin intermediate. RAGI dimers (c) are shown as ribbon diagrams in two orthogonal with the dyad perpendicular to the plane (left) or in the plane (right). Each dimer consists of a cyan anda green subunit. The catalytic RNH domains are highlighted in pink, and the conserved catalytic residues are shown as red ball-and-sticks. Thecatalytic divalent metal ions are shown as green spheres if present. The DNAs; coloured in yellow (cleaved by the cyan subunit) and views, viewing

<!-- image -->

orange (cleaved by the green subunit), have similar orientations in the Hermes and Tn5 complexes (as indicated by the arrows). Arrows with dashed outlines indicate that the DNAs are in the back of the plane. Notably, the of RNH domains is oriented similarly in all three cases. The predicted orientations of DNAs bound to RAGI are indicated by the yellow and orange arrows, and the a-helices connected to the third catalytic carboxylates (shown in light purple) probably bridge two DNAs in RAGI recombinase as in Hermes and Tn5. viewing

<!-- image -->

Extended Data Figure 6 Transposases that do not form a hairpin a-c, Retroviral integrase from Prototype virus (Pfv; PDB 30S0)36 (a), bacterial MuA transposase (PDB code 4FCY) * (b) and eukaryotic Mosl mariner transposase (PDB 3HOT)39 (c) are shown in comparable Data Fig: 5. Each catalytic dimer consists of a cyan and a subunit. Two accessory subunits in Pfv are shown in light blue and green; and two accessory foamy7 green

<!-- image -->

domains are highlighted in pink. The DNAs, coloured in yellow (cleaved by the cyan subunit) and orange (cleaved by the green subunit), have similar orientations (within 30 ) as indicated by the arrowheads, but each differs more than 90 the corresponding DNA in Hermes or Tn5 transposase carboxylate (coloured in light purple) does not cross over to interact with a second DNA from

<!-- image -->

Extended Data Figure 7 Surface potential and conservation of RAGI RAGI b, Orthogonal views of the molecular surface of RAGI-RAG2 with absolutely

<!-- image -->

conserved residues highlighted in The NBD is well conserved The views with dyad in plane here are related to the image shown in Fig 5c by ~509 rotation around the dyad. deep purple

<!-- image -->

## Extended Data Table 1 Statistics of native and SeMet SAD data collection and structure refinement

|                             | Native                | Crystal #1          |               | Crvstal #3    | Crystal #4    |               | Crystal #6           |
|-----------------------------|-----------------------|---------------------|---------------|---------------|---------------|---------------|----------------------|
| Space group                 | C2221                 | C2221               |               | C2221         |               | C2221         | C2221                |
| Cell dimensions             |                       |                     |               |               |               |               |                      |
|                             |                       | 168,7, 179.0, 199.3 |               |               |               |               | 169.1 , 179.6, 200,0 |
|                             | 90,90, 90             |                     | 9090, 90      | 90,90,90      |               |               | 90, 90, 90           |
| Absorption (Se)             |                       | Peak                | Peak          | Peak          | Peak          | Peak          | Peak                 |
| Wavelength (A)              |                       | 0.97918             | 0,97918       | 0.97918       | 0.97918       | 0,97913       | 0,97918              |
| Resolution                  | 50-3.2                | 50.0-3.8            | 50,0-3.7      | 50.0-40       | 50.0-3.9      |               | 50.0-3.9             |
|                             | (3.31 3.2)            | (3.94-3.8)          | (3.83-3,7)    | (4.14-4.0)    |               | (3.94-3.8)    |                      |
|                             |                       | 0.151 (0.778)       | 0.149 (0,831) | 0.199 (0,859) | 0.194 (0 796) | 0.174 (0.873) | 0.200 (0,977)        |
| Ilal                        | 12.75 (2.23)          |                     |               | 14,4 (4.1)    |               |               | 13.1 (3.8)           |
| Completeness (9) Redundancy | 98.82 (99.9) 71 (3.4) | 15.0 (15.3)         |               |               | 14.9 (15.3)   | 15.0 (15.3)   | 15.0 (15.3)          |
| Refinement                  |                       |                     |               |               |               |               |                      |
| Resolution (A)              |                       |                     |               |               |               |               |                      |
|                             | 49907                 |                     |               |               |               |               |                      |
|                             | 0.206 /0.259          |                     |               |               |               |               |                      |
| No. aloms                   |                       |                     |               |               |               |               |                      |
| Prolein                     | 14976                 |                     |               |               |               |               |                      |
| Ligand ion (Zn              |                       |                     |               |               |               |               |                      |
| Water                       |                       |                     |               |               |               |               |                      |
| B-factors                   |                       |                     |               |               |               |               |                      |
| Protein                     | 106,4                 |                     |               |               |               |               |                      |
| Ligand ion                  |                       |                     |               |               |               |               |                      |
| Water                       |                       |                     |               |               |               |               |                      |
|                             | 0.007                 |                     |               |               |               |               |                      |

Asterisk indicates that data in the highest resolution shell is shown in parenthesis.

## Extended Data Table 2

| Human mutation   | Mouse residue   | Predicted Structural Effects                                    |
|------------------|-----------------|-----------------------------------------------------------------|
| RAGI             |                 |                                                                 |
| R394WIQ          | R39IA           | nonamer binding                                                 |
| R396LHC          | R393A           | nonamer binding                                                 |
|                  | 5398            | nonamcr binding                                                 |
| T403P            | T400            | nonamer binding                                                 |
| R4O4WIAQ         | RAOIA           | nonamer binding                                                 |
|                  | R4O7A           | nonamer binding                                                 |
|                  |                 | Structural integrity of NBD                                     |
| D429G            | D426            | Structural integrity of NBD                                     |
| V433M            | V430            | Structural integrity of NBD                                     |
|                  | 1432            | Structural integrity of NBD                                     |
| A444V            | A441            | Structural integrity of NBD                                     |
|                  | R446            | Probably DNA binding (spacer)                                   |
| L454Q            | L451            | Structural integrity of RAGI dimer                              |
| RA74S/HC 58      |                 | Structure & DNA binding in DDBD Structure & DNA binding in DDBD |
| S480G LSO6F      | L503            |                                                                 |
| R737H            | RSO4            | Structural integrity of DDBD                                    |
| RSO7W G516A      | G513            | Solvent exposed, DNA binding?                                   |
| W522C            |                 | Structural integrity of RAGI                                    |
|                  | W519            | Structural integrity of preR                                    |
| D539V            | D536            |                                                                 |
|                  | R556            | At the edge of RAGI/2 interface                                 |
| AS6SD            | A562            | Structural integrity of preR                                    |
| S6OIP            |                 | Structural integrity of active site                             |
| C6o2W            | C599 H6O9L      | Structural integrity of active site                             |
|                  |                 | Disordered, near RAG2 Structural integrity of RNHI              |
| A622P            | R62IA           | Active site, adjacent to D6oo                                   |
| E669G            | E666            | RAGI/2 interface                                                |
| R699Q/W          | R696            | Structural stability of RNH                                     |
| G7O9D            | G706            | Structural integrity, active site                               |
|                  |                 | Structural integrity of RAGI2                                   |
| 59 G720C         | G717            |                                                                 |
| E722K            | E7I9K           |                                                                 |
| C73OEF L732FIP   | C727 L729       | Structural integrity of ZnC2 Structural integrity of ZnC2       |
|                  | R734A           | Possibly DNA binding (coding end)                               |
| H7S3L            | H7SOA           |                                                                 |
| R764P            | R761            |                                                                 |
| E77OK            | E767            | RAGI/2  interface                                               |
| R776Q            | R773A           | RAGI/2  interface                                               |
|                  | R77SA           | Structural integrity of RAGI/2                                  |
|                  | P783            | RAGI/2  interface                                               |
| 1794T 6          | 1791            | Structural integrity of ZnH2                                    |
| R841WIQ          | R838            | DNA binding (near heptamer)                                     |
| NSSSI            |                 | Interacts with 3 end of RSS                                     |
| L8SSR            |                 | Structural integrity of ZnH2                                    |
| W896R            | W893A           | Structural integrity of ZnH2                                    |
| Y9I2C            |                 | Structural integrity of ZnH2                                    |
|                  | 19S3R           | Structural integrity of ZnH2                                    |
| R973HIC          | R97o            | Heptamer binding (intra-subunit)                                |
| F974L            | F971            | Structural integrity of CTD                                     |
| R97SWIQ          | R972            | Structural integrity of CTD                                     |
| Q98IRP           | Q978            | Heptamer binding (inter-subunit)                                |
|                  | K989            | Probable DNA binding                                            |
|                  | MIOO3           | Domain interface of CTD-DDBD                                    |
| RAG2             | RAG2            | RAG2                                                            |
| G3SV             | G35             | RAGI/2 interface (E666 of RAGI)                                 |
| R39G             | R39A            | RAGI/2 interface (E719, R773)                                   |
|                  | C41             | Structure, and RAGI/2 interface                                 |
|                  | G95             | Structure integrity of RAG2                                     |
|                  | R229            | RAGI/2 interface (D546 of RAGI)                                 |
| M2SSR            | M28S            |                                                                 |

<!-- image -->

<!-- image -->

## Extended Data Table 3 Mouse RAG1-RAG2 mutations presented in ref. 4

| Mutations                                              | Location and potential functional roles                                                          |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| RAGI mutations: RAG2 binding +, all other              | RAGI mutations: RAG2 binding +, all other                                                        |
|                                                        | Nonamer binding                                                                                  |
| R4O7A                                                  | R4O7A                                                                                            |
| R773A/R775A                                            | R773 is at RAGI/2 interface between E719 (RAGI) and R39 (RAG2) R775 is exposed to solvent.       |
| H937A/K938A                                            |                                                                                                  |
| H942A                                                  | Zinc coordination                                                                                |
| R969A/R97OA                                            | Next to CTD in the positive groove for DNA binding                                               |
| RAGI mutations: RSS binding +, Nicking and Hairpinning | RAGI mutations: RSS binding +, Nicking and Hairpinning                                           |
| K596A                                                  | H-bond to the carbonyl of A957 and A955. stabilizes the W956 conformation in the apo-structure   |
| R7I3A                                                  |                                                                                                  |
| E7I9K                                                  | RAGI/2 interface                                                                                 |
| R734A                                                  | Solvent exposed. but could bind coding-end DNA                                                   |
| W760A                                                  | RAGI/2 interfacc                                                                                 |
| 11795A                                                 | In the active site; next to D708                                                                 |
| W956A                                                  | W956 is ncar E962 but exterior and separate from the active site by the protein backbone. facing |
| RAGI mutations:                                        | Nicking +, Hairpinning                                                                           |
| K6O8A                                                  | Disordered                                                                                       |
| H6O9L                                                  | Disordered                                                                                       |
|                                                        | K856 is oriented toward the CTDIDDBD. R855 is solvent exposed                                    |
| W893A                                                  | Structural integrity of ZnH2                                                                     |
| K98OA                                                  | On the CTD charged surface; potential for heptamer binding                                       |
| RAGI mutations: Joining negative or defective          | RAGI mutations: Joining negative or defective                                                    |
|                                                        | Probable nonamer binding                                                                         |
| E423Q                                                  | Forming a salt bridge with R4O7 that probably binds nonamer                                      |
| R440A                                                  | Probable nonamer binding                                                                         |
| E547Q                                                  |                                                                                                  |
| S723A/C                                                | Adjacent to E719 (OS) and close to R39 of RAG2                                                   |
| RAGI mutations: Gain-of-function (I2RSS processing)    | RAGI mutations: Gain-of-function (I2RSS processing)                                              |
| E649A                                                  | Solvent exposed and adjacent to N961 and S963 near E962.                                         |
| RAG2 mutations: RAGI bindingt, all other               | RAG2 mutations: RAGI bindingt, all other                                                         |
|                                                        | Solvent exposed and part of the positive top rim of the Y" shaped RAGI/2 complex                 |
| K283A/R                                                | Near M28SR (OS) stabilizing the of 306-315 loop                                                  |
|                                                        | RAG2 mutations: RSS bindingt. Nicking and Hairpinning                                            |
|                                                        | RAGI/2 interface: possible coding-end binding                                                    |
| K34A                                                   | RAG2 mutations: Joining negative or defective                                                    |
|                                                        | Solvent exposed. may interact with coding                                                        |
| R73A H94A                                              | RAGI/2 interface (adjacent to K34 and K97)                                                       |
| K97A                                                   | Near OS mutation G95R at RAGI/2 interface (K34 and R73)                                          |
| KII9R                                                  | Exposed to solvent and adjacent to K56 and K58                                                   |
| RI67A                                                  |                                                                                                  |
|                                                        | without PHD and regulatory\_domains                                                               |

<!-- image -->

## METHODS

The spectroscopy on J0100+2802 was first carried out on 29 December 2013 with the Yunnan Fainter Object Spectrograph and Camera (YFOSC) of the (GI2, at a clearly shows a breakat about 8,800 Aand no consistent with a quasar spcctrum at a redshift bcyond 6.2.To confirm this discov subsequent spectroscopic observations were obtained on 9 and 24 mirror Large Binocular Telescope (LBT) in the USA, respectively. Thelow to medium (obtained by the Lya line) . optical grism sharp optical

The near-infrared K-band spectroscopy on J0100+2802 was carried out with LBTILUCI-1 on 2 January 2014. Owing to the short exposure time (15 min), the spectrum is ofmodest signal-to-noise ratio (SIN). Although the Mg uline was clearly LBT spectrum did not allow us to accurately measure the line August and 7 October 2014, respectively. The exposure time was 3,600s for GNIRS and 3,635s the FIRE andthe GNIRS spectra, and scaled the combined spectrum according to in the high-quality J,H,K-band spectra also clearly display abundant absorption features; which have been identified as from intervening or associated systems with redshifts from 2.33 to 6.14 (Extended Data Fig 4). noisy optical being

is lower. An Fen emissionline is fitted with two broad Gaussian components. Thefour Mg I absorp lines in order to remove their effects on the with an uncertainty of 150 km s The continuum has a slope of = 1.43andthe continuum luminosity 1047 ergs 12,13 other z > 6 quasars After applying a virial black-hole mass estimator based on Although the systematic uncertainty of virial black-hole mass estimation can be up 10 black-hole mass obtained by assuming an Eddington luminosity of J0100+2802, which leads to a mass of 1.3 X 10" Considering the contribution of Balmer continuum, as done for other z > 6 quasars leads to a decrease of Lz,ooo to erg s an increaseofFWHMof to5,300 = 200 km s considering Balmer continuum is insignificant for the black-hole mass measure ment of J0100+2802. In addition; if we adopt a different virial black-hole mass which is still well consistent with the result we obtained above. fittings ofMg Mg' Mg "

- 31 Binocular Large
- 32.
- 33. Sloan Digital Sky
- Vestergaard, M. & Osmer, P. S. Mass functions of the active black holes in distant color-selected sample of the SDSS Fall Equatorial Stripe. Astrophys: J 699, 800-816 (2009).

After redshift and Galactic extinction corrections, the rest-frame H-and K-band

Extended Data Figure relatively bright in other bands (lower three rows). It is consistent with a point

<!-- image -->

source in the bands with high signal-to-noise detections. The size is 1' X 1' for all images. The circle represents an size of 10" in each image. angular green

<!-- image -->

<!-- image -->

Extended Data Figure 2 The LBT K-band image of J0100+2802. The size shows a morphology consistent with a source. fully point

<!-- image -->

Extended Data Figure 3 The rest-frame spectral energy distributions of The redshifts of these

<!-- image -->

of J1148+5251, and seven times higher than that of ULAS J1120+0641. The photometric data are from literature for J1148+5251 and J1120+0641. The

<!-- image -->

<!-- image -->

Extended Data Figure The major absorption features identified from optical and near-infrared spectroscopy of J0100+2802. Most of them are

<!-- image -->

absorption materials at 6.14,6.11,5.32,5.11,4.52, 4.22,3.34 and 2.33, respectively. Studies of intervening and associated absorption systems will be discussed elsewhere.

<!-- image -->

## METHODS

The protocol for teleporting a spin-orbit composite quantum state. The com bined state of photons 1 2 and 3 can be rewritten in the basis ofthe 16 orthogonal and complete hyper-entangled Bell states as follows:

)1z

6 and; respectively, the ÓAM qubits. It indicates that, regardless of the unknown state ) 1 the 16 measurement outcomes are equally likely, each with a probability of 1/16. By carrying the hyper-entangled Bell state measurement (h-BSM) on photons 1 and 2 to unambiguously distinguish one from the group of 16 hyper entangled Bell states, Alice can project photon 3 onto one ofthe 16 corresponding states. After Alice tells Bob her h-BSM result as four-bit classical information via a classical communication channel, Bob can convert the state of his photon 3 into the original state by applying appropriate twolocal unitary transformations qubit

Two-photon interference of spin-orbit composite state on a PBS. The input and output of photons 1 and 2 encoded in SAM and OAM on a PBS as shown in Fig can be summarized as follows: because the reflection the sign of OAM. Therefore; the output state for each of the input 16 hyper-entangled Bell states can be listed below: flips

(2)

(3)

(5)

We can see that only the Bell state |07 12 result in there one and only one photon in each output, whereas for the three other Bell states the two input photons will coalesce into a single output mode. Among these three Bell states, the )1z can be further distinguished by measuring two single photons in will being

1

74

(8

(9

(10) (11 ) (12) (13) (14) (15) (16)

ofthe output modes arc passing through two polarizers at 45 . Only the output with onc photon in cach output mode with an and the 4 corresponding input hyper-entangled Bell   states are of BSM on thc OAM qubits. being

BSM and teleportation of OAM qubits. SAM qubit, next we BSM on the OAM with a single degree of freedom is more straightforward, and can be implemented using a beam splitter. at a beam Having perform qubit. Dealing splitter

v2

2v2

2v2

to unambiguously discriminate two The overall efficiency of h-BSM combining all three steps is 1/8 x 1/2x 1/2=1/32. from

Generating three photon Ultrafast laser pulses with an average power of duration of 120 fs and repetition rate 0f76 MHz successively pass through three ß-barium borate (BBO) crystals (Fig; 2) axes aligned in perpendicular planes. All of the down-converted photons and thus has the highest brightness The second photon pair (2-3) is simulta statc Weestimatethe mean numbers ofphoton pairs generated per as 0.1,~0.01 and ~0.05 for the first, second and third respectively. pairs. pulse optic pulse

Sagnac interferometer to prepare the spin-orbit hybrid entangled state to ')/v2. Photon 1 is initially prepared in the respectively . Considering an double reflections in the PBS, the final output state is is deterministic. from

respectively. We measure each single photon from the two outputs of the PBS in modes). At zero where the photons are optimally overlapped in time; the orthogonal SAM input yields an For the parallel SAM input, the output state is quantum state becomes a classical mixture. Thus,at the counts appear the coherence length of the detected photons and stay stable for weeks. photon spatial delay delays

The two-photon interferences on beam splitters 1 and 2 are for the teleportation OAM states. It is interesting to note that, in stark contrast to the conventional Hong-Ou-Mandel interference; only having the two input OAM states ortho canlead toan interference dip, because the reflection at thebeam splitter is shown in Extended Data Fig Ib, c. flips gonal dclay

used with an efficiency of 80%. These high-efficiency OAM measurement devices boost the sixfold coincidence count rate in our present experiment by more than two orders of magnitude; compared with the previous use of hologram gratings. Error budget. The sources of crror in our experiment include double cmis sion in spontancous paramctric down-conversion; partial distinguishability of the independent photons that interfere at the PBS (~59) and the bcam splitters (~59); state mcasurcment crror duc to zero-order OAM (~29); imperfection of entangled photon 2-3 (~5%) and 4-5 (~9%); and imperfection ofthe to-be-teleported single-photon hybrid entangled state ( ~8%) Pair fidelity fidelity pairs

OAM measurement devices in the previous experiments is off-axis hologram 'challenging than the (p in the previous two-photon OAM for efficient OAM readout . uscd scaling

The first type is what we refer to as 'dual-channel' OAM measurement devices, after the two beam splitters. The strategy is to transfer the OAM information to the method is as follows. After the beam splitter, each photon passes through a HWP and is are then sent into Sagnac inside '2 (Fig 2), which is placed at a r/8 angle with respect to the interferometer forwards and with respective phases e" and e coordinate system; which pass through uscd They prism prism prism polar

contributed a ~15% background to the overall sixfold coincidence counts. If this were subtracted, the average teleportation would be improved to 0.74. Second, the imperfectly entangled photon pair 4-5 and the imperfect two-photon interference at beam splitters 1 and 2 (for the QND and OAM Bell-state measure ments, respectively) degradethe teleportation fidelity forallstatesby ~13%. Third, the imperfect state measurements mainly due to the zero-order OAM cause a degradation of ~2%\_ fidelity leakage

imperfect two-photon interference at the PBS degrades the teleportation fidelities However, for the states |p) where the photon is horizontally or vertically polarized; the actual teleportation does not require two-photon interference at the PBS; and is therefore immune to the imperfection of the interference. This explains why the teleportation fidelities for the states |6) and are the highest. This is inconsistent with the previous results: for the experiments the teleportation fidelities in the horizontal-vertical basis are higher than those in the = 45 linear and circular using

a Dove ei/' and e will be added to the two orthogonal OAM modes. Finally, the The overall transformations can be summarized as CNOT between the OAM and SAM: prism gate

HWP QWP Sagnac QWP

Effectively; the OAM is deterministically and redundantly encoded by the SAM suring the SAM using a PBS two output channels; we can recover information about thc OAM with Sagnac interferometers are used in the Bell states can be discriminatcd a bcam splitter qubit qubit, with

the secondtype is like a one-channel readout device (like a polarizer for SAM), and that the photon can be coupled into a single-mode fibre; while all other higher OAM readout.

where / is an phases of eil and e photon when it passes through the SPP forwards and, experiment; the OAM qubits are encoded in the OAM first-order subspace with the topological 16-phase-level SPP with an efficiency of ~979. shape phase bcing using

For the coherent transformation between the OAM zero mode and the super -

<!-- image -->

polarization bases; whereas for the experiments non-polarizing beam splitter, the teleportation fidelities in all polarization bases are largely unbiased using

lowest; which is affected by the imperfection ( ~8%) in the state preparation ofthe error and noise present in the experiment. It can be expected that all entangled strated, and should similar reductions in fidelity. undergo

We emphasize that, before the photons into the second beam splitter; for ment to ensure the two photons can be fed into the subsequent cascaded inter ferometers. Here the QND should prescrve the quantum information in the Yand Z DoFs. 'Thus; quantum teleportation of two DoFs of a single photon is required 'experiment

These sources of noise can in principle be eliminated in future by various methods. For instance; deterministic entangled photons ' do not suffer the problem of double pair emission. We also plan to develop bright OAM-entangled photons with higher fidelity; and a more precise 32-phase-level SPP for the next experiment

A universal scheme for teleporting NDoFs. Weillustrate in Extended Data Fig 2 discuss an example for thrce DoFs (Extended Data Fig 2b), labelled X, There are in total 64 hyper-entangled Bell states:

states. The required resources include photon entangled in the Z DoF;, hyper-entangled in the X-Y-Z DoFs, functionality non polarizing beam splitter and single-photon detectors; all of which are commercially available or have been experimentally demonstrated previously . pairs pairs

It has been known that iftwo single photons are superposed at a beam splitter, molecular-like quantum states. There are in total 28 possible combinations that are states;, follows: asymmetric as cxiting

After the photons have passed through the first beam splitter; we can filter out and onc following 16 states filtered the 28: being from

We perform a bit-flip operation on the X DoF on one of the arms of the inter ferometer, erasing the information in the X DoF. We then pass them into the second beam splitter, filtering out and retaining the six asymmetric combinations

combinations: again

pass the two photons into the third beam splitter, finally out the only remaining asymmetric state: filtering

By detecting one and only one photon in the output of the third splitter; we can from the 64 hyper-entangled Bell states on three DoFs.

To experimentally demonstrate the teleportation of three DoFs, the scheme would need in total ten photons (or five entangled photon from SPDC) which is within the reach of near-future experimental abilities; given the recent the above protocol can be extended to more DoFs as displayed in Extended Data Fig 2c. pairs

Feed-forward scheme for spin-orbit composite states. To realize a deterministic teleportation; feed-forward Pauli operations on the teleported particle based on sent this can be done for the spin-orbit composite state. For the SAM qubits; active feed-forward has been demonstrated before fast electro-optical modula advantage of this technology, which has been demon strated to have highfidelity, we use a coherent quantum SWAP gate between the OAM and SAM qubits. The SWAP is defined as using -speed gate gate

SWAP

The operation sequence for the feed-forward operation on the spin-orbit com tion. Third, an EOMis uscd tooperateon the 'new' SAMthat is converted from the operation on the SAM is unaffected. Lastly, a final SWAP gate converts the SAM back to OAM, which completes the feed-forward for spin-orbit composite states. Fig

composed of three CNOT gates (Extended Data Fig 3b). In the first and third CNOT gates (blue shading) the SAM qubit is the control qubit rccombincd at a PBS On the reflection arm only, a Dove is insertcd to Methods   section The extra Dove and HWP in front of the PBS are used to compensate for the phase shift inside the Sagnac interferometer . gate prism prism

- 31. 060404 (2013)
- 32. Slussarenko; S. etal The polarizing Sagnac interferometer: a tool for light orbital angular momentum sorting and spin-orbit photon processing Opt Express 18,
- Univ. Press, 2012)

- Jack B. etal Precise quantum tomography of photon pairs with entangled orbital
- realization of freely propagating teleported qubits. Nature 421,721-725 (2003).
- system. Nature 2,678-682 (2006)
- kilometre free-space channels. Nature 488, 185-188 (2012)
- forward. Nature 445.65-69 (2007)

<!-- image -->

- (1997)
- 39. Ma, X-S. etal. Quantum teleportation over 143 kilometres active feed using
- 40. 174-176 (2014)

<!-- image -->

a

<!-- image -->

b

<!-- image -->

Extended Data Figure Ou-Mandel interference of multiple independent photons encoded with SAMor OAM a, Interference at the PBS where input photons 1 and 2 are intentionally prepared in the states The yaxis shows the raw fourfold (the trigger photont andphotons 1, 2 and 3) coincidence counts. The extracted visibility is 0.75 + 0.03, calculated from without any background subtraction at zero for and, respectively, orthogonal SAMs. The red and blue lines are Gaussian fits to the raw data. b, Two-photon interference on beam splitter 1, where photons 1 and 4 are Hong delay parallel

<!-- image -->

prepared in orthogonal OAM states. The black line is a Gaussian fit to the raw data of fourfold (the trigger photon and photons 1,4and 5) coincidence counts. is the fitted counts at zero and, respectively, infinite delays. c, Two-photon interference at beam splitter 2, where input photons 1 and5 are prepared in the orthogonal OAM states. The black line is a Gaussian fit to the data points. The interference visibility is 0.69 = 0.03 calculated in the same way as in b. Poissonian counting statistics of the raw detection events. from

<!-- image -->

Extended Data Figure 2 A universal scheme for teleporting NDoFs of a single photons. a, A scheme for teleporting two DoFs ofa single photon three beam splitters; which is slightly different from the one presented in the main text PBS and two beam splitters. Through the first ensured by teleportation-based QND on the Y DoF. After passing the two photons through the two filters that project them into thel1 and |0) states for the X DoF, four states, |w)x survive. can result in one photon in each output. Finally we can discriminate the state using using

<!-- image -->

entangled Bell states. b, Teleportation of three DoFs of a single photons (Methods). Note that to ensure that there is one and teleportation-based QND on two DoFs in a (dashed circle). c, Generalized teleportation of N DoFs of a single photons. The h-BSM on N DoFs can be implemented as follows: (1) the beam splitter post-selects the asymmetric hyper-entangled Bell states in N DoFs which contain an odd number of asymmetric Bell states in one DoF, (2) two filters and one bit-flip operation erase the information on the measured DoF and further post-select asymmetric states; and (3) teleportation-based QND. hyper

<!-- image -->

Extended Data Figure 3 Active feed-forward for spin-orbit composite a, The active feed-forward scheme. This composite active feed-forward could be completed in a step-by-step manner. First, we use an EOM to implement the active feed-forward for SAM qubits. It is important to note that SAM; whose active feed-forward operation is done by a second FOM: Then the gate

<!-- image -->

OAM and SAM qubits second SWAP operation and are converted to the original DoFs. b, The quantum circuit for a SWAP gate between the OAM and SAM qubits. The SWAP is composed of three CNOT in the first and third CNOT the SAM and OAM qubits act as the control this is reversed undergo gate gates: gates, gate

## METHODS

Chemicals. The following chemicals were used as received: sodium dodecyl sulphate diacrylate (90%), trimethylolpropane ethoxylate triacrylate (Mn 1,2-dichlorobenzene (99%), Zonyl FS-300 (40% solids), methoxyperfluorobutane Aldrich ); siliconc oil (for oil baths 40 to +200 C), 1173 (Ciba); fluorinated acrylate oligomer (Sartomer); Nile Red (99%) (Acros); N-dodecylpropane-1,3-diamine made by the literature procedurezs32 . Fluorinated coumarin dye was made by the literature procedure' '. Cleavable surfactant sodium 2,2-bis(hexyloxy)propyl sul (Sigma-\_

a mixture of 2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9-hexadecafluorodecane-1,10-diol (10g toluene (250 ml) was heated to reflux with azeotropic removalofwater (Dean-Stark trap) After three the mixture was cooled to room temperature and washed perfluorohexanes (150 ml) and filtered: The filtrate was evaporated to 7.81g 598; found, 598. NMR spcctra werc obtained on a Bruker Avance 400 MHz spectrometer. LRMS was acquired on an Agilent 5973N GCMS. Plcase sec Extended Data Fig 3 and Extended Data Fig 4 for reaction scheme and days; yield

General fabrication of complex emulsions. The hydrocarbon and fluorocarbon varied depending on the solutions. Solutions were emulsified either inbulk by shak ing orby coaxial glass capillary microfluidics and cooledtoinduce phase separation: For hexane-perfluorohexane emulsions; the emulsions were chilled on ice before imaging and often imaged while immersed in a cool water bath to maintain a glass capillary microfluidic device made from an outer square capillary (outer diameter, 1.5 mm; inner diameter; 1.05 mm; AIT Glass) and inner cylindrical capillary (outer diameter, mm; World Precision Instruments) pulled to a 30um tip using a P-10OO Micropipette Puller (Sutter Instrument Company). The microfluidic set-up was heated above the Tc of the inner solution using a heat Emulsions were then cooled below Tc to induce phase separation. Emulsions were observed to be stable the time periods used (of the order of days). Longer-term stability experiments were not conducted. using phase during

madc were taken 5s until the interfacial tension appeared to be nearing equilibrium or the droplet became unstable. The hexane water interfacial tension was measured tobe 50 mNm and the perfluorohexane water interfacial tension was measured to be 55 mNm using drop drop every

Microscopy- Lateral confocal cross-sections of the droplets were imaged microscopy was conducted on Totake side-view images ofthe drops, emulsions were shaken to induce the using gold ning drops

Fabrication of magnetic Janus droplets. Magnetite nanoparticles were made as follows: 25 mlof concentrated NH,OH was added to an acidified solution of 1.6g ticle precipitate was collected with a magnet, washed with water and redispersed. by evaporation of solvent; and was subsequently redispersed in dichlorobenzene. Janus droplets were obtained by heating the nanoparticle-dichlorobenzene solution

<!-- image -->

andethyl nonafluorobutylether above Tzand in0.2% SDSand0.2% Zonyl were oriented using a neodymium magnet. shaking drops

perfluorohexane in equal volumes were used as the inner phase; and a mixture of 0.1% light-sensitive surfactant and 0.1% Zonyl FS-300 in an 8.2 ratio was used as surfactants in the aqueous phase. Slight adjustments to the surfactant concentra tions werc made achieve thedesired outcome; for example; more Zonyl was needed to generate lets that transitioned from a Janus droplet to a hexane-perfluorohexane-water double emulsion. A mercury lamp was used as the intense light source; and DAPI and FITC filters were used to sclectively allow ultraviolet ( ; 365 nm) and blue Fabrication of reversibly responsive pH-sensitive emulsions. Hexane and perfluo above and below pH4.7 by addition of HCl and NaOH during dropina

Fabrication of emulsions an acid-cleavable surfactant. Hexane and perfluorohexane in to 3 microscope stage while images were periodically made over an hour. using equal using

Fabrication of fluorous-hydrocarbon Janus particles. Fluorinated oligomer, fluorinated crosslinker; 1,4-butanediol diacrylate and trimethylolpropane ethoxylate triacrylate were used in a volume ratio of 15.3.14:10. 5% Darocur 1173 sified in 1% SDS and polymerized with ultraviolet light over ice. acrylate

Fabrication of hemispherical partices: 1,6-hexanediol diacrylate with 4% Darocur above Tcand emulsified. which werethen polymerized under a Dymax Blue Wave 200 ultraviolet lamp while kept cold on ice.

Fabrication of four-phase emulsions. Light mineral oil with 20 wt% octadecane fluorobutyl ether were used as the inner phases in a volume ratio of 6.7:13. The mineral oilandethyl nonafluorobutylether both partition into the silicone oil such that on phase separation the silicone oil phase is enriched with some quantity of were used as the outer phase; and emulsions were formed in bulk by shaking:

Estimation of equilibrium interfacial tensions in the presence of surfactants. pendant-drop method accurately for periods oftime while maintaining stable volume because surfactant continued to adsorb at the droplet inter face;further reducing the already low interfacial tensions. Therefore, it islikely that tively, the perfluorohexane-water interface for different surfactant compositions, la, are not the equilibrium interfacial ten long very drop Fig long

Rosen suggested  that the dynamic interfacial tension of surfactants could be accurately modelled using an empirical model of the form

Yo (5 =Yeqb

The value of n depends on the type of surfactant and the interface considered, as determined for every set of experimental conditions. The constant t* is the half-life of thc interfacial tension eters t*and n) can be determined from a least-squares fìt of equation (5) to

equation (5) to fit the interfacial tension data for all the surfactant systems considered are pre sented in Extended Data Table 1. The smallest value of R? obtained for the experimental data across all the systems studied was0.909, indicating very lagreement between the predictions made using equation (5) and the experimental data gen erated the goniometer . using good using

The resulting extracted values have been used to plot the variation in the

<!-- image -->

mate the equilibrium interfacial tensions with the 0.1mNm would alter the interfacial tensions relative to those of the pure liquids. desig

hexane and perfluorohexane have an upper consolute temperature, Teofapproxi mately 22 €, with a critical density of 1.14gcm and a volume ratio very close to temperatures close to (but below) this upper consolute temperature is close to zero, and, consequently; it is difficult to measure accurately conventional labora tory techniques such as pendant or Du matein the physical chemistry literature comes from the predictions ofa model for capillary fluctuations at an interface fitted to reflectivity measurements?  . In mNm using drop Nuoy X-ray

1 26 Tc T (6) Tc

perfluorohexane interfacial tension should be0.4mN m We were unable to find other experimental data in the literature to support this estimate: However; given the equilibrium interfacial tension values and images of the resulting Janus drop-

The relationships between the of Janus droplets and the ratio ofthe volmagnitudes ofthe interfacial tensions operating at the various interfaces of the droplet have been examined in shapes '

Yu YE Ru

The 'ofa typical hexane-perfluorohexane Janus droplet in water is illustrated in Extended Data Fig 2a. The droplet's interfaces are spherical arcs with different of contact between thetwo on the outer (water of the type shown in Extended Data Fig 2b, each shape 'phases with

From the definition of the volume ratio; k, between the hexane and perfluorohexane phases, it follows that:

(RF-D) k 8) Vcap Vcap

The volumc ofa

D allows us to solve equation (8) for the radius of curvature of the F-H interface, RFH. Equation (7) can then be used to solve for the missing

contact can be computed by analysing the images of the Janus droplets. atic of the analysis process is shown in Extended Data Fig 2c-e. A raw image of a Janus droplet (Extended Data Fig 2c) is first subjected tothe Canny dctection algorithm based on the non-normalized contrast, with a Gaussian kernel radius results in the dctection ofthe outer (water-facing) interfaces ofthe Janus droplet as shown in Extended Data Fig 2d. Arcs corresponding to the H-W and F-W inter faces are then selected by visual inspection and fitted to circles Taubin's (with grcen dots for centres) in Extended respectively. The diameter, D,ofthe circle of contact between the hexane and per fluorohexane phases is calculated as the minimum separation betwccn the points lying between the arcs chosen to represent the H-W and F\_W interfaces. This line of minimum separation is shown in Extended Data 2e. Image preprocessing and interfacial tension calculation was performed in MATLAB. using Data Fig

This droplet analysis was performed for six Janus droplets; three from each of the two conditions fsDs betwecn the two sets of surfactant systems; which is consistent with our expecta tion that FH is at best only weakly affected by the composition of the surfactant.

Wenote that accurately curvature ofthe interfaces ofthe droplet is feasible only in the absence of fluid flow gradientsin surfactant concentration and inducing Marangoni stresses Thc inter play between these effects ultimately determines the interfacial tensions at any ona complex emulsion droplet. Higher shear rates can dramatically disrupt droplet stability, to the fragmentation of the complex emulsion and the relcasc of the encapsulated phases phenomenon whose onset has been examined in detail point

- 32.
- 33.
- 34,
- 35. Harris, J W. & Stöcker, H. Handbook of Mathematics and Computational Science 107 (Springer, 1998)
- 36.
- 37. defined by implicit equations with applications to edge and range image
- 38. P.Emulsion drops in external flow fields the role of liquid
- 39. flows J. Fluid Mech. 211,123-156 (1990)
- 40. Muguet; V. et al. W/O/W multiple emulsions submitted to a linear shear flow: correlation between fragmentation and release. J Colloid Interface Sci 218, 335-337 (1999).

<!-- image -->

Extended Data Figure 1 Dynamic interfacial tension data was used to estimate the equilibrium interfacial tensions for the hexane-water and perfluorohexane-water interfaces. Dynamic interfacial tension data (in blue) was obtained the pendant method; the representative data (such that the aqueous solution contained 0.1% SDS and 0.1% Zonyl in a 9:1 ratio). The data was fitted to an empirical model (in red) to estimate the from drop

<!-- image -->

was performed for all measured interfacial tensions and the fitted parameter results are tabulated in Extended Data Table 1.b, The estimated equilibrium interfacial tension values were used to plot the hexane-water (squares) and perfluorohexane water (circles) interfacial tensions asa function ofthe fraction Methods for more details fitting

SDS

<!-- image -->

<!-- image -->

Extended Data Figure 2 The geometry of a Janus droplet can be used to estimate the interfacial tension between hydrocarbon and fluorocarbon internal phases. a, Sketch of a Janus droplet consisting of hydrocarbon (grey) of curvature of the H-W (Ru) F-W (RF) and F-H (RFH) interfaces are related to their respective interfacial tensions through the Young-Laplace equation. The diameter of the circle of contact between the two phases (dashed line) is denoted as D. b, The Janus droplet is composed of three spherical caps, and the volume; Vcap of each constituent spherical cap is a function of the radius of curvature of the spherical surface and the base diameter D. Here we show the cap at the intersection of the hydrocarbon and fluorocarbon phases in

<!-- image -->

which is a function of RFH and D. c An exemplary image of a hexane perfluorohexane Janus droplet obtained at fsDs 0.6, which was used to detection to determine theH-W and F-W interfaces. e, The resulting edges are fitted to circles (red lines with contact is then perfluorohexane interface; which was subsequently used to estimate %FH- See discussion in Methods for more details and Extended Data Table 2 for Vcap green

<!-- image -->

<!-- image -->

(ppm)

Extended Data Figure 3 Reaction scheme and H-NMR of the fluorinated crosslinker. Reaction scheme for the synthesis of the fluorinated crosslinker. BHT, 3,5-di-tert-butyl-4-hydroxytoluene b, 'H-NMR spectrum of the fluorinated crosslinker.

<!-- image -->

<!-- image -->

210 200 190 180 170 160 150 140 130 120 110 100 90 80 70 60 50 40 30 20 10

2115 (ppm)

<!-- image -->

Extended Data Figure "C-NMR and I9F-NMR of the fluorinated crosslinker. fluorinated crosslinker .

<!-- image -->

## Extended Data Table 1 Parameter values obtained by fitting an empirical model to interfacial tension measurements obtained using pendant-drop goniometry

|          | Hexane-water interface   | Hexane-water interface   | Hexane-water interface   | Perfluorohexane-water interface   | Perfluorohexane-water interface   | Perfluorohexane-water interface   |
|----------|--------------------------|--------------------------|--------------------------|-----------------------------------|-----------------------------------|-----------------------------------|
| fraction |                          |                          | R?                       | Yeqb (mN m')                      |                                   | R?                                |
| 0.00     | 7.33 0.12                | 156 24                   | 0.925                    | 4.42 0.14                         | 159 42                            | 0.980                             |
| 0.20     | 0.03                     | 337 15                   | 0.989                    | 5.80 + 0.04                       | 106 +                             | 0.979                             |
| 0.40     | 7.21 0.14                | 315 53                   | 0.956                    | 6.49 0.05                         | 233 22                            | 0.978                             |
| 0.60     | 6.33 0.22                | 293 113                  | 0.947                    | 6.45 + 0.12                       | 54                                | 0.982                             |
| 0.90     | 6.39 0.02                | 35 +                     | 0.992                    | 7.66 0.03                         | 57                                | 0.994                             |
| 0.95     | 5.78 0.06                | 41 + 1                   | 0.993                    | 7.73 0.06                         | 85                                | 0.991                             |
| 1.00     | 0.15                     |                          | 0.909                    | 19.56 0.3                         | 702                               | 0.967                             |

was above 0 9 signifying a good fit

<!-- image -->

Extended Data Table 2 composition of the surfactant added to the system; fsDs

|   0.4 |   0.6 |
|-------|-------|
|  1.06 |  0.93 |
|  1.17 |  1.18 |
|  0.99 |  1.1  |

## METHODS

Image availability- Amateur images. Available at the following databases: Associ ation of Lunar and Planetary Observers-Japan, http:llalpo-jasahikawa-medacjpl Latest/Marshtm (2012), and Société Astronomique de France (Commission sur -

Hubble Space Telescope images. Available at NASA Planetary Data System (PDS)

MRO MARCI Weather Reports. Malin Space Science Systems. Captioned Image 28 March 2012 http:l /www.

Release No. MSSS-216 03/21/and Captioned Image Release No. MSSS-217 images/2012/03/28/.

Image analysis and measurement. Most images were obtained with broadband 450 = 50nm) green (G, 520 = 50nm)and aligning and re-centring sequences of frames captured in video mode; and application of the 'Iucky imaging' method?? and photometric analysis) at a wavclength of 450nm is 0.317 arcsec and the of25 km on Mars; typically used in high resolution planetary images where recordfeatures depends, for excellent conditions, on resolution and features coverage of the projected plume is 1g). Image navigation; that is, the determination ofthe planetary limb and ter minator was performed two well-testedsoftware packages (LAIA, WinJupos; bright Martian limb was used as a rcference but not the terminator whose defini rately controlled by measuring the position ofwell-known surface features (Olympus Mons and Tharsis volcanoes) . The projected plume top altitude on the sky plane (definedas theborder between the feature andthe dark background, contrast forced) simply determined from its distance tothe Mars disk centre and subtraction of the measured Martian radius (all in pixel units) . Navigation and image measure ments were 'performed independently by four of us From these multiple measure determinations. We estimate that the positioning error is 42 pixels and that, for surements result from brightness diffusion at the top and sides ofthe plumes and the determination of the base location ofthe plume relative to the navigated terminator, including its brightness irregularities. ming d-g ing seeing spatial Fig using from

As a further step in navigation control, we used the image series of 20 March by cedures: (1) through measurements on each image of the planet and plume top radius to calculate the plume maximum altitude; (2) through determination of the mean radius for the whole image series (and its uncertainty) and then using this mean consisyield

The measured topaltitude values (H) andtheterminator west longitudes (L,defined gave the values at Lmax 43,164.8,01 401.8,02 = 0.929 Peak

Plume altitude model. Angular distance between the plumes base and the central meridian. Our coordinate system is placedat the centre of Mars: the xaxis will be on the observer's visualand the y-z plane is coincident with the sky plane. Coordinate system geometry is depicted in Extended Data Fig: 4, with the cloud near the west morning limb and the sub-Earth point on the equator. The longitude of the Central Meridian (CM) is /CM, and the latitude and longitude of the plume are related to the angular distance ß betwcen the plume and the limb as a reference the negative y axis, by: rising taking

where ß is positive if the limb is behind the cloud, and negative if the cloud is

Cy and €z 1/2 being

The minimum height of the plume Hmin to protrude from the limb (z(ß) = 0) is

Ry Hmin RM {1 = cos? B}

Real plume altitude derived from its projected length. When ß <0, by expression (2) z(ß) must satisfy

RM

and the actual plume altitude is:

H= RM {1 =

height H is now given by:

z(ß) H=

Correction when Mars a declination De as observed from Earth. By taking the declination angle + De when the north rotation has pole pole

cos DE sinDE cos DE

Therefore; expressions (5) and (6) must be corrected taking into account that:

Sy=y

In   the rotated   coordinate the transformed coordinates of the plume top, with the non-transformed coordinates of the plume top given by: being

Expressing gives its real height

1/2 (10) cos DE

dition to expression (10) and after somc algcbraic manipulations; we obtain: Owing

sin

the and we have: planet

H= (12) {cos? cos? ß+ sinßsinDe)? } Pc

Mars' shadow 'projection on the plume: Given the coordinates ofthe subsolar on Mars by an angle: point (is

(13)

ß when we are close to the morning limb and:

on the y-z the planet centre is larger than the planet's radius With plane from

(14)

planet's shadow projected on the plume is:

Ru Sc

equations (5) and (15),the visible projected length ofthe planet's shadow projected on the protruding plume is: using

1 2 S(B) Ru (16)

For ß > 0the planet's shadow projected on the plume is completely visible, since and according to cquation (6) the projected shadow's hcight will be: again,

Ru {cos? ß+sin? (17) cos?

Again; if the planet's rotation axis is tilted by = DE WC obtain dcgrees,

S(ß) cos  sinß ~RM (18)

(19)

for ß2 Pum

The model predictions are shown in 2 A 7 calculation between the mea sured top altitudes considering the individual error and the predictions from the geometric model for a uniform plume shows that for 20 March 7 for alti tudes 190-195 km (best fit) but for 21 March /(min) = 20 for top altitudes 240 250km. Thelarge deviations between the modelandtheobservations for 21 March data rule out a uniform structure for the plume. Fig 44 top

Altitude ofthe 1997 HSTfeature The 17 1997 event was single image at each wavelength; and thus do not show the plume in rotation at the limblterminator. Therefore we can only constrain the maximum and minimum altitudes for the feature as seen projected on the terminator. The solar zenith anglc SZA 90 (grazing illumination) the minimum altitude is given by equation (15): Hmin Hmax will occur for a vertical feature whose projection Las seen on the terminator (RM +S) RM and then 480km May specific

Photometric calibration. (1) Ground-based observations (20-21 March 2012). Stacked and aligned unprocessed images were used for reflectivity measurements. whoseabso lute (I/F) reflectivity is known 4. The resulting I/F can be seen as an average for the cloudat B, Gand R, and from independent measurements by the team members of the same images; we estimate an uncertainty of 209 Mars

Radiative transfer model. We conducted radiative transfer calculations of the reflectivity I/F with a backward Monte Carlo model designed spherical-shell atmospheres The model produces as output the full Stokes vector of radiances; but only the first vector element (intensity) was considered for comparison with the grazing illumination/viewing geometries ofboth the 1997 and 2012 events. In its specific implementation here the model assumes a uniform cloud of geometrical thickness Dthat enshrouds the entire planet. The observer looks upon the planet terminator with a line of sight that sequentially probes the full range of altitudes tical direction at the planet's terminator and the Sun illumination direction), and Thc cosine of thc anglc viewing direction and the local vertical at the terminator is for viewing polar

of the plume from the the 2012 event, the prescribed azimuth angle and the cosine ofthe angle are enter the atmosphere followinggrazing trajectories; and penetratehalfway through the limb before scattered towards the observer at the terminator Tocompare with the box-averaged I/Fs observations; the model-calculated I/Fs were also averaged over the cloud gcometrical thickness D from the observer's vantage A number of photon realizations between 10'and 10' ensured accuracies typically better than 5%, which is much less than the measured uncertainties. The atmospheric inputs to the model include the cloud particles' optical properties and the cloud D. point being from point.

by the two moments ren (effective radius) and ven (effective variance)'  . Particle

The particles' properties required in the radiative transfer calculations phase function and extinction cross-section; respectively. Each ofthese properties is specified at the appropriate radiation wavelength /. For the determination ofthe properties we used Mie theory, which applies to scattering by spherical par ticles. Ifthe particles are non-spherical, Mie may bias the properties of inferred properties between spherical and non-spherical particles depend on the particles' composition and on the radiation wavelength. Numerical investigations have . Ithese differences over a limited Without additional information on the cloud particles, it is difficult to assess the consistency in the treatment with Mie theory ofthe radi ative transfer problem: We can nevertheless tentatively quantify it by comparison function; which is particularly sensitive to the particles' few studies sugthe differences between spherical and non-spherical particles are not usually more than a few tens of per cent. These differences are less than for larger values of xeff optical optical 'theory shape 'explored against shape,

Overall, each radiative transfer calculation requires user-inputted values for ;, composition (and therefore wavelength-dependent refractive indices), reff itics I/F model calculations and observations is thereforc multi-parametric Intheexplorationofthe space ofparameters; webuilt a ofsolutions tothe radiwith valucs adopted in from 16 to 10 31 values in steps following radiative transfer calculations for each of the 1997 and 2012 events exceeds 105 particle from prior

For cach possible spectrum within the of calculations with identical particle 'quadratic deviation of the model theobserved data weighted by the observation errors (73). A subset for the 1997 event and Extended Data Fig 7 for the 2012 event. In the former case, dust particles do not fit the data with /? < 1.0. While a number ofsub-optimal solu tions for different combinations of the free parameters can be found, the highest the free parameters. This happens for particles with effective radii of the order of framework, there is no way to discriminate between the variances and this also impedes a choice between HzO and COz as the most likely particle type. Similarly, the 7 results for the 2012 observations show a broad range of particle include dust particles during the 2012 event, it is possible to retrieve acceptable fits for particle sizes rang tuned   Observations at shorterllonger wavelengths might potentially break this degeneracy. grid from Fig making They

All in all, the radiative transfer calculations for both the 1997 and 2012 events model fit translates into particle density after dividing the thickncss by the cross-section at 502 nm and the cloud geometrical thickness optical optical particle

(2) HST calibration (17 1997). Hubble Space Telescope observations acquired in filters the ultraviolet (F2SSW) to the near-infrared (FIOA2M) (Extended instructions. Radiances were converted into absolute reflectivity I/F the solar spectrum The resulting I/Fas a function of planetary geographical coordinates was confirmed against values given by other authors for selected locations of the planet 'and with albedo values of the planet The intensity calibration method for ground-based images was validated with a similar procedure to that used in HST images and comparison with the above procedure. May from using

Code availability. version of the model is freely available through: http:lldx.doi. 1051/00046361/201424042. This version contains instructions to run the model, test cases and model outputs that can be compared to calculations tabulated in ref. 38.In the analysis of the Mars plumc, we uscd a version of the PBMC suitable for 'spherical shell atmospheres. The spherical-shell model is available on request from AGM. (tonhingm@gmailcom) parallel org/10.

General Circulation Model. As supplied in the Mars Climate Databasc at Mars

water-ice density as 0.93gcm (ref. 40) g; the corres 10* , taking For the retrieved cloud density 0.01 cm evaporation of On the other hand, the atmospheric density is 40 Ls 90  , because of oxygen dominance The number density of molecules in Therefore; evaporation of the water ice will produce an enrichment of water by a factor ~1,000 over normal conditions, Taking NAvo

the mass of a spherical particle the 'corresponding number of molec ules resulting from evaporation is mNAvJu' is the gand

<!-- image -->

cloudevaporation will produce ~10* particles per cm On theother hand, the 0.09,the number density ofmolecules inthe atmosphereis N(COzatm Therefore; CO2 ice evaporation will produce a 5% enrichment of from )

- 29.
- 30.
- 31
- 32. 2010 perihelic opposition of Jupiter observed from Barbados. The
- 34, surface mineralogy from Hubble Space Telescope imaging during 1994-1995: observations; calibration; and initial results. Geophys. Res 102,9109-9123 (1997) Mars
- 35. 722-741 (2010)
- 37
- of the Sun for comparison with solar analog stars Astron J 112,307-315 (1996)
- 38. García Muñoz, A & Mills F.P.Pre-conditioned backward Monte Carlo solutions to radiative transport in planetary atmospheres. Fundamentals: sampling of
- 247-258 (1986)
- 40. 2010)

<!-- image -->

Extended Data Figure Images of the 2012 plume event (ringed) on 12-20 March. Dates in March (and authors) are as follows: a, 12 (MD); each is in UTC.

<!-- image -->

<!-- image -->

Extended Data Figure 2 | Images of the 2012 plume events (ringed) on 22 March and 13 April. a, First event on 22 March, 04:12 UTC (image by WJ); b, second event on 13 April, 20.03 UTC (image by D. Peach).

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

Extended Data Figure Martian viewing geometry. Angle definitions with the simulated protrusion of altitude Hlocated at c and out of the illuminated part of the disk near the limb. b, as a reference the the equator (but the latitude of the subsolar is not zero). Green arrows represent the projected cloud altitude as seen from Earth in the extreme point Top taking point

<!-- image -->

situations when the cloud is on the terminator and follows the grazing sunlight; and when it follows the planets radius. To simplify the figure; and without loss of generality, the sub-Earth is placed on the the subsolar and the cloud base. c, General side view of the geometry of the planet's projected shadow. linking point arc point

<!-- image -->

<!-- image -->

<!-- image -->

Extended Data Figure 5 | Hubble Space Telescope images of the event on 17 1997 Wavelengths and times in UTC were: a, 255 nm (17:27); May

| Identification   | HST number     | Filter   | Wavelength (nm)   |   FWHM (nm) |
|------------------|----------------|----------|-------------------|-------------|
|                  | u3gi770lm fits | F2SSW    | 257.3             |        42.6 |
| b                | u3gi7703m fits |          |                   |        18.2 |
|                  | u3gi7704m fits | FSO2N    | 5012.2            |         3.6 |
|                  | u3gi7705m fits | F673N    | 673.2             |         6.3 |
|                  | u3gi7707m fits | FIO42M   | 1045.3            |        89.7 |
|                  | u3gi7708m fits | FS88N    | 589.3             |         6.4 |

Table at bottom identifies each image and its HST number; and also shows filters used, giving their central wavelength and bandwidth (FWHM)

Extended Data Figure 6

<!-- image -->

This is an example of the degeneracy of the model solution due to the narrow wavelength range covered in the 2012 event. Model fit as follows: solid

calculations. As in Fig: 3, open black triangles show the observed reflectivity of the 2012 cloud The error bars represent the average quadratic deviation of the measured reflectivity in the integration box:

<!-- image -->

<!-- image -->

Extended Data Figure 7 | Assessment of the radiative transfer model fit for the 1997 event. a-i, Colours show values of / (for measured I/F versus model calculation; colour scale at right) for the effective radius in pm) versus depth at 502 nm), and for different particle types and values of the indicated particle variance shown in parentheses) as follows. CO2 (0.5); optical

<!-- image -->

provide the they

<!-- image -->

Extended Data Figure 8 and particle variance, but for the 2012 event.

<!-- image -->

<!-- image -->

## METHODS

Preprocessing. Working directly with raw Atari 2600 frames; which are 210 X 160 limages with a 128-colour palette; can be demanding in terms of computation and memory requirements. Weapply a basic preprocessing step aimed at reducing the input dimensionality and with some artefacts of the Atari 2600 emu valuc ovcr the frame cncoded and the previous frame. This was necessary to remove flickering that is present in games where some objects appear only in even frames while other objects appear only in odd frames, an artefact caused by the limited number of sprites Atari 2600 can display at once. Second, we then extract the Y channel, also known as luminance, from the RGB frame and rescale it to ing to the m most recent frames and stacks them to produce the input to the Q-function, in which m = 4, although the algorithm is robust to different values of m (for example; 3 or 5) pixel dealing being

Model architecture. There are several possible ways of parameterizing Q neural network Because Q maps history-action pairs to scalar estimates of their Q-valuc; the history and the action have bcen uscd as inputs to the ncural nctwork is that a scparate forward pass is required to compute the Q-value of cach action; architecture in which there is a separate output unit for each possible action; and only the state representation is an input to the neural network. The outputs correspondto the predicted Q-values ofthe individual actions for the input state: The main advantageofthis type ofarchitecture is the ability tocompute Q-values for all possible actions inagiven state with only a single forward pass through the network using

the neural network consists ofan 84 X 84 X 4 image produced by the preprocess con volves 64 filters of 4 X 4 with stride 2, again followed by a rectifier nonlinearity. This is followedby a thirdconvolutionallayer that convolves 64 filtersof3 X 3 with stride 1 followed by a rectifier. The final hidden is fully-connected and con sists of 512 rectifier units. The output is a fully-connected linear layer with a single output for each valid action. The number of valid actions varied between 4 and 18 on the games we considered. ing layer layer layer

Training details. We performed experiments on 49 Atari 2600 games where results were on each game: the same network architecture; learning algorithm and hyperpara meter settings (see Extended Data Table 1) were used across all games, showing that our approach is robust enough to work on a variety of games while incorporating only minimal fied games; we made one change to the reward structure of the games only. As the scale of scores varies greatly Clipping the rewards in this manner limits the scale of the error derivatives and makes it easier to use the same it could affect the performance of our agent since it cannot differentiate between rewards of different magnitude. For games where there is a life counter, the Atari 2600 emulator also sends the number oflives left in the game, which is then used to mark the end of an episode training: prior during training from during

In thcsc 32. The behaviour policy training was % fora total of 50 million frames (that is, around 38 ofgame experience in total) and used a replay memory of 1 million most recent frames during from days -

The values ofall thehyperparameters and optimization parameters were selected by performing an informal search on the games Breakout, Seaquest, Space Invaders and Beam Rider. We did not perform a systematic grid search owing to the high computational cost. These parameters were then held fixed acrossallother Data Table 1. Pong

Following previousapproaches to playing Atari 2600 games, we also use asimple frame, and its last action is repeated on skipped frames. Becausc running the emulator forward for one step requires much less computation than the agent select an action; this techniquc allows the agent to play roughly k times more games without significantly increasing the runtime. We use k = 4 for all games. cvery having

Our experimental setup amounts to the following minimal knowledge: that the input data consisted of visual images (motivating our use of a convolutional network), the game-specific score (with no modification), number of actions, although not their correspondences (for example; specification of the up 'button') and the life count. using prior deep

The professional human tester usedthe same emulator engine as the agents, and played under controlled conditions. The human tester was not allowed to pause, save or reload games. As in the original Atari 2600 environment; the emulator was rewardachieved from around 20 episodes ofeach game lasting a maximum of5 min each; following around 2h of practice playing each game:

Evaluation procedure. The trained agents were evaluated by playing each game 30 times for up to 5 min each time different initial random conditions ('noop cedure is adopted to minimize the possibility of overfitting evaluation. The random agent scrved as a baseline comparison and chose a random action at 10 Hz sixth frame, repeating its last action on intervening frames, 10 Hz is the random agent to this frequency avoids spurious baseline scores in a handful of the at 60 Hz (that is, frame). This had a minimal effect: changing the normalized performed the expert human by a considerable margin: with during every setting every Crazy

Algorithm. We consider tasks in which an agent interacts with an environment, At each time-step the agent selects an action a, from the set oflegal game actions, and the game score. In general the environment may be stochastic. The emulator's Xrelld Note that in general the game score may dependon the whole previous sequenceof actions andobservations; feedback about an action may only be receivedafter many thousands of time-steps have elapsed. from

Because the agent only observes the current screen; thetask is partially observed and many emulator states are perceptually aliased (that is, it is impossible to fully algorithm; which then learns game strategies depending upon these sequences. All steps. This formalismgives risetoa but finite Markov decision process (MDP) in which each sequence is a distinct state. As a result; we can apply standard rein large

The ofthe agent is tointeract with the emulator by selecting actions in a that maximizes future rewards. Wemake the standard assumption that future rewards goal way

define the future discounted return at time tas Rr = in which Tis the

time-step at which the game terminates define the action-valuc function Q (s,a) as the maximum expected return achievable by following any policy, after seeing some sequence $ and then distributions over actions) Wc optimal taking

The optimal action-valuc function an important identity known as the then the obeys 'optimal

Q (s.a)

The basic idca bchind many rcinforcement lcarning algorithms is to estimate the action-value function by using the Bellman equation as an iterative update; tothe is impractical, because the action-value function is estimated separately for each ment learning community this is typically a linear function approximator, but

sometimes a nonlinear function approximator is used instead, such as a neural i to reduce the mean-squared error in the Bellman equation; where the optimal target values r +" max;' Q (s.a ) are substituted with approximate target values

replay the behaviour distribution is averaged over many of its previous states, smoothing out learning and avoiding oscillations or divergence in the parameters. Note that when learning by experience replay; it is necessary to learn off-policy ple) which motivates the choice of Q-learning:

Note that the targets depend on the network weights; this is in contrast with the each stage ofoptimization; we hold the parameters from the previous iteration 0; fixed when optimizing the ith loss function L(0,), resulting in a sequence of well defined optimization problems. The final term is the variance ofthe targets; which therefore be ignored Differentiating the loss function with respect to the weights we arrive at the following gradient:

max

computationally expedient to the loss function by stochastic gradient can bc rccovercd in this framcwork by updating the weights after every time step, replacing the expectations 0; optimize using setting

Training algorithm for Q-networks. The full algorithm for training according to an #-greedy policy based on Q Because using histories of arbitrary above. The algorithm modifies standard online Q-learning in two ways to make it suitable for training large neural networks without diverging deep deep

Note that this algorithm is model-free: it solves the reinforcement learning task directly adequate exploration of the state space: In practice; the behaviour distribution is often selected by an #-greedy policy that follows the greedy policy with probability 1 = c and selects a random action with probability € using

First, we use a technique known as experience replay? in which we store the over many episodes (where the end of an episode occurs when a termi nalstate is reached) intoa replay memory. During the inner ofthe algorithm (s,a,r,s') U(D), drawn at random from the ofstored samples. This approach has severaladvantages over standard online Q-learning First, each step ofexperience is potentially used in many weight updates; which allows for greater data efficiency . Second, Icarning dircctly corrclations between the randomizing the samples breaks these correla tions and therefore reduces the variance of the updates. Third; when learning on policy the current parameters determine the next data sample that the parameters samples will be dominated Itiscasy to scehow unwanted fccdback stuck in apoorlocal minimum, or even pooled loop pool from samples; ing by loops

In practice; our algorithm only stores the last N experience tuples in the replay memory,and samples uniformly at random from Dwhen performing This approach is in some respects limited because the memory buffer does not differ entiate important transitions and always overwrites with recent transitions owing to the finite memory size N. Similarly, the uniform sampling gives equal impor tancetoall transitions in the replay memory. A more sophisticated sampling strat egy might emphasize transitions from which we can learn the most; similar to prioritized sweeping

The second modification to online Q-learning aimed at further improving the stability of our method with neural networks is to use a separate network erating the targets y; in the Q-learning precisely, Cupdates we clone the network Q to obtain a target network Q and use Q for generating the that increases Q(spa ) often also increases Q(sr to oscillations or 'divergence ofthe policy. Generating the targets using an older set ofparameters adds a between the time an update to Qis made and the time the oscillations much more unlikely . for update. More every leading delay update

maxa 1, Bccausc thc absolutc valuc loss for all positive values of x, clipping the squared error to be between =1 and 1 cor responds to an absolute value loss function for errors outside of the ( =1,1) interval This form oferror clipping further improved the stability ofthe algorithm: update using

## Algorithm I: deep Q-learning with experience replay.

Initialize replay memory Dto capacity N

Initialize action-value function Q with random weights 0

Initialize target action-value function Q with weights 0

Initialize sequence $1 = {x1

otherwisc sclect a = argmaxa

in D

Sample random minibatch of transitions

if terminates at step j+1 0 otherwise episode Sety =

Perform a gradient descent step on network parameters 0 Csteps reset Q= Q Every

## End For End For

- 31. architecture for object recognition? Proc; IEEE Int Conf Comput Vis 2146-2153 (2009)
- 32
- 33. Kaelbling L P, Littman, M. L & Cassandra AR Planning and acting in partially observable stochastic domains. Artificial Intelligence 101,99-134 (1994)

<!-- image -->

Extended Data Figure Two-dimensional t-SNE embedding of the representations in the last hidden assigned by DQN to game states hidden layer representation assigned by DQN to game states experienced there is similar structure in the two-dimensional embeddings corresponding to the DQN representation of states experienced during human play (orange layer during

<!-- image -->

points) and DQN play (blue points) suggests that the representations learned by DQN do indeed generalize to data generated from policies other than its own: The presence in the t-SNF embedding of overlapping clusters of points corresponding to the network representation of states experienced during human and agent play shows that the DQN agent also follows sequences of states similar to those found in human play. Screenshots corresponding to

<!-- image -->

a

Extended Data Figure 2 Visualization of learned value functions on two games, Breakout and a, A visualization of the learned value function on the game Breakout. At time and 2,thestate value is predictedtobe ~17 clearing the bricks at the lowest level: Each of the in the value function curve corresponds to a reward obtained by clearing a brick the value increases to ~21 in anticipation of breaking out and clearing a set of bricks. At 4, the value is above 23 and the agent has broken through. After this point, the ball will bounce at the upper part of the bricks clearing many of them by itself.b, A visualization of the learned action-value function on the game At time 1, the ball is moving towards the controlled by the agent on the right side of the screen and the values of Pong points Peaks large point point Paddle

<!-- image -->

all actions are around 0.7, reflecting the expected value of this state based on previous experience. At time 2, the agent starts moving the towards theball and the value ofthe 'up' action stays high while the value of the 'down' action falls to ~0.9. This reflects the fact that pressing 'down' would lead to the agent the ball and incurring a reward of = 1. At time the agent hits the ball by pressing 'up' andthe expected reward increasing until time 4,when the ball reaches theleft edgeofthe screen and the value of all actions reflects that the agent is about to receive a reward of 1. Note, the dashed line shows the past trajectory of the ball purely for illustrative Interactive, Inc. paddle point losing point keeps point

<!-- image -->

## Extended Data Table 1 List of hyperparameters and their values

| Hyperparameter                  | Value   | Description                                                                                                                                                                     |
|---------------------------------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| minibatch size                  | 32      | Number of training cases over which each stochastic gradient descent (SGD) update                                                                                               |
| replay memory size              | 1000000 | SGD updates are sampled from this number of most recent frames                                                                                                                  |
| agent history length            |         | The number of most recent frames experienced by the agent that are given as input to the Q network                                                                              |
| target network update frequency | 10000   | The frequency (measured in the number of parameter updates) with which the target network is updated (this corresponds to the parameter C from Algorithm 1)                     |
| discount factor                 | 0.99    |                                                                                                                                                                                 |
| action repeat                   |         | Repeat each action selected by the agent this many times a value of 4 results in the agent seeing only every 4th input frame Using                                              |
| update frequency                |         | The number of actions selected by the agent between successive SGD updates\_ a value of 4 results in the agent selecting 4 actions between each of successive updates Using pair |
| learning rate                   | 0.00025 | The learning rate used by RMSProp                                                                                                                                               |
| gradient momentum               | 0.95    |                                                                                                                                                                                 |
| squared gradient momentum       | 0.95    | Squared gradient (denominator) momentum used by RMSProp.                                                                                                                        |
| min squared gradient            | 0.01    | Constant added to the squared gradient in the denominator of the RMSProp update                                                                                                 |
| initial exploration             |         | Initial value of € in €-greedy exploration                                                                                                                                      |
| final exploration               | 0.1     | Final value of € in €-greedy exploration;                                                                                                                                       |
| final exploration frame         | 1000000 | The number of frames over which the initial value of € is linearly annealed to its final value                                                                                  |
| replay start size               |         | resulting experience is used to populate the replay memory.                                                                                                                     |
| no-op max                       | 30      | Maximum number of "do nothing" actions to be performed by the agent at the start of                                                                                             |

an episode

Thevalues otallthe hyperparameters were selected by performing an informal search on the games search owing to the high corputational cost, although it is conceivable that even better results could be obtained by systematically tuning the hyperparameter values Pong'

Extended Data Table 2 | Comparison of games scores obtained by DQN agents with methods from the literature12.15 and professional human games tester

<!-- image -->

| Game                | Random Play   | Best Linear Learner   | Contingency (SARSA)   | Human   | DQN (+ std)     | Normalized DQN (% Human)   |
|---------------------|---------------|-----------------------|-----------------------|---------|-----------------|----------------------------|
| Alien               | 227.8         | 939.2                 | 103.2                 | 6875    | 3069 (+1093)    |                            |
| Amidar              | 5.8           | 103.4                 | 183.6                 | 167     | 739.5 (+3024)   | 43.99                      |
| Assault             |               | 628                   | 537                   | 1496    | 3359(+775)      | 246.2%                     |
| Asterix             | 210           | 987.3                 | 1332                  | 8503    | 6012 (+1744)    |                            |
| Asteroids           |               | 907.3                 | 89                    | 13157   |                 | 7.39                       |
| Atlantis            | 12850         | 62687                 | 852.9                 | 29028   | 85641(+17600)   | 449.99                     |
| Bank Heist          | 14.2          | 190.8                 | 67.4                  | 734.4   | 429.7 (+650)    |                            |
| Battle Zone         | 2360          | 15820                 | 16.2                  | 37800   | 26300 (+7725)   | 67.69                      |
| Beam Rider          | 363.9         | 929.4                 | 1743                  | 5775    | 6846 (+1619)    | 119.89                     |
| Bowling             | 23.1          | 43.9                  | 36.4                  | 154.8   | 42.4 (+88)      |                            |
| Boxing              | 0.1           | 44                    | 9.8                   | 4.3     | 71.8 (+8.4)     | 1707.99                    |
| Breakout            | 1.7           | 5.2                   | 6.1                   |         | 401.2 (+26.9)   | 1327.29                    |
| Centipede           | 2091          | 8803                  | 4647                  | 11963   | 8309(+5237)     | 63.09                      |
| Chopper Command     | 811           | 1582                  | 16.9                  | 9882    | 6687 (+2916)    | 64.89                      |
| Crazy Climber       | 10781         | 23411                 | 149.8                 | 35411   | 114103 (+22797) | 419.5%                     |
| Demon Attack        | 152.1         | 520.5                 |                       | 3401    | 9711 (+2406)    |                            |
| Double Dunk         |               |                       | 416                   |         |                 | 17.1%                      |
| Enduro              |               | 129.1                 | 159.4                 |         | 301.8 (+24.6)   | 97.59                      |
| Fishing Derby       |               |                       |                       | 5.5     | 0.8 (+19.0)     |                            |
| Freeway             |               | 19.1                  | 19.7                  | 29.6    | 30.3 (+0.7)     | 102.4%                     |
| Frostbite           | 65.2          | 216.9                 | 180.9                 | 4335    | 328.3 (+250.5)  | 6.29                       |
| Gopher              | 257.6         |                       | 2368                  | 2321    | 8520 (+3279)    | 400.4%                     |
| Gravitar            | 173           | 387.7                 | 429                   | 2672    | 306.7 (+223.9)  | 5.39                       |
| HER.O               | 1027          | 6459                  | 7295                  | 25763   | 19950 (+158)    | 76.59                      |
| Ice Hockey          | 411.2         | 9.5                   |                       | 0.9     |                 | 79.39                      |
| James Bond          | 29            | 202.8                 | 354.1                 | 406.7   |                 | 145.09                     |
| Kangaroo            | 52            | 1622                  | 8.8                   |         | 6740 (+2959)    |                            |
| Krull               | 1598          | 3372                  | 3341                  | 2395    | 3805 (+1033)    | 277.09                     |
| Kung-Fu Master      | 258.5         | 19544                 | 29151                 | 22736   | 23270 (+5955)   | 102.4%                     |
| Montezuma's Revenge |               | 10.7                  | 259                   | 4367    | 0 (+0)          | 0.09                       |
| Ms. Pacman          | 307.3         | 1692                  | 1227                  | 15693   |                 | 13.09                      |
| Name This Game      | 2292          | 2500                  | 2247                  | 4076    | 7257 (+547)     | 278.39                     |
| Pong                |               |                       |                       | 9.3     | 18.9 (+1.3)     |                            |
| Private Eye         | 24.9          | 684.3                 | 86                    | 69571   | 1788 (+5473)    | 2.59                       |
|                     | 163.9         | 613.5                 | 960.3                 | 13455   | 10596 (+3294)   | 78.59                      |
| River Raid          | 1339          | 1904                  | 2650                  | 13513   | 8316 (+1049)    |                            |
| Road Runner         | 11.5          | 67.7                  |                       | 7845    | 18257 (+4268)   |                            |
| Robotank            | 2.2           | 28.7                  |                       | 11.9    | 51.6 (+4.7)     | 509.09                     |
| Seaquest            | 68.4          | 664.8                 | 675.5                 | 20182   | 5286(+1310)     | 25.99                      |
| Space Invaders      | 148           | 250.1                 | 267.9                 | 1652    | 1976 (+893)     |                            |
| Star Gunner         | 664           | 1070                  |                       | 10250   | 57997 (+3152)   | 598.1%                     |
| Tennis              |               | 0.1                   |                       |         | 25 (+1.9)       | 143.29                     |
| Time Pilot          | 3568          | 3741                  | 24.9                  | 5925    |                 | 100.99                     |
| Tutankham           | 11.4          | 114.3                 | 98.2                  | 167.6   | 186.7 (+41.9)   | 112.29                     |
| Up and Down         | 533.4         |                       | 2449                  | 9082    | 8456 (+3162)    | 92.7%                      |
| Venture             |               | 66                    | 0.6                   | 1188    | 3800 (+238.6)   | 32.09                      |
| Video Pinball       |               | 16871                 | 19761                 | 17298   | 42684 (+16287)  | 2539.49                    |
| Wizard of Wor       | 563.5         |                       |                       |         |                 |                            |
|                     |               | 1981                  | 36.9                  | 4757    |                 | 67.59                      |
| Zaxxon              | 32.5          | 3365                  | 21.4                  | 9173    | 4977 (+1235)    | 54.1%                      |

Best Linear Learner is the best result obtained by a linear function approximator on different types of hand designed features 2. Contingency (SARSA) agent figures are the results obtained in ref: 15. Note the randorn play score) (hurnan score

<!-- image -->

## Extended Data Table 3 The effects of replay and separating the target Q-network

| Game           |   With replay, with target Q | With replay, without target Q   |   Without replay; with target Q |   Without replay, without target Q |
|----------------|------------------------------|---------------------------------|---------------------------------|------------------------------------|
| Breakout       |                        316.8 | 240.7                           |                            10.2 |                                3.2 |
| Enduro         |                       1006.3 | 831.4                           |                           141.9 |                               29.1 |
| River Raid     |                       7446.6 | 4102.8                          |                          2867.7 |                             1453   |
| Seaquest       |                       2894.4 |                                 |                          1003   |                              275.8 |
| Space Invaders |                       1088.9 | 826.3                           |                           373.2 |                              302   |

network; and three ditferent learning Extended Data Table 2 (5Omillion trames) 0

Comparison of DQN performance with linear function approximator

| Game           |    DQN | Linear   |
|----------------|--------|----------|
| Breakout       |  316.8 | 3.00     |
| Enduro         | 1006.3 |          |
| River Raid     | 7446.6 | 2346.9   |
| Seaquest       | 2894.4 | 656.9    |
| Space Invaders | 1088.9 | 301.3    |

The performance of the DQN agent is compared with the performance of alinear function approximator on the 5 validation games (that is, where a single linear layer was used instead of the convolutional reported Note that these evaluation episodes were not truncated at 5 min leading to higher scores on Enduro than the ones reported In Extended Data Table 2 Note also that the number of training frames shorter (1Omillion frames) as compared to the main results presented in Extended Data Table 2 (50million frames)

<!-- image -->