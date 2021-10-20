import math
from prettytable import PrettyTable
from z3 import *
travdict={}
import math
from prettytable import PrettyTable
from z3 import *
def pres(f1):
    count=0
    dummy=f1.arg(0)
    while True:
        if(dummy.num_args()==2):
            if(type(dummy.arg(0))==z3.z3.IntNumRef):
                count=count+1
                break
            else:
                dummy=dummy.arg(0)
                count=count+1
        if(dummy.num_args()==0):
            count=count+1
            break
        if(dummy.num_args()==1):
            count=count+1
            break
    print(count)
    n=count
    if (n==1):
        lst=[0,1]
    else:
        import itertools
        lst = list(itertools.product([0, 1], repeat=n))

    head="State"
    li1=[head]
    for i in range(2**n):
        li1.append(lst[i])
    t=PrettyTable(li1)

    dummy=f1.arg(0)
    print(dummy)
    exp=[]
    
    i=0
    while True:
        if(dummy.num_args()==0):
            exp.append(dummy)
            break
        if(dummy.num_args()==1):
            exp.append(dummy.arg(0))
            break
        if(type(dummy.arg(0))==z3.z3.IntNumRef):
            exp.append(dummy.arg(1))
            break
        if(dummy.arg(1).num_args()==2):
            exp.append(dummy.arg(1).arg(1))
        if(dummy.arg(1).num_args()==0):
            exp.append(dummy.arg(1))
        dummy=dummy.arg(0)

    exp.reverse()
    

    g=f1.arg(0)
    initial=f1.arg(1)
    int_inti=int(str(initial))
    visit=[int_inti]
    queue=[int_inti]
    while(len(queue)>0):
        trav=queue[0]
        if(trav==int_inti):
            s2=str(trav)+"I"
            if(trav<0):
                s2=s2+'F'
        else:
            if(trav<0):
                s2=str(trav)+"F"
            else:
                s2=trav
        li_ins=[0]*(1+2**n)
        li_ins[0]=s2
        del queue[0]
        for i in range(len(lst)):
            li=lst[i]
            subs = []
            for j in range(1,n+1):
                if(n==1):
                    subs.append((exp[j-1],IntVal(li)))
                else:
                    subs.append((exp[j-1],IntVal(li[j-1])))
            h = substitute(g, subs)
            search=eval(str(h))
            search=int(str(search))
            newstate=math.floor((trav-search)/2)
            if newstate not in visit:
                visit.append(newstate)
                queue.append(newstate)   
    
            li_ins[i+1]=newstate
        
        t.add_row(li_ins) 
    
    return t
 

f1=2*x1+x2<=8
print(f1)
t1=pres(f1)
print(t1)
def pres(f1):
    travlist=[]
    count=0
    dummy=f1.arg(0)
    while True:
        if(dummy.num_args()==2):
            if(type(dummy.arg(0))==z3.z3.IntNumRef):
                count=count+1
                break
            else:
                dummy=dummy.arg(0)
                count=count+1
        if(dummy.num_args()==0):
            count=count+1
            break
        if(dummy.num_args()==1):
            count=count+1
            break
    print(count)
    n=count
    if (n==1):
        lst=[0,1]
    else:
        import itertools
        lst = list(itertools.product([0, 1], repeat=n))

    head="State"
    li1=[head]
    for i in range(2**n):
        li1.append(lst[i])
    t=PrettyTable(li1)

    dummy=f1.arg(0)
    print(dummy)
    exp=[]
    
    i=0
    while True:
        if(dummy.num_args()==0):
            exp.append(dummy)
            break
        if(dummy.num_args()==1):
            exp.append(dummy.arg(0))
            break
        if(type(dummy.arg(0))==z3.z3.IntNumRef):
            exp.append(dummy.arg(1))
            break
        if(dummy.arg(1).num_args()==2):
            exp.append(dummy.arg(1).arg(1))
        if(dummy.arg(1).num_args()==0):
            exp.append(dummy.arg(1))
        dummy=dummy.arg(0)

    exp.reverse()
    

    g=f1.arg(0)
    initial=f1.arg(1)
    int_inti=int(str(initial))
    visit=[int_inti]
    queue=[int_inti]
    while(len(queue)>0):
        trav=queue[0]
        if(trav==int_inti):
            s2=str(trav)+"IF"
        else:
            if(trav>=0):
                s2=str(trav)+"F"
            else:
                s2=trav
        li_ins=[0]*(1+2**n)
        li_ins[0]=s2
        del queue[0]
        for i in range(len(lst)):
            li=lst[i]
            subs = []
            for j in range(1,n+1):
                if(n==1):
                    subs.append((exp[j-1],IntVal(li)))
                else:
                    subs.append((exp[j-1],IntVal(li[j-1])))
            h = substitute(g, subs)
            search=eval(str(h))
            search=int(str(search))
            newstate=math.floor((trav-search)/2)
            if newstate not in visit:
                visit.append(newstate)
                queue.append(newstate)   
    
            li_ins[i+1]=newstate
        travlist.append(li_ins)
        t.add_row(li_ins) 
    print(t)
    return travlist


