import os
import pandas as pd

def LabelList(path_dicoms, path_labels):

    dicom_names = os.listdir(path_dicoms)
    pids = []
    for filename in dicom_names:
        pid = os.path.splitext(filename)[0]
        pids.append(pid)


    df = pd.read_csv(path_labels)
    ary = df.values
    labellist = {}
    for label in ary:
        pid = label[0]

        if pid in pids:
            if pid in labellist:
                t_label = labellist[pid]
                t_label['n_bbox'] += 1
                t_label['x-min'].append(int(label[1]))
                t_label['y-min'].append(int(label[2]))
                t_label['width'].append(int(label[3]))
                t_label['height'].append(int(label[4]))
            else:
                if label[5]:
                    labellist[pid] = {'n_bbox': 1,
                                      'x-min': [int(label[1])],
                                      'y-min': [int(label[2])],
                                      'width': [int(label[3])],
                                      'height': [int(label[4])]}
                else:
                    labellist[pid] = {'n_bbox': 0,
                                      'x-min': [],
                                      'y-min': [],
                                      'width': [],
                                      'height': []}
        else:# in case of no dicom file
            pass

    return labellist
