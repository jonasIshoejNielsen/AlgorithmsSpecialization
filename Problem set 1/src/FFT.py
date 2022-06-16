from sys import stdin
import math
import cmath


def parse_start():
    n=0  
    A=[]
    B=[]
    for (line_number, line) in enumerate(stdin):
        if line_number==0:
            n= int(line)
        else:
            split = line.replace(" \n", "").split(" ")
            if (len(split)==2):
                A.append(int(split[0]))
                B.append(int(split[1]))
            else:
                print(line)
    return (A,B,n)

#i=1j
i=complex(0.0, 1.0)
def fft(p):
    n=len(p)
    if n==1:
        return p
    p_e,p_o=p[0::2], p[1::2]
    res_e, res_o=fft(p_e), fft(p_o)
    nHalf=n//2      #int(n/2)
    return [res_e[k]+cmath.exp(2j*cmath.pi*k/n)*res_o[k] for k in range(nHalf)] + [res_e[k]+cmath.exp(2j*cmath.pi*(k+nHalf)/n)*res_o[k] for k in range(nHalf)]

def ifft(p):
    n=len(p)
    res = fft(p)
    res_correct=[0]*n
    for (i,v) in enumerate(res):
        res_correct[i]=res[(n-i)%n]/n

    return res_correct

def combineLists(a,b):
    c=[0]*len(a)
    for i in range(len(a)):
        c[i]=(a[i]*b[i])
    return c

def getLargestPowerOf2Larger(n):
    res = 2
    while(res<n):
        res*=2
    return res
def makeLenght(p, n):
    return p+[0]*(n-len(p))

def multiply2Polynomials(a,b):
    n=getLargestPowerOf2Larger(max(len(a), len(b))*2)
    a_large = makeLenght(a,n)     #from n coefficients to 2n coefficients
    b_large = makeLenght(b,n)     #from n coefficients to 2n coefficients
    fft_A=fft(a_large)
    fft_B=fft(b_large)
    fft_C=combineLists(fft_A, fft_B)
    return ifft(fft_C)[:-1]

def roundLst(lst):
    return [complex(round(v.real), round(v.imag)) for v in lst]

def testOne(P, name):
    FFT_P=fft(P)
    FFT_FFT_P=fft(FFT_P)
    ifft_P=ifft(FFT_P)
    print(name,"=",roundLst(P))
    print("\t","fft_",name,"=",roundLst(FFT_P))
    print("\t","fft_fft_",name,"=",roundLst(FFT_FFT_P))
    print("\t","ifft_",name,"=",roundLst(ifft_P))
    print("")

def main():
    (A,B,n) = parse_start()
    testOne(A.copy(), "A")
    testOne(B.copy(), "B")
    print("A*B = ", roundLst(multiply2Polynomials(A,B)))
main()