def no(f1):
    count=0
    dummy=f1.arg(0)
    while True:
        if(dummy.num_args()==2):
            if(type(dummy.arg(0))==z3.z3.IntNumRef):
                count=count+1
                break
            else:
                dummy=dummy.arg(0)
                count=count+1
        if(dummy.num_args()==0):
            count=count+1
            break
        if(dummy.num_args()==1):
            count=count+1
            break
    return count

        
def pres2(f1,n,p):
    twod2=[]
    if (n==1):
        lst=[0,1]
    else:
        import itertools
        lst = list(itertools.product([0, 1], repeat=n))

    head="State"
    li1=[head]
    for i in range(2**n):
        li1.append(lst[i])
    t=PrettyTable(li1)
    dummy=f1.arg(0)
    exp=[]
    original=[0]*n
    i=0
    while True:
        if(dummy.num_args()==0):
            exp.append(dummy)
            break
        if(dummy.num_args()==1):
            exp.append(dummy.arg(0))
            break
        if(type(dummy.arg(0))==z3.z3.IntNumRef):
            exp.append(dummy.arg(1))
            break
        if(dummy.arg(1).num_args()==2):
            exp.append(dummy.arg(1).arg(1))
        if(dummy.arg(1).num_args()==0):
            exp.append(dummy.arg(1))
        dummy=dummy.arg(0)

    exp.reverse()
    for i in range(len(exp)):
        original[i]=exp[i]
    for i in range(len(exp),len(original)):
        original[i]=exp[0]
    
    
    g=f1.arg(0)
    initial=f1.arg(1)
    int_inti=int(str(initial))
    visit=[int_inti]
    queue=[int_inti]
    index=0
    while(len(queue)>0):
        trav=queue[0]
        if(trav==int_inti):
            s2=str(trav)+"IF"
        else:
            if(trav>=0):
                s2=str(trav)+"F"
            else:
                s2=trav
        dict2[trav]=index
        li_ins=[0]*(1+2**n)
        li_ins[0]=s2
        del queue[0]
        for i in range(len(lst)):
            li=lst[i]
            subs = []
            for j in range(1,n+1):
                if(n==1):
                    subs.append((original[j-1],IntVal(li)))
                else:
                    subs.append((original[j-1],IntVal(li[j-1])))
            h = substitute(g, subs)
            search=eval(str(h))
            search=int(str(search))
            newstate=math.floor((trav-search)/2)
            if newstate not in visit:
                visit.append(newstate)
                queue.append(newstate)   
            li_ins[i+1]=newstate
        index=index+1
        twod2.append(li_ins)
        
        t.add_row(li_ins)
    if p==0:
        print(t)
    return twod2


def pres1(f1,n,p):
    twod1=[]
    if (n==1):
        lst=[0,1]
    else:
        import itertools
        lst = list(itertools.product([0, 1], repeat=n))

    head="State"
    li1=[head]
    for i in range(2**n):
        li1.append(lst[i])
    t=PrettyTable(li1)
    dummy=f1.arg(0)
    exp=[]
    original=[0]*n
    i=0
    while True:
        if(dummy.num_args()==0):
            exp.append(dummy)
            break
        if(dummy.num_args()==1):
            exp.append(dummy.arg(0))
            break
        if(type(dummy.arg(0))==z3.z3.IntNumRef):
            exp.append(dummy.arg(1))
            break
        if(dummy.arg(1).num_args()==2):
            exp.append(dummy.arg(1).arg(1))
        if(dummy.arg(1).num_args()==0):
            exp.append(dummy.arg(1))
        dummy=dummy.arg(0)

    exp.reverse()
    for i in range(len(exp)):
        original[i]=exp[i]
    for i in range(len(exp),len(original)):
        original[i]=exp[0]
    
    g=f1.arg(0)
    initial=f1.arg(1)
    int_inti=int(str(initial))
    visit=[int_inti]
    queue=[int_inti]
    index=0
    while(len(queue)>0):
        trav=queue[0]
        if(trav==int_inti):
            s2=str(trav)+"IF"
        else:
            if(trav>=0):
                s2=str(trav)+"F"
            else:
                s2=trav
        dict1[trav]=index
        li_ins=[0]*(1+2**n)
        li_ins[0]=s2
        del queue[0]
        for i in range(len(lst)):
            li=lst[i]
            subs = []
            for j in range(1,n+1):
                if(n==1):
                    subs.append((original[j-1],IntVal(li)))
                else:
                    subs.append((original[j-1],IntVal(li[j-1])))
            h = substitute(g, subs)
            search=eval(str(h))
            search=int(str(search))
            newstate=math.floor((trav-search)/2)
            if newstate not in visit:
                visit.append(newstate)
                queue.append(newstate)   
            li_ins[i+1]=newstate
        index=index+1
        twod1.append(li_ins)
        
        t.add_row(li_ins)
    if(p==0):
        print(t)
        
    return twod1


