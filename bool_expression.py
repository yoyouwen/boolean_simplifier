from sympy import *
from sympy.logic.boolalg import to_cnf,to_dnf
from sympy.logic import simplify_logic
import sys
def count_str(str):
    dic={}
    for i in str:
        dic[i]=str.count(i,0)
    return dic





f=open(sys.argv[1],'r')

list= f.readlines()
result=False
for i in range(0, len(list)):
    partial_result=True
    list[i]=list[i].replace("Boolean expr: ","")
    list[i]=list[i].replace(" ","")
    list[i]=list[i].replace("AND","")
    begin=0
    end=0
    #print(list[i])
    while(begin<len(list[i])):
        
        end=list[i].find("=",begin)
        if (end==-1):
            break
        #print(begin,end)
        if (list[i][end+1]=='T'):
            partial_result=partial_result & symbols(list[i][begin:end])
        else:
            partial_result=partial_result & ~ symbols(list[i][begin:end])
        begin=end+2

    result=result | partial_result
print(to_dnf(result, simplify=True))
print(to_cnf(result, simplify=True))