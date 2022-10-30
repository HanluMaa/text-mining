# text-mining

# Project Writeup and Reflection

# Project Overview
I use the data source of SMS spam collection. I utilized natural language processing and text similarity and conducted summary statistics about the text, including characterizing by word frequencies, calculating top 20 common words in the text, and etc. Throughout the project, I hope that I can discover some characteristics of the spam messages and non-spam messages and provides some insights on distinguishing the spam messages and non-spam messages.

# Implementation
After obtaining the data source of SMS messages, I divide the datasets into two lists -- spam list and ham list (non-spam list) -- since I intend to analyze the similarities and diffrences within and between the two lists in the following procedures. I start my first portion of text analysis to obtain a brief overview about the most frequent words in both lists. Accordingly, I map all the words in the spam list and ham list into spam dictionary and ham dictionary and sort the values in these dictionaries in a descending manner to obtain the first 20 words that are most common in both dictionaries. Secondly, I figure out the most frequent words that only appears in spam messages or ham messages, which can provide a more determining insight for users to categorize the spam messages and non-spam messages. Thirdly, I calculate the text similarities within and between the spam messages and ham messages to investigate whether the senders with different intentions will unintentionally or intentionally contain some overlapping sentences or words. Lastly, I conduct a sensitivity analysis for the spam messages and ham messages to understand the preference of the senders and the mood/atmosphere they endeavor to build. 

# Results
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
acronymn or messing words
