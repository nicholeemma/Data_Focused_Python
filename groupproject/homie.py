from xlrd import open_workbook
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display

#open the cleaned and merged data sheet and put the data into a dictionary
wb = open_workbook('Final_Data.xlsx')
for sheet in wb.sheets():
    rows_num = sheet.nrows
    columns_num = sheet.ncols
    house_info= dict()
    for row in range(rows_num):
        each_house_info = []
        for col in range(columns_num):
            value  = sheet.cell(row,col).value
            each_house_info.append(value)
        house_info[row]=each_house_info

#set the 1st sub-score to each house based on the price
price_score=[]
prices=dict()
for i in range(1,rows_num):
    prices[i]=house_info[i][3]
for i in prices.keys():
    if prices[i]<200:
        price_score.append(100)
    elif prices[i]<210:
        price_score.append(95)
    elif prices[i]<220:
        price_score.append(90)
    elif prices[i]<230:
        price_score.append(85)
    elif prices[i]<240:
        price_score.append(80)
    elif prices[i]<250:
        price_score.append(75)
    elif prices[i]<260:
        price_score.append(70)
    elif prices[i]<270:
        price_score.append(65)
    elif prices[i]<280:
        price_score.append(60)
    elif prices[i]<290:
        price_score.append(55)
    elif prices[i]<300:
        price_score.append(50)
    elif prices[i]<350:
        price_score.append(45)
    elif prices[i]<400:
        price_score.append(40)
    elif prices[i]<450:
        price_score.append(35)
    elif prices[i]<500:
        price_score.append(30)
    elif prices[i]<550:
        price_score.append(25)
    elif prices[i]<600:
        price_score.append(20)
    elif prices[i]<650:
        price_score.append(15)
    elif prices[i]<700:
        price_score.append(10)
    else:
        price_score.append(0)

#set the 2nd sub-score to each house based on the distance
distance=[house_info[i][8] for i in range(1,rows_num)]
distance_score=[]
for i in range(0,len(distance)):
    if distance[i]<5:
        distance_score.append(100)
    elif distance[i]<10:
        distance_score.append(90)
    elif distance[i]<15:
        distance_score.append(80)
    elif distance[i]<20:
        distance_score.append(70)
    elif distance[i]<25:
        distance_score.append(60)
    elif distance[i]<30:
        distance_score.append(50)
    elif distance[i]<35:
        distance_score.append(40)
    elif distance[i]<40:
        distance_score.append(30)
    elif distance[i]<50:
        distance_score.append(20)
    else:
        distance_score.append(10)

#set the 3rd sub-score to each house based on the number of crimes happened in its district
safety_score=[]
crime_num={house_info[i][0]: [house_info[i][2],house_info[i][12]] for i in range(1,rows_num)}
for i in crime_num.keys():
    if crime_num[i][1]<100:
        safety_score.append(100)
    elif crime_num[i][1]<200:
        safety_score.append(90)
    elif crime_num[i][1]<300:
        safety_score.append(80)
    elif crime_num[i][1]<400:
        safety_score.append(70)
    elif crime_num[i][1]<500:
        safety_score.append(60)
    elif crime_num[i][1]<600:
        safety_score.append(50)
    elif crime_num[i][1]<700:
        safety_score.append(40)
    elif crime_num[i][1]<800:
        safety_score.append(30)
    elif crime_num[i][1]<900:
        safety_score.append(20)
    else:
        safety_score.append(10)

#set the 4th sub-score to each house based on the number of restaurants around it
restaurant_score=[]
restaurant_num={house_info[i][0]: [house_info[i][2],house_info[i][13]] for i in range(1,rows_num)}
for i in restaurant_num.keys():
    if restaurant_num[i][1]<5:
        restaurant_score.append(10)
    elif restaurant_num[i][1]<10:
        restaurant_score.append(20)
    elif restaurant_num[i][1]<15:
        restaurant_score.append(30)
    elif restaurant_num[i][1]<20:
        restaurant_score.append(40)
    elif restaurant_num[i][1]<25:
        restaurant_score.append(50)
    elif restaurant_num[i][1]<30:
        restaurant_score.append(60)
    elif restaurant_num[i][1]<35:
        restaurant_score.append(70)
    elif restaurant_num[i][1]<40:
        restaurant_score.append(80)
    elif restaurant_num[i][1]<45:
        restaurant_score.append(90)
    else:
        restaurant_score.append(100)

#ask user to input the number of beds, baths, and parkings they want, and filter out the houses that do not meet the requirements 
bed_num=input('The number of beds you want: ')
bath_num=input('The number of baths you want: ')
parking_num=input('The number of car parkings you want: ')

#ask user to rank the priority level for the following four elements
print('\n\nRate your priority: choose from  1, 2, 3, 4.')
first=input('Your priority for price is: ')
second=input('Your priority for safety is: ')
third=input('Your priority for distance is: ')
forth=input('Your priority for the number of restaurants around the accommodation is: ')

#define the finction to convert each priority level to its weight
def weigh (s):
    if s == '1':
        a=0.4
    elif s=='2':
        a=0.3
    elif s=='3':
        a=0.2
    elif s=='4':
        a=0.1
    return a

# use a dataframe to conatin info that matters to the user, and add all 4 sub-scores and the total score to the dataframe
dict1={house_info[0][i]:[house_info[j][i] for j in range(1,rows_num)]for i in range(len(house_info[0]))}
df1=pd.DataFrame(dict1,index=[house_info[j][0] for j in range(1,rows_num)])
# calculate the total_score
total_score=[restaurant_score[i]*weigh(forth)+safety_score[i]*weigh(second)+distance_score[i]*weigh(third)+price_score[i]*weigh(first) for i in range(len(price_score))]
df1['price score'] = price_score
df1['distance score'] = distance_score
df1['safety score'] = safety_score
df1['restaurant score'] = restaurant_score
df1['total score'] = total_score
del df1['House Number']

#filter out accommodations that do not meet the requirements specified by the user
cond1=(df1['Number of beds']==int(bed_num))
cond2=(df1['Number of baths']==int(bath_num))
cond3=(df1['Number of Car Parks']==int(parking_num))
selected_house= df1[cond1&cond2&cond3]

#sort the remained accommodations based on the total score
result = selected_house.sort_values(['total score'],ascending=False)

#change some format parameters for better output readability 
count_row = result.shape[0]
result.index = range(1,count_row+1) 
pd.set_option('display.max_colwidth',100)
pd.option_context('display.colheader_justify','left')
pd.options.display.float_format = '{:,.0f}'.format

#visualize the scores of the top ten accomodations 
df2=result.loc[1:10,'price score':'restaurant score']
df2['price score'] *= weigh(first) 
df2['distance score'] *= weigh(third)
df2['safety score'] *= weigh(second)
df2['restaurant score'] *= weigh(forth)
df2.plot.bar(stacked=True)
plt.show()

#display the final recommadations list sorted by the total score. It contains the URL link and the total score.
df3=result.loc[:,['Detailed URL','total score']]
if df3.empty:
    print('\n***No results found!')
else:
    print('\n***Here is your options:')
    display(df3)
