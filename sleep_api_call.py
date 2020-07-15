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
    # body = '{\n  "aggregateBy": [{\n    "dataTypeName": "com.google.activity.segment",\n    "dataSourceId": "raw:com.google.activity.segment:com.xiaomi.hm.health:"\n  }],\n  "bucketByTime": { "durationMillis": '+ f'{durationMillis}' + ' },\n  "startTimeMillis": ' + f'{startTimeMillis}' + ',\n  "endTimeMillis": ' + f'{endTimeMillis}' + '\n}\n'
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
                         return 1
                        # return L4[i4]["intVal"]

    # return -1
      return 0
    except:
      return 0

def is_sleeping(startTimeMillis, endTimeMillis, access_token):

    resp = read_activity(startTimeMillis, endTimeMillis, access_token)
    # print(resp.json())
    return sleep_code_in(resp.json())


if __name__ == '__main__' :

    access_token = "ya29.a0AfH6SMDqv1rzOXHHiI-I3nYRRZWxUaGKo8rBmSidY2hXnoQmnfxq4fRrQBNoI3gs48ec2dp45-Lg4NxBz31Uxz5JuxJrd8HXw0SlCZGGUodbL7KcHCzXSQxCVeAfZw8YxrDAfcstWFu3SPQK9m9vc1l_AVtJ5dGPR7pD"
    is_sleep = is_sleeping(1584157920000,1584157920001,access_token)
    print(is_sleep)
