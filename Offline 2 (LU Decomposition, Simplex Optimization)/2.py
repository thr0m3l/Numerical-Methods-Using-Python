import numpy as np

def gen_table(c,a,b):
    (con,var) = a.shape
    l = len(c)
    
    table = np.zeros((con+1,con+var+2))
    table[:con, :var] = a
    
    for i in range (con):
        table[i,i+var] = 1
    
    table[:-1,-1] = b
    table[-1,:l] = -c
    table[-1,-2] = 1    
    return table
    
def find_optimum(table,results):
    index = []
    for i in range (len(table[-1]) - 1):
        if table[-1,i] < 0:
           index.append(i) 
    
    if len(index) == 0:
        return (True, results)
    
    minc = np.argmin(table[-1,:-1])
    
    column = table[:-1,minc]
    ratio = (table[:-1,-1]/column)
    
    minr = 0
    for i in range(len(ratio)):
        if ratio[i]<ratio[minr] and ratio[i]>=0:
            minr = i    
    row = table[minr]/table[minr][minc]
    
    r = np.array([minr,minc])
    results = np.append(results, r)
    
    table[:] -= np.outer(table[:, minc], row)
    table[minr, :] = row
    #print(table)
    with np.printoptions(precision=4, suppress=True):
        print(table)
        print()
    
    return (False,results) 
def simplex(c,a,b):
    results = np.array([])
    table = gen_table(c,a,b)
    
    with np.printoptions(precision=4, suppress=True):
        print(table)
        print()
    
    quit = False
    while not quit:
        quit, results = find_optimum(table,results)
    x = np.zeros(len(c)+1)
    print("\n")
    
    for i in range(0,len(results),2):
        if results[i+1] >= len(c):
            continue
        x[int(results[i+1])] = table[int(results[i]),-1]
    
    x[len(c)] = table[-1,-1]
    print(x)
    
if __name__ == "__main__":
    
    file = open("in2.txt","r")
    line = file.readline()
    num = line.split()
    num = list(map(int, num))
    c = np.array(num);
    
    lines = file.readlines()
    data = []
    var = len(c)
    i = 0;
    for line in lines:
        data += [float(x) for x in line.split()]
        
    data = np.array(data)

    a = []
    b = []
    for i in range(len(data)):
        if (i+1) % (var+1) == 0:
            b.append(data[i])
        else:
            a.append(data[i])
           
    a = np.array(a)
    b = np.array(b)
 
    a = a.reshape(int(len(a)/var),var)
    
    simplex(c,a,b)
    
    