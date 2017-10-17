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
## Evaluation results


#### Car color detection:

#### Day

| Car | red | black | blue | yellow | green | white |  
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| False positive | 0/1739 < 0.1% | 444/1619 ~= 27% | 336/1827 ~= 18% | 38/1746 ~= 2% | 182/2103 ~= 9% | 122/1626 ~= 8% |
| False negative | 45/393 ~= 11% | 115/513 ~= 22% | 49/305 ~= 16% | 7/386 ~= 2% | 6/29 ~= 21% | 36/506 ~= 7% |

#### Night

| Car | red | black | blue | yellow | green | white |  
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| False positive | 206/1112 < 19% | 116/907 ~= 13% | 159/1126 ~= 14% | 68/1056 ~= 6% | 45/1210 ~= 4% | 111/724 ~= 15% |
| False negative | 16/115 ~= 14% | 29/320 ~= 9% | 2/101 ~= 2% | 10/171 ~= 6% | 1/17 ~= 6% | 49/503 ~= 10% |

#### Person color detection:

| Person | red | black | blue | yellow | green | white |  
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| False positive | 46/901 ~= 5% | 164/825 ~= 20% | 91/911 ~= 10% | 96/1040 ~= 9% | 153/1047 ~= 15% | 85/901 ~= 9% |
| False negative | 49/224 ~= 22% | 5/300 ~= 2% | 9/214 ~= 4% | 0/85 < 0.1% | 4/78 ~= 5% | 17/224 ~= 8% |



#### Face color detection:

| Face | dark skin | light skin |
| :---: | :---: | :---: |
| False positive | 3/55 ~= 5% | 11/36 ~= 31% |
| False negative | 12/36 ~= 33% | 2/55 ~= 4% |


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
