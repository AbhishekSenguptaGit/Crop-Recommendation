import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier()
data=pd.read_csv(r'C:\Users\admin\AppData\Local\Programs\Python\Python36\Techie\Crop recommendation system\Crop_dataset.csv',index_col=False)
da=np.array(data)
crop=da[:,0:1]
state=da[:,1:2]
a2_fl=da[:,2:3]#total_cost-labour cost
cc=da[:,3:4]#actual cost or commission for agricultural cost and prices
production=da[:,4:5]
cyield=da[:,5:6]
def Cr():
    cpy=input('1.Cultivation Cost,2.Production Cost,3.Yield input')
    if(cpy=='1'):
        cul=input('press 1 for actual cost(cc),2 for total cost-labour cost')
        if(cul=='1'):
            print('Actual Cost to be between',min(cc),'and',max(cc))
            ip=int(input('Enter the amount farmer can invest in cultivation'))
            m=(ip<=max(cc))&(ip>=min(cc))
            if(m==True):
                inde=np.where(m)
                f=cc
        elif(cul=='2'):
            print('totalcost-labourcost to be between',min(a2_fl),'and',max(a2_fl))
            ip=int(input('Enter the amount farmer can invest in cultivation'))
            m=(ip<=max(a2_fl))&(ip>=min(a2_fl))
            if(m==True):
                inde=np.where(m)
                f=a2_fl
        Trained=clf.fit(f,l)
        res=Trained.predict([[ip]])
        print(res)
    elif(cpy=='2'):
        print(('Production cost to be between',min(production),' and ',max(production)))
        ip=int(input('Enter the amount farmer can expect from production'))
        m=(ip<=max(production))&(ip>=min(production))
        if(m==True):
            inde=np.where(m)
            f=production
            Trained=clf.fit(f,l)
            res=Trained.predict([[ip]])
            print(res)
    elif(cpy=='3'):
         ip=int(input('Enter the amount farmer can expect in yeild'))
         m=(ip<=max(cyield))&(ip>=min(cyield))
         if(m==True):
             inde=np.where(m)
             f=cyield
             Trained=clf.fit(f,l)
             res=Trained.predict([[ip]])
             print(res)
    else:
        print('Wrong Input')
