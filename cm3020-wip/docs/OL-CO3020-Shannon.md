## Online library: digital copies

## Copyright Notice

Staff and students of the University of London are reminded that copyright subsists in this extract and the work from which it was taken. This Digital Copy has been made under the terms of a CLA licence which allows Course Users to:

- · access and download a copy;
- · print out a copy.

This Digital Copy and any digital or printed copy supplied under the terms of this Licence are for use in connection with this Course of Study. They should not be downloaded or printed by anyone other than a student enrolled on the named course.

All copies (including electronic copies) shall include this Copyright Notice and shall be destroyed and/or deleted if and when required by the University.

Except as provided for by copyright law, no further copying, storage or distribution (including by e-mail) is permitted without the consent of the copyright holder.

The author (which term includes artists and other visual creators) has moral rights in the work and neither staff nor students may cause, or permit, the distortion, mutilation or other modification of the work, or any other derogatory treatment of it, which would be prejudicial to the honour or reputation of the author.

Name of Designated Person authorising scanning:

Publishing Manager, University of London Worldwide

Course of study:

Extract title:

Title author:

CM3020

Programming a Computer for Playing Chess

Shannon, C

Publication year, Volume, Issue:

Page extent:

Source title:

ISBN:

1950, 41(4)

256-275

Philosophical magazine

0031-8086

<!-- image -->

XXII. Programming  a  Computer  for  Playing  Chess *.

## By CLAUDE  E.  SHANNON, Bell Telephone Laboratories, Inc., Murray Hill, N.J. t

## [Received November 8,  1949.J

## 1. INTRODUCTION.

THIS  paper is  concerned wtth the problem of constructing a  computing routine  or  "  program "  for  a  modern  general  purpose  computer  which will enable it to play chess.  Although perhaps of no practical importance, the question is  of theoretical interest, and it is  hoped that a  satisfactory solution of this problem will  act as a  wedge in attacking other problems of a  similar nature and of greater significance.  Some possibilities in this direction  are :-

- ( l)  Machines for  designing filters,  equalizers,  etc.
- (2) Machines for  designing  relay and switching  circuits.
- (3) Machines  which  will  handle  routing  of telephone  calls  based  on the individual circumstances rather than by fixed patterns.
- (4) Machines  for  performing  symbolic  (non-numerical)  mathematical operations.
- (5) Machines capable of translating from one language to another.
- (6) Machines  for  making  strategic  decisions  in  simplified  military 'operations.
- (7)  Machines capable of orchestrating a melody.
- (8) Machines capable of logical deduction.
- It is  believed that  all  of these  and  many other  devices  of a  similar nature are possible developments in the immediate future.  The techniques developed for  modern electronic  and relay type  computers  make them not only theoretical possibilities,  but in several  cases  worthy of serious consideration from the economic point of view.

Machines of this general type are an extension over the ordinary use· of numerical computers in several ways.  First, the entities dealt with are not primarily numbers, but rather chess positions, circuits, mathematical expressions,  words,  etc. Second,  the proper procedure involves general principles,  something  of the nature of judgment, and considerable trial and error, rather than a  strict, unalterable  computing process. Finally, the solutions of these problems are not merely right or wrong but have a  continuous range of "  quality "  from the best down to the worst.  We might be satisfied with a  machine that designed good filters even though they were not always the best possible.

- *  First  presented  at  the  National  IRE  Convention,  March  9,  1949,  New York,  U.S.A.
- t Communicated by the Author.

## XXII. Programming  a  Computer  for  Playing  Chess *.

## By CLAUDE  E.  SHANNON, Bell Telephone Laboratories, Inc., Murray Hill, N.J. t

## [Received November 8,  1949.]

## 1. INTRODUCTION.

Tms paper is  concerned with the problem of constructing a  computing routine  or  "  program "  for  a  modern  general  purpose  computer  which will enable it to play chess.  Although perhaps of no practical importance, the question is  of theoretical interest, and it is hoped that a  satisfactory solution of this problem will  act as a  wedge in attacking other problems of a  similar nature and of greater significance.  Some possibilities in this direction  are :-

- ( l)  Machines for  designing filters,  equalizers, etc.
- (2) Machines for  designing  relay and switching  circuits.
- (3) Machines  which  will  handle  routing  of telephone  calls  based  on the individual circumstances rather than by fixed patterns.
- (4) Machines  for  performing  symbolic  (non-numerical)  mathematical operations.
- (5) Machines capable of translating from one language to another.
- (6) Machines  for  making  strategic  decisions  in  simplified  military , operations.
- (7)  Machines capable of orchestrating a melody.
- (8) Machines capable of logical deduction.

It is  believed that all  of these  and  many other  devices  of a  similar· nature are possible developments in the immediate future.  The techniques developed for  modern electronic  and relay type  computers  make them not only theoretical possibilities,  but in several  cases  worthy of serious consideration from the economic point of view.

Machines of this general type are an extension over the ordinary use of numerical computers in several ways.  First, the entities dealt with are not primarily numbers, but rather chess positions, circuits, mathematical expressions,  words,  etc. Second,  the proper procedure involves  general principles,  something  of the nature of judgment, and considerable trial and error, rather than a  strict, unalterable  computing process. Finally,. the solutions of these problems are not merely right or wrong but have a  continuous range of" quality" from the best down to the worst.  We might be satisfied with a  machine that designed good filters even though. they were not always the best possible.

- *  First  presented  at  the  National  IRE  Convention,  March  9,  1949,  New· York,  U.S.A.
- t Communicated by the Author.

The chess machine is an ideal one to start with, since:  (1)  the problem is sharply  defined  both  in  allowed  operations  (the  moves)  and  in  the ultimate goal  (checkmate) ;  (2)  it is  neither  so  simple  as  to  be trivial nor t oo  difficult  for  satisfactory  solution; (3)  chess  is  generally  con­ sidered to require "  thinking " for skilful play ;  a  solution of this problem. will force  us  either to admit  the  possibility  of mechanized  thinking  or to further restrict our concept of "  thinking ";  (4)  the discret e structure of chess fits well into the digital nature of modern computers.

