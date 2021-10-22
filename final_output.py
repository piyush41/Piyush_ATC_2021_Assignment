import math
from prettytable import PrettyTable
from z3 import *
travdict={}
show=0
def decimalToBinary(n):
    return bin(n).replace("0b", "")
def binaryToDecimal(n):
    return int(n,2)

def notoperator(travlist):
    
    for i in range(len(travlist)):
        rep=travlist[i][0]
        if(rep.find('F')==-1 and rep!="Err"):
            rep=rep+'F'
        else:
            rep=rep.replace("F","")
        travlist[i][0]=rep
    cols=int(math.log(((len(travlist[0]))-1),2))
    n=cols
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
    for i in range(len(travlist)):
        t.add_row(travlist[i])
    print(t)
    return travlist


def pres(f1):
    print(f1)
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
    
    exp=[]
    error=0
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
    operator=f1.decl().name()
   
    initial=f1.arg(1)
    int_inti=int(str(initial))
    visit=[int_inti]
    queue=[int_inti]
    while(len(queue)>0):
        trav=queue[0]
        
        if(trav==int_inti):
            s2=str(trav)+"I"
            if(trav>=0 and operator== "<="):
                s2=s2+'F'
            if(trav==0 and operator== "="):
                s2=s2+'F'
        else:
            if(trav>=0 and operator== "<="):
                
                s2=str(trav)+"F"
            elif(trav==0 and operator== "="):
                s2=str(trav)+"F"
            else:
                s2=str(trav)
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
            if(operator=="<="):
                newstate=math.floor((trav-search)/2)
                if newstate not in visit:
                    visit.append(newstate)
                    queue.append(newstate)   
                li_ins[i+1]=newstate
            else:
                if(search%2==trav%2):
                    newstate=math.floor((trav-search)/2)
                    if newstate not in visit:
                        visit.append(newstate)
                        queue.append(newstate)  
                    li_ins[i+1]=newstate
                else:
                    li_ins[i+1]="Err"
                    error=1       
        travlist.append(li_ins)
        t.add_row(li_ins) 
    if(error==1):
        li_ans=[]
        for lp in range(len(li_ins)):
            li_ans.append("Err")
        t.add_row(li_ans)
        travlist.append(li_ans)
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

    

def pres1equal(f1,n,p):
    print(f1)
    output=[]
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
    
    operator=f1.decl().name()
    
    g=f1.arg(0)
    initial=f1.arg(1)
    int_inti=int(str(initial))
    visit=[int_inti]
    queue=[int_inti]
    index=0
    error=0
    while(len(queue)>0):
        trav=queue[0]
        if(trav==int_inti):
            s2=str(trav)+"I"
            if(trav>=0 and operator== "<="):
                s2=s2+'F'
            if(trav==0 and operator== "="):
                s2=s2+'F'
                
        else:
            if(trav>=0 and operator== "<="):
                s2=str(trav)+"F"
            elif(trav==0 and operator== "="):
                s2=str(trav)+"F"
            else:
                s2=str(trav)
                
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
            
            
            if(operator=="<="):
                newstate=math.floor((trav-search)/2)
                if newstate not in visit:
                    visit.append(newstate)
                    queue.append(newstate)   
                li_ins[i+1]=newstate
            else:
                if(search%2==trav%2):
                    newstate=math.floor((trav-search)/2)
                    if newstate not in visit:
                        visit.append(newstate)
                        queue.append(newstate)  
                    li_ins[i+1]=newstate
                else:
                    li_ins[i+1]="Err"
                    error=1       
        twod1.append(li_ins)
        t.add_row(li_ins)
    if(error==1):
        li_ans=[]
        for lp in range(len(li_ins)):
            li_ans.append("Err")
        t.add_row(li_ans)
        twod1.append(li_ans)
    
    if(p==0):
        print(t)
    output.append(twod1)
    output.append(exp)
    return output

def pres1(f1,n,p):
    output=[]
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
                s2=str(trav)
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
    output.append(twod1)
    output.append(exp)
    return output


