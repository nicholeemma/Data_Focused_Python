# Author: Zichen Li (Andrew ID:zichenli); Jiayue Yang(Andrew ID:jiayueya)

# 2.a
fa=open('Desktop/expenses.txt','r')
records=list()
for line in fh:
    records.append(line.rstrip())
for line in records:
    print(line)
fa.close()

#2.b
fb=open('Desktop/expenses.txt','r')
records2=[line.rstrip() for line in fb]
print("\nrecords == records2:", records == records2, '\n')
fb.close()

#2.c
fc=open('Desktop/expenses.txt','r')
records3=tuple(tuple(line.rstrip().split(':')) for line in fc)
for tup in records3:
    print(tup)

#2.d
cat_set=set(tup[1] for tup in records3[1:])
date_set=set(tup[2] for tup in records3[1:])
print('Categories:', cat_set, '\n')
print('Dates:     ', date_set, '\n')

#2.e
rec_num_to_record={i:records3[i] for i in range(len(records3))}
for rn in range(len(rec_num_to_record)):
    print('{:3d}: {}'.format(rn,
rec_num_to_record[rn]))

for i in rec_num_to_record.items():
    print('{:3d}: {}'.format(i[0], i[1]))
for k, v in rec_num_to_record.items():
    print('{:3d}: {}'.format(k, v))
