u=["U   U"]*4+[" UUU"];d={'C':{0:' CCCC',4:' CCCC',1:'C',2:'C',3:'C'},'L':{4:'L'*5,0:'L',1:'L',2:'L',3:'L'},'O':{0:' OOO',4:' OOO'},'D':{0:'D'*4,4:'D'*4},'U':{}};p=print
for l in range(5):
 for L in d:p(d[L].get(l,u[l].replace("U",L)).ljust(10," "),end="")
 p()
u=["U   U"]*4+[" UUU"];d={'D':{0:'D'*4,4:'D'*4},'V':{3:' V V',4:'  V'},'W':{3:'W '*3,4:' W W'},'H':{2:'H'*5,4:'H   H'},'U':{}};p=print
for l in range(5):
 for L in d:p(d[L].get(l,u[l].replace("U",L)).ljust(10," "),end="")
 p()
import base64,gzip;b=b'ABzY86gn$d0{>HR1_A{T@KJyRe}8`nBNU1i6kLFS%Nec$q1YdaQ51tPO;sx(oDBkK&Q=Hwg(wC)8vxUXJX_-c000';print(gzip.decompress(base64.b85decode(b)).decode())
import re
from sys import*
P,p,o,D=*map(int,argv[1:]),print,{100:0,50:0,20:0,10:0,5:0,1:0}
r=P-p
if r<1:exit(o(0))
for d in sorted(D,reverse=True):
 v=r//d
 if v:r-=d*v;D[d]+=v
o(D)
A=''';print(("A="+("'"*3+A)*2).translate({65:66,66:65}))''';print(("A="+("'"*3+A)*2).translate({65:66,66:65}))
s=input()[::-1];f='NESW'.find;b=f(s[0])
for c in s:b=(b+f(c))/2+(abs(b-f(c))>2)*2
print(b*90)
x=10
x/x
print x
f=open(__file__,"r+")
s=f.read()
f.seek(0)
f.write(s.replace(`x`,`x-1`))
import re
def f(x,V='.*?([aeiouy])'):b,c,v=re.findall('(.*?['+V+'([^'+V+'.*?(['+V,x)[0];return b+c+("pgtvkgbzdfshjlmnqrwx"["bcdfgkpstvzhjlmnqrwx".index(c)]+v)*2
x=10
print x*x/x
f=open(__file__,"r+")
s=f.read()
f.seek(0)
f.write(s.replace(`x`,`x-1`))
import re
from itertools import combinations
from collections import Counter
size = 5
def p(x):print(x,end='')
l={}
for i,c in enumerate(input()):
 if l.get(c,i+9)<i+9:
  p(i-l[c]-1)
 else:
  p(c)
 l[c]=i
from itertools import *
def excl(ns,pr):
    return (i for i in ns if i%pr)
print(sorted(ls, key=lambda x: x%2!=0))
import re
m=re.findall(r'(\+|-|\*|\d+)',input());i=int
while'*'in m:
 j=m.index('*')
 m=m[:j-1]+[i(m[j-1])*i(m[j+1])]+m[j+2:]
while len(m)>1:
 m[:3]=[i(m[0])+i(m[2])]if m[1]=='+'else[i(m[0])-i(m[2])]
print(m[0])
import numpy as np
import cv2
import os
import sys
from time import sleep
from itertools import count
print(x)
def h(n):
 r=0;i=[*range(n)];o=i[:];h=len(i)//2
 while True:
  i=[x for y in map(lambda x:(x[1],x[0]),zip(i[:h],i[h:]))for x in y];r+=1
  if o==i:return r
import re
s="The first of the Force is Forte"
f=re.compile("first|force",2)
n=f.split(s)
y=f.findall(s)
def r(s):
    print("replacing in", s)
    S="ioscteIOSCTEoicsetOICSET"
    for x in zip(S[::2],S[1::2]):
        s=s.replace(*x)
    return s
print(''.join(N+r(Y) for N,Y in zip(n,y))+n[-1])
def h(f,t,n):
 if n!=1:yield from h(f,6-f-t,n-1)
 yield f,t
 if n!=1:yield from h(6-f-t,t,n-1)
for step in h(1,3,int(input())):
 print(step)
import re
lambda x,d='(.)$',o=r'\1':re.sub(*[('$','0'*6),(d,b*6),('(..)$',b*3),('(\w)',b*2),('.'+'(.)'*4,r'#\1\4\2\4\3\4'),(d,b*2),('','')][len(x)-1],x)
import time
s=4*'.'+6*' '
while 1:
 for n in range(10):time.sleep(.1);print('['+(n>0and s[-n:]or'')+s[:10-n],end=']\r')
