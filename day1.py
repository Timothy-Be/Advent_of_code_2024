"""=========================PART 1=============================="""

list1 = []
list2 = []

f = open("input_day_1.txt", "r")
for line in f:
    s1, s2 = line.split()
    list1.append(int(s1))
    list2.append(int(s2))

list1.sort()
list2.sort()

total = 0
for i in range(len(list1)):
    total += abs(list1[i] - list2[i])

print(total)


"""=========================PART 2=============================="""

h = {}
for v in list2:
    h[v] = h.get(v, 0) + 1

similarity = 0
for v in list1:
    similarity += v * h.get(v, 0)

print(similarity)
