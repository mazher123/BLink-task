import json
from datetime import datetime
import flask
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
@app.route('/',defaults={ 'BanglaLink : Start Something new '})

@app.route('/time-difference',methods=['GET'])
def CalculateTimeInSec():
        Requests =request.get_data()
        # accept two test case input of Task A in body 
        #t1 = Test 1 input 1
        #t2 = Test 1 input 2
        #s1 = Test 2 input 1
        #s2 = Test 2 input 2

        data=json.loads(Requests)
  
