# text-mining

# Project Writeup and Reflection

# Project Overview
I use the data source of SMS spam collection. I utilized natural language processing and text similarity and conducted summary statistics about the text, including characterizing by word frequencies, calculating top 20 common words in the text, and etc. Throughout the project, I hope that I can discover some characteristics of the spam messages and non-spam messages and provides some insights on distinguishing the spam messages and non-spam messages.

# Implementation
After obtaining the data source of SMS messages, I divide the datasets into two lists -- spam list and ham list (non-spam list) -- since I intend to analyze the similarities and diffrences within and between the two lists in the following procedures. I start my first portion of text analysis to obtain a brief overview about the most frequent words in both lists. Accordingly, I map all the words in the spam list and ham list into spam dictionary and ham dictionary and sort the values in these dictionaries in a descending manner to obtain the first 20 words that are most common in both dictionaries. Secondly, I figure out the most frequent words that only appears in spam messages or ham messages, which can provide a more determining insight for users to categorize the spam messages and non-spam messages. Thirdly, I calculate the text similarities within and between the spam messages and ham messages to investigate whether the senders with different intentions will unintentionally or intentionally contain some overlapping sentences or words. Lastly, I conduct a sensitivity analysis for the spam messages and ham messages to understand the preference of the senders and the mood/atmosphere they endeavor to build. 

# Results
MOST COMMON WORDS: If people need to decide whether a message is a spam message by merely observing the words rather than the context, they can randomly pick few words from the message and decide whether these words contain any traits in the features discussed in the following.

Briefly browsing through the 20 most common words in spam messages and ham messages, they both have a huge proportion of personal pronouns (e.g. 'you', 'your','u'). However, as for the non-spam messages, they include more prepositions (e.g. 'in', 'of', 'for', 'that', 'but', 'on') and have a greater diversity of personal pronouns, including first person point-of-view and second person point-of-view. For the spam messages, they tend to restrict the personal pronouns into second person point-of-view. In addition, spam messages will include more words related with cell-phone, such as 'call', 'text', and 'mobile'.
```
The top 20 words with highest frequency in spam messages are:
to 689
a 378
call 346
you 287
your 263
 223
free 216
the 204
for 203
now 189
or 188
2 173
is 158
txt 150
u 147
on 145
ur 144
have 135
from 128
mobile 123
```
```
The top 20 words with highest frequency in ham messages are:
i 1880
you 1768
to 1560
the 1095
a 1079
 1034
u 939
and 826
in 802
me 748
is 717
my 708
it 575
of 522
for 499
that 471
have 417
but 408
your 399
on 394
```

MOST COMMON UNIQUE WORDS: If people need to decide whether a message is a spam message by merely observing the words rather than the context, they can randomly pick few words from the message and decide whether these words contain any traits in the features discussed in the following.

For the most frequent 20 words in spam messages only, most of the words are well-written (i.e. words are written in a complete form; no acronym; less words with typo) and are more formal. In addition, this list also include some words that lure people to fall in the trap, such as 'prize', 'won', 'awarded', and etc. For the most frequent 20 words in ham message only, most of them include acronym (e.g. 'k' for ok, 'y' for why) and typo (e.g. 'orry', 'ey', 'ow', and etc). For these words, they usually require people to read them in the context in order to understand these words. 
```
The top 20 most frequent words that are in spam messages, but not in ham messages are:
claim 113
prize 92
won 73
guaranteed 50
tone 48
18 43
awarded 38
â£1000 35
150ppm 34
ringtone 26
entry 26
collection 26
tones 25
weekly 24
mob 24
valid 23
500 23
â£100 22
150p 22
sae 21
```
```
The top 20 most frequent words that are in ham messages, but not in spam messages are:
lt;#&gt 276
he 207
k 161
lor 160
i'll 152
later 133
da 129
she 120
ã¼ 117
orry 93
said 87
h 87
ask 87
ey 86
amp 84
doing 82
y 80
ow 80
morning 76
hat 75
```

TEXT SIMILARITY:
While no significant similarity within various spam messages and differences between the spam messages and non-spam messages, the comparative higher score for the text similarity within the spam messages implies that a greater proclivity of consistent message patterns may appear in spam messages. In addition, since every spam messages will adjust the content to better promote different organizations and events, the the text similarity will significantly boost as these disparities become consistent. Therefore, people can better discern the spam message if they found similar patterns existing in several messages. 

Furthermore, since the text similarity between the spam messages and ham messages are the lowest in three calculated ones, we can properly conclude that if people feel an obvious difference in two messages (i.e. one message from unknown sender and one message from the know person or friend), there is a high chance that the message from the unknown sender belongs to a spam message. 
```
The text similarity within the strings of the spam list is 32.4678.
The text similarity within the strings of the ham list is 26.5087.
The text similarity between the strings of the spam list and the strings of the ham list is 23.3286.
```

SENSITIVITY ANALYSIS:
Comparing the sensitivity analysis result for the spam messages and non-spam messages, I discover that the overall text of the spam message tends to be more positive, and the ham message tends to cluster more on the neutral tones and spend slightly less emphasis on positive tone and more emphasis on negative tone. Extending to the broader view of spam message's intention, these senders intentionally create a positive and attractive tones in order to excite the target group and encourage them to take actions.
```
The sensitivity analysis for spam messages:
{'neg': 0.038, 'neu': 0.744, 'pos': 0.217, 'compound': 1.0}
The sensitivity analysis for ham messages:
{'neg': 0.076, 'neu': 0.774, 'pos': 0.149, 'compound': 1.0}
```

# Reflection
Everyhing goes smoothly except the natural language processing part. After following the instructions of the assignment, I still fail to process the sensitivity analysis. However, after importing the following two lines into the Visual Studio Code and into the Command Prompt, I successfully conduct the sensitivity analysis. After getting all the results from the various techniques, the outcome does not appear to be as distinguished as I thought. For example, previously, I expected a significant higher difference in the text similarity between the spam messages and ham messages, but no huge gap exists when I actually observe the result. Nevertheless, by infering some possibilities in the results, I still extract some plausible insights for the text-mining assignment. For the next time, I could adopt greater amount of spam messages with more updated data. In addition, I also intend to upgrade the functions. For example, for the text_similarity function and text_similarities function, I utilized the randomization method to randomly pair two messages. However, sometimes, the randomization may unintentionally compare two exactly same messages and exclude some messages, which will all disturb the outcome. Therefore, I aim to upgrade the text_similarity function and text_similarities function and enable every message to compare with every other string, which allows the final score to be more persuading. 
```
import nltk
nltk.download('vader_lexicon')
```