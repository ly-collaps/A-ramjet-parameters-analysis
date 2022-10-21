from turtle import title
import matplotlib.pyplot as plt
import numpy as np
cp=1004 
R=287
gamma=1.4
T0=216.7
PCI =44800
Tt4= 2200
a0=295.07
tau_m = PCI/(cp*T0)

#creation of empty arrays to append on 
M0_values=[]
f_tau_lambda6_values=[]
f_tau_lambda7_values=[]
f_tau_lambda8_values=[]
f_tau_lambda9_values=[]
f_tau_lambda10_values=[]

fstar_tau_lambda6_values=[]
fstar_tau_lambda7_values=[]
fstar_tau_lambda8_values=[]
fstar_tau_lambda9_values=[]
fstar_tau_lambda10_values=[]

s_tau_lambda6_values= []
s_tau_lambda7_values= []
s_tau_lambda8_values= []
s_tau_lambda9_values= []
s_tau_lambda10_values= []

n_theo_lambda6_values= []
n_theo_lambda7_values= []
n_theo_lambda8_values= []
n_theo_lambda9_values= []
n_theo_lambda10_values= []

#n_thermal_values=[]
for M0 in np.arange(0,4,0.1): 
    #Calcul of V9/V0 values 
    #tau_lambda varies [6,10]

        tau_r = 1 + (((gamma-1)/2)*(M0**2))
        tau_m= 250 #tau_m varies [100,150,200,220,250]

#Calcul of fuel/air ratio values 
        f_tau_lambda6 = ((6/tau_r)-1)/((tau_m/tau_r)-1)
        f_tau_lambda7 = ((7/tau_r)-1)/((tau_m/tau_r)-1)
        f_tau_lambda8 = ((8/tau_r)-1)/((tau_m/tau_r)-1)
        f_tau_lambda9 = ((9/tau_r)-1)/((tau_m/tau_r)-1)
        f_tau_lambda10 = ((10/tau_r)-1)/((tau_m/tau_r)-1)
    
        f_tau_lambda6_values.append(f_tau_lambda6)
        f_tau_lambda7_values.append(f_tau_lambda7)
        f_tau_lambda8_values.append(f_tau_lambda8)
        f_tau_lambda9_values.append(f_tau_lambda9)
        f_tau_lambda10_values.append(f_tau_lambda10)

 #Calcul of specific thrust values 
        fstar_tau_lambda6 = M0*(((1+f_tau_lambda6)*np.sqrt(6/tau_r))-1) * a0
        fstar_tau_lambda7 = M0*(((1+f_tau_lambda7)*np.sqrt(7/tau_r))-1)* a0
        fstar_tau_lambda8 = M0*(((1+f_tau_lambda8)*np.sqrt(8/tau_r))-1)* a0
        fstar_tau_lambda9 = M0*(((1+f_tau_lambda9)*np.sqrt(9/tau_r))-1)* a0
        fstar_tau_lambda10 = M0*(((1+f_tau_lambda10)*np.sqrt(10/tau_r))-1)* a0
        fstar_tau_lambda6_values.append(fstar_tau_lambda6)
        fstar_tau_lambda7_values.append(fstar_tau_lambda7)
        fstar_tau_lambda8_values.append(fstar_tau_lambda8)
        fstar_tau_lambda9_values.append(fstar_tau_lambda9)
        fstar_tau_lambda10_values.append(fstar_tau_lambda10)

#Calcul od specific thrust fuel consumption values 
        s_tau_lambda6 = f_tau_lambda6/fstar_tau_lambda6
        s_tau_lambda7 = f_tau_lambda7/fstar_tau_lambda7
        s_tau_lambda8 = f_tau_lambda8/fstar_tau_lambda8
        s_tau_lambda9 = f_tau_lambda9/fstar_tau_lambda9
        s_tau_lambda10 = f_tau_lambda10/fstar_tau_lambda10
        s_tau_lambda6_values.append(s_tau_lambda6)
        s_tau_lambda7_values.append(s_tau_lambda7)
        s_tau_lambda8_values.append(s_tau_lambda8)
        s_tau_lambda9_values.append(s_tau_lambda9)
        s_tau_lambda10_values.append(s_tau_lambda10)

