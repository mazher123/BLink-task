from datetime import datetime

#This funtion Calculate time difference in seconds 
def TimeDifferenceInSec(t1, t2):

    #Time format  -  Day dd Mon yyyy hh:mm:ss +xxxx 
    time_format = '%a %d %b %Y %H:%M:%S %z'

    #creates a datetime object from the given string with given format.
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)

    #return  time difference in seconds
    return str(int(abs((t1-t2).total_seconds()))) 


#Taking input
t = int(input())

#iterate through t and take input 
for t_itr in range(t):
    t1 = input()
    t2= input()

    #final result is fetch from the function 
    output = TimeDifferenceInSec(t1,t2)
    print(output)
