path="F:\course\python\week2\cme.20180831.c.pa2\cme.20180831.c.pa2"
f=open(path)
g=open('F:\course\python\week2\\assignment2\hh.txt','w')
#字符转换问题 a后需要两个\\
i=0
for x in f:
    if len(x)>1:
        if x.startswith('B') and (x[5:8]=='CL 'or x[5:8]=='LO ') and x[99:102]=='CL ':
            if x[5:7]=='CL':
                if (201811<int(x[18:24])<202101):
                
                    g.writelines(x)
            else:
                if (201811<int(x[27:33])<202101):
                    g.writelines(x)
          
        elif x.startswith('81') and (x[5:8]=='CL 'or x[5:8]=='LO ')and x[15:18]=='CL ':
            if x[5:7]=='CL':
                if (201811<int(x[29:35])<202101):
                   
                    g.writelines(x)
            else:
                if (201811<int(x[38:44])<202101):
                    
                    g.writelines(x)

g.close()
#B:CL  CL_expirations_and_settlements
Futures_Code=[]
Contract_Month=[]
Contract_Type=[]
Futures_Exp_Date=[]
Options_Code=[]
Options_Exp_Date=[]
Futures=[]
Contract_Month1=[]
Contract_Type1=[]
Strike_Price=[]
Settlement_Price=[]
h=open('F:\course\python\week2\\assignment2\hh.txt')
for x in h:
    if x.startswith('B'):
        if x[5:7]=='CL':
            Futures_Code.append('CL')
            Contract_Month.append(x[18:24])
            Contract_Type.append(x[15:18])
            Futures_Exp_Date.append(x[91:99])
            Options_Code.append(' ')
            Options_Exp_Date.append(' ')            
        else:
            Futures_Code.append('CL')
            Contract_Month.append(x[18:24])
            Contract_Type.append(x[15:18])
            Futures_Exp_Date.append(' ')
            Options_Code.append(x[5:7])
            Options_Exp_Date.append(x[91:99])
    else:
        if x[5:7]=='CL':
            Futures.append('CL')
            Contract_Month1.append(x[29:35])
            Contract_Type1.append(x[26:29])
            Strike_Price.append(x[47:54])
            Settlement_Price.append(x[108:122])
        else:
            Futures.append('CL')
            Contract_Month1.append(x[29:35])
            Contract_Type1.append(x[28:29])
            Strike_Price.append(x[47:54])
            Settlement_Price.append(x[108:122])
for q in range(len(Contract_Month)):
    Contract_Month[q]=str(Contract_Month[q])[0:4]+'-'+str(Contract_Month[q])[4:6]
for w in range(len(Futures_Exp_Date)):
    if Futures_Exp_Date[w]!=' ': 
        Futures_Exp_Date[w]=str(Futures_Exp_Date[w])[0:4]+'-'+str(Futures_Exp_Date[w])[4:6]+'-'+str(Futures_Exp_Date[w])[6:8]
for e in range(len(Options_Exp_Date)):
    if Options_Exp_Date[e]!=' ': 
        Options_Exp_Date[e]=str(Options_Exp_Date[e])[0:4]+'-'+str(Options_Exp_Date[e])[4:6]+'-'+str(Options_Exp_Date[e])[6:8]
for z in range(len(Strike_Price)):
    Strike_Price[z]=float(Strike_Price[z])/100
for z1 in range(len(Settlement_Price)):
    Settlement_Price[z1]=float(Settlement_Price[z1])/100
for t in range(len(Contract_Month1)):
    Contract_Month1[t]=str(Contract_Month1[t])[0:4]+'-'+str(Contract_Month1[t])[4:6]
f1=open('F:/course/python/week2/assignment2/CL_expirations_and_settlements.txt','w')
f1.writelines('{0:<20}{1:<20}{2:<20}{3:<20}{4:<20}{5:<20}\n'.format('Futures','Contract','Contract','Futures','Option','Option'))
f1.writelines('{0:<20}{1:<20}{2:<20}{3:<20}{4:<20}{5:<20}\n'.format('Code','Month','Type','Exp Date','Code','Exp Date'))
for n in range(len(Futures_Code)):    
    f1.writelines("{0:<20s}{1:<20s}{2:<20s}{3:<20s}{4:<20s}{5:<20s}".format(Futures_Code[n],Contract_Month[n],Contract_Type[n],Futures_Exp_Date[n],Options_Code[n],Options_Exp_Date[n]))
    f1.write('\n')
f1.writelines("{0:<15}{1:<15}{2:<15}{3:<15}{4:<15}".format("Futures","Contract","Contract","Strike","Settlement"))
f1.write('\n')
f1.writelines("{0:<15}{1:<15}{2:<15}{3:<15}{4:<15}".format("Code","Month","Type","Price","Price"))
f1.write('\n')
f1.writelines("{0:<15}{1:<15}{2:<15}{3:<15}{4:<15}".format("-------","-------","-------","-------","-------"))
f1.write('\n')
for k in range(len(Futures)):    
    f1.writelines("{0:<15}{1:<15}{2:<15}{3:>15.2f}{4:>15.2f}".format(Futures[k],Contract_Month1[k],Contract_Type1[k],Strike_Price[k],Settlement_Price[k]))
    f1.write('\n')
f1.close()   

