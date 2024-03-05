def prime(n):
    Prime_sum=0
    for x in range(2,n):
        Prime=True
        for i in range(2,x):
            if x%i==0:
                Prime=False
                break

        if Prime and x>1:
            print(x,end=' ')
            Prime_sum=Prime_sum+x


    print('\nSum of Prime Number upto 50 is',Prime_sum)

n=int(input('Enter any Number :'))
prime(n)
