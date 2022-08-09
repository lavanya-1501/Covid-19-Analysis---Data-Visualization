import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_excel('graphs.xlsx','Sheet1')

fig=plt.figure(figsize=(9,7))
fig.suptitle('Statewise COVID 19 Cases Analytic Report on 25-04-2021 in India Using various charts',font = 'Pristina',
             fontweight = 'bold', color = 'Red', fontsize = '25')
fig.canvas.set_window_title('Analytic using various graphs')

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.6, 
                    hspace=0.6)


df = df.sort_values(by=['Confirmed'],ascending=False)

#Bar Plot
ax=plt.subplot(2,2,1)

w=0.25

bar1=plt.bar(df['State'][:5], df['Confirmed'][:5],label='Confirmed', align='center',color='b')
bar2=plt.bar(df['State'][:5], df['Cured'][:5],label='Cured',align='center',color='g')
bar3=plt.bar(df['State'][:5], df['Deaths'][:5],label='Deaths', align='center',color='r')

r1 = np.arange(len(df['State']))[:5]
r2 = [x + w for x in r1]
r3 = [x + w for x in r2]

labels = df['State'][:5]
plt.legend() 

bars=bar1+bar2+bar3

for re in bars:
    height=re.get_height()
    plt.text(re.get_x()+re.get_width()/2.0,height,height,fontsize=6, ha='center', va='bottom',fontweight='bold',color='black')


plt.ylabel('Number of Confirmed Cases')
plt.xticks(rotation = 20)

plt.title('States with maximum confirmed cases, cures and deaths')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Histogram
plt.subplot(2,2,2)

plt.hist(df['Confirmed'], bins=5, fc='Blue', ec='white')
plt.xlabel('Confirmed Cases')
plt.ylabel('Count of States')
plt.title('Count of States with maximum confirmed cases')




#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Scatter Plot
plt.subplot(2,2,3)

plt.scatter(df['State'][:5], df['Confirmed'][:5],color='b', label='Confirmed')
plt.scatter(df['State'][:5], df['Cured'][:5],color='g',label='Cured')
plt.scatter(df['State'][:5], df['Deaths'][:5],color='r',label='Deaths')
plt.legend()

plt.ylabel('Number of Cases')
plt.xticks(rotation = 20)

plt.title('States with maximum confirmed cases, cures and deaths')




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Area Plot
plt.subplot(2,2,4)

plt.plot([],[],color='b', label='Confirmed', linewidth=5)
plt.plot([],[],color='g', label='Cured', linewidth=5)
plt.plot([],[],color='r', label='Deaths', linewidth=5)
 
plt.stackplot(df['State'][:5], df['Confirmed'][:5],df['Cured'][:5],df['Deaths'][:5], colors=['b','g','r'])

plt.ylabel('Number of Cases')
plt.xticks(rotation = 20)
plt.title('States with maximum confirmed cases, cures and deaths')
plt.legend()

plt.show()
