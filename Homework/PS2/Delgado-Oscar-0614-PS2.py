import numpy as np  #you may need to install this package
from timeit import default_timer as timer


def part_A(A):
    max_profit_so_far = 0
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            coins = A[j]-A[i]
            if (coins > max_profit_so_far):
                max_profit_so_far = coins  
    return max_profit_so_far


def part_D(A):
    max = 0
    m = [0]
    x = 0
    for i in range(0,len(A)):
        if A[i]<A[m[x]]:
            m.append(i)
            x=x+1
    m.append(len(A))
    for i in range(0,len(m)-1):
        for j in range(m[i],m[i+1]):
            temp = A[j]-A[m[i]]
            if max < temp:
                max = temp
    return max

times = []
print('Part D results:')
for seed in range(10):  #running the loop for 10 iterations, using sps2_solution.pyps2_solution.pyeed for the random generator
    np.random.seed(seed)  # sets the seed for the random generator
    exchange_rates = np.random.randint(low=1,high=1001, size=1000)#exchange_rates is list with 1000 elements, where the elements are positive integers in range(1, 1000)

    start_A = timer()   #start the timer for part A
    result_A = part_A(exchange_rates) #run part A algorithm
    total_time_A = timer() - start_A    #calculate total time for part A

    start_D = timer()   #start the timer for part D
    result_D = part_D(exchange_rates) #run part D algorithm
    #print(result_D)
    total_time_D = timer() - start_D    #calculate total time for part D

    times.append([total_time_A, total_time_D])  #add the times to the list

    if result_A != result_D:    #checks if the algorithms are calculating the same result
        print('One of your algorithms has a mistake.')
        quit()

times = np.array(times) #makes the list print nicely
print()
print('[Part A Times, Part D Times]')
print(times)