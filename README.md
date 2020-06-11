# YOLOv3-Plant

Train and Test YOLOv3 to detect Plant Village Disease.

Clone this Repo:
```
git clone https://github.com/cdyangzhenyu/YOLOv3-plant.git
cd YOLOv3-plant
pip3 install -r requirements.txt
```

Preparing the Yolov3 plant Dataset:
```
python utils/prepare_database.py
```

Clone Darknet Repo:
```
git clone https://github.com/pjreddie/darknet.git
```

Compile Darknet (edit Makefile to use GPU, CUDNN and OPENCV).

After you got the `darknet` binary, download the Pretrained Convolutional Weights:

```
cd models
wget https://pjreddie.com/media/files/darknet53.conv.74
```

- Train:
```
cd darknet
./darknet detector train ../cfg/plant.dataset ../cfg/yolov3_plant.cfg ../models/darknet53.conv.74
```

- Test:
```
./darknet detector test ../cfg/plant.dataset ../cfg/yolov3_plant_test.cfg ../models/yolov3_plant.backup strawberry_healthy2.jpg  -i 0 -thresh 0.5
```

- Use
```
cd backup
cat yolov3_plant.tar.bz2a* | tar xj
```

- To tensorflow pb models

```
cd backup
python ../../OpenVINO-YoloV3/convert_weights_pb.py --class_names ../data/plant.names.list  --weights_file yolov3_plant.backup.2100 --data_format NHWC
```
