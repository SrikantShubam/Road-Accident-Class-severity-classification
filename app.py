from flask import Flask,render_template, request, send_file
import pandas as pd
import pickle
import gzip
import sklearn
import numpy as np
app = Flask(__name__)



@app.route("/")
def hello_world():
    
    return render_template( 'index.html',data='data inserted successfully')

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
    msg="""sumary_line"""
    driver_age=request.form['Age']
    
    driver_sex=request.form['sex']
 
    educational_level=request.form['ed_lvl']
    vehicle_driver_relation=request.form['relation']
    driving_experience=request.form['dr_exp']
    lanes=request.form['lanes']
    junction_type=request.form['junc_type']
    surface_type=request.form['road_type']
    light_condition=request.form['light']
    weather_condition=request.form['weather']
    collision_type=request.form['colli_type']
    vehicle_movement=request.form['veh_move']
    pedestrian_movement=request.form['ped_move']
    accident_cause=request.form['acci_cause']

    
    df={'driver_age':[driver_age], 'driver_sex':[driver_sex], 'educational_level':[educational_level],
       'vehicle_driver_relation':[vehicle_driver_relation], 'driving_experience':[driving_experience], 'lanes':[lanes],
       'junction_type':[junction_type], 'surface_type':[surface_type], 'light_condition':[light_condition], 'weather_condition':[weather_condition],
       'collision_type':[collision_type], 'vehicle_movement':[vehicle_movement], 'pedestrian_movement':[pedestrian_movement],
       'accident_cause':[accident_cause]}
    data=pd.DataFrame(df)
    print("the dataframe is----->",data)
    # for i in data.columns:
    #    data[i]= data[i].astype('object')

    # print(type(data["driver_age"]))
    df2=pd.DataFrame()
#Load the encoding object from the file using pickle
    with open("encoding.pkl", 'rb') as f:
         le = pickle.load(f)
    
         for col in data.columns:
                df2[col] = le.fit_transform(data[col])
    print(df2)
    return render_template( 'index.html',data='data inserted successfully')
if __name__=="__main__":
    app.run(debug=True,use_reloader=True)