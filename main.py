from matplotlib import pyplot as plt

from DicomDataLoader import DicomDataLoader
from LabelList import LabelList

path_dicoms = './Data/train_dicoms'
dataloader = DicomDataLoader(path_dicoms, batch_size=2)

path_labels = './Data/stage_1_train_labels.csv'
labellist = LabelList(path_dicoms, path_labels)

for sample in dataloader:
    img = sample['img']
    pids = sample['pid']
    print(labellist[pids[0]])
    plt.imshow(img[0])
    plt.show()
    print(labellist[pids[1]])
    plt.imshow(img[1])
    plt.show()
    print()
