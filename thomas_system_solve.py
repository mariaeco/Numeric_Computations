import numpy as np

def thomas(A):
    n = len(A)
    a = np.zeros(n)
    b = np.zeros(n)
    c = np.zeros(n)
    d = np.zeros(n)
    
    
    b[0] = A[0][0]
    c[0] = A[0][1]
    d[0] = A[0][-1]
    
    for i in range(1, n-1):
        a[i] = A[i][i-1]
        b[i] = A[i][i]
        c[i] = A[i][i+1]
        d[i] = A[i][-1]

    a[-1] = A[-1][-3]
    b[-1] = A[-1][-2]
    c[-1] = A[-1][-1]

    den = float(b[0])
    c[0] /= den
    d[0] /= den
    
    for i in range(1,n):
        den = float(b[i]-a[i]*c[i-1])
        c[i] /= den
        d[i] = (d[i]-a[i]*d[i])/den
        
    x = np.copy(d)
    for i in range(n-2, -1, -1):
        x[i] -=c[i]*x[i+1]

    
    for i in range(len(x)):
        print("x", i+1, "=", round(x[i],4))

