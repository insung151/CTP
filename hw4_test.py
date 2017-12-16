#Jang TaeJun
#ctp17 HW4 test
#Ver.3.5.0

from ctp.hw4_ex1 import is_valid1; from ctp.hw4_ex2 import is_valid2
from ctp.hw4_ex3 import sanitize_and_sort
from ctp.hw4_ex4 import similarity; from ctp.hw4_ex5 import where_you_at

#data
def make_loc(lat, lon, time, name, keys):
    dic={'latitude': lat, 'longitude': lon, 'timestamp': time, \
         'name': name, 'keywords': keys}
    return dic

loc_lst=[];i=0
while i<30:
    a=int(i%3); b=int(i*11/7); c=int(i/10+21+a*3)
    loc_lst.append(make_loc(a+c+0.01, b+c-0.01, int(i*10-(i%3)*15+50), \
                     str(int(i*10-(i%3)*15+50)), [str(a%11), str(b%11), str(c%11), str((a+b)%11), str((b*c)%11)]))
    i=i+1

def make_sorted_locs(n):
    sorted_loc_lst=[]; j=0
    while j<n:
        a=int(j%3); b=int(j*11/7); c=int(j/10+21+a*3)
        sorted_loc_lst.append(make_loc(a+c+0.01, b+c-0.01, j*10+10, \
                     str(j*10+10), [str(a%11), str(b%11), str(c%11), str((a+b)%11), str((b*c)%11)]))
        j=j+1
    return sorted_loc_lst

w1loc1={'latitude': 1.1, 'timestamp': 100, \
         'name': 'none lon', 'keywords': ['Wrong loc']}
w1loc2={'longitude': 1.2, 'latitude': 1.1, 'timestamp': '100', \
         'name': 'wrong time type', 'keywords': ['a','d']}
w1loc3={'latitude': 1.1, 'longitude': 1.2, 'timestamp': 100, \
         'name': 'over keys', 'keywords': ['a','d'], 'preference':92}
w1loc4={'latitude': 1.1, 'longitude': 'a', 'timestamp': 100, \
         'name': 'wrong lon type', 'keywords': ['a','d']}

w2loc1=make_loc(1.1, 1.1, -100, 'False time only 2', ['a','b','c'])
w2loc2=make_loc(100.0, 1.2, 100, 'False lat only 2', ['a','e'])
w2loc3=make_loc(1.1, 1.2, 100, ['wrong name'], ['a', 'c'])
w2loc4=make_loc(1.1, 1.2, 100, 'wrong keywords', [1, 2])

rloc1=make_loc(1.1, 1.2, 10, 'right loc',[])
rloc2={'keywords': ['right', 'loc'], 'longitude': 1.2, 'latitude': 1.1, \
       'name': 'tangled sequence', 'timestamp': 321}

wlocs=[w1loc1, w1loc2, w1loc3, w1loc4, \
       w2loc1, w2loc2, w2loc3, w2loc4, \
       rloc1, rloc2]

ans_t1=[False,False,False,False,\
       True,True,False,False,True,True]
ans_t2=[False,False,False,False,\
       False,False,False,False,True,True]

loc_lst=loc_lst+wlocs

#test ex1
def test1() :
    print('\n----------Ex1----------'); i=0; wrong=[]
    print('Yours | Right')
    while i < 10:
        print(is_valid1(wlocs[i]),'|',ans_t1[i])
        if ans_t1[i] != is_valid1(wlocs[i]):
            wrong.append(i)
        i=i+1
    if wrong==[]:
        print('\nAll Right')
    else :
        print('\nWrong')
        an1=input('\nDo you want to see? Y/N :')
        if an1 in ['Y','y','yes','YES','Yes']:
            print(' '); j=0; l=len(wrong)
            while j<l:
                print(wrong[j], wlocs[wrong[j]]['name'])
                print(wlocs[wrong[j]],'\n'); j=j+1
    print('\n')

#test ex2
def test2() :
    print('\n----------Ex2----------'); i=0; wrong=[]
    print('Yours | Right')
    while i < 10:
        print(is_valid2(wlocs[i]),'|',ans_t2[i])
        if ans_t2[i] != is_valid2(wlocs[i]):
            wrong.append(i)
        i=i+1
    if wrong==[]:
        print('\nAll Right')
    else :
        print('\nWrong')
        an1=input('\nDo you want to see? Y/N :')
        if an1 in ['Y','y','yes','YES','Yes']:
            print(' '); j=0; l=len(wrong)
            while j<l:
                print(wrong[j], wlocs[wrong[j]]['name'])
                print(wlocs[wrong[j]],'\n'); j=j+1
    print('\n')
    
