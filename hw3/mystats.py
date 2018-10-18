import numpy as np

import operator
# File: mystats.py

# define the mean function here
def is_iter(v):
    v_is_iter = True
    try:
        iter(v)
    except:
        v_is_iter = False
    return v_is_iter



def mean(*args):
    try:
        sum=0
        i=0
        for v in args:
            if is_iter(v):
                for a in v:
                    sum=a+sum
                    i+=1
            else:
                sum=v+sum
                i+=1
        return sum/i
    except:
        return("FAIL")
# define the stddev function here
def stddev(*args):
    sum=0
    i=0
    for v in args:
            if is_iter(v):
                for a in v:
                    sum=a+sum
                    i+=1
            else:
                sum=v+sum
                i+=1
    m=sum/i
    
    s=0
    for f in args:
        if is_iter(f):
            for b in f:
                s=s+pow(b-m,2)
        else:
            s=s+pow(f-m,2)
    
    return pow(s/(i-1),0.5)

# define the median function here
def median(*args):
    i=0
    array=[]
    for v in args:
        if is_iter(v):
            
              
            array=sorted(v)
            for f in array:
                i+=1
        else:
            array.append(v)
            i+=1
            
        
    array=sorted(array)    
        
    if ((i%2)==0):
        n=(int)(i/2)
        nn=n-1
        return (array[n]+array[nn])/2
    else:
        y=(int)((i-1)/2)
        return array[y]
# define the mode function here
def mode(*args):
    i=0
    list1=[]
    list3=[]
    list4={}
    list5=[]
    for v in args:
        if is_iter(v):
            for a in v:
                list1.append(a)
                i+=1
        else:
            list1.append(v)
            i+=1
    
    list2=set(list1)
    for x in list2:
        list3.append(list1.count(x))
    list4=dict(zip(list2,list3))
    list4=sorted(list4.items(),key=operator.itemgetter(1))
    list4.reverse()    
    list3=sorted(list3)
    list3.reverse()
    l=len(list3)
    for i in range(0,l-1):
        if (list3[i]!=list3[i+1]):
            break;
    
    list4=list4[0:i+1:1]
    for v in list4:
        if is_iter(list4):
            for a in v:
                list5.append(a)
                i+=1
        else:
            list5.append(v)
            i+=1
    return(tuple(list5[::2]))
     


if __name__ == '__main__':
            
# part (a)
    print('The current module is:', __name__)
# when main is the main module,the output is __main__
#part (b)
    print('mean(1) should be 1.0, and is:', mean(1))
    print('mean(1,2,3,4) should be 2.5, and is:',mean(1,2,3,4))
    print('mean(2.4,3.1) should be 2.75, and is:',mean(2.4,3.1))
    print('mean() should FAIL:',mean())

#part (c)
    print('mean([1,1,1,2]) should be 1.25, and is:',mean([1,1,1,2]))
    print('mean(1, (2,), 3, [4,6]) should be 3.2,' +'and is:', mean(1, (2,), 3, [4,6]))

# part (d)
# your code here
    for i in range(10):
        print("Draw", i, "from Norm(0,1):",
                        np.random.randn())
    ls50=[np.random.randn() for y in range(50)]
#print(ls50)
    print("Mean of", len(ls50), "values from Norm(0,1):",
                        mean(ls50))
    ls10000=[np.random.randn() for y in range(10000)]
    print("Mean of", len(ls10000), "values from " +
           "Norm(0,1):", mean(ls10000))

# part (e)
# your code here
    np.random.seed(0)
    a1 = np.random.randn(10)
    print("a1:", a1)    # should display an ndarray of 10 values
    print("the mean of a1 is:", mean(a1))
# part (f)
# your code here
    print("the stddev of a1 is:", stddev(a1))
# part (g)
# your code here
    print("the median of a1 is:", median(a1))
    
    print("median(3, 1, 5, 9, 2):", median(3, 1, 5, 9, 2))
# part (h)
# your code here
    print("mode(1, 2, (1, 3), 3, [1, 3, 4]) is:",
            mode(1, 2, (1, 3), 3, [1, 3, 4]))

