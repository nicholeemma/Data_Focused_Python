#define an empty list
records=[]
fh = open('expenses.txt',encoding='utf-8')
#lines from txt and append excluding its terminating newline character
for lines in fh:
    records.append(lines.rstrip())
##records=[x.rstrip() for x in fh]
fh.close()
#print(records)
import re
# 1a
#pat = r'D'

# 1b
#pat = r'\''

# 1c
#pat = r'\"'

# 1d
##pat = r'^7'

# 1f
#pat = r'\.'


#1g
##pat = r'(r)(g)*'

# 1h
#pat = r'[A-Z][A-Z]'

# 1i
##pat = r'\,'

# 1j
##pat = r',.*,.*,.*'
# 1k
##pat = r'^[^v|w|x|y|z]*$'

# 1l
##pat = r'^[1-9][0-9]\.[0-9][0-9]'

# 1m
##pat = r'(,){3}'

# 1n
##pat = r'\('

# 1o
##pat=r'^[1][0-9][0-9]\.[0-9][0-9]\:meal\:'

# 1p
##pat=r'\:[a-z][a-z][a-z][a-z]\:'

# 1q
##pat=r'\:2017[0][3]'

# 1r
##pat = r'(a)(b)(c)*'

# 1s有问题
######pat = r'(..){3}.*'

# 1t
##pat = r'(a)[.\][0-9]*|[.\][0-9](a)*'

# 1u
pat = r'^[^[A-Z]]*$'

# 1v
##pat = r'di?'
##for x in records:
##    print(x)
for line in records:
    if re.search(pat, line) != None:
        print(line)
 