def perform(twod1,twod2,n):
    travlist=[]
    
    t1_ini=twod1[0][0]
    t2_ini=twod2[0][0]
    if(t1_ini.find('I')!=-1):
        t1_ini=t1_ini.replace("I","")
    if(t1_ini.find('F')!=-1):
        t1_ini=t1_ini.replace("F","")
    if(t2_ini.find('I')!=-1):
        t2_ini=t2_ini.replace("I","")
    if(t2_ini.find('F')!=-1):
        t2_ini=t2_ini.replace("F","")
    
    t1_ini=eval(t1_ini)
    t2_ini=eval(t2_ini)
    dict_2={}
    dict_1={}
    output1=[]
    output2=[]
    for i in range(len(twod2)):
        point=twod2[i][0]
        if(type(point)==int):
            dict_2[point]=i
        else:
            if(point.find('I')!=-1):
                point=point.replace("I","")
            if(point.find('F')!=-1):
                point=point.replace("F","")
                output2.append(eval(point))
            if(point=="Err"):
                dict_2[point]=i
            else:
                dict_2[eval(point)]=i
                
            
    for i in range(len(twod1)):
        point=twod1[i][0]
        if(type(point)==int):
            dict_1[point]=i
        else:
            if(point.find('I')!=-1):
                point=point.replace("I","") 
            if(point.find('F')!=-1):
                point=point.replace("F","")
                output1.append(eval(point))
            if(point=="Err"):
                dict_1[point]=i
            else:
                dict_1[eval(point)]=i
    
    mt1=t1_ini
    mt2=t2_ini
    if(type(t1_ini)==int):
        mt1=(t1_ini,)
    if(type(t2_ini)==int):
        mt2=(t2_ini,)
    r=(mt2,mt1)
    start=sum(r, ())
    n1=1
    n2=1
    if(type(t1_ini)==tuple):
        n1=len(t1_ini)
    if(type(t2_ini)==tuple):
        n2=len(t2_ini)
    
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
    visit.append(start)
    queue.append(start)
    index=0
    while(len(queue)>0):
        trav=queue[0]
        
        if(len(trav)==2):
            table2=trav[0]
            table1=trav[1]
        else:
            if(n2>1):
                table2=trav[:n2]
            else:
                table2=trav[0]
            if(n1>1):
                table1=trav[n2:]
            else:
                table1=trav[-1]
        
        travdict[trav]=index
        index=index+1
        s2=str(trav)
        if(trav==start):
            s2=s2+"I"
        if(table2 in output2):
            if(table1 in output1):
                s2=s2+"F"
        li_ins=[0]*(1+2**n)
        li_ins[0]=s2
        del queue[0]
        for i in range(len(lst)):
          
            row2=dict_2[table2]
            row1=dict_1[table1]
            
            mt1=twod1[row1][i+1]
            mt2=twod2[row2][i+1]
            
            if(type(mt1)==int or type(mt1)==str):
                mt1=(mt1,)
            if(type(mt2)==int or type(mt2)==str):
                mt2=(mt2,)
            r=(mt2,mt1)
            element=sum(r, ())
            if element not in visit:
                visit.append(element)
                queue.append(element)
            li_ins[i+1]=element
        travlist.append(li_ins)
        t.add_row(li_ins)
    print(t)
    return travlist



def valuefindand(valuelist,travlist):
    
    rows=len(valuelist)
    trav_dict={}
    output=[]
    for i in range(len(travlist)):
        point=travlist[i][0]
        if(point.find('F')!=-1):
            if(point.find('I')!=-1):
                pointnew=point.replace("IF","")
            else:
                pointnew=point.replace("F","")
            trav_dict[pointnew]=i
            output.append(pointnew)
        else:
            trav_dict[point]=i
    

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
        search_row=trav_dict[str(nextele)]
    nextele=str(nextele)
    
    if(nextele in output):
        print("The output after assigning the value into the automata is yes")
    else:
        print("The output after assigning the value into the automata is no")

def extendtable(travlist,n,secondlist):
    newtravlist=[] 
    if (n==1):
        lst=[0,1]
    else:
        import itertools
        lst = list(itertools.product([0, 1], repeat=n))
    
    for i in range(len(travlist)):
        li_ins=[0]*(1+2**n)
        li_ins[0]=travlist[i][0]
        for j in range(len(lst)):
            checktu=lst[j]
            bi=""
            for k in range(len(secondlist)):
                if(secondlist[k]==1):
                    bi=bi+str(checktu[k])
            
            newcol=binaryToDecimal(bi)
            li_ins[j+1]=travlist[i][newcol+1]
        newtravlist.append(li_ins)
    
    return newtravlist
            
def perform_not_inside(f1):
    if(f1.decl().name()=='not'):
        pair=perform_not_inside(f1.arg(0))    
    else:
        count1=no(f1)
        pair=pres1equal(f1,count1,0)
    print(Not(f1))
    listof=notoperator(pair[0])
    return pair        
    
