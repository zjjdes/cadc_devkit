'''
This script converts the LiDAR points clouds from .bin to .csv
'''

import os, sys, csv
import numpy as np
import cv2

cadcd = {
    '2018_03_06': [
        '0001','0002','0005','0006','0008','0009','0010',
        '0012','0013','0015','0016','0018'
    ],
    '2018_03_07': [
        '0001','0002','0004','0005','0006','0007'
    ],
    '2019_02_27': [
        '0002','0003','0004','0005','0006','0008','0009','0010',
        '0011','0013','0015','0016','0018','0019','0020',
        '0022','0024','0025','0027','0028','0030',
        '0031','0033','0034','0035','0037','0039','0040',
        '0041','0043','0044','0045','0046','0047','0049','0050',
        '0051','0054','0055','0056','0058','0059',
        '0060','0061','0063','0065','0066','0068','0070',
        '0072','0073','0075','0076','0078','0079',
        '0080','0082'
    ]
}

BASE = 'G:/LiDAR datasets/cadc_devkit/data/cadcd/'

for date in cadcd:
  for drive in cadcd[date]:
    directory = BASE + date + '/' + drive + '/labeled/lidar_points/data/'

    for filename in os.listdir(directory):
      if filename.endswith('.bin'): 
        frame = os.path.splitext(filename)[0]
        framePath = os.path.join(directory, filename)

        print(framePath)

        points = np.fromfile(framePath, dtype=np.float32).reshape(-1, 4)

        with open(os.path.join(directory, frame) + '.csv', 'w', newline='') as csvf:
          writer = csv.writer(csvf)

          for row in points:
              writer.writerow(row)
        
        print('Done')
        continue
      else:
        continue
