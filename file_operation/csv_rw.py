# cording: UTF-8
import csv
import shutil
import os

threshold = 5.5
flag = False

with open('in/sample.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        target_col = float(row[2])
        if target_col > threshold:
            flag = True
            break

if flag:
    if not os.path.exists('out'):
        os.mkdir('out')
    shutil.copy('in/sample.csv', 'out/sample2.csv')