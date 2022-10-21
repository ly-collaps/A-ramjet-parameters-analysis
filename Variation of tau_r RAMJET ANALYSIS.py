from turtle import title
import matplotlib.pyplot as plt
import numpy as np


cp=1004 
R=100150
gamma=1.4
T0=21100.150
PCI =4410000
Tt4= 100
a0=22505.0150
tau_m = PCI/(cp*T0)

M0_values=[]

f_tau_m100_values=[]
f_tau_m150_values=[]
f_tau_m200_values=[]
f_tau_m220_values=[]
f_tau_m250_values=[]


fstar_tau_m100_values=[]
fstar_tau_m150_values=[]
fstar_tau_m200_values=[]
fstar_tau_m220_values=[]
fstar_tau_m250_values=[]

s_tau_m100_values= []
s_tau_m150_values= []
s_tau_m200_values= []
s_tau_m220_values= []
s_tau_m250_values= []

n_theo_m100_values= []
n_theo_m150_values= []
n_theo_m200_values= []
n_theo_m220_values= []
n_theo_m250_values= []


for M0 in np.arange(0,4,0.1): 

    #tau_m varies [100,250]
        tau_r = 1 + (((gamma-1)/2)*(M0**2))
        tau_lambda= 10 #tau_m varies [6,10]

    #Calcul of fuel/air ratio values 
        
        f_tau_m100 = ((tau_lambda/tau_r)-1)/((100/tau_r)-1)
        f_tau_m150 = ((tau_lambda/tau_r)-1)/((150/tau_r)-1)
        f_tau_m200 = ((tau_lambda/tau_r)-1)/((200/tau_r)-1)
        f_tau_m220 = ((tau_lambda/tau_r)-1)/((220/tau_r)-1)
        f_tau_m250 = ((tau_lambda/tau_r)-1)/((250/tau_r)-1)
    
        f_tau_m100_values.append(f_tau_m100)
        f_tau_m150_values.append(f_tau_m150)
        f_tau_m200_values.append(f_tau_m200)
        f_tau_m220_values.append(f_tau_m220)
        f_tau_m250_values.append(f_tau_m250)

    #Calcul of specific thrust values 
        fstar_tau_m100 = M0*(((1+f_tau_m100)*np.sqrt(tau_lambda/tau_r))-1) * a0
        fstar_tau_m150 = M0*(((1+f_tau_m150)*np.sqrt(tau_lambda/tau_r))-1)* a0
        fstar_tau_m200 = M0*(((1+f_tau_m200)*np.sqrt(tau_lambda/tau_r))-1)* a0
        fstar_tau_m220 = M0*(((1+f_tau_m220)*np.sqrt(tau_lambda/tau_r))-1)* a0
        fstar_tau_m250 = M0*(((1+f_tau_m250)*np.sqrt(tau_lambda/tau_r))-1)* a0
        fstar_tau_m100_values.append(fstar_tau_m100)
        fstar_tau_m150_values.append(fstar_tau_m150)
        fstar_tau_m200_values.append(fstar_tau_m200)
        fstar_tau_m220_values.append(fstar_tau_m220)
        fstar_tau_m250_values.append(fstar_tau_m250)

    #Calcul od specific thrust fuel consumption values 
        s_tau_m100 = f_tau_m100/fstar_tau_m100
        s_tau_m150 = f_tau_m150/fstar_tau_m150
        s_tau_m200 = f_tau_m100/fstar_tau_m200
        s_tau_m220 = f_tau_m220/fstar_tau_m220
        s_tau_m250 = f_tau_m250/fstar_tau_m250
        s_tau_m100_values.append(s_tau_m100)
        s_tau_m150_values.append(s_tau_m150)
        s_tau_m200_values.append(s_tau_m200)
        s_tau_m220_values.append(s_tau_m220)
        s_tau_m250_values.append(s_tau_m250)

        #Calcul od specific thrust fuel consumption values 
        n_theo_m100 = 1 - (1/tau_r)
        n_theo_m150 = 1 - (1/tau_r)
        n_theo_m200 = 1 - (1/tau_r)
        n_theo_m220 = 1 - (1/tau_r)
        n_theo_m250 = 1 - (1/tau_r)
        n_theo_m100_values.append(n_theo_m100)
        n_theo_m150_values.append(n_theo_m150)
        n_theo_m200_values.append(n_theo_m200)
        n_theo_m220_values.append(n_theo_m220)
        n_theo_m250_values.append(n_theo_m250)
      
        M0_values.append(M0)



plt.subplot(3,2,1,title='The feul air ratio',xlabel='M', ylabel='f')
tau_m100, =plt.plot(M0_values,f_tau_m100_values, color="#FF0000", linewidth=1)
tau_m150, =plt.plot(M0_values,f_tau_m150_values, color="#100c33", linewidth=1)
tau_m200, =plt.plot(M0_values,f_tau_m200_values, color="#000000", linewidth=1)
tau_m220, =plt.plot(M0_values,f_tau_m220_values, color="#FFA500", linewidth=1)
tau_m250, =plt.plot(M0_values,f_tau_m250_values, color="#00FF00", linewidth=1)
#plt.legend([tau_m150, tau_m100,tau_m250,tau_m250], ['tau_m=150', 'tau_m=100', 'tau_m=250', 'tau_m=250'])

plt.subplot(3,2,2,title='The specific thrust',xlabel='M', ylabel='F* (N.s/Kg)')
plt.plot(M0_values,fstar_tau_m100_values, color="#FF0000", linewidth= 1)
plt.plot(M0_values,fstar_tau_m150_values, color="#100c33", linewidth= 1)
plt.plot(M0_values,fstar_tau_m200_values, color="#000000",linewidth= 1 )
plt.plot(M0_values,fstar_tau_m220_values, color="#FFA500",linewidth= 1 )
plt.plot(M0_values,fstar_tau_m250_values, color="#00FF00", linewidth= 1)


plt.subplot(3,2,3,
#title='The thrust-specific fuel consumption',
xlabel='M', ylabel='S (Kg/N.s)')
plt.plot(M0_values,s_tau_m100_values, color="#FF0000", linewidth= 1)
plt.plot(M0_values,s_tau_m150_values, color="#100c33", linewidth= 1)
plt.plot(M0_values,s_tau_m200_values, color="#000000",linewidth= 1 )
plt.plot(M0_values,s_tau_m220_values, color="#FFA500",linewidth= 1 )
plt.plot(M0_values,s_tau_m250_values, color="#00FF00", linewidth= 1)

plt.subplot(3,2,4,
#title='The thermal efficiency',
xlabel='M', ylabel='n th')
plt.plot(M0_values,n_theo_m100_values, color="#FF0000", linewidth= 1)
plt.plot(M0_values,n_theo_m150_values, color="#100c33", linewidth= 1)
plt.plot(M0_values,n_theo_m200_values, color="#000000",linewidth= 1 )
plt.plot(M0_values,n_theo_m220_values, color="#FFA500",linewidth= 1 )
plt.plot(M0_values,n_theo_m250_values, color="#00FF00", linewidth= 1)


plt.subplot(3,2,5)
plt.legend([tau_m100,tau_m150, tau_m100,tau_m220,tau_m250], ['tau_m=100','tau_m=150', 'tau_m=100', 'tau_m=220', 'tau_m=250'])

plt.show()
