# iRONYUN Color Detection

A Color Detection Engine for Object Detector

## Getting Started

Please have opencv2, PIL, numpy, matplotlib, apscheduler==2.1.2 intalled in your system

## Prerequisites
```
# python2.7 is used.
sudo apt-get -y install python-opencv libopencv-dev python-numpy python-dev
sudo pip install matplotlib apscheduler==2.1.2 Pillow
```

## Running the demo

```
# input test.jpg
python search_color.py
# input group of test images
unzip data/car.zip
python demo.py
```

## Running the evaluation

Explain what these tests test and why

```
python tools/color_eval.py
```

## Running optimization over a new dataset

```
mv 'your dataset' tools/opt_color/.
config target folder in tools/opt_color/config.py
cd tools/opt_color
python opt_color.py
```

## Docker

```
cd docker
cp ~/.ssh/id_rsa .
docker build -t <name> .
```

## Authors

TsungJen Hsu
