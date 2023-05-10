import numpy as np
# 打开并解析文件，对数据进行分类：1代表不喜欢 2代表魅力一般 3代表极具魅力

def loadfile(filename):
    fr = open(filename)
    arrayLines = fr.readlines()
    # print(arrayLines)
    numLines = len(arrayLines)
    data = np.zeros((numLines,3))
    labels = []
    index = 0
    for line in arrayLines:
        line = line.strip()
        listFromLine = line.split('\t')
        data[index,:] = listFromLine[0:3]
        if listFromLine[-1] == 'didntLike':
            labels.append(1)
        elif listFromLine[-1] == 'smallDoses':
            labels.append(2)
        elif listFromLine[-1] == 'largeDoses':
            labels.append(3)
        index += 1
    return data, labels

# data, labels = loadfile('dataset.txt')
# print(len(data))
# print(labels)