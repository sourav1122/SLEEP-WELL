from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import datetime
import json
import time
from flask import request
from urllib2 import urlopen
from urllib2 import Request, urlopen, URLError
#from urllib.request import urlopen,URLError
#from urllib2 import Request, urlopen, URLError
import json
import mimetools
BOUNDARY = mimetools.choose_boundary()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test2.db'
db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    avatar = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=False)
    tokens = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    
    def __repr__(self):
        return str([str(self.id),str(self.email),str(self.name),str(avatar),str(self.active),str(self.tokens),str(self.created_at)])
####################### calling of refresh token function ###############################
BOUNDARY = mimetools.choose_boundary()
CRLF = '\r\n'
obj = User.query.filter(row=condition).first()
obj.column=new
db.session.commit()
def EncodeMultiPart(fields, files, file_type='application/xml'):
    """Encodes list of parameters and files for HTTP multipart format.

    Args:
      fields: list of tuples containing name and value of parameters.
      files: list of tuples containing param name, filename, and file contents.
      file_type: string if file type different than application/xml.
    Returns:
      A string to be sent as data for the HTTP post request.
    """
    lines = []
    for (key, value) in fields:
      lines.append('--' + BOUNDARY)
      lines.append('Content-Disposition: form-data; name="%s"' % key)
      lines.append('')  # blank line
      lines.append(value)
    for (key, filename, value) in files:
      lines.append('--' + BOUNDARY)
      lines.append(
          'Content-Disposition: form-data; name="%s"; filename="%s"'
          % (key, filename))
      lines.append('Content-Type: %s' % file_type)
      lines.append('')  # blank line
      lines.append(value)
    lines.append('--' + BOUNDARY + '--')
    lines.append('')  # blank line
    #print(CRLF.join(lines))
    return CRLF.join(lines)
def refresh_token(val):
    #print(val)
    url = "https://oauth2.googleapis.com/token"
    headers = [
             ("grant_type",  "refresh_token"),
             ("client_id", "dummy_value.apps.googleusercontent.com"),
             ("client_secret", "dummy_value"),
             ("refresh_token",val),
             ]
#ya29.a0AfH6SMD9tm8FBT7a7woiFqGb4G4Mn4ZM9gMmGd75YJVSGU9Gyb_dJTUYF9hN3wqkL5FU-6tlos0LGYWaOQ_se9Ub43fT5wWbvy3GaXWsWYFjdjm-50uoECQnu_VHQU6zh7p8huR_MJfohCJCNAJpWriRT8kTcu-XvRk
    files = []
    edata = EncodeMultiPart(headers, files, file_type='text/plain')
    #print(EncodeMultiPart(headers, files, file_type='text/plain'))
    headers = {}
    request = Request(url, headers=headers)
    request.add_data(edata)

    request.add_header('Content-Length', str(len(edata)))
    request.add_header('Content-Type', 'multipart/form-data;boundary=%s' % BOUNDARY)
    response = urlopen(request).read()
    response = json.loads(response) 
    return response["access_token"]
########################end of refresh token functn ##############################



############################## sleep read functn############################
import requests
import json

def read_activity(startTimeMillis, endTimeMillis, access_token, durationMillis=3600000):
    '''
    returns the response containing activities in range [startTimeMillis, endTimeMillis]
    '''
    headers = {
    'Content-Type': 'application/json',
    }
    params = (
        ('access_token', access_token),
    )
    body = '{\n  "aggregateBy": [{\n    "dataTypeName": "com.google.activity.segment"\n  }],\n  "bucketByTime": { "durationMillis": '+ str(durationMillis) + ' },\n  "startTimeMillis": ' + str(startTimeMillis) + ',\n  "endTimeMillis": ' + str(endTimeMillis) + '\n}\n'

    url = "https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate"

    resp = requests.post(url=url, headers=headers, params=params, data=body)

    return resp
def sleep_code_in(resp):
    '''
    returns a bool value 'true' if user is sleeping
    '''
    # L = resp["bucket"][0]["dataset"][0]["point"]

    # for i in range(len(L)):
    #     L1 = L[i]["value"]
    #     for j in range(len(L1)):
    #         if L1[j]["intVal"] in [72, 109, 110, 111, 112]:
    #             # return True
    #             return L1[j]["intVal"]

    # return -1
    try:
      L1 = resp["bucket"]

      for i1 in range(len(L1)):
         L2 = L1[i1]["dataset"]
         for i2 in range(len(L2)):
             L3 = L2[i2]["point"]
             for i3 in range(len(L3)):
                 L4 = L3[i3]["value"]
                 for i4 in range(len(L4)):
                     if L4[i4]["intVal"] in [72, 109, 110, 111, 112]:
                         return True
                        # return L4[i4]["intVal"]

    # return -1
      return False
    except:
      return 0

def is_sleeping(startTimeMillis, endTimeMillis, access_token):
    resp = read_activity(startTimeMillis, endTimeMillis, access_token)
    return sleep_code_in(resp.json())
##########################################################################

########################   main_user_functn  ###############################
c=2
while(c!=0):
  email=[]
  name=[]
  avatar=[]
  active=[]
  a_token=[]
  r_token=[]
  #created_at=[]
  old_year=[]
  old_month=[]
  old_day=[]
  old_hour=[]
  all_user=User.query.all()
  for i in all_user:
    email.append(i.email)
    name.append(i.name)
    avatar.append(i.avatar)
    active.append(i.active)
    test_string=i.tokens
    res = json.loads(test_string) 
    a_token.append(res["access_token"])
    r_token.append(str(res['refresh_token']))
    times=i.created_at
    old_year.append(times.year)
    old_month.append(times.month)
    old_hour.append((times.hour)*3600+(times.minute)*60+times.second)
    old_day.append(times.day)
  new_year=[]
  new_month=[]
  new_day=[]
  new_hour=[]
  dt=datetime.datetime.today()
  new_year.append(dt.year)
  new_month.append(dt.month)
  new_hour.append((dt.hour)*3600+(dt.minute)*60+dt.second)
  new_day.append(dt.day)
  print(all_user)
  i=0
  while(c>0):
    c-=1
    i=i%len(a_token)
    #print(r_token[i])
    current_user_ac=a_token[i]
    endTimeMillis=int(round(time.time() * 1000))
    startTimeMillis=endTimeMillis-5000
    #print(r_token[i],"yhape")
    #if abs(new_hour[i]-old_hour[i])>=1800:
    #  print(refresh_token(r_token[i]))
    #  current_user_ac=refresh_token(r_token[i])
    if is_sleeping(1584157920000,1584157920001,"ya29.a0AfH6SMB3dO8D7Id6SxY8OBtM-PkHH0tjZSYC7ASSf3zXAdjmzVhGAgBZvdpK39ovzicW22lKa9_WL56fBxmT7lsMsDLCn-qjVNIf5X_YHF3QoRVqHhEoc14-9eQoqvwshHBE4XfemNCpbTg3-rodsitR7k4jlZFdXxFv")==1:
      print("is sleeping")
    else:
      print("not_sleeping")
    i+=1
