def IoU(bbox1, bbox2):
    xA = max(bbox1[0], bbox2[0])
    yA = max(bbox1[1], bbox2[1])
    xB = min(bbox1[0]+bbox1[2]-1, bbox2[0]+bbox2[2]-1)
    yB = min(bbox1[1]+bbox1[3]-1, bbox2[1]+bbox2[3]-1)

    area_intersect = max(0, xB-xA+1) * max(0, yB-yA+1)
    area_bbox1 = bbox1[2]*bbox1[3]
    area_bbox2 = bbox2[2]*bbox2[3]

    iou = area_intersect / (area_bbox1+area_bbox2-area_intersect)
    return iou