There  is  already  a  considerabM  literature  on  the  subject  of  chess­ playing  machines. During the  late  18th and early  19th centuries,  t he Maelzel  Chess  Automaton,  a  device  invented  by von  Kempelen,  was. exhibited widely as a chess-playing machine.  A number of papers appeared at the time, including an analytical essay by Edgar Allan  Poe  (entitled Maelzel's  Chess  Player)  purporting  to  explain  its  operation. Most  of these  writers  concluded,  quite  correctly,  t hat  the  Automaton  was operated by  a  concealed human chess-master ;  the arguments leading to this  conclusion,  however,  were  frequently  fallacious. Poe assumes,  for example,  that it is  as  easy to  design  a  machine  which  will  invariably win as one which wins occasionally, and argues that since the Automaton was  not invincible  it was  therefore  operated  by a  human,  a  clear non sequitur. For a  complete account of the history and method of operation of the Automaton, the reader is referred to a series of articles by Harkness. and Battell in Chess  Review, 1947.

A  more  honest  attempt to design  a  chess-playing  machine was  made in  191 4  by Torres  y  Quevedo,  who  constructed a  device  which  played an end game of king and rook against king (Vigneron, 1914).  The machine played  the side with king and rook and would force  checkmate in a few moves  however  its  human  opponent  played. Since  an  explicit  set  of rules  can be given for making satisfactory moves in such an end game,. the  problem  is  relatively  simple,  but the  idea  was  quite  advanced  for that period.

The thesis we will  develop is  that modern general purpose computers can be used to play a tolerably good game of chess by the use of a suitable computing  routine  or  "  program ". While  the  approach  given  here  is believed  fundamentally  sound,  it  will  be  evident  that  much  further­ experimental and theoretical work remains to be done.

## 2.  GENERAL  CoNSIDERA'IIO-"S.

A chess "  position "  may be defined to include the following data :­

- ( 1)  A  statement of the positions of all pieces on the board.
- (2 )  A  statement of which side, White or Black, has the move.
- (3 )  A  statement as to whether the kings and rooks have moved.  This. is important since by moving a  rook, for example, the right to castle on that  side  is  forfeited.

- (4)  A  statement of,  say,  the last move. This will  determine whether a  possible en passant capture is legal, since this privilege is forfeited after one move.
- (5)  A  statement  of the  number  of moves  made  since  the  last  pawn move or capture.  This is important because of the 50 move drawing rule. For simplicity,  we  will  ignore the rule of draw after three repetitions of .a position.

In  chess  there  is  no  chance  element  a part  from  the  original  choice of which player has the first mote.  This is in contrast with card games, backgammon, etc.  Furthermore, in chess each of the two opponents has ~'  perfect information "  at each move as to all previous moves (in contrast with Kriegspiel, for example). These two facts imply (von Neumann and Morgenstern,  1944)  that any given position of the chess  pieces  must be ·either:-

- ( 1) A won position for White.  That is, White can force a  win, however Black defends.
- (2)  A  draw position.  White can force at least a  draw, however Black plays, and likewise Black can force at least a  draw, however White plays. If both sides play correctly the game will end in a  draw.
- (3)  A  won position for Black.  Black can force  a  win,  however White plays.

This is,  for  practical purposes,  of the nature of an existence theorem. No  r\_,xactical  method  is  known  for  determining  to  which  of the  three categories  a  general  position  belongs. If there  were  chess  would  lose most of its interest as a ,game.  One could determine whether the initial position is  won,  drawn,  or  lost for  White and the  outcome  of a  game between  opponents knowing the method would  be fully  determined at the  choice  of the first  move. Supposing the initial position a  draw (as suggested by empirical evidence from master games*) every game would end in a  draw.

It is interesting that a  slight change in the rules of chess gives a  game for  which it  is  provable  that  White  has  at least  a  draw in  the  initial position. Suppose the rules  the  same as  those  of chess  except  that  a player is  not forced to move a  piece at his turn to play, but may, if he chooses,  "  pass ".  Then we  can prove as a  theorem that White can at least  draw by proper play.  For in the initial  position either he has  a winning move or not. If so,  let  him  make this move. If not, let him pass.  Black is now faced with essentially the same position that White had  before,  because  of the  mirror  symmetry  of the initial  position t­ Since White had no winning move before, Black has none now.  Hence, B~ack at best can draw.  Therefore, in either case White can at least draw.

- *  The world championship match between Capablanca and Alekhine ended with the score Alekhine 6,  Capablanca 3,  drawn 25.
- t The  fact  that  the  number  of moves  remaining  before  a  draw  is  called by the 50-move rule has decreased does not affect this argument.

In some  games  there  is  a  simple evaluation function  f (P)  which  can be  applied to a  position P  and whose value determines to which category ,(won,  lost, etc.) the position P  belongs. In the game of Nim (Hardy and Wright, 1938), for example, this can be determined by writing the number .of matches in each pile in binary notation.  These numbers are arranged in a column (as though to add them).  If the number of ones in each column is even, the position is lost for the player about to move, otherwise won.

If such an evaluation functionf(P) can be found for a game it is easy to .design  a  machine capable of perfect play.  It would never lose  or draw .a  won position and never lose a  draw.n  position and if the opponent ever made a  mistake the  machine  would  capitalize  on  it. This  could  be ,clone  as follows .:  Suppose

f(P)= 1 for a  won position,

f(P)=0 for a  drawn position,

f(P ) =  -1 for a  lost position.

At the machine's turn to move it calculates f (P) for the various positions ,obtained from the present position  by each possible  move that  can be m::1de. It chooses  that move  (or  one  of the  set)  giving  the  maximum value  to f. In the case  of Nim where such a  function f(P) is  known,  a machine has actually been constructed which plays a  perfect game *.

With chess it is possible, in principle, to play a perfect game or construct a  machine  to  do  so  as  follows :  One  considers  in a  given  position  all possible moves, then all moves for the opponent, etc., to the end of the game (in each variation).  The end must occur, by the rules of the game, after a  finite number of movest (remembering the 50 move drawing rule) . .Each of these variations ends in win, loss or draw.  By working backward from  the  end  one  can  determine  whether  there  is  a  forced  win,  the position is a  draw or is lost. It is easy to show, however, that even with the high computing speeds  available in electronic  calculators this  com­ putation is  impractical.  In typical  chess  positions there will  be  of the order of 30 legal moves.  The number holds fairly constant until the game is nearly finished  as shown in Fig. I.  This graph was  constructed from data  given by De Groot, who  averaged the number of legal moves in a large  number of master games  (De  Groot,  1946, a). Thus a  move for White and then one for  Black gives  about  10 3 possibilities. A  typical game  lasts  about  40  moves  to  resignation  of one  party. This  is  con­ servative for  our  calculation since  the  machine  should  calculate  out to checkmate, not resignation.  However,  even at this figure  there will  be

- * Condon,  Tawney  and  Derr,  U.S.  Patent  2,215,544. The  " Nimotron " based  on  this  patent  was  built  and  exhibited  by Westinghouse  at the  1938 New  York  World's Fair.
- t  The longest possible chess game is 6350 moves, allowing 50 moves between each  pawn move or capture.  The longest toun;iament game on record between masters lasted  168  moves,  and the  shortest  four  moves. (Chernev, Curioiis Chess Fact.s, The Black Knight Press, 1937.)

10 120 variations to  be  calculated from  the initial  position. A  machine­ operating  at  the  rate  of  one  variation  per  micro-microsecond  would require over 10 90 years to calculate its first move!

Another  (equally impractical)  method is  to  have  a  "  dictionary" of all possible positions of the chess pieces.  For each possible position there is  an  entry  giving  the  correct  move  (either  calculated  by  the  above process or supplied by a  chess master).  At the machine's turn to move it  merely  looks  up  the  position  and  makes  the  indicated  move. The number of possible positions, of the general order of 64  l I 32  ! 8 ! 2 2 ! 6 , or roughly  10 4 3, naturally makes such a  design  unfeasible.

It is  clear  then that the problem is  not that of designing  a  machine to play perfect chess  (which is  quite impractical) nor one  which merely plays legal  chess  (which  is  trivial). We would like it to play a  skilful game, perhaps comparable to that of a  good human player.

A strategy for chess may be described as a  process for choosing a  move in any given position.  If the process  always chooses the same move in.

Fig.  l.

<!-- image -->

th " e  same pure "  s po tra sition tegy. the strategy is  known  in  the  theory  of games  as  a If the process involves statistical elements and does not  always  result  in  the  same  choice  it is  a  "  mixed "  strategy. The following are simple examples of strategies :-

- ( l )  Number the possible  legal  moves  in  the  position  P,  according to some standard procedure.  Choose  the first  on the list. This  is  a  pure strategy.
- (2)  Number the legal moves and choose one at random from the list .. This is a  mixed strat egy.

Both  of these,  of  course,  are  extremely  poor  strat egies,  making  no attempt to select good moves.  Our problem is to develop a tolerably good strategy for selecting the move to be made.

## 3.  APPROXIMATE  EVALUATING  FUNCTIONS.

Although  in  chess  there  is  no  known  simple  and  exact  evaluating function f(P ), and probably never will  be  because  of the arbitrary and .complicated nature of the rules of the game, it is still possible to perform .an  approximate evaluation of a  position.  Any good chess  player must, in fact,  be  able to perform such a  position evaluation.  Evaluations are based  on the general structure of the.position, the number and kind of Black and White pieces, pawn formation, mobility, etc.  These evaluations are not perfect,  but the stronger the player the  better his  evaluations. Most · of  the maxims and principles  of correct play are really assertions .about evaluating positions, for example :-

- (1) The relative values  of queen,  rook,  bishop,  knight  and pawn are about 9,  5,  3,  3,  1,  respectively.  Thus other things being equal (!) if we add the  numbers of pieces for the two sides with these coefficients,  the .side  with the largest total has the better position.
- (2)  Rooks  should  be  placed  on  open  files. This  is  part  of a  more general  principle  that  the  side  with  the  greater  mobility,  other things equal, has the better game.
- (3) Backward, isolated and doubled pawns are weak.
- (4) An exposed king is a  weakness (until the end game).

These  and  similar  principles  are  only  generalizations  from  empirical evidence of numerous games, and only have a kind of statistical validity. Probably any chess principle can be  contradicted by particular counter ,examples. However,  from  these  principles  one  can  construct  a  crude evaluation function.  The following is an example :-'

.f(P)=200(K-K')+9(Q-Q')+5(R-R')+3(B-B'+N-N')+(P-P') -·5(D-D'+S-S'+I-I')+·l(M-M')+ .. ·

in  which:-

K, Q, R, B, N, Pare the number of White kings, queens, rooks, bishops, knights and pawns on the board.

- D,  S,  I  are doubled,  backward and isolated White pawns.

M= White  mobility  (measured,  say,  as  the  number  of  legal  moves available  to  White).

Primed letters are the similar quantities for Black.

The  coefficients  ·5  and  · l  are  merely  the  writer's rough  estimate. Furthermore, there  are  many  other  terms  that  should  be  included *. The formula is given only for illustrative purposes.  Checkmate has been artificially included here by giving the king the large value 200  (anything greater than the maximum of all other terms would do).

It may be  noted that this  approximate  evaluation f(P) has  a  more ·Or less continuous range of possible values, while with an exact evaluation there are only three possible values.  This is as it should be.  In practical

play a  position may be  an  "  easy win "  if a  player is,  for  example,  a queen ahead,  or a  very difficult  will' with only a  pawn advantage. In the former  case  there are  many ways to win  while  in the latter exact play  is  required,  and  a  single  mistake  often  destroys  the  advantage .. The unlimited intellects  assumed in the theory of games,  on the other hand,  never make a  mistake and the smallest winning advantage is  as good as mate in one.  A  game between two such mental giants,  Mr.  A and Mr. B, would proceed as follows.  They sit down at the chessboard,. draw for colours, and then survey the piecef for a moment.  Then either

- (1)  Mr.  A  says,  "I resign" or
- (2)  Mr.  B  says,  " I  resign "  or
- (3 ) Mr: A says,  "I offer  a  draw,"  and Mr.  B  replies,  "I accept."

## 4.  STRATEGY  BASED  ON  AN  EVALUATION  FUNCTION.

A  very important point about the simple type of evaluation function given  above  (and general  principles  of chess)  is  that they can  only  be applied in relatively quiescent  positions. For example,  in an exchange of queens White plays, say, Q x Q ( x =captures) and Black will  reply· P X Q. It would be absurd to calculate the function f(P) after Q X Q while  White is,  for  a  moment,  a  queen  ahead,  since  Black will  imme­ diately  recover  it. More  generally  it  is  meaningless  to  calculate  an. evaluation of the general type given above during the course of a  com-­ bination or a  series  of exchanges.

More terms 'could be added to f(P) to account for exchanges in progress,. but it appears that combinations,  and forced  variations in general,  are better accounted for  by examination of specific  variations. This is,  in fact,  the  way chess  players  calculate. A  certain number of variations. are investigated m0ve  by move until a  more or less  quiescent  position is reached and at this point something of the nature of an evaluation is. applied  to  the  resulting  position. The  player  chooses  the  variation leading to the highest evaluation for him when the opponent is assumed to be playing to reduce this evaluation.

The process  can  be  described  mathematically. We omit at first  the fact that f(P) should only be applied in quiescent positions.  A  strategy· of play  based  on f (P)  and operating one  move  deep  is  the  following. Let M 1 , M 2 , M 3 , ... , M 8 be the moves that can be made in position P and let M 1 P, M 2 P, etc.  denote symbolically the resulting positions when M1,  M2,  etc. are applied to P.  Then one chooses the Mm which maximizes f(MmP).

A  deeper  strategy  would  consider  the  opponent's  replies. Let  Mil, M;2 , ·· · , M; 8 be  the possible  answers  by Black, if White chooses  move M;, Black should play to minimize f(P). Furthermore, his choice occurs. after White's move. Thus, if White plays M;  Black may be assumed to­ play the M; 1 such that

is  a minimum. White should play his first move such that f is a  maximum after  Black  chooses  his  best  reply. Therefore,  White  should  play  to maximize on Mi the quantity

min f(MijMiP).

## Mij

The mathematical process involved is shown for a simple case in Fig. 2. The  point  at  the  left  represents  the  position  being  considered. It is assumed  that  there  are  three  possible  moves  for  White,  indicated  by the three solid lines,  and if any of .these is  made there are three possible moves for  Black,  indicated by the dashed lines. The possible  positions after a  White and Black move are then the nine points on the right, and the  numbers are the evaluations for these positions.  Minimizing on the upper three gives  +·l which is the resulting value if White chooses the-

<!-- image -->

upper  variation  and  Black replies  with  his  best  move. Similarly,  the­ second and third moves lead to values of -7 and -6.  Maximizing on White's move, we obtain +·l with the upper move as White's best choice.

In a similar way a two-move strategy (based on considering all variations out to 2 moves) is given by

Max Min  Max Min f(~jkl M;jk  M;j M;  P)

## M; Mij Mijk  Mijkl

.

(1)

The order of maximizing and minimizing this function is important.  It derives from the fact that the choices of moves occur in a definite order.

A  machine  operating  on  this  strategy  at the  two-move  level  would first  calculate  all  variations  out  to  two  moves  (for  each  side)  and the resulting positions.  The evaluations j(P) are calculated for each of these positions.  Fixing all but the last Black move, this last is varied and the move chosen which minimizes f. This is  Black's assumed last move in

the  variation  in  question. Another  move  for  White's second  move  is chosen and the process repeated for Black's second move.  This is  done for each second White move and the one chosen giving the largest final J (after  Black's best  assumed reply in each  case). In this  way  White's .second  move in each variation is  determined. Continuing  in this  way the machine works back to the present position and the best first White move.  This move is then played.  This process generalizes in the obvious way for any number of moves.

A strategy of this sort, in which all variations are considered out to a -definite number of moves and the ·move then determined from a  formula such as  (1)  will  be  called  a  type A  strategy. The type A  strategy has certain basic weaknesses, which we will discuss later, but is conceptually simple,  and we  will  first  show how a  computer can be programmed for such  a  strategy.

## 5. PROGRAMMING  A  GENERAL  PURPOSE  COMPUTER  FOR  A TYPE A STRATEGY.

We assume a  large-scale  digital computer, indicated schematically in :Fig.  3,  with the following  properties:-

Fig. 3.

<!-- image -->

- (1)  There is a large internal memory for storing numbers.  The memory is divided into a number of boxes each capable of holding, say, a ten-digit number.  Each box is assigned a" box number".
- (2)  There  is  an  arithmetic  organ  which  can  perform  the  elementary ·operations of addition, multiplication, etc.
- (3)  The  computer  operates  under  the  control  of  a  " program " . The  program  consists  of  a  sequence  of  elementary  " orders ". A typical  order is  A 372,  451,  133. This  means,  extract  the  contents  of box 372 and of box 451, add these numbers, and put the sum in box 133. Ano'ther type of order involves a  decision,  for example,  C 291,  118,  345. This tells the machine to compare the contents of box 291  and 118.  If 'the first is  larger the machine goes on to the next order in the program. If not, it takes its next order from box 345.  This type of order enables the  machine  to  choose  from  alternative  procedures,  depending  on  the results of previous  calculations.  It is  assumed that orders are available for  transferring  numbers,  the  arithmetic  operations,  and decisions.

Our  problem  is  to  represent  chess  as  numbers  and  operations  on numbers,  and  to  reduce  the  strategy  decided  upon  to  a  sequence  of computer orders.  We will  not carry this out in detail but only outline the  programs. As  a colleague  puts  it,  the  final  program  for  a computer must be written in words of one microsyllable.

The  rather  Procrustean  tactics  of forcing  chess  into  an  arithmetic computer are  dictated  by economic  considerations. Ideally,  we  would like  to  design  a  special  computer for  ch~ss  containing,  in place  of the arithmetic organ,  a  " chess  organ "  specifically designed to perform the simple  chess  calculations. Although  a  large  improvement  in  speed  of operation would undoubtedly result, the initial cost of computers seems to prohibit such a  possibility.  It is planned, however, to experiment with a simple  strategy  on  one  of  the  numerical  computers  now  being -constructed.

Fig. 4.

## BLACK

|   70 | 71    |   72 | 73   |   74 |   75 |   76 |   77 |
|------|-------|------|------|------|------|------|------|
|   60 | 61    |   62 | 63   |   64 |   65 |   66 |   67 |
|   50 | 51    |   52 | 53   |   54 |   55 |   56 |   57 |
|   40 | '  41 |   42 | 43   |   44 |   45 |   46 |   47 |
|   30 | 31    |   32 | ~    |   34 |   35 |   36 |   37 |
|   20 | 21    |   22 | 23   |   24 |   25 |   26 |   27 |
|   10 | II    |   12 | 13   |   14 |   15 |   16 |   17 |
|   00 | 01    |   02 | 03   |   04 |   05 |   06 |   07 |

WHITE

I

2

3

4

5

6

BLACK  -I

-2  -3  -4  -5  -6

0  = EMPTY SQUARE

## CODE  FOR  MOVE

(OLD SQUARE, NEW SQUARE, NEW PIECE (IF PROMOTION))

P  K4-( 14,  34,-) P  K8(Q)(64,  74, 5)

WH ITE

A  game  of chess  can  be  divided into three  phases,  the  opening,  the middle  game,  and  the  end  ga.me. Different  principles  of play  apply in the different phases.  In the opening, which generally lasts for about ten  moves,  development  of the  pieces  to  good  positions  is  the  main objective. During the middle game tactics  and combinations are pre­ dominant. This  phase  lasts  until  most  of the  pieces  are  exchanged, leaving only kings,  pawns and perhaps one or two pieces  on each side. The end game is mainly concerned with pawn promotion.  Exact timing and such possibilities as" Zugzwang ", stalemate, etc. become important.

Due  to  the  difference  in  strategic  aims,  different  programs  should be used for the different phases of a  game.  We will be chiefly concerned with the middle game and will not consider the end game at all.  There seems no reason, however, why an end game strategy cannot be designed and programmed equally well. ·

## CODE  FOR  PIECES

P

N

B

R

Q

K

A square on a  chessboard can be occupied in 13  different ways:  either it is  empty (0) or  occupied  by one  of  the six  possible  kinds  of White pieces  (P=l, N=2, B=3, R=4, Q=5, K=6) or one of the six possible Black pieces (P=-1, N=-2, ... , K=-6).  Thus, the state of a  square is specified by giving an integer from  -6 to +6.  The 64  squares can be numbered according to a  co-ordinate  system as  shown in Fig. 4. The position  of all  pieces  is  then given  by a  sequence  of 64  numbers  each lying between - 6 and +  6.  A total of 256 bits (binary digits) is sufficient memory in this representation.  Although not the most efficient encoding, it  is  a  convenient  one for  calculation. One further  number A will  be +  1 or -1 according as it is White's or Blaclc's move.  A few more should be added for data relating to castling privileges  (whet her the White or Black  kings  and  rooks  have  moved),  and en  passant captures (e.g. , a statement of the last move). We will  neglect these,  however. In this notation the starting chess position is given by :-

4, 2, 3, 5, 6, 3, 2, 4· 1, 1, 1, 1, 1, 1, 1, l· ' ' 0, 0, 0, 0, 0, 0, 0, O· 0, 0, 0, 0, 0, 0, 0, O; ' 0, 0, 0, 0, 0, 0, 0, O· 0, 0, 0, 0, 0, 0, ,0 O; ' -1, -1, -1, -1, -1, -1, -1, -1; -4, -2, -3, -5, -6, -3, - 2,  - 4; +1 (=A). .

A. move (apart from castling and pawn promotion) can be specified by giving the original and final squares occupied by the moved piece.  Each of these squares is a  choice from 64, thus 6 binary digits each is sufficient, a  total of 12 for the move.  Thus the initial move P-K4 would be repre­ sented by 1,  4;  3,  4. To represent pawn promotion a set of three binary· digits can be added specifying the piece that the pawn becomes.  Castling is described by giving the king move (this being the only way the king can move two squares).  Thus, a  move is represented by (a,  b, c)  where a and b are squares and c specifies a  piece in case of promotion.

The complete  program  for  a  type  A  strategy  consists  of nine  sub­ programs  which  we  designate  T 0 ,  Ti,  ... , and  a  master  program T 8 T 9 . The basic functions of these programs are as follows :-

T0~  Makes move (a,  b, c)  in position P  to obtain the resulting position. T 1 -Makes a  list  of the possible  moves  of a  pawn at square (x,  y) in position P.

T 2 , ·.. ,  T 6 -Similarly for other types of pieces:  knight, bishop, rook, queen and king.

T 7 -Makes list of all possible moves in a  given position.

T 8 -Calculates the evaluating function f(P) for  a  given position P.

T 9 -Master program  ;  performs  maximizing  and minimizing  calculation to determine proper move.

With a  given position P  and a  move (a ,  b, c)  in the internal memory of the machine it can m\_ake  the move and obtain the resulting position by the following program T 0 .

- ( l) The square corresponding to number a in the position is  located \_ in the position memory.
- (2)  The number in this square x\_ is extracted and replaced by O (empty) ..
- (3) (a) If x=l, and the  first  co-ordinate of a is  6  (White pawn being promoted) or if x=-1, and the first  co-ordinate of a is  l  (Black pawn being promoted), the number c is  placed in square b (replacing whatever was there).
- (b) If x=6 and a-b=2 (White  castles,  king  side)  0  is  placed in squares 04 and 07 and 6 and 4 in squares 06 and 05, respectively.  Similarly for the cases x=6, b-a=2 (White castles, queen side) and x= -6, a- b= ± 2 (Black castles, king or queen side).
- (c)  In all other cases, x is placed in square b.
- ( 4) The sign of ,\  is  changed.

For each type of piece there is  a  program for  determining its possible moves. As  a  typical  example  the  bishop  program, T 3 , is  briefly  as follows. Let  (x, y) be the  co-ordinates  of the  square occupied  by the bishop.

- (1) Construct (x+l,  y+I) and read the contents u of this square in t he  posi~ion P.
- (2) If u=O (empty) list the move  (x, y), (x+l,  y+l) and start over with (x+2, y+2) instead of (x+l, y+I).

If ,\u is positive (own piece in the square) continue to 3.

- If ,\u is  negative  (opponent's piece  in the square)  list the  move  and'. continue to 3.
- If the square does not exist continue to 3.
- (3)  Construct (x+ 1, yl) and perform similar calculation.
- (4)  Similarly with (x-1, y+l).
- (5)  Similarly with (x-1, y-1).

By this  program  a  list  is  constructed  of  the  possible  moves  of  a bishop in a  given  position  P . Similar  programs  would list the moves of any  other  piece. There  is  considerable  scope  for  opportunism  in simplifying  these  programs; e. g. , the  queen  program, T 5 , can  be  a combination of the bishop and rook programs,  T 3 and T 4 ·

Using  the  piece  programs  T 1 .. · T 6 and  a  controlling  program. T 7 the machine  can construct a  list-of all possible  moves in any given position P . The controlling  program  T 7 is  briefly  as  follows  (omitting details):-

- (1) Start at square 1,1 and extract contents x.
- (2)  If ,\x is  positive  start  corresponding  piece  program Tx and when complete return to (1) adding 1 to square number. If ,\x is zero or negative, return to 1 adding 1 to square number.
- (3)  Test each of the listed moves for iegality and discard those which. are illegal. This is  done by making each of the moves in the position P · (by program T 0 ) and examining whether it leaves the king in check.  ,

With the  programs  T 0 ·.· T 7 it  is  possible  for  the  machine  to play legal  chess,  merely  making  a  randomly chosen  legal move at each turn to move.  The level of play with such a strategy is unbelievably bad.*  The writer  played a  few  games  against  this random strategy and was  able to checkmate generally in four or five  moves (by fool's mate, etc.).  The following game will illustrate the utter purposelessness of random play :-.

|      | White  (Random)   | Black      |
|------|-------------------|------------|
| (1)  | P-KN3             | P-K4       |
| (.2) | P-Q3              | B-B4       |
| (3)  | B~Q2              | Q-B3       |
| (4)  | N-QB3             | Q X  Pmate |

We  now  return  to  the  strategy  based  on  an  evaluation f(P). The program  T 8 performs  the  function  of evaluating  a  position  according to  the  agreed-upon f(P). This  can  be  done  by the  obvious  means  of .scanning the squares and adding the terms involved.  It is not difficult to .include terms such as doubled pawns, etc.

The final master  program T 9 is  needed to  select  the  move  according to  the  maximizing  and  minimizing  process  indicated  above. On  the ·basis of one m'ove (for each side) T 9 works as follows:-

- (1)  List the legal moves (by T 7 ) possible in the present position.
- (2)  Take the first in the list and make this move by T 0 , giving position M 1 P.
- (3)  List  the Black moves in M 1 P.
- (4)  Apply the first one giving M 11 M 1 P, and evaluate by T 8 .
- -(5) Apply the second Black move M 12 and evaluate.
- ,(6) Compare, and reject the move with the smaller evaluation.
- (7) Continue with the third Black move and compare with the retained value,  etc.
- (8)  When the Black moves are exhausted, one will be retained together with its evaluation.  The process is now repeated with the second White move.
- (9)  The final  evaluations from  these two  computations are compared and the maximum retained.
- (10)  This is continued with all White moves until the best is  selected (i. e. the one remaining after all are tried). This is the move to be made.
- *  Although  there is  a  finite  probability,  of the order of 1075 , that random play would win a game from Botvinnik.  Bad as random play is, there are even worse  strategies  which  choose  moves  which  actually aid the opponent. For example,  White's  strategy  in  the  following  game : 1. P- KB3,  P- K4. 2. P-K.1~4,  Q- R5  mate.

These programs are, of course, highly iterative. For that reason they· should not require a great deal of program memory if efficiently worked out .. The internal memory for positions and temporary results of calculations when playing three moves deep can be estimated . . Three positions should probably be remembered:  the initial position, the next to the last, and. the last  position  (now  being  evaluated). This  requires  some  800  bits. Furthermore,  there  are  five  lists  of  moves  each  requiring  about 30 x 12=360 bits,  a  total of 1800. Finally,  about 200  bits would cover the  selections  and  evaluations  up  to  the  present  calculation. Thus, some  3000  bits should suffice.

## 6.  IMPROVEMENTS  IN  THE  STRATEGY.

Unfortunately a  machine operating according to this type A  strategy would be both slow and a  weak player.  It would be slow since even if each  position were evaluated in one microsecond (very optimistic) there are about 10 9 evaluations to be made after three moves  (for  each side). Thus,  more than 16  minutes would be required for  a  move,  or 10  hours. for its half of a  40-move game.

It would be weak in playing skill because it is only seeing three moves deep and because we have not included any conditions about quiescent positions  for  evaluation. The  machine  is  operating  in  an  extremely inefficient fashion-it computes all variations to exactly three moves and then stops (even though it or the opponent be in check).  A good human player examines only a  few  selected variations and carries these out to a  reasonable stopping-point.  A  world champion can construct (at best) combinations  say,  15  or  20  moves  deep. Some  variations  given  by Alekhine  (" My  Best  Games  of Chess  1924-1937 " )  are  of this  length. Of course,  only  a  few  variations  are  explored to  any  such  depth. In a;mateur play variations are seldom examined more deeply than six or eight moves, and this only when the moves are of a  highly forcing nature (with very limited possible replies).  More generally, when there are few threats and forceful moves, most calculations are not deeper than one or two  moves,  with  perhaps  half-a-dozen  forcing · variations  explored  to· three,  four  or five  moves.

On this  point  a  quotation from  Reuben  Fine  (Fine  1942),  a  leading American master, is interesting:  "Very often people have the idea that masters foresee everything or nearly everything;  that when they played P-R3 on the thirteenth move they foresaw that this  would be  needed to provide a  loophole for the king after the complications twenty moves later,  or even that when they play 1 P-K4 they do it with the idea of preventing Kt-Q4 on Black's twelfth turn,  or they feel  that everything is  mathematically calculated down to the smirk when the Queen's Rook Pawn queens one move ahead of the opponent's King's Knight's Pawn. All  this is,  of course,  pure fantasy.  The best course to follow  is  to note­ the  major  consequences  for  two  moves,  but  try  to  work  out  forced variations as they go. ''

The  amount  of  selection  exercised  by  chess  masters  in  exammmg possible variations h'1s been studied experimentally by De Groot (1946, b). He showed  various typical  positions to  chess  masters  and asked them to decide on the best move, describing aloud their analyses of the positions . as they thought them through.  In this manner the number and depth of the variations examined could be determined.  Fig. 5 shows the result · of one such experiment.  In this case the chess master examined sixteen variations,  ranging  in  depth  from  1/2  (one  Black  move)  to  4-1/2  (five Black and four White) moves.  The to.tal number of positions considered ·was 44.

Fig.  5.

<!-- image -->

From these remarks it appears that to improve the speed and strength . of play the machine must :-

- ( l)  Examine  forceful  variations  out  as  far  as  possible  and  evaluate -only  at  reasonable  positions,  where  some  quasi-stability  has  been . established.
- Q2)  Select  the variations to  be  explored by some  process  so  that the machine does not waste its time in totally pointless variations.
- A strategy  with  these  two  improvements  will  be  called  a  type  B strategy.  It is  not  difficult  to  construct  programs  incorporating these features. For the  first  we  define  a  function g(P) of a  position  which determines  whether  approximate  stability  exists  (no  pieces en  prise, ·.etc.). A crude definition might be :

c. (P) = g

{

1 if any piece is attacked by a piece of lower value, or by more pieces  then defences  or if any check  exists  on a  square controlled by opponent.

o otherwise.

Using this function, variations could be explored until g(P)=O, always, ·however, going at least two moves and never more than say,  10.

The second improvement would require a  function h(P, M)  to  decide whether a  move Min position P  is worth exploring. It is important that this preliminary screening should not eliminate moves which merely look bad  at  first  sight,  for  example,  a mo\re which  puts  a  piece en  prise ; frequently such  moves  are  actually very strong  since  the  piece  cannot be  safely  taken.

"  Always  give  check,  it  may  be  mate "  is  tongue-in-cheek  advice given to beginners aimed at their predilection for useless checks.  "Always investigate a check, it may lead to mate" is sound advice for any player. A  check is  the most forceful type of move.  The opponent's replies  are highly  limited-he  can  never  answer  by  counter  attack,  for  example. This  means that a  variation starting with a  check can be  more readily calculated than any other.  Similarly captures, attacks on major pieces, threats of mate, etc. limit the opponent's replies and should be calculated whether the move looks good at first sight or not.  Hence, h(P, M)  should be given large values for all forceful moves (checks, captures and attacking moves),  for  developing  moves,  medium values for  defensive  moves,  and low values for other moves.  In exploring a  variation h(P, M)  would be calculated 'as  the  machine  computes  and would  be  used  to  select  the variations considered.  As it gets further into the variation the require­ ments  on h are  set  higher  so  that  fewer  and fewer  subvariations  are -examined.  Thus, it would start considering  every first  move for  itself, only the more forceful replies, etc.  By this process its computing efficiency would be greatly improved.

It is  believed  that  an  electronic  computer  incorporating  these  two improvements  in  the  program  would  play  a  fairly  strong  game,  at speeds  comparable to human speeds. It may be noted that a  machine has  several advantages  over humans :-

- ( l)  High-speed operation in individual calculations.
- (2)  Freedom from errors.  The only errors will  be due to deficiencies -of the  program  while  human  players  are  continually  guilty  of  very simple and obvious blunders.
- (3)  Freedom from  laziness. It is  all  too  easy for  a  human player to make instinctive moves  without proper analysis  of the position.
- (4)  Freedom from  "nerves". Human players are prone to  blunder -due  to  over-confidence  in  "won "  positions  or  defeatism  and  self­ recrimination in " lost "  positions.

These  must  be  balanced  against  the  flexibility,  imagination  and :inductive and learning capacities of the human mind.

Incidentally,  the  person  who  designs  the  program  can  calculate­ the move that the machine will  choose  in any position,  and thus in a sense  can  play  an  equally  good  game. In actual  fact,  however,  the calculation  would  be  impractical  because  of the time  required. On a fair  basis  of  comparison,  giving  the  machine  and  the  designer  equal time to decide on a move, the machine might well play a stronger game.

## 7.  VARIATIONS  IN  P¾AY  AND  IN  STYLE.

As described so far the machine once designed would always make the same move in the same position.  If the opponent made the same moves. this would always lead to the same game. It is  desirable to avoid this, since  if the  opponent  wins  one game he  could play the same  variation and win  continuously,  due  perhaps to  some  particular position  arising in the variation where the machine chooses a  very weak move.

One way to prevent this is to ha,ve a statistical element in the machine. Whenever there are two or more moves which are of nearly equal value according to the machine's calculations it chooses from them at random. In the same position a second time it may then choose another in the set.

The opening is  another place where statistical variation can be intro­ duced. It would  seem  desirable  to  have  a  number  of the  standard openings stored in a  slow-speed memory in the machine.  Perhaps a  few hundred would be satisfactory.  For the first few moves (until either the opponent ,deviates from the " book "  or the end of the stored variation is  reached)  the machine plays by memory.  This is  hardly "cheating " since  that is the way chess  masters play the opening.

It is interesting that the " style "  of play of the machine can be changed very  easily  by  altering  some  of the  coefficients  and  numerical  factors involved  in  the  evaluation  function  and  the  other  programs. By placing high values on positional weaknesses, etc. a positional-type player results. By more intensive examination of forced variations it becomes a  combination  player. Furthermore,  the strength of the  play  can  be easily  adjusted  by  changing  the  depth  of calculation  and  by  omitting or adding terms to the evaluation function.

Finally we may note that a machine of this type will play" brilliantly" up to its limits. It will readily sacrifice a  queen or other piece in order to gain more material later or to give checkmate provided the completion of the combination occurs within its computing limits.

The chief weakness is that the machine will not learn by its mistakes. The  only  way  to  improve  its  play  is  by  improving  the  program. Some thought  has  been  given  to  designing  a  program  which  is  self­ improving but, although it appears to be possible, the methods thought of so far do not seem to be very practical.  One possibility is  to have a higher level program which changes the terms and coefficients  involved in the evaluation function depending on the results of games the machine has  played. Small  variations  might  be  introduced in these terms and .. the values selected to give the greatest percentage of "wins''.

8.  ANOTHER  TYPE  OF  STRATEGY.

The  l!ltrategies  described  above  do  not,  of course,  exhaust  the  possi­ bilities.  In fact, there are undoubtedly others which are far more efficient in the  use of available computing time on the machine.  Even with the improvements we have discussed the above strategy gives an impression of relying too much on " brute force "  calculations rather than on logical analysis  of a  position.  It plays something like a  beginner at chess  who has  been  tGld  some  of the  principles  and  is  possessed  of tremendous ,energy and accuracy for calculation t>ut  has no experience with the game. A chess  master, on the other hand, has available knowledge of hundreds -or  perhaps  thousands  of standard  situations,  stock  combinations,  and common manreuvres  which  occur time and again in the game. There are,  for  example, the typical sacrifices  of a  knight at B7 or a  bishop at R7,  the  standard  mates  such  as  the  "  Philidor  Legacy ",  manoouvres based  on  pins,  forks,  discoveries,  promotion,  etc. In a  given  position he recognizes some similarity to a  familiar situation and this directs his · mental  calculations along  lines  with greater probability of success.

There  is · no  reason  why  a  program  based  on  such "type positions" could  not  be  constructed. This  would  require,  however,  a  rather for­ midable analysis of the game.  Although there are ~arious books analysing combination  play  and  the  middle  game,  they  are  written  for  human consumption, not for computing machines.  It is possible to give a person one or two specific  examples of a  general situation and have him under­ .s tand  ap.d  apply the general principle  involved. With a  computer an -exact and completely explicit characterization of the situation must be given  with  all  limitations,  special  cases,  etc.  taken  into  account. We are  inclined  to  believe,  however,  that if this  were  done  a  much  more -efficient program would result.

To  program  such  a  strategy  we  might  suppose  that  any  position in  the  machine  is  accompanied  by  a  rather  elaborate  analysis  of the tactical structure of the position suitably encoded.  This analytical data will state that, for example, the Black knight at B3 is pinned by a bishop, that  the  White  rook  at  Kl  cannot  leave  the  back  rank  because  of a threatened mate on B8, that a White knight at R4 has no move, etc. ;  in short, all the facts to which a  chess  player would ascribe importance in analysing  tactical  possibilities. These  data  would  be  supplied  by  a program  and  would  be  continually  changed  and  kept  up-to-date  as -the  game  progressed. The  analytical  data  would  be  used  to  trigger various  other  programs  depending  on  the  particular  nature  of  the position. A  pinned  piece  should  be  attacked. If a  rook  must  guard the back rank it cannot guard the pawn in front of it, etc.  The machine ·obtains in this manner suggestions of plausible moves to investigate.

It is not being suggested that we should design the strategy in our own 'image. Rather it should be matched to the  capacities and weaknesses -of the  computer. The  computer is  strong  in  speed  and  accuracy  and ·,weak in analytical ability and recognition.  Hence, it should make more

.SER.  7,  VOL.  4r, NO. 314--1\II.A.RCH r950

use  of  brutal  calculations  than  humans,  but  with  possible  variations increasing  by .a  factor  of 10 3 every move,  a  little selection goes  a  long way toward improving blind trial and error.

## ACKNOWLEDGMENT.

The  writer  is  indebted  to  E. G.  Andrews,  L. N.  Enequist  and H. E. Singleton  for  a  number  of suggestions  that  have  been  incorporated in the paper.

October  8,  1948.

## APPENDIX.

THE  EVALUATION  FUNCTION  FOR  CHESS.

The evaluation functionf(P) should take into account the" long term ·· advantages and disadvantages of a  position,  i. e. effects  which  may  be expected  to  persist  over  a  number  of  moves  longer  than  individual variations are calculated.  Thus the evaluation is mainly concerned with positional or strategic considerations rather than combinatorial or tactical ones. Of course there is  no sharp line  of division;  many features of a position are on the borderline.  It appears,  however,  that the following might  properly be included in f(P) :-

- ( l)  Material  advantage  (difference  in total material).
- (2)  Pawn  formation :
- (a) Backward, isolated and doubled pawns.
- (b) Relative control of centre (pawns £1,t  K4, Q4,  B4).
- (c) Weakness of pawns near king (e. g. advanced KNP).
- (d) Pawns on opposite colour squares from bishop.
- (e)  Passed pawns.
- (3)  Positions of pieces :
- (a) Advanced knight  (at K5,  Q5,  B5, K6,  Q6,  B6),  especially if p:,;otected by pawn and free from pawn attack.
- (b) Rook on open file,  or semi-open file.
- (<;) Rook on seventh rank.
- (d) Doubled rooks.
- ( 4;) Commitments, attacks and options :
- (a) Pieces which are required for guarding \_functions .and,,th~refore,  committ,ed and with limited mobility~ .  :··. : ·
- (b) Attacks  on  JJieces  which , give  one  player . an  option  of exchanging.
- (c) Attacks on squares adjacent to king. ,
- (d) Pins. We  mean  here  immobilizing  pins  where  the  pinned pi,~ce . is  of  value  not  greater  than the  pinning  piece ;  for example,  a  knight  pinned  by. a . bish9p.
- , ( 5) Mobility.

These factors will apply in the middle game:  during the opening and end game different  principles  must  be used.  · The relative values to  be given each  of the above  quantities is  open to  considerable  debate,  and should  be determined by some experimental procedure.  There a,re  also numerous other factors  which may well \_be worth inclusion.  The more violent tactical weapons, such as discovered checks, forks and pins by a piece  of lower  value  are  omitted  since  they are  best  accounted for  b~r the examination of specific  variations.

## REFERENCES.·

CHERNEV,  1937, Curious  Chess  Facts, The  Black Knight Press. DE GROOT, A. D., 1946a, HetDenken1;andenSchaker 17-18, Amsterdam;  1946b, Ibid., Amsterdam, 207.

F:rNE,  R., 1942, Chess  the  Easy  Way, 79, David McKay. HARDY  and WRIGHT,  1938, The Theory of Numbers, 116,  Oxford. VoN  NEUMANN  and  MORGENSTERN,  1944, Theory  of Games, 125,  Princeton. VrnNERON,  H.,  1914, Les Automates, La Natura. WIENER,  N.,  1948, Cybernetics, John Wiley.