import os
import pydicom
import torch
from torch.utils.data import Dataset, DataLoader

def read_dicom(path_dicom):

    ds = pydicom.dcmread(path_dicom)
    img = ds.pixel_array
    return torch.from_numpy(img)

class DicomDataset(Dataset):

    def __init__(self, path_dicoms):
        self.path_dicoms = path_dicoms
        self.dicom_names = os.listdir(path_dicoms)

    def __len__(self):
        return len(self.dicom_names)

    def __getitem__(self, idx):
        filename = self.dicom_names[idx]
        pid = os.path.splitext(filename)[0]
        img = read_dicom(os.path.join(self.path_dicoms, filename))
        sample = {'pid': pid, 'img': img}
        return sample

def DicomDataLoader(path_dicoms, batch_size=1, num_workers=0):

    dataset = DicomDataset(path_dicoms)
    dataloader = DataLoader(dataset,
                            batch_size=batch_size,
                            shuffle=True,
                            num_workers=num_workers)
    return dataloader
