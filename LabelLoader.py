import pandas as pd

def get_labels(label_path):
    df = pd.read_csv(label_path)
    ary = df.values

    labels = {}
    for label in ary:

        pid = label[0]

        if label[0] in labels :
            t_label = labels[pid]
            t_label['n_bbox'] += 1
            t_label['x-min'].append(int(label[1]))
            t_label['y-min'].append(int(label[2]))
            t_label['width'].append(int(label[3]))
            t_label['height'].append(int(label[4]))

        else:
            if label[5]:
                labels[pid] = {'n_bbox': label[5],
                               'x-min': [int(label[1])],
                               'y-min': [int(label[2])],
                               'width': [int(label[3])],
                               'height': [int(label[4])]}

            else:
                labels[pid] = {'n_bbox': 0}

    return labels
