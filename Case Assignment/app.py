# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:13:39 2020

@author: RebekahDSK
"""

# -*- coding: utf-8 -*-
#%%
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from flask import Flask
#%%
engine = create_engine('sqlite:///Resources/hawaii.sqlite')
#%%
app = Flask(__name__)
#%%
@app.route("/")
def welcome():
    return(f"Welcome to the Home Page <br/>"
           f"Here are the available routes <br/>"
           f"/api/v1.0/precipitation<br/>"
           f"/api/v1.0/stations<br/>"
           f"/api/v1.0/tobs<br/>"
           f"/api/v1.0/<start><br/>"
           f"/api/v1.0/<start>/<end>")
#%%
print('testing')
@app.route('/api/v1.0/precipitation')
def prcp():
    conn = engine.connect()
    query = f'''
        SELECT 
            date,
            AVG(prcp) as avg_prcp
        FROM
            measurement
        WHERE
            date >= (SELECT DATE(MAX(date),'-1 year') FROM measurement)
        GROUP BY
            date
        ORDER BY 
            date
    '''
    # Save the query results as a Pandas DataFrame and set the index to the date column
    prcp_df = pd.read_sql(query, conn)
    # Convert the date column to date
    prcp_df['date'] = pd.to_datetime(prcp_df['date'])
    # Sort the dataframe by date
    prcp_df.sort_values('date')
    prcp_json = prcp_df.to_json(orient='records')
    conn.close()
    return prcp_json

#%%
print('testing')
@app.route('/api/v1.0/stations')
def stations():
    conn = engine.connect()
    query = f'''
        SELECT name
        FROM station
   '''
station_names = pd.read_sql(query, conn) 
station_json = station_names.to_json(orient='records')
conn.close()
return station_json
    
#%%

if __name__ == '__main__':
    app.run(debug=True)    
#%%
'''
/api/v1.0/precipitation
Convert the query results to a dictionary using date as the key and prcp as the value.
Return the JSON representation of your dictionary.
/api/v1.0/stations
Return a JSON list of stations from the dataset.
'''