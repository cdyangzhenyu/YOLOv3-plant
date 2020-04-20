import glob
import os
import shutil

names_file = "data/plant.names.list"
train_file = "data/plant/plant.train.list"
test_file = "data/plant/plant.test.list"
img_path = "data/plant/images/"
label_path = "data/plant/labels/"

cwd = os.getcwd()

names_fw = open(names_file, "w")
train_fw = open(train_file, "w")
test_fw = open(test_file, "w")
size = (256, 256)
bbox_size = 250
classes = []
# gen images from data/plant/images/
def prepare_dataset():
    plant_dirs = glob.glob("raw/*")
    for plant_dir in plant_dirs:
        for t in ["train", "test"]:
            catalogs = glob.glob("%s/%s/*" % (plant_dir, t))
            for cata in catalogs:
                if t == "train":
                    names_fw.write(cata.split('/')[-1] + "\n")
                    classes.append(cata.split('/')[-1])
                img_files = glob.glob("%s/*" % cata)
                for img_file in img_files:
                    img_new_file = img_file.replace(' ', '_').replace('..', '.')
                    img_name = img_new_file.split('/')[-1].replace('strawberry', 'sberry')
                    img_new_path = cwd + "/" + img_path + img_name
                    #cv2.imwrite(img_new_path, cv2.imread(img_file), [int(cv2.IMWRITE_JPEG_QUALITY), 90])
                    if t == "train":
                        train_fw.write(img_new_path + "\n")
                    elif t == "test":
                        test_fw.write(img_new_path + "\n")
                    shutil.copy(img_file, img_new_path)
                    x = 0.5
                    y = 0.5
                    w = float(bbox_size) / size[0]
                    h = float(bbox_size) / size[1]
                    c = classes.index(cata.split('/')[-1])
                    txt_path = label_path + img_name.split('.')[0] + '.txt'
                    with open(txt_path, "w") as f:
                        data = "{} {} {} {} {}".format(c, x, y, w, h)
                        f.write(data)

    print("Prepare Dataset Successfully!!!")
                
prepare_dataset()
names_fw.close()
train_fw.close()
test_fw.close()
