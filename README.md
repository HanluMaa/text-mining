# text-mining

# Project Writeup and Reflection

# Project Overview
I use the data source of SMS spam collection. I utilized natural language processing and text similarity and conducted summary statistics about the text, including characterizing by word frequencies, calculating top 20 common words in the text, and etc. Throughout the project, I hope that I can discover some characteristics of the spam messages and non-spam messages and provides some insights on distinguishing the spam messages and non-spam messages.

# Implementation
After obtaining the data source of SMS messages, I divide the datasets into two lists -- spam list and ham list (non-spam list) -- since I intend to analyze the similarities and diffrences within and between the two lists in the following procedures. I start my first portion of text analysis to obtain a brief overview about the most frequent words in both lists. Accordingly, I map all the words in the spam list and ham list into spam dictionary and ham dictionary and sort the values in these dictionaries in a descending manner to obtain the first 20 words that are most common in both dictionaries. Secondly, I figure out the most frequent words that only appears in spam messages or ham messages, which can provide a more determining insight for users to categorize the spam messages and non-spam messages. Thirdly, I calculate the text similarities within and between the spam messages and ham messages to investigate whether the senders with different intentions will unintentionally or intentionally contain some overlapping sentences or words. Lastly, I conduct a sensitivity analysis for the spam messages and ham messages to understand the preference of the senders and the mood/atmosphere they endeavor to build. 

# Results
Most Common Words:

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
acronymn or messing words
