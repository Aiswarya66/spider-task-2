#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


def cal(a):                                 #task 2A
    n=len(a)
    i=j=0
    while((i<n)&(j>=0)):
        if(a[i]=='<'):
            j+=1
        elif(a[i]=='>'):
            j-=1
        i+=1
    if(i%2==0):
        return(i)
    else:
        return(i-1)
t=int(input()) #input number of strings
for i in range(t):
    if((t>=1)&(t<=500)):
        a=input().split()
        n=len(a);n1=t*n
        if((n>=1)&(n<=10**6)&(n1<=5*10**6)):
            print(cal(a))


# In[1]:


#task 2(B) Basic mode
n=int(input())
q=int(input())
a=[]
for i in range(n):
    a.append(i+1)
for j in range(q):
    b=list(map(int,input().split()))[:3]
    l=b[0];r=b[1];k=b[2]    
    i=l-1
    while(i<r):
        a[i]+=k
        i+=1
if((n in range(1,10**5+1))&(q in range(1,101))):
    print(max(a))


# In[1]:


#task 2(B) hacker mode(1)
n=int(input())
q=int(input())
a=[]
for i in range(n):
    a.append(i+1)
for j in range(q):
    b=list(map(int,input().split()))[:3]
    l=b[0];r=b[1];k=b[2]
    i=l-1
    while(i<r):
        a[i]+=k
        i+=1
if((n in range(1,10**5+1))&(q in range(1,10**5+1))):
    print(max(a))


# In[ ]:




