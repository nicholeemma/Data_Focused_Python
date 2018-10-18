##a&c
from urllib.request import urlopen  # b_soup_1.py
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

# Treasury Yield Curve web site, known to be HTML code
html = urlopen('https://www.treasury.gov/resource-center/'
               'data-chart-center/interest-rates/Pages/'
               'TextView.aspx?data=yieldYear&year=2018')

# create the BeautifulSoup object (BeautifulSoup Yield Curve)
bsyc = BeautifulSoup(html.read(), "lxml")

#omit some rpocesses to find what we need
#tc_table is what we need, data and name of parameters
tc_table = bsyc.findAll('table',
                      { "class" : "t-chart" } )[0]
daily_yield_curves=[[]*12 for i in range(184)]
i=0
for c in tc_table.children:
    for r in c.children:
        daily_yield_curves[i//12].extend(r.contents)
        i+=1
#print(daily_yield_curves)

#concert interest into float
j=0
i=0
interest=[[]*11 for i in range(183)]

for j in range(1,184):
    for x in range(12):
        if(i%12!=0):
            daily_yield_curves[j][x]=float(daily_yield_curves[j][x])
            interest[i//12].append(daily_yield_curves[j][x])
        i+=1
##print(interest)
##change into datafram
frame=pd.DataFrame(daily_yield_curves)
#.drop()if not set inplace=True，the result coudld only be shown on new datafram，not delete in original one
frame.drop([0],inplace=True)
##change columns' names
frame.columns=[daily_yield_curves[0]]
#print(frame)
fh = open('daily_yield_curves.txt', 'wt', encoding='utf-8')
fh.write(frame.to_string())
fh.close()

##b
#print(len(daily_yield_curves))
x=[[x]*11 for x in range(len(daily_yield_curves)-1)]
x=np.array(x)
X=x
y=[[1, 3, 6, 12, 24, 36, 60, 84, 120, 240, 360] for i in range(len(daily_yield_curves)-1)]
y=np.array(y)
Y=y
##X,Y=np.meshgrid(x,y)
Z=np.array(interest)
fig = plt.figure()
ax = fig.gca(projection='3d')
#set x,y,z labels
plt.xlabel("trading days since 01/02/18")
plt.ylabel("months to maturity")
ax.set_zlabel('rate')
#Customize x,y,z axis
my_x_ticks = np.arange(0, 200, 50)
my_y_ticks = np.arange(0, 400, 100)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
ax.set_zlim(0,4,1)
ax.zaxis.set_major_locator(LinearLocator(5))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.f'))
surf = ax.plot_surface(x, y, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False)
### Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
##plt.colorbar(shrink=.70)

# Plot a basic wireframe.
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
ax2.set_zlim(0,4,1)
ax2.zaxis.set_major_locator(LinearLocator(5))
ax2.zaxis.set_major_formatter(FormatStrFormatter('%.f'))
ax2.set_zlabel('rate')

ax2.set_xlabel("trading days since 01/02/18")
ax2.set_ylabel("months to maturity")
my_x_ticks = np.arange(0, 200, 50)
my_y_ticks = np.arange(0, 400, 100)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
ax2.plot_wireframe(X,Y,Z,rstride=1,cstride=1)
plt.title("Interest Rate Time Series,2018 thru 9/15")
plt.show()

#c
yield_curve_df=frame.set_index('Date')
print(frame)
print(yield_curve_df)
yield_curve_df.plot()
plt.show()
by_day_yield_curve_df=yield_curve_df[0:140:20]
by_day_yield_curve_df=pd.DataFrame.transpose(by_day_yield_curve_df)

by_day_yield_curve_df.index=[1,2,6,12,24,36,60,84,120,240,360]
by_day_yield_curve_df.plot()
plt.title("2018 Yield Curves,2D Day Intervals")
plt.show()
