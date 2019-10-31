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
        elif a == '_':
            num.append(1)
        else:
            return -1
    return num

def compress(num):
    for i in range(0,len(num)-1):
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
    for j in diff:
        if j != 'x':
            return j
    return 'x'


seq1 = "AGTCCT"
seq2 = "TAGTCGA"
num1 = []
num2 = []
num1 = convert(seq1, num1)
num2 = convert(seq2, num2)
print(num1, num2)
t1 = num1
t2 = num2
while compare(t1, t2) != 'x':
    t1 = compress(t1)
    t2 = compress(t2)

    if compare(t1,t2) != 'x':
        print(t1, t2)
        num1 = t1
        num2 = t2
    else:
        break

ans = compare(num1, num2)
print (ans)

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

print (seq1)
print (seq2)