import io
import numpy as np

Data=[]
def get_info():
    url="E:\\code\\CART1.txt"
    source=open(url,"r",encoding='utf-8')
    for line in source.readlines():  
       line=line.strip('\n')  
       line=line.split(",")
       line=line[1::]
       for i in range(len(line)):
           line[i]=line[i].strip()
       Data.append(line)
    print(Data)
       

       

class Treenode:
    attr=''#大属性
    attrj=''#大属性中的分支
    lefttree=''
    righttree=''
    gini=0
    flag=''
    def __init__(self,attr,attrj,gini,lefttree,righttree):
        self.attr=attr
        self.attrj=attrj
        self.lefttree=lefttree
        self.righttree=righttree
        self.gini=gini
#计算基尼指数构造树，停止条件当数据集中只有一个属性时

def get_gini(D,attr):
    types = {}
    index= D[0].index(attr)
    for li in D[1::]:
        if(li[index] in types):
            types[li[index]]+=1
        else:
            types[li[index]]=1
    min_gini=np.inf
    min_attr=''
    for key in types.keys():
        D1,D2=dividedata(D,key,attr)
        gini=(types[key]*Gini(D1)+ (len(D)-1-types[key])*Gini(D2))/len(D)
        if(min_gini>=gini):
           min_gini=gini
           min_attr=key
    #得到最小的基尼指数属性
    return min_gini,min_attr

def Gini(data):
    coun=0
    for li in data:
        if(li[-1]=='是'):
            coun=coun+1
    return 2*(coun/len(data))*(1-coun/len(data))

def recursion(D):
     #判断是否到达停止条件

    m_g=np.inf
    m_a=''
    m_k=''
    if(len(D)==0):
        return ''
    le=len(D[0])-2
    for attr in D[0][0:le]:
        gini,key= get_gini(D,attr)
        if(m_g>=gini):
           m_g=gini
           m_k=key
           m_a=attr
    #构造最优切分节点

    sum=0
    for l in D[1::]:
        if(l[-1].encode(encoding="utf-8")=='是'.encode(encoding="utf-8")):
            sum=sum+1
            

    if(sum==0):
        T=Treenode(m_a,m_k,m_g,'','')
        T.flag='否'
        print("$$$$$$$$$$$$$$$$$$$")
        return T
    if(sum==len(D)-1):
        T=Treenode(m_a,m_k,m_g,'','')
        T.flag='是'
        print("#################")
        return T
    else:
        Da,Db=dividedata2(D,m_k,m_a)
        T=Treenode(m_a,m_k,m_g,recursion(Da),recursion(Db))
        print(Da)
        print(Db)
        return  T

   
    
def dividedata(data,key,attr):
    D1=[]
    D2=[]
    D1.append(data[0])
    D2.append(data[0])
    Da=data
    index= Da[0].index(attr)
    for li in  Da[1::]:
        if(li[index]==key):
            D1.append(li)
        else:
            D2.append(li)
    return D1,D2

def dividedata2(data,key,attr):
    
    D1=[]
    D2=[]
    if(attr==''):
        return D1,D2
    D1.append(data[0].copy())
    D2.append(data[0].copy())
    Da=data
    index= Da[0].index(attr)
    for li in  Da[1::]:
        if(li[index]==key):
            D1.append(li.copy())
        else:
            D2.append(li.copy())
    for li in D1:
        del li[index]
    for li in D2:
        del li[index]
        

    return D1,D2


get_info()
Tree=recursion(Data)
laber=[]
def main():
    url="E:\\code\\CART1test.txt"
    source=open(url,"r",encoding='utf-8')
    test_data=[]
    for line in source.readlines():  
       line=line.strip('\n')  
       line=line.split(",")
       for i in range(len(line)):
           line[i]=line[i].strip()
       test_data.append(line)
    laber.append(test_data[0])
    print(laber)
    for li in test_data[1::]:
        test(li,Tree)

def test(data,tree):
    if(tree.lefttree=='' or tree.righttree=='' ):
        print(tree.flag)
        return
    index=laber[0].index(tree.attr)
    if(data[index]==tree.attrj):
        test(data,tree.lefttree)
    else:
        test(data,tree.righttree)

main()