def perform(twod1,twod2,n):
    travlist=[]
    t1_ini=int(twod1[0][0][0])
    t2_ini=int(twod2[0][0][0])
    dict_2={}
    dict_1={}
    for i in range(len(twod2)):
        point=twod2[i][0]
        if(type(point)==int):
            dict_2[point]=i
        else:
            if(point[0]=='-'):
                newst=point[0]+point[1] 
                dict_2[int(newst)]=i
            else:
                dict_2[int(point[0])]=i
            
    for i in range(len(twod1)):
        point=twod1[i][0]
        if(type(point)==int):
            dict_1[point]=i
        else:
            dict_1[int(point[0])]=i
    start=(t2_ini,t1_ini)
    if (n==1):
        lst=[0,1]
    else:
        import itertools
        lst = list(itertools.product([0, 1], repeat=n))

    head="State"
    li1=[head]
    for i in range(2**n):
        li1.append(lst[i])
    t=PrettyTable(li1)
    visit=[]
    queue=[]
    visit.append((t2_ini,t1_ini))
    queue.append((t2_ini,t1_ini))
    index=0
    while(len(queue)>0):
        trav=queue[0]
        travdict[trav]=index
        index=index+1
        s2=str(trav)
        if(trav==start):
            s2=s2+"I"
        if(trav[0]>=0 and trav[1]>=0):
            s2=s2+"F"
        li_ins=[0]*(1+2**n)
        li_ins[0]=s2
        del queue[0]
        for i in range(len(lst)):
            table2=trav[0]
            table1=trav[1]
            row2=dict_2[table2]
            row1=dict_1[table1]
            element=(twod2[row2][i+1],twod1[row1][i+1])
            if element not in visit:
                visit.append(element)
                queue.append(element)
            li_ins[i+1]=element
        travlist.append(li_ins)
        t.add_row(li_ins)
    print(t)
    return travlist

def decimalToBinary(n):
    return bin(n).replace("0b", "")
def binaryToDecimal(n):
    return int(n,2)

def valuefindand(valuelist,travlist):
    rows=len(valuelist)
    trav_dict={}
    #print(travlist)
    for i in range(len(travlist)):
        trav_dict[travlist[i][0]]=i
    #print(trav_dict)
    cols = decimalToBinary(max(valuelist))
    col=len(cols)
    A = []
    for i in range(rows):
        bina=decimalToBinary(valuelist[i])
        li=[]
        for i in range(len(bina)):
            li.append(int(bina[i]))
        li.reverse()
        l=len(li)
        li.extend([0]*(col-l))
        A.append(li)
    search_row=0
    for i in range(col):
        deci=""
        for j in range(rows):
            deci=deci+str(A[j][i])
        search_col=binaryToDecimal(deci)
        nextele=travlist[search_row][search_col+1]
        search_row=travdict[nextele]
    if(nextele[0]>=0 and nextele[1]>=0):
        print("yes")
    else:
        print("no")

    
def perform_and(f1,f2):
    count1=no(f1)
    print(f1)
    t1=pres1(f1,count1,0)

    count2=no(f2)
    print(f2)
    t2=pres2(f2,count2,0)

    dictmax={}
    dictmax[count1]=f1
    dictmax[count2]=f2
    if(count1!=count2):
        if(count1 < count2):
            t1=pres1(f1,count2,1)
        else:
            t2=pres1(f2,count1,1)
    travlist=perform(t1,t2,max(count1,count2))
    return travlist
    

    
x1=Int('x1')
x2=Int('x2')
        
f=eval(input())
n=int(input())
valuelist=[0]*n
for i in range(n):
    valuelist[i]=int(input())  
print(f)
if(f.decl().name()=='and'):
    f1=f.arg(0)
    f2=f.arg(1)
    travlist=perform_and(f1,f2)
    print(travdict)
    valuefindand(valuelist,travlist)
else:
    travlist=pres(f)
    
