#!/usr/bin/env python3
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image, ImageOps
import numpy as np
from sys import argv

def main():
    logo_path, output_path = get_args()
    logo, mask = get_logo_and_mask(logo_path)
    wc = get_wordcloud(mask=mask, frequencies=frequencies)
    recombined = recombine(wc,logo,mask)
    
    visualize(logo,mask,recombined)
    save(recombined, output_path)

##
def get_args():
    try:
        logo_path = argv[1] 
    except:
        logo_path = "./cr-mask-negative-fullpage.png"

    try:
        output_path = argv[2] 
    except:
        output_path = "cr-wordcloud.png"

    return logo_path, output_path


def get_logo_and_mask(logo_path):
    logo = Image.open(logo_path)
    mask = 255*(np.array(
            ImageOps.grayscale(logo)) != 255)

    return logo, mask 

def get_wordcloud(mask,frequencies):
    wc = WordCloud(background_color="white", max_words=100, mask=mask)
    wc.generate_from_frequencies(frequencies)
    return wc

def recombine(wc,logo,mask):
    logo_masked = np.einsum("ij,ijk->ijk",mask,logo)[:,:,:3]/255
    wc_masked = np.einsum("ij,ijk->ijk",255-mask,wc)/255

    return np.array( logo_masked + wc_masked, dtype=np.uint8)

def visualize(*figs):
    for fig in figs:
        plt.figure()
        plt.imshow(fig, interpolation="bilinear")
        plt.axis("off")

    plt.show()

def save(fig,output_path):
    plt.imshow(fig,interpolation="bilinear")
    plt.axis("off")
    plt.savefig(output_path)

###

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


if __name__ == "__main__":
    main()