def perform_and(f1,f2):
    if(f1.decl().name()=='and'):
        lol1=perform_and(f1.arg(0),f1.arg(1))
        
    elif(f1.decl().name()=='not'):
        
        lol1=perform_not_inside(f1.arg(0))       
    else:
        count1=no(f1)
        lol1=pres1equal(f1,count1,0)
    
    if(f2.decl().name()=='and'):
        lol2=perform_and(f2.arg(0),f2.arg(1))
    elif(f2.decl().name()=='not'):
        lol2=perform_not_inside(f2.arg(0))         
    else:
        count2=no(f2)
        lol2=pres1equal(f2,count2,0)
    
    t1=lol1[0]
    t2=lol2[0]
    variable1=lol1[1]
    variable2=lol2[1]
    #print(variable1)
    #print(variable2)
    nv1=len(variable1)
    nv2=len(variable2)
    
    final_list = list(set(variable1) | set(variable2))
    ulen=len(final_list)

    newlist1=[2]*len(final_list)
    newlist2=[2]*len(final_list)
    
    newlist=[2]*ulen
    
    proper_dict={}
    final_list_string=[]
    for i in range(len(final_list)):
        proper_dict[str(final_list[i])]=final_list[i]
        final_list_string.append(str(final_list[i]))
    
    final_list_string.sort()
    
    for i in range(len(final_list)):
        final_list[i]=proper_dict[final_list_string[i]]
    
    for i in range(len(final_list)):
        if(final_list[i]in variable1):
            newlist1[i]=1
        else:
            newlist1[i]=0
        
        if(final_list[i]in variable2):
            newlist2[i]=1
        else:
            newlist2[i]=0
    
    
    if(nv1<ulen):
        t1=extendtable(t1,ulen,newlist1) 
    if(nv2<ulen):
        t2=extendtable(t2,ulen,newlist2)
    #if(count1!=count2):
        #if(count1 < count2):
            #lol1=pres1(f1,count2,1)
            #t1=lol1[0]
        #else:
            #lol2=pres1(f2,count1,1)
            #t2=lol2[0]
    outputand=[]
    print(And(f1,f2))
    travlist=perform(t1,t2,ulen)
    outputand.append(travlist)
    maxvariable=final_list
    outputand.append(maxvariable)
    
    return outputand
    
def findvalue(valuelist,travlist):
    rows=len(valuelist)
    dict_2={}
    #print(travlist)
    output=[]
    
    for i in range(len(travlist)):
        point=travlist[i][0]
        if(type(point)==int):
            dict_2[point]=i
        else:
            if(point=="Err"):
                dict_2[point]=i
                #output.append(point)
            elif(point[0]=='-'):
                newst=point[0]+point[1] 
                dict_2[int(newst)]=i
                if(point.find('F')!=-1):
                    output.append(int(newst))
            else:
                dict_2[int(point[0])]=i
                if(point.find('F')!=-1):
                    output.append(int(point[0]))
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
        search_row=dict_2[nextele]
    if(nextele in output):
        print("yes")
    else:
        print("no")
def perform_not(f1):
    if(f1.decl().name()=='not'):
        travlist=perform_not(f1.arg(0))    
    elif(f1.decl().name()=='and'):
        f3=f1.arg(0)
        f4=f1.arg(1)
        listof=perform_and(f3,f4)
        travlist=listof[0]
    else:
        
        travlist=pres(f1)
    print(Not(f1))
    listof=notoperator(travlist)
    return listof
        
def inductive(f,n,valuelist):
    if(f.decl().name()=='and'):
        f1=f.arg(0)
        f2=f.arg(1)
        
        listof=perform_and(f1,f2)
        #print(travdict)
        valuefindand(valuelist,listof[0])
    elif(f.decl().name()=='not'):
        f1=f.arg(0)
        listof=perform_not(f1)
        valuefindand(valuelist,listof)
    else:
        travlist=pres(f)
        valuefindand(valuelist,travlist)
        
               
x1=Int('x1')
x2=Int('x2')
x3=Int('x3')
x4=Int('x4')
x5=Int('x5')
x6=Int('x6')
#f=Not((Not(2*x1+x2<=5)))     
#f=Not(And(x1+x2==10,x2==6))
#f=Not(And(And(x1==4,x1 + x2 == 7),And(x2<=2,x1+x2<=6)))
#f=And(Not(x1 + x2 <= 5), x2 <= 6)

#valuelist=[2,3]
#n=2

f=eval(input())
n=int(input())
valuelist=[0]*n
for i in range(n):
    valuelist[i]=int(input())
inductive(f,n,valuelist)