#test ex3
def test3() :
    print('\n----------Ex3----------')
    ssloc_lst=sanitize_and_sort(loc_lst); i=0; times=[]; f=0
    if len(ssloc_lst)==31:
        while i<31:
            print(ssloc_lst[i]['timestamp'], end='  ')
            if i !=30:
                if ssloc_lst[i]['timestamp'] > ssloc_lst[i+1]['timestamp']:
                    print('Wrong!'); f=f+1
                    print(i,'th sequence is wrong\n',\
                          '\n',ssloc_lst[i-1]['timestamp'],\
                          '\n',ssloc_lst[i]['timestamp'],\
                          '\n',ssloc_lst[i+1]['timestamp'])
            i=i+1
    if f==0: print('\n\nAll Right')
    print('\n')
    
#test ex4
def test4() :
    print('\n----------Ex4----------')
    a=int(input('a number in 1~30 : '))-1
    b=int(input('another number in 1~30 : '))-1
    loc1=loc_lst[a]; loc2=loc_lst[b]
    print(loc1['keywords'], loc2['keywords'])
    print(similarity(loc1, loc2), '\n')

    loc01=loc_lst[0]; loc02=loc_lst[29]
    print(loc01['keywords'], loc02['keywords'])
    print(similarity(loc01, loc02))
    if similarity(loc01, loc02) == 0: print('Right\n')
    else : print('Wrong\n')
    
    loca1=loc_lst[13]; loca2=loc_lst[23]
    print(loca1['keywords'], loca2['keywords'])
    print(similarity(loca1, loca2))
    if similarity(loca1, loca2) == 0.42857142857142855 : print('Right\n')
    else : print('Wrong\n')

    locb1=loc_lst[5]; locb2=loc_lst[27]
    print(locb1['keywords'], locb2['keywords'])
    print(similarity(locb1, locb2))
    if similarity(locb1, locb2) == 1/9: print('Right\n')
    else : print('Wrong\n')

    locc1=loc_lst[3]; locc2=loc_lst[21]
    print(locc1['keywords'], locc2['keywords'])
    print(similarity(locc1, locc2))
    if similarity(locc1, locc2) == 1/9 : print('Right\n')
    else : print('Wrong\n')

    print(w1loc1['keywords'], loc_lst[1]['keywords'])
    print(similarity(w1loc1, loc_lst[1]))
    if similarity(w1loc1, loc_lst[1]) == -1 : print('Right\n')
    else : print('Wrong\n')

    print(rloc1['keywords'], loc_lst[1]['keywords'])
    print(similarity(rloc1, loc_lst[1]))
    if similarity(rloc1, loc_lst[1]) == 0 : print('Right\n')
    else : print('Wrong\n')

    print('\n')
    
#test ex5
def test5() :
    print('\n----------Ex5----------')
    locss=make_sorted_locs(30)
    print(where_you_at(locss, 49))
    print(where_you_at(locss, 400))
    print(where_you_at(locss, 125))
    
    k=10; ff=[]
    print('\ntesting',len(locss)*10+10,'examples')
    while k < ((len(locss)*10)+10):
        ans=where_you_at(locss, k)
        rans=str(k-(k%10))
        if ans != rans: print(k); ff.append(k)
        k=k+1
    if ff==[]:
        print('All right')
    else:
        print('Something wrong', ff)
    
    n=int(input('\nGive a natural number: '))
    locs=make_sorted_locs(n) #You can change the number
    i=10; f=[]
    print('\ntesting',len(locs)*10+10,'examples')
    while i < ((len(locs)*10)+10):
        ans=where_you_at(locs, i)
        rans=str(i-(i%10))
        if ans != rans: print(i); f.append(i)
        i=i+1
    if f==[]:
        print('All right')
    else:
        print('Something wrong', f)
        
    print('\n')
    
#test sellecting one
def run_test(k) :
    if k in [1,2,3,4,5]:
        if k == 1: test1()
        if k == 2: test2()
        if k == 3: test3()
        if k == 4: test4()
        if k == 5: test5()
    else :
        print("ERROR\n")

#interface
def test() :
    print('\n-------Test Start-------')
    print('\nDo you want test'); ans=input('Yes / No : ')
    if ans in ['No', 'N', 'no', 'n']:
        print('\nThank you.\n')
        print('\n------Test Done!-------')
    else :
        print('Which ex do you want to test?')
        print("('all', '1', '2', '3', 'done')")
        print("(Please enter one at each time)"); n=[]; i=0
        while i==0 :
            a=input(': ')
            if a in ['all', '1', '2', '3', '4', '5', 'done'] :
                if a=='done' : i=1
                elif a=='all': n=[1,2,3,4,5]; i=1
                else : n.append(int(a)); print('please enter next one')
            else : print("that is a wrong answer")
        for r in n :
            if r != 'done' : run_test(r)
        print('\n\n\n~~~~~~~~Re Start~~~~~~~~')
        test()

#real running
test()
