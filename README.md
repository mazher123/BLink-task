# Blink-task
python service that calculate date time difference in seconds according to location 


#Task - A 
Take number of test case  Input from User\

In each test case:\
Take t1 - first input of date time GMt String\
Take T2 - second input of date time Gmt String\ 
Print time difference in Seconds\

#Task B 
Flask is Install by PIP install flask \

run python main.py 

hit URL www.serverURL/time-difference

Accept 4 data from API body \  
t1  is testcase 1 input 1  \
t2 is testcase 1 input 2 \
s1 is testcase 2 input 1 \
s2 is testcasse2 input 2  \

Time difference in seconds is calculated and return as order json array\ 


#Task-C

add hostname environment variable  to get the node id 
containerize the application with dockerfile
run two containers from the docker image

build command :  docker build -t backend .
run command : conatiner1 : docker  run -d -p 8080:8000 backend 
              container2 :docker run -d -p  8081:8000 backend 

Hit url :  Localhost:8081/
           Localhost:8080/










