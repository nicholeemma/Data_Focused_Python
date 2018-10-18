# Author: Zichen Li (Andrew ID:zichenli); Jiayue Yang(Andrew ID:jiayueya)

fh=open('desktop/cme.20180831.c.pa2/cme.20180831.c.pa2','r')  # I put the original file in my desktop.
fh2=open('outfile.txt', 'wt')
for line in fh:
    if (line[0]=='B')|(line[:2]=='81'):
        fh2.write(line)
fh.close()
fh2.close()
fh=open('C:/Users/guin/outfile.txt','r')
fh2=open('outfile2.txt','wt')
for line in fh:
    if line[0]=='B':
        if ((line[5:15]=='CL        ')|(line[5:15] =='LO        '))&(line[99:109]=='CL        '):
            fh2.write(line)
    elif line[0:2]=='81':
        if ((line[5:15]=='CL        ')|(line[5:15] =='LO        '))&(line[15:25]=='CL        '):
            fh2.write(line)
fh.close()
fh2.close()

fh=open('C:/Users/guin/outfile2.txt','r')

futures_code=list(); contract_month=list(); contract_type=list(); exp_date=list()
options_underlying_commodity_code=list(); options_code=list(); contract_month_options=list(); contract_type_options=list(); exp_date_options=list()
futures_code_81=list(); contract_month_81=list(); contract_type_81=list(); strike_price=list(); settlement_price=list()

for line in fh:
    if line[0]=='B':
        if (line[15:18]=='FUT')&(int(line[18:24])>=201812)&(int(line[18:24])<=202012):
            futures_code.append(line[5:7]); contract_month.append(line[18:24]);
            contract_type.append(line[15:18]); exp_date.append(line[91:99])
        elif (line[15:18]=='OOF')&(int(line[18:24])>=201812)&(int(line[18:24])<=202012):
            options_underlying_commodity_code.append(line[99:101]); options_code.append(line[5:7]); contract_month_options.append(line[27:33]);
            contract_type_options.append(line[15:18]); exp_date_options.append(line[91:99])

    else:
        if (line[5:7]=='CL')&(int(line[29:35])>=201812)&(int(line[29:35])<=202012):
            futures_code_81.append(line[15:17]); contract_month_81.append(line[29:35]); contract_type_81.append(line[25:28])
            strike_price.append('    '); settlement_price.append(line[108:122])
        elif (line[5:7]=='LO'):
            if (int(line[38:44])>=201812)&(int(line[38:44])<=202012):
                futures_code_81.append(line[15:17]); contract_month_81.append(line[38:44]);
                if line[28]=='C':
                    contract_type_81.append('Call')
                elif line[28]=='P':
                    contract_type_81.append('Put')
                strike_price.append(line[47:54]); settlement_price.append(line[108:122])
fh.close()

fh2=open('CL_expirations_and_settlements.txt.','wt')
fh2.write('Futures   Contract   Contract   Futures     Options   Options\n')
fh2.write('Code      Month      Type       Exp Date    Code      Exp Date\n')
fh2.write('-------   --------   --------   --------    --------  --------\n')
template='{0:s} {1:s}-{2:s} {3:s} {4:s}-{5:s}-{6:s}'
for i in range(len(futures_code)):
    fh2.write(template.format(futures_code[i].ljust(9), contract_month[i][0:4], contract_month[i][4:].ljust(5), 'Fut'.ljust(10), exp_date[i][0:4], exp_date[i][4:6], exp_date[i][6:]))
    fh2.write('\n')
template2='{0:s} {1:s}-{2:s} {3:s} {4:s} {5:s}-{6:s}-{7:s}'
for j in range(len(options_code)):
    fh2.write(template2.format(options_underlying_commodity_code[j].ljust(9), contract_month_options[j][0:4],contract_month_options[j][4:].ljust(5), 'Opt'.ljust(22), options_code[j].ljust(9), exp_date_options[j][0:4], exp_date_options[j][4:6], exp_date_options[j][6:]))
    fh2.write('\n')
fh2.write('\n')

fh2.write('Futures   Contract   Contract   Strike   Settlement\n')
fh2.write('Code      Month      Type       Price    Price\n')
fh2.write('-------   --------   --------   ------   ----------\n')
template3='{0:s} {1:s}-{2:s} {3:s} {4:.2f}'
template4='{0:s} {1:s}-{2:s} {3:s} {4:<10.2f}{5:6.2f}'
for k in range(len(futures_code_81)):
    if contract_type_81[k] =='FUT':
        fh2.write(template3.format(futures_code_81[k].ljust(9), contract_month_81[k][0:4], contract_month_81[k][4:6].ljust(5), 'Fut'.ljust(21), int(settlement_price[k])/100 ))
        fh2.write('\n')
    if contract_type_81[k] =='Put':
        fh2.write(template4.format(futures_code_81[k].ljust(9), contract_month_81[k][0:4], contract_month_81[k][4:6].ljust(5), 'Put'.ljust(10), int(strike_price[k])/100, int(settlement_price[k])/100 ))
        fh2.write('\n')
    elif contract_type_81[k] =='Call':
        fh2.write(template4.format(futures_code_81[k].ljust(9), contract_month_81[k][0:4], contract_month_81[k][4:6].ljust(5), 'Call'.ljust(10), int(strike_price[k])/100, int(settlement_price[k])/100 ))
        fh2.write('\n')
fh2.close()
