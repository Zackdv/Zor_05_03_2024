d=[]
def prime(n):
    for x in range(2,n):
        Prime= True
        for j in range(2,x):
            if x%j==0:
                Prime = False
                break

        if Prime and x>1 :
            d.append(x)

n=int(input('Enter Number'))
prime(n)

print('sum of prime number upto {} is {}'.format(n,sum(d)))



