import json
from datetime import datetime
import flask

import os

from flask import Flask , jsonify,request


#This funtion Calculate time difference in seconds 
def TimeDifferenceInSec(t1, t2):

    #Time format  -  Day dd Mon yyyy hh:mm:ss +xxxx 
    time_format = '%a %d %b %Y %H:%M:%S %z'

    #creates a datetime object from the given string with given format.
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)

    #return  time difference in seconds
    return str(int(abs((t1-t2).total_seconds()))) 


app = Flask(__name__)

 
input1 ='Sun 10 May 2015 13:54:36 -0700'
input2 ='Sun 10 May 2015 13:54:36 -0000'
input3 ='Sat 02 May 2015 19:54:36 +0530'
input4 ='Fri 01 May 2015 13:54:36 -0000'


@app.route('/',methods=['GET'])
def CalculateTimeInSec():
        
        # accept two test case input of Task A in body 
        #t1 = Test 1 input 1
        #t2 = Test 1 input 2
        #s1 = Test 2 input 1
        #s2 = Test 2 input 2

        t1 = str(input1)
        t2 = str(input2)
        s1 =str(input3)
        s2 = str(input4)
        testCase1 = TimeDifferenceInSec(t1,t2)
        testCase2 = TimeDifferenceInSec(s1,s2)
        host= os.getenv('HOSTNAME')
        ResData= json.dumps({'id': host,"result":[testCase1, testCase2]})

  
        resp =  flask.Response(ResData)    
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.content_type = 'application/json'
        return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=8000)  
