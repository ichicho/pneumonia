import pydicom
from matplotlib import pyplot as plt

def get_dcm(path_dicom):

    ds = pydicom.dcmread(path_dicom)
    img = ds.pixel_array

    return img