q=1
while(q):
    inp=input('press 1 for crop,2 for state output')
    if(inp=='1'):
        l=crop
        a=Cr()
        yn=input('Do you want the coressponding states of the crop y/n:')
        if(yn=='y'):
            crop_input=input('Renter the crop output')
            m=(crop_input in crop)
            if(m==True):
                ind=np.where(crop==crop_input)
                print(state[ind])
                x=cc[ind]
                y=a2_fl[ind]
                z=cyield[ind]
                w=production[ind]
                cpy=input('Enter 1 for cultivation cost of the crop 2 for production and 3 for yield 4 to exit')
                a1=[]
                a2=[]
                if(cpy=='1'):
                    a1=cc[ind]
                    a2=a2_fl[ind]
                    b1=max(a1)
                    b2=max(a2)
                    c1=min(a1)
                    c2=min(a2)
                    print(a1,a2)
                    print('Maximun cultivation cost',b1,b2)
                    print('Minimum Cultivation cost',c1,c2)
                    di=input('Do you want the diagramatic representation y-yes, n-no')
                    if(di=='y'):
                        fig1,ax1=plt.subplots()
                        ax1.pie(a2_fl[ind],labels=state[ind],autopct='%1.1f%%',shadow=True,startangle=90)
                        ax1.axis('equal')
                        ax1.set_title("Cost of Cultivation A2+FL")
                        plt.show()
                        fig2,ax2=plt.subplots()
                        ax2.pie(cc[ind],labels=state[ind],autopct='%1.1f%%',shadow=True,startangle=90)
                        ax2.axis('equal')
                        ax2.set_title("Cost of Cultivation CC")
                        plt.show()
                    else:
                        pass
                elif(cpy=='2'):
                    a1=production[ind]
                    b=max(a1)
                    c=min(a1)
                    print(a1)
                    print('Maximum Production cost',b)
                    print('Minimum Production cost',c)
                    di=input('Do you want the diagramatic representation y-yes, n-no')
                    if(di=='y'):
                        fig1,ax1=plt.subplots()
                        ax1.pie(production[ind],labels=state[ind],autopct='%1.1f%%',shadow=True,startangle=90)
                        ax1.axis('equal')
                        ax1.set_title("Cost of Production")
                        plt.show()
                elif(cpy=='3'):
                    a1=cyield[ind]
                    b=max(a1)
                    c=min(a1)
                    print(a1)
                    print('Maximum Yield',b)
                    print('Minimum Yield',c)
                    di=input('Do you want the diagramatic representation y-yes, n-no')
                    if(di=='y'):
                        fig1,ax1=plt.subplots()
                        ax1.pie(cyield[ind],labels=state[ind],autopct='%1.1f%%',shadow=True,startangle=90)
                        ax1.axis('equal')
                        ax1.set_title("Yield")
                        plt.show()
                elif(cpy=='4'):
                    q=0
                    break
                else:
                    print('Wrong Input')
                    q=0
                    break
            else:
                print('Crop does not exist in the database')
                q=0
                break

    elif(inp=='2'):
        l=state
        b=Cr()
        yn=input('Do you want the coressponding crops of that state y/n:')
        if(yn=='y'):
            state_input=input('Renter the state output')
            n=(state_input in state)  
            if(n==True):
                ind=np.where(state==state_input)
                print(crop[ind])
                new=int(input('Press 1 to continue and 0 to exit'))
                if(new==0):
                    q=0
                    break
                cpy=input('Enter 1 for cultivation cost of the crop 2 for production and 3 for yield 4 to exit')
                a1=[]
                a2=[]
                if(cpy=='1'):
                    a1=cc[ind]
                    a2=a2_fl[ind]
                    b1=max(a1)
                    b2=max(a2)
                    c1=min(a1)
                    c2=min(a2)
                    print(a1,a2)
                    print('Maximum cultivation cost',b1,b2)
                    print('Minimum cultivation cost',c1,c2)
                    di=input('Do you want the diagramatic representation y-yes, n-no')
                    if(di=='y'):
                        fig1,ax1=plt.subplots()
                        ax1.pie(a2_fl[ind],labels=crop[ind],autopct='%1.1f%%',shadow=True,startangle=90)
                        ax1.axis('equal')
                        ax1.set_title("Cost of Cultivation A2+FL")
                        plt.show()
                        fig2,ax2=plt.subplots()
                        ax2.pie(cc[ind],labels=crop[ind],autopct='%1.1f%%',shadow=True,startangle=90)
                        ax2.axis('equal')
                        ax2.set_title("Cost of Cultivation CC")
                        plt.show()

                elif(cpy=='2'):
                    a1=production[ind]
                    b=max(a1)
                    c=min(a1)
                    print(a1)
                    print('Maximum Production cost',b)
                    print('Minimum Production cost',c)
                    di=input('Do you want the diagramatic representation y-yes, n-no')
                    if(di=='y'):
                        fig1,ax1=plt.subplots()
                        ax1.pie(production[ind],labels=crop[ind],autopct='%1.1f%%',shadow=True,startangle=90)
                        ax1.axis('equal')
                        ax1.set_title("Cost of Production")
                        plt.show()
                elif(cpy=='3'):
                    a1=cyield[ind]
                    b=max(a1)
                    c=min(a1)
                    print(a1)
                    print('Maximum Yield',b)
                    print('Minimum Yield',c)
                    di=input('Do you want the diagramatic representation y-yes, n-no')
                    if(di=='y'):
                        fig1,ax1=plt.subplots()
                        ax1.pie(cyield[ind],labels=crop[ind],autopct='%1.1f%%',shadow=True,startangle=90)
                        ax1.axis('equal')
                        ax1.set_title("Yield")
                        plt.show()
                elif(cpy=='4'):
                    q=0
                    break
                else:
                    print('Wrong Input')
                    q=0
                    break
            elif(state_input=='0'):
                q=0
                break
            else:
                print('This state does not produce any crop')
                q=0
                break
    else:
        print('Wrong input')
        q=0
        break
        



           
