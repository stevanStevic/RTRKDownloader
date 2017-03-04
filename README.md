README v0.0 / MARCH 2017

# RTRKDownloader

## Introduction

Python scripts for downloading materials from http://www.rt-rk.uns.ac.rs/. This is a page for students which contains lecture presentations and exercise materials, but has no *Download all* button.  

## Installation

These spiders are using Scrapy library for python. [**Here**] are instructions for installation.

## Usage

There are 2 spiders in case only lectures (*rtrkLec-dl.py*) or only exercises (*rtrkExec-dl.py*) are downloaded. For bouth just run bouth spiders.  
To run spider (for lectures) type:

>scrapy runspider rtrkLec-dl.py -a link="http://www.rt-rk.uns.ac.rs/predmeti/zeljeni/predmet" -a dir="/path/to/dir"

**link** argumet is required to run spider
**dir** argument is optional. If not used, files be downloaded to spider's directory
