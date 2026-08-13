#!/usr/bin/env python3
from wordcloud import WordCloud
from matplotlib import pyplot as plt

wc = WordCloud(background_color="white", max_words=10)
frequencies = {"git": 10, 
               "github": 5,
               "sphinx": 3, 
               "gitlab":2, 
               "pytest":2,
               "conda":3,
               "AI-assisted coding": 3,
               "responsibility": 4,
               "automated testing": 2,
               "social coding": 4,
               "containers": 2,
               "reproducibility": 5,
               "open science": 3,
               "software licenses": 2,
               }
wc.generate_from_frequencies(frequencies)
plt.imshow(wc)
plt.axis("off")
plt.savefig("cr-wordcloud.png")