#Calcul od specific thrust fuel consumption values 
        n_theo_lambda6 = 1 - (1/tau_r)
        n_theo_lambda7 = 1 - (1/tau_r)
        n_theo_lambda8 = 1 - (1/tau_r)
        n_theo_lambda9 = 1 - (1/tau_r)
        n_theo_lambda10 = 1 - (1/tau_r)
        n_theo_lambda6_values.append(n_theo_lambda6)
        n_theo_lambda7_values.append(n_theo_lambda7)
        n_theo_lambda8_values.append(n_theo_lambda8)
        n_theo_lambda9_values.append(n_theo_lambda9)
        n_theo_lambda10_values.append(n_theo_lambda10)
    
        M0_values.append(M0)



plt.subplot(3,2,1,title='The feul air ratio',xlabel='M', ylabel='f')
tau_lambda6, =plt.plot(M0_values,f_tau_lambda6_values, color="#6c3376", linewidth=1)
tau_lambda7, =plt.plot(M0_values,f_tau_lambda7_values, color="#6c3376", linewidth=1)
tau_lambda8, =plt.plot(M0_values,f_tau_lambda8_values, color="#000000", linewidth=1)
tau_lambda9, =plt.plot(M0_values,f_tau_lambda9_values, color="#FFA500", linewidth=1)
tau_lambda10, =plt.plot(M0_values,f_tau_lambda10_values, color="#00FF00", linewidth=1)
#plt.legend([tau_lambda7, tau_lambda8,tau_lambda9,tau_lambda10], ['tau_lambda=7', 'tau_lambda=8', 'tau_lambda=9', 'tau_lambda=10'])

plt.subplot(3,2,2,title='The specific thrust',xlabel='M', ylabel='F* (N.s/Kg)')
plt.plot(M0_values,fstar_tau_lambda6_values, color="#6c3376", linewidth= 1)
plt.plot(M0_values,fstar_tau_lambda7_values, color="#6c3376", linewidth= 1)
plt.plot(M0_values,fstar_tau_lambda8_values, color="#000000",linewidth= 1 )
plt.plot(M0_values,fstar_tau_lambda9_values, color="#FFA500",linewidth= 1 )
plt.plot(M0_values,fstar_tau_lambda10_values, color="#00FF00", linewidth= 1)


plt.subplot(3,2,3,
#title='The thrust-specific fuel consumption',
xlabel='M', ylabel='S (Kg/N.s)')
plt.plot(M0_values,s_tau_lambda6_values, color="#6c3376", linewidth= 1)
plt.plot(M0_values,s_tau_lambda7_values, color="#6c3376", linewidth= 1)
plt.plot(M0_values,s_tau_lambda8_values, color="#000000",linewidth= 1 )
plt.plot(M0_values,s_tau_lambda9_values, color="#FFA500",linewidth= 1 )
plt.plot(M0_values,s_tau_lambda10_values, color="#00FF00", linewidth= 1)

plt.subplot(3,2,4,
#title='The thermal efficiency',
xlabel='M', ylabel='n th')
plt.plot(M0_values,n_theo_lambda6_values, color="#6c3376", linewidth= 1)
plt.plot(M0_values,n_theo_lambda7_values, color="#6c3376", linewidth= 1)
plt.plot(M0_values,n_theo_lambda8_values, color="#000000",linewidth= 1 )
plt.plot(M0_values,n_theo_lambda9_values, color="#FFA500",linewidth= 1 )
plt.plot(M0_values,n_theo_lambda10_values, color="#00FF00", linewidth= 1)


plt.subplot(3,2,5)
plt.legend([tau_lambda6,tau_lambda7, tau_lambda8,tau_lambda9,tau_lambda10], ['tau_lambda=6','tau_lambda=7', 'tau_lambda=8', 'tau_lambda=9', 'tau_lambda=10'])
plt.show()


