# Holmes  :smiley_cat: 
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/Omoshirokunai/holmes?style=flat-square) ![GitHub](https://img.shields.io/github/license/Omoshirokunai/holmes?style=flat-square) ![GitHub repo size](https://img.shields.io/github/repo-size/Omoshirokunai/holmes?style=flat-square)

**Image fogery detection tool using streamlit + electron**


## Table of contents
* [General info](#general-info)
* [Available features](#Available-features)
* [Technologies](#technologies)
* [Setup](#setup)
* [TODO](#TODO)
* [Known issues](#known-issues)


## General info
Holmes is an image forensics tool to help detect if an image is tampered or not. Holmes uses [streamlit](https://github.com/streamlit/streamlit) and electron as browser 

**Note**: Holmes is still early in development and missing a features and UI polish

![image](https://user-images.githubusercontent.com/65668668/104768691-5b9d8100-576e-11eb-858d-e89e49a28c82.png)

## Available features:
* Exif viewer
* Quantization tables viewer(not yet complete)
* Error level analysis
	
## Technologies
Project is created with:
* python: 3.8
* streamlit
* electron: 11.1.0
	
## Setup

To run this project
1) install necessary pip libraries

```bash
pip install -r requirements.txt
```

2) Install necessary npm libraries

```bash
npm install electron
```
3) run streamlit

```bash
streamlit run holmes.py --server.headless true
```
4) view in electron
```bash
npm start
```

## File structure:
The current file structure will most likely be updated as I go along

Holmes: the main script , contains streamlit page setup and page navigation
every other module is named after what they accomplish

## TODO:
* convolutional neural net in tensorflow that takes noise stream and rgb or ycbcr as inputs and outputs if an image is tampered or not
* imporve file structure
* script to run both streamlit and electron quickly



## Known issues:
* open file box opens behind the electron window
