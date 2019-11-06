import math


def convert(seq, num):
    for a in seq:
        if a == 'A':
            num.append(2)
        elif a == 'C':
            num.append(3)
        elif a == 'G':
            num.append(5)
        elif a == 'T':
            num.append(7)
        else:
            return -1
    return num


def compress(num):
    for i in range(0, len(num)-1):
        num[i] = num[i] * num[i+1]
    return num[0:len(num)-1]


def search(x, target):
    for i in range(0, len(x)):
        if x[i] == target:
            return i
    return ''


def compare(a, b):
    diff = []
    for i in range(0, len(a)):
        temp = search(b, a[i])
        if temp != '':
            diff.append(temp - i)
        else:
            diff.append('x')
    print(diff)
    if diff[2] == 'x':
        return diff
    else:
        return 'x'


seq1 = "AATCTATA"
seq2 = "AAGATA"
num1 = []
num2 = []
num1 = convert(seq1, num1)
num2 = convert(seq2, num2)
c = 0

while compare(num1, num2) == 'x':
    num1 = compress(num1)
    num2 = compress(num2)
    c += 1
    print(num1, num2, c)
ans = compare(num1, num2)
for i in range(0, len(ans)):
    if ans[i] == 'x':
        seq2 = seq2[:i] + '_' + seq2[i:]
print(ans)
"""
if ans > 0:
    print("Move sequence " + str(ans) + " spaces to the right")
    if len(seq1) < len(seq2):
        for i in range(0,ans):
            seq1= "_"+seq1
    else:
        for i in range(0,ans):
            seq2="_"+seq2
elif ans < 0:
    print("Move sequence " + abs(ans) + " spaces to the left")
    if len(seq1) < len(seq2):
        for i in range(0,ans):
            seq1= seq1+"_"
    else:
        for i in range(0,ans):
            seq2= seq2 + "_"
"""
print (seq1)
print (seq2)