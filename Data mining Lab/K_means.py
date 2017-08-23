data = []
data_set = open("K_means_data.csv", "r")
for addr in data_set:
    quotes = addr.split(",")
    fields = [f.strip('"') for f in quotes]
    data.append([int(f) for f in fields])

k = int(input())

Clusters = [data[i] for i in range(k)]
Class = [-1 for x in range(len(data))]
CLass_count = [0 for x in range(k)]
dist = [0 for x in range(k)]
prev_Class = [1 for x in range(len(data))]

while Class != prev_Class:
    prev_Class = Class
    dist = [0 for x in range(k)]
    for i in range(len(data)):
        dist = [((data[i][0] - Clusters[j][0])**2 + (data[i][1] - Clusters[j][1])**2) for j in range(k)]
        temp = 0
        for j in range(k):
            if dist[temp]>dist[j]:
                temp = j
        Class[i] = temp
        dist = [0 for x in range(k)]
    Clusters = [[0 for i in range(2)] for y in range(k)]
    for i in range(len(data)):
        Clusters[Class[i]] = [(Clusters[Class[i]][j] + data[i][j]) for j in range(2)]
        CLass_count[Class[i]] = CLass_count[Class[i]] + 1
    for i in range(k):
        Clusters[i] = [(Clusters[i][j]/CLass_count[i]) for j in range(2)]

print(Clusters)
