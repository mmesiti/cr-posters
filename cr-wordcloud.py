#!/usr/bin/env python3
from wordcloud import WordCloud
from matplotlib import pyplot as plt

wc = WordCloud(background_color="white", max_words=100)
frequencies = {"git": 10, 
               "git commit": 1,
               "git push": 1,
               "git stash": 1,
               "git add": 1,
               "git log": 1,
               "git bisect": 1,
               "code reviews": 1,
               "collaborative software development": 3,
               "code reuse": 1,
               "pull request": 1,
               "github": 5,
               "gitlab": 2, 
               "issues/work items": 1, 
               "sphinx": 3, 
               ".md": 3, 
               "MyST": 1, 
               "test coverage": 1,
               "conda":3,
               "AI-assisted coding": 3,
               "responsibility": 4,
               "automated testing": 3,
               "social coding": 2,
               "containers": 3,
               "reproducibility": 5,
               "open science": 4,
               "OSS licenses": 2,
               "research integrity": 3,
               "data repositories": 1,
               "snakemake": 2,
               "pytest": 1,
               "Test.jl": 1,
               "testthat": 1,
               "Catch2": 1,
               "GoogleTest": 1,
               "github actions": 1,
               "gitlab CI/CD": 1,
               "python":1,
               "R":1,
               "C++":1,
               "Julia":1,
               "docker": 1,
               "apptainer": 1,
               "agentic AI": 1,
               "security": 1,
               "TDD": 1,
               }

wc.generate_from_frequencies(frequencies)
plt.imshow(wc)
plt.axis("off")
plt.savefig("cr-wordcloud.png")
