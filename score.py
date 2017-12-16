# Created by Inseong on 2017-12-16

d = dict()
f1 = open("hw1_score.txt", 'r')
f2 = open("hw2_score.txt", 'r')
f3 = open("hw3_score.txt", 'r')
f4 = open("hw4_score.txt", 'r')
f1.readline()
f2.readline()
f3.readline()
f4.readline()
while (True):
    l = f1.readline()
    if l == "":
        break;
    l = l.split()
    s = round(float(l[-1])/120*100,2)
    if l[0] in d:
        d[l[0]] += s
    else :
        d[l[0]] = s

while (True):
    l = f2.readline()
    if l == "":
        break;
    l = l.split()
    s = round(float(l[-1])/80*100,2)
    if l[0] in d:
        d[l[0]] += s
    else :
        d[l[0]] = s
while (True):
    l = f3.readline()
    if l == "":
        break;
    l = l.split()
    s = round(float(l[-1])/60*100,2)
    if l[0] in d:
        d[l[0]] += s
    else :
        d[l[0]] = s

while (True):
    l = f4.readline()
    if l == "":
        break;
    l = l.split()
    s = float(l[-1])
    if l[0] in d:
        d[l[0]] += s
    else :
        d[l[0]] = s
result = (sorted(filter(lambda x:x[1]>250,list(d.items())), key = lambda x:x[1],reverse = True))
print(result)
print(len(result))
f1.close()
f2.close()
f3.close()
f4.close()