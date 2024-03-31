#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import matplotlib.pyplot as plt
x=int(input("Enter your monthly salary:"))
y=int(input("Enter expected savings from each month:"))
f=int(input("Enter house rent:"))
a=int(input("Enter current bill:"))
b=int(input("Enter credit card bills and EMI payments"))
c=int(input("Enter Ration bill"))
d=int(input("Enter medical emergency expenses(if any):"))
e=int(input("Enter personal expenses or purchases:"))
l=[]
for i in range(4):
    inpt=int(input("Enter weekly expenditure:"))
    l.append(inpt)
X=np.array([1,2,3,4])
Y=np.array(l)
print(Y)
print("CONGRATULATIONS, YOU HAVE REACHED THE END OF THE MONTH.\nHere is your budget analysis:")
f1={'family':'goudy stout','color':'black','size':30}
f2={'family':'serif','color':'blue','size':20}
plt.title("WEEKLY EXPENDITURE ANALYSIS",fontdict=f1,loc='center')
plt.xlabel("WEEK COUNT",fontdict=f2)
plt.ylabel("AMOUNT SPENT",fontdict=f2)
plt.bar(X,Y)
plt.show()
print("Total weekly expenses",sum(l))
P=np.array([a,b,c,d,e,f,sum(l)])
Q=np.array(['current bill','CCB & EMI','Ration','Medical expenses','personal expenses','House rent','weekly expenses'])
myexplode=[0.1,0.1,0.1,0.1,0.1,0.1,0.1]
plt.pie(P,labels=Q,explode=myexplode)
plt.legend(title='BUDGET ANALYSIS')
plt.show()
total_expenditure_of_the_month=(a+b+c+d+e+f+sum(l))
print("TOTAL EXPENDITURE OF THE MONTH:",total_expenditure_of_the_month)
A=x-total_expenditure_of_the_month
print("SAVINGS MADE FOR THIS MONTH:",A)
amount_saved=np.array([y,A])
mylabel=np.array(['Expected savings','actual savings'])
plt.pie(amount_saved,labels=mylabel)
plt.legend(title='SAVING ANALYSIS')
plt.show()
if(A<y):
    print("MAKE SURE TO SAVE MONEY REGULARLY FROM NEXT MONTH\nYOU HAVE NOT SAVED ENOUGH MONEY THIS MONTH\nTARGET NOT ACCOMPLISHED")
else:
    print("CONGRULATIONS, YOU HAVE REACHED THE TARGET, KEEP SAVING MONEY!")


# 

# In[ ]:




