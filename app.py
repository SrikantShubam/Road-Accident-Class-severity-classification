from flask import Flask, render_template, request, send_file
import pandas as pd
import pickle
import gzip
import sklearn
import numpy as np
app = Flask(__name__)


@app.route("/")
def hello_world():

    return render_template('index.html', data='data inserted successfully')

# @app.route('/video')
# def video():
#     return send_file('path/to/video.mp4', mimetype='video/mp4', conditional=True, add_etags=True)
# @app.after_request
# def after_request(response):
#     response.headers.add('Accept-Ranges', 'bytes')
#     return response


@app.route('/submit', methods=['POST'])
# list=[]
def post():
    msg = """sumary_line"""
    driver_age = request.form['Age']

    driver_sex = request.form['sex']

    educational_level = request.form['ed_lvl']
    vehicle_driver_relation = request.form['relation']
    driving_experience = request.form['dr_exp']
    lanes = request.form['lanes']
    junction_type = request.form['junc_type']
    surface_type = request.form['road_type']
    light_condition = request.form['light']
    weather_condition = request.form['weather']
    collision_type = request.form['colli_type']
    vehicle_movement = request.form['veh_move']
    pedestrian_movement = request.form['ped_move']
    accident_cause = request.form['acci_cause']

    df = {'driver_age':driver_age, 'driver_sex':driver_sex, 'educational_level':educational_level,
          'vehicle_driver_relation':vehicle_driver_relation, 'driving_experience':driving_experience, 'lanes':lanes,
          'junction_type':junction_type, 'surface_type':surface_type, 'light_condition':light_condition, 'weather_condition':weather_condition,
          'collision_type':collision_type, 'vehicle_movement':vehicle_movement, 'pedestrian_movement':pedestrian_movement,
          'accident_cause': accident_cause}
   


    dct = {k:[v] for k,v in df.items()} # WORKAROUND
    data = pd.DataFrame(dct)
    # print("the dataframe is----->", data)
    # for i in data.columns:
    #    data[i]= data[i].astype('object')

    # print(type(data["driver_age"]))
 
    # data.to_csv("original.csv")
# Load the encoding object from the file using pickle
    

        # for col in data.columns:
        #     data[col] = le.fit_transform(data[col])
    dict1 = {'driver_age': {'18-30': 0,
                            '31-50': 1,
                            'Over 51': 2,
                            'Under 18': 3,
                            'Unknown': 4},
             'driver_sex': {'Female': 0, 'Male': 1, 'Unknown': 2},
             'educational_level': {'Above high school': 0,
                                   'Elementary school': 1,
                                   'High school': 2,
                                   'Illiterate': 3,
                                   'Junior high school': 4,
                                   'Unknown': 5,
                                   'Writing & reading': 6},
             'vehicle_driver_relation': {'Employee': 0,
                                         'Other': 1,
                                         'Owner': 2,
                                         'Unknown': 3},
             'driving_experience': {'1-2yr': 0,
                                    '2-5yr': 1,
                                    '5-10yr': 2,
                                    'Above 10yr': 3,
                                    'Below 1yr': 4,
                                    'No Licence': 5,
                                    'Unknown': 6,
                                    'unknown': 7},
             'lanes': {'Double carriageway (median)': 0,
                       'One way': 1,
                       'Two-way (divided with broken lines road marking)': 2,
                       'Two-way (divided with solid lines road marking)': 3,
                       'Undivided Two way': 4,
                       'Unknown': 5,
                       'other': 6},
             'junction_type': {'Crossing': 0,
                               'No junction': 1,
                               'O Shape': 2,
                               'Other': 3,
                               'T Shape': 4,
                               'Unknown': 5,
                               'X Shape': 6,
                               'Y Shape': 7},
             'surface_type': {'Asphalt roads': 0,
                              'Asphalt roads with some distress': 1,
                              'Earth roads': 2,
                              'Gravel roads': 3,
                              'Other': 4,
                              'Unknown': 5},
             'light_condition': {'Darkness - lights lit': 0,
                                 'Darkness - lights unlit': 1,
                                 'Darkness - no lighting': 2,
                                 'Daylight': 3},
             'weather_condition': {'Cloudy': 0,
                                   'Fog or mist': 1,
                                   'Normal': 2,
                                   'Other': 3,
                                   'Raining': 4,
                                   'Raining and Windy': 5,
                                   'Snow': 6,
                                   'Unknown': 7,
                                   'Windy': 8},
             'collision_type': {'Collision with animals': 0,
                                'Collision with pedestrians': 1,
                                'Collision with roadside objects': 2,
                                'Collision with roadside-parked vehicles': 3,
                                'Fall from vehicles': 4,
                                'Other': 5,
                                'Rollover': 6,
                                'Unknown': 7,
                                'Vehicle with vehicle collision': 8,
                                'With Train': 9},
             'vehicle_movement': {'Entering a junction': 0,
                                  'Getting off': 1,
                                  'Going straight': 2,
                                  'Moving Backward': 3,
                                  'Other': 4,
                                  'Overtaking': 5,
                                  'Parked': 6,
                                  'Reversing': 7,
                                  'Stopping': 8,
                                  'Turnover': 9,
                                  'U-Turn': 10,
                                  'Unknown': 11,
                                  'Waiting to go': 12},
             'pedestrian_movement': {"Crossing from driver's nearside": 0,
                                     'Crossing from nearside - masked by parked or statioNot a Pedestrianry vehicle': 1,
                                     'Crossing from offside - masked by  parked or statioNot a Pedestrianry vehicle': 2,
                                     'In carriageway, statioNot a Pedestrianry - not crossing  (standing or playing)': 3,
                                     'In carriageway, statioNot a Pedestrianry - not crossing  (standing or playing) - masked by parked or statioNot a Pedestrianry vehicle': 4,
                                     'Not a Pedestrian': 5,
                                     'Unknown or other': 6,
                                     'Walking along in carriageway, back to traffic': 7,
                                     'Walking along in carriageway, facing traffic': 8},
             'accident_cause': {'Changing lane to the left': 0,
                                'Changing lane to the right': 1,
                                'Driving at high speed': 2,
                                'Driving carelessly': 3,
                                'Driving to the left': 4,
                                'Driving under the influence of drugs': 5,
                                'Drunk driving': 6,
                                'Getting off the vehicle improperly': 7,
                                'Improper parking': 8,
                                'Moving Backward': 9,
                                'No distancing': 10,
                                'No priority to pedestrian': 11,
                                'No priority to vehicle': 12,
                                'Other': 13,
                                'Overloading': 14,
                                'Overspeed': 15,
                                'Overtaking': 16,
                                'Overturning': 17,
                                'Turnover': 18,
                                'Unknown': 19}}

    for i in data.columns:
        item = data[i][0]
    #     print(item)
        if i in dict1:
            # print(i)
            if item in dict1[i]:
                data[i][0] = dict1[i][item]
    # print(data.head)
    # data.to_csv("data.csv")
    with gzip.open('model.pkl.gz', 'rb') as f:
         compressed_data = f.read()
         model = pickle.loads(compressed_data)
         pred=model.predict(data)
        #  print("Shree ram jaanki baithe hain mere seene mai")
        #  print(pred)
    return render_template('predict.html', data=pred,cause=accident_cause,road_type=surface_type)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
