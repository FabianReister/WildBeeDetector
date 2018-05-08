# Wild Bee Watch

## Introduction

This is a weekend project to detect wild bees on my balcony.

![Bee](tests/data/single_bee.jpg)

## Installation

Download the repository and run

        pip install -r requirements.txt
to install missing packages.

Then, install the package via

        python setup.py install

## Usage

Currently, you can only run the detection algorithm on a video file.

Therefore, execute

        run_on_video -h
and see the help for more information.

The script will create a video with a bounding box overlay as shown in the following video (youtube)

[![Wild Bee Detection](http://img.youtube.com/vi/Q43Me7gmU0Y/0.jpg)](http://www.youtube.com/watch?v=Q43Me7gmU0Y "Wild Bee Detection")

### Adjustments
You can use any camera that is mounted statically (not allowed to move within the sequence).

As a perspective transformation is performed, you need to provide the corner points of the box.

Therefore, modify the configuration file (config/config.yaml).

All other parameters can be left untouched but feel free to change them =)

## Algorithm

I added some jupyter notebook files under *docs* that show the relevant steps of preprocessing and detection.

## Contribution

You are welcome to contribute.

If you are interested in the video material (approx. 1h @ 30Hz), don't hesitate to contact me.
