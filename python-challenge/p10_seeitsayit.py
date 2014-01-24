__author__ = 'julenka'
# compute see it say it sequence
# 1, 11, 21, 1211, 111211, 311221, 13212211, 111212112211, 31121112212211


cur = '11'
result = []
for i in range(29):
    counts = []
    v = cur[0]
    c = 1
    for j in cur[1:]:
        if j != v:
            counts.extend([str(c), v])
            v = j
            c = 0
        c += 1
    counts.extend([str(c),v])
    cur = ''.join(counts)
    result.append(cur)

print result
print len(result[28])

