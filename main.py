# uvicorn main:app --host 0.0.0.0 --port 5050

from fastapi import FastAPI
import pandas as pd

app = FastAPI()

bus_course = pd.read_excel('./datasets/seoul_busId_course.xlsx')
stop_location = pd.read_excel('./datasets/seoul_busStop_location.xlsx')


@app.get('/work')
def work():
    bus_list = []
    stop_list = []

    for idx in range(len(bus_course)):
        bus_dict = {'bus_name': bus_course['노선명'].iloc[idx], 'route_id': int(bus_course['ROUTEID'].iloc[idx])}
        bus_list.append(bus_dict)

    for idx in range(len(stop_location)):
        stop_dict = {'stop_id': int(stop_location['NODE_ID'].iloc[idx]),
                     'ars_id': int(stop_location['ARS_ID'].iloc[idx]), 'Stop_name': stop_location['정류소명'].iloc[idx],
                     'x': stop_location['X좌표'].iloc[idx], 'y': stop_location['Y좌표'].iloc[idx]}
        stop_list.append(stop_dict)

    result = {
        'bus': bus_list,
        'stop': stop_list
    }

    return result
