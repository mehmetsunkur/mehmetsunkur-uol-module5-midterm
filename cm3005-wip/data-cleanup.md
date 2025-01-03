## data-cleanup

December 31, 2024

```
[30]: import pandas as pd import logging # Configure logging logging.basicConfig(level=logging.INFO) [31]: # Read the CSV file from the data/raw folder input\_file\_path = 'data/raw/Spotify\_Youtube.csv' df = pd.read\_csv(input\_file\_path) [32]: df.head() [32]: Id Artist Url\_spotify \ 0 0 Gorillaz https://open.spotify.com/artist/3AA28KZvwAUcZu… 1 1 Gorillaz https://open.spotify.com/artist/3AA28KZvwAUcZu… 2 2 Gorillaz https://open.spotify.com/artist/3AA28KZvwAUcZu… 3 3 Gorillaz https://open.spotify.com/artist/3AA28KZvwAUcZu… 4 4 Gorillaz https://open.spotify.com/artist/3AA28KZvwAUcZu… Track \ 0 Feel Good Inc. 1 Rhinestone Eyes 2 New Gold (feat. Tame Impala and Bootie Brown) 3 On Melancholy Hill 4 Clint Eastwood Album Album\_type \ 0 Demon Days album 1 Plastic Beach album 2 New Gold (feat. Tame Impala and Bootie Brown) single 3 Plastic Beach album 4 Gorillaz album Uri Danceability Energy Key … \ 0 spotify:track:0d28khcov6AiegSCpG5TuT 0.818 0.705 6.0 … 1 spotify:track:1foMv2HQwfQ2vntFf9HFeG 0.676 0.703 8.0 … 2 spotify:track:64dLd6rVqDLtkXFYrEUHIU 0.695 0.923 1.0 … 3 spotify:track:0q6LuUqGLUiCPP1cbdwFs3 0.689 0.739 2.0 … 4 spotify:track:7yMiX7n9SBvadzox8T5jzT 0.663 0.694 10.0 …
```

```
[33]:
```

0

True

True

1.040235e+09

1

True

True

3.100837e+08

2

True

True

6.306347e+07

3

True

True

4.346636e+08

4

True

True

6.172597e+08

## [5 rows x 28 columns]

```
# Remove columens has no use to the analysis and keeps big data df = df.drop(columns=['Url\_spotify','Url\_youtube','Description']) # Save the modified CSV file to the data/processed folder output\_file\_path = 'data/processed/Spotify\_Youtube.csv' df.to\_csv(output\_file\_path, index= False ) logging.info(f"Modified CSV saved to { output\_file\_path } ") df.head()
```

INFO:root:Modified CSV saved to data/processed/Spotify\_Youtube.csv

```
[33]: Id Artist Track \ 0 0 Gorillaz Feel Good Inc. 1 1 Gorillaz Rhinestone Eyes 2 2 Gorillaz New Gold (feat. Tame Impala and Bootie Brown)
```

- Url\_youtube \

```
0 https://www.youtube.com/watch?v=HyHNuVaZJ-k 1 https://www.youtube.com/watch?v=yYDmaexVHic 2 https://www.youtube.com/watch?v=qJa-VFwPpYA 3 https://www.youtube.com/watch?v=04mfKJWDSzI 4 https://www.youtube.com/watch?v=1V\_xRb0x9aw
```

Title

Channel

Views

\

```
0 Gorillaz - Feel Good Inc. (Official Video) Gorillaz 693555221.0 1 Gorillaz - Rhinestone Eyes [Storyboard Film] (… Gorillaz 72011645.0 2 Gorillaz - New Gold ft. Tame Impala & Bootie B… Gorillaz 8435055.0 3 Gorillaz - On Melancholy Hill (Official Video) Gorillaz 211754952.0 4 Gorillaz - Clint Eastwood (Official Video) Gorillaz 618480958.0
```

```
Likes Comments Description \ 0 6220896.0 169907.0 Official HD Video for Gorillaz' fantastic trac… 1 1079128.0 31003.0 The official video for Gorillaz - Rhinestone E… 2 282142.0 7399.0 Gorillaz - New Gold ft. Tame Impala & Bootie B… 3 1788577.0 55229.0 Follow Gorillaz online:\nhttp://gorillaz.com \… 4 6197318.0 155930.0 The official music video for Gorillaz - Clint …
```

Licensed official\_video

Stream

## [35]:

3

3

Gorillaz

On Melancholy Hill

4

4

Gorillaz

Clint Eastwood

```
Album Album\_type \ 0 Demon Days album 1 Plastic Beach album 2 New Gold (feat. Tame Impala and Bootie Brown) single 3 Plastic Beach album 4 Gorillaz album
```

|    | Uri                                  |   Danceability |   Energy |   Key |   Loudness |
|----|--------------------------------------|----------------|----------|-------|------------|
|  0 | spotify:track:0d28khcov6AiegSCpG5TuT |          0.818 |    0.705 |     6 |     -6.679 |
|  1 | spotify:track:1foMv2HQwfQ2vntFf9HFeG |          0.676 |    0.703 |     8 |     -5.815 |
|  2 | spotify:track:64dLd6rVqDLtkXFYrEUHIU |          0.695 |    0.923 |     1 |     -3.93  |
|  3 | spotify:track:0q6LuUqGLUiCPP1cbdwFs3 |          0.689 |    0.739 |     2 |     -5.81  |
|  4 | spotify:track:7yMiX7n9SBvadzox8T5jzT |          0.663 |    0.694 |    10 |     -8.627 |

…

Tempo

Duration\_ms

\

0

…

138.559

222640.0

1

…

92.761

200173.0

2

…

108.014

215150.0

3

…

120.423

233867.0

4

…

167.953

340920.0

0

Gorillaz - Feel Good Inc. (Official Video)

Gorillaz

693555221.0

1

Gorillaz - Rhinestone Eyes [Storyboard Film] (…

Gorillaz

72011645.0

2

Gorillaz - New Gold ft. Tame Impala & Bootie B…

Gorillaz

8435055.0

3

Gorillaz - On Melancholy Hill (Official Video)

Gorillaz

211754952.0

4

Gorillaz - Clint Eastwood (Official Video)

Gorillaz

618480958.0

|    |            Likes |        | Comments Licensed official\_video   |      |      Stream |
|----|------------------|--------|------------------------------------|------|-------------|
|  0 |      6.2209e+06  | 169907 | True                               | True | 1.04024e+09 |
|  1 |      1.07913e+06 |  31003 | True                               | True | 3.10084e+08 |
|  2 | 282142           |   7399 | True                               | True | 6.30635e+07 |
|  3 |      1.78858e+06 |  55229 | True                               | True | 4.34664e+08 |
|  4 |      6.19732e+06 | 155930 | True                               | True | 6.1726e+08  |

## [5 rows x 25 columns]

```
# Read the CSV file from the data/raw folder with specified encoding most\_streamed\_file\_path = 'data/raw/Most Streamed Spotify Songs 2024.csv' most\_streamed\_df = pd.read\_csv(most\_streamed\_file\_path, encoding='ISO-8859-1') # Display the first few rows of the dataframe most\_streamed\_df.head()
```

Title

Channel

Views

\