import bz2
import random
s=4*'.'+6*' '
while 1:print('\r[%s]'%s,end='');time.sleep(.1);s=s[-1]+s[:-1]
def f(A,q="?",u=str.isnumeric):
 print(A)
 e,z=A
 if e+z in(e,z):return""
 o,O,t,T,*x=e[0],e[1:2],z[0],z[1:2],e[1:],z[1:]
 if"?"in o+t:return f([e,x[0]][o==q],z)
 if u(o):
  if u(t):return t+f(x)if O==q!=T else o+f(x)if o==t or T==q!=O else 1
  return o+f(x)
 if u(t):return t+f(x)
def g(s):
 for a,b in zip(map(chr,range(65,91)),"2223334445556667777888999"):s=s.replace(a,b)
 return f(s.split(" / "))
f=lambda x:''.join(map(str,map(s.find,x))if x[0]in s else(s[int(y)]for y in x))
def f(t):
 while len(t)>2:
  m=min(x for x in t if len(t[x])<2);yield t[m][0];del t[m]
  for x in t:m in t[x]and t[x].remove(m)
r=range
x=lambda c,n:print('\n'.join(f' {c} '*i for i in[*r(1,n+1),*r(n-1,1,-1)]))+x(c,n)
lambda t,r:sum(x.count("=")/eval(x.strip("=")) for x in re.findall("\d+\D+",r))>t
n=int(input())
S=sum
l=[1]
i=s=1
while S(l)<n:i+=1;l+=[i]
while S(l)!=n:
 while S(l)>n:l.pop(0)
 s+=1
 if S(l)<n:i+=1;l+=[i];s+=1
print(s)
lambda y:"".join(map(chr,filter(lambda x:not(767<x<880or 6831<x<6912or 7615<x<7680or 8399<x<8448or 65055<x<65072),map(ord,y))))
lambda y:"".join(chr(x)for x in map(ord,y)if not(767<x<880or 6831<x<6912or 7615<x<7680or 8399<x<8448or 65055<x<65072))


lambda y:"".join(s if not any(ord(s)in range(x,x+y)for x,y in[(767,113),(6831,81),(7615,65),(8399,49),(65055,17)])else''for s in y)
lambda y:"".join(y.replace(ord(s),'')for r in[(767,113),(6831,81),(7615,65),(8399,49),(65055,17)] for s in range(*r))
y=input()
for a,b in[(767,113),(6831,81),(7615,65),(8399,49),(65055,17)]:
 for s in range(a,a+b):
  y.replace(chr(s),'')
L=list
M=map
S=sum
Z=zip
Q=len
G,H,J,K,Y,I=[[0,1],[0,-1],[1,0],[-1,0],[-1,1],[1,-1]]
def R(p,u):
 global w,h,e,l,F
 u=[[I,H][u!=G],[H,J][u!=K],[G,J][u!=K],[K,Y][u!=I]][[[0,w],[h,e],[h,0],[l,e]].index(p)]
 p=L(M(S,Z(p,u)))
 return u,p
def U(p,c,u,a):
 global w,h,e,l,F
 F+=c*a
 try:u=[G,J,I,I,Y,K,H][[[0,h],[0,w],[h,w],[h,e],[h,0],[l,0],[l,e]].index(p)]
 except:0
 p=L(M(S,Z(p,u)))
 return F,p,u
def f(a):
 global w,h,e,l,F
 a=L(M(L,a.split('\n')))
 p=[0,0]
 for i in range(Q(a[0])):
    if' '!=a[0][i]:p=[0,i-1];break
 c,P,F,w,h,e,l,t=a[p[0]][p[1]],'><^v/','',Q(a[0])-1,Q(a)//2,Q(a[-1])-1,Q(a)-1,{'v':J,'^':K,'>':G,'<':H}
 C,u,s,r,E=[[0,w],[0,h],[h,w],[h,e],[h,0],[l,0],[l,e]],[G,t.get(c,I)][c in P],0,1,[[0,w-1],[1,w-1],[1,w],[h-1,1],[h,1],[e-2,e+1],[e-2,e]]
 while'1'!=c:
    if s:s=0;u=u[::-1]
    if c in' ,':F,p,u=U(p,c,u,0)
    elif c in P:
     if p in C:
        if'/'==c:
         if[0,h]==p:u=I
         elif p[1]!=w:u=Y
         else:u=I
        else:u=t[c]
        p=L(M(S,Z(p,u)))
     elif p in E:
        if'/'!=c:u=t[c];p=L(M(S,Z(p,u)));s=1
        else:F,p,u=U(p,c,u,1)
     else:
        o=t.get(c,u)
        try:
         n=a[p[0]+o[0]][p[1]+o[1]]
         if(' '!=n)*((p[0]!=0)*('^'==c)):u=o
        except:0
        if u!=t.get(c):F,p,u=U(p,c,u,1)
        else:p=L(M(S,Z(p,u)))
    elif'?'==c:
        if(p not in C)*(F[-1]!=c):F+=c
        if not r:
         if p in[[0,w],[h,e],[h,0],[l,e]]:u,p=R(p,u)
        else:F,p,u=U(p,c,u,0)
        r=not r
    else:F,p,u=U(p,c,u,1)
    c=a[p[0]][p[1]]
 return F.strip().replace(',','')
