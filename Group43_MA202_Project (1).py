import math
sine=math.sin
pi=math.pi
Tc = 60/72
Ts = 2*Tc/5
#calculation of Io

time=0
step=0.01
answer=0
while(time<Tc):
    answer+=sine(pi*(time%Tc)/Ts)*step
    time+=step
print("Value of Io using discrete values at each interval",end=": ")
print(90/answer)
time=0
answer=0
while(time<Tc):
    answer+=(sine(pi*(time%Tc)/Ts)+sine(pi*((time+step)%Tc)/Ts))*(step/2)
    time+=step
print("Value of Io using trapezoidal method",end=": ")
print(90/answer)
time=0
Time=[]
while(time<Tc):
    Time.append(time)
    time+=step
#print(Time)
i=1
answer=0
k=len(Time)
I=[]
#calculation of Io using value of Tc and Ts
while(i<k):
    if(k%2!=0):
        firstterm=sine(pi*(Time[i]%Tc)/Ts)
        secondterm=sine(pi*(Time[i+1]%Tc)/Ts)
        thirdterm=sine(pi*(Time[i+2]%Tc)/Ts)
        answer+=(firstterm+4*secondterm+thirdterm)*(step/3)
        i+=2
    else:
        if(k-i>2):
            firstterm=sine(pi*(Time[i]%Tc)/Ts)
            secondterm=sine(pi*(Time[i+1]%Tc)/Ts)
            thirdterm=sine(pi*(Time[i+2]%Tc)/Ts)
            answer+=(firstterm+4*secondterm+thirdterm)*(step/3)
            i+=2
        else:
            i+=1
print("Value of Io using Simpson 1/3 rule",end=": ")
print(90/answer)
Io=90/answer

#current at different time 
def I(time):
    return sine(pi*(time%Tc)/Ts)

R=0.95
C=1.066
p=[0]
P_prev=0
#calculation of Pressure at different time slots

while(time<100):
    P_next=P_prev+(I(time)-P_prev)*(step)/(R*C)
    time+=step
    p.append(P_next)
    P_prev=P_next
print("Pressure at time = 100s is",end=": ")
print(p[len(p)-1])
Element1=p[len(p)-1]

r = 0.05
R = 0.95
R1 = 0.9
C = 1.066
time=0
p=[0]
P_prev=0
while(time<100):
    P_next=P_prev+(((1+(r/R))*I(time)*step)+(C*R1*(I(time+step)-I(time)))-(P_prev*step/R))/5
    time+=step
    p.append(P_next)
    P_prev=P_next
print("Pressure at time = 100s is",end=": ")
print(p[len(p)-1])
print("Error in 2-element method is",end=": ")
answer=(Element1-p[len(p)-1])/p[len(p)-1]
print(answer*100,"%")
