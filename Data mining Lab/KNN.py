w = 3
h = 5

data_set = [[0 for x in range(w)] for y in range(h)]

for i in range(h):
    for j in range(w):
        data_set[i][j] = int(input())

test_data = [3, 8]

k = int(input())

knn = [[0 for x in range(2)] for y in range(h)]

dist = 0

for i in range(h):
    dist = ((data_set[i][0] - test_data[0])**2 + (data_set[i][1] - test_data[1])**2)**0.5
    knn[i][0] = dist
    knn[i][1] = data_set[i][2]

label = 0

for i in range(k):
    temp = i
    j = i
    while j < h:
        if knn[temp][0] > knn[j][0]:
            temp = j
        j = j + 1
    tempdata = knn[temp][0]
    knn[temp][0] = knn[i][0]
    knn[i][0] = tempdata
    tempdata = knn[temp][1]
    knn[temp][1] = knn[i][1]
    knn[i][1] = tempdata


for i in range(k):
    label = knn[i][1] + label

label = label/k

if label >= 0.5:
    print("label = 1")
else:
    print("label = 0")