from itertools import*
s=input()
l=~(~s.find('\n')or~len(s))
s=s.replace('\n','')
a=s.split('\n')
f=lambda k:[(x/l,x%l)for x in range(len(s))if s[x]==k]
h=lambda x,i,j:x[:i]+(x[i]+j,)+x[i+1:]
g=lambda x,i:[(h(q,i,-1),h(q,i,1))for q in x]
d=lambda l,r,c:z((l,c))+z((r,c))==z((l,r))+1
v=f('C')
e=g(f('-'),1)+g(f('|'),0)
E=[V for V in v if sum(e,()).count(V)==1]
j=lambda E,v:E[1-E.index(v)]
o=lambda v:[j(E,v)for E in e if v in E and j(E,v)]
m=lambda p:len(v)if not p else min(p)
def z(n,c=[]):k=[x for x in o(n[0])if x not in c];return 1if n[0]==n[1]else m([z((j,n[1]),c+k)for j in k])+1
Z=lambda a:map(lambda b:z((a[0],b)),a[1])
T=lambda a:lambda b:z((a,b))
C=list(product(E,E))
a=map(z,C)
c=[C[x]for x in range(len(a))if a[x]==max(a)]
t=tuple
s={k:[t(E)for E in v if d(k[0],k[1],E)]for k in c}
n='mepbphhondudetrueeecoenothotnxptncddh p t t   ee          cc'
b=lambda a,e:[x for x in v if z((x,a),e)<len(v)and x not in e]
O=lambda r,n:sorted(n,key=T(r))
F=lambda c:lambda a:Z((a,c)).index(2)
H=[]
R=0
for w in s:R=max(len(s[w]),R);s[w]=O(w[0],s[w]);a=sum([list(set(o(k))-set(s[w]))for k in s[w]],[]);H+=[zip(*[map(F(s[w]),a)]+[map(Z,[(A,b(A,s[w]))for A in a])])]
if not any(H):print n[R-1::12].strip()+'ane';exit(0)
H=[h for h in H if len(h)==max(map(len,H))]
K=[[h[0]for h in Q]for Q in H]
H=[H[i]for i in range(len(K))if K[i]==min(K)]
K=[[len(J[1])for J in j]for j in H]
H=[H[i]for i in range(len(K))if min(K[i])==min(sum(K,[]))]
K=[len([J[1]for J in j if len(set(J[1]))!=len(J[1])])for j in H]
G=lambda a:n[max(a)-1::12].strip()+'yl'if sorted(a)==range(1,1+max(a))else['isopropyl','butyl-tert','butyl-sec','isobutyl'][len(a)+a.count(3)-3]
H=[[p[0]+1,G(p[1])]for p in [H[i]for i in range(len(K))if K[i]==min(K)][0]]
print'-'.join([','.join([`k[0]`for k in H if k[1]==x])+'-'+'-'.join(x.split('-')[::-1])for x in sorted(list(set(zip(*H)[1])))])+n[R-1::12].strip()+'ane'
z=len
M=max
r=range
def q(a,l,x,y,b):l[y][x]=b[(b.index(l[y][x])+a)%z(b)]
h=' -='
v=' |"'
s=input()
p=z(s[0])
X=M(0,(z(s)-1)/2-p)
Y=M(0,(p-1)/2-z(s))
S=[[' ']*X+k+[' ']*X for k in s]
g=lambda:[[' ']*z(S[0])for i in r(Y)]
S=g()+S+g()
P=z(S[0])
for i in r(X+2,X+p-2):q(-1,S,i,Y,h);q(1,S,i,min(Y+i-X-1,Y+P-i-X-2),h);q(-1,S,i,z(S)-Y-1,h);q(1,S,i,M(z(S)-Y-i,z(s)-p+Y+i+1),h)
for j in r(Y+2,Y+z(s)-2):q(-1,S,X,j,v);q(1,S,min(X+j-Y-1,X+z(S)-j-Y-2),j,v);q(-1,S,P-X-1,j,v);q(1,S,M(P-X-j,p-z(s)+X+j+1),j,v)
print'\n'.join(map(''.join,S))
