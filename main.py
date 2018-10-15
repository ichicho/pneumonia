from matplotlib import pyplot as plt

from DataLoader import createDataLoader

path_dicoms = './Data/train_dicoms'
dataloader = createDataLoader(path_dicoms, batch_size=2)

for sample in dataloader:
    img = sample['img']
    pids = sample['pid']
    print(pids[0])
    plt.imshow(img[0])
    plt.show()
    print(pids[1])
    plt.imshow(img[1])
    plt.show()
    print()
