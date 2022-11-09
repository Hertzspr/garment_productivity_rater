import pandas as pd
import numpy as np
import sklearn
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor
import bentoml

#

print("..ingesting data..")

gwp = 'garments_worker_productivity.csv'
data = pd.read_csv(gwp)

data['team'] = data['team'].astype('category')
data.date = pd.to_datetime(data.date, dayfirst=False, yearfirst=False) 
data['date_as_int'] = data.date.dt.strftime("%Y%m%d").astype(int)

cols_object = data.dtypes[data.dtypes=='object'].index.values
for col in cols_object:
    data[col] = data[col].str.lower().str.strip().str.replace(' ', '_')

data.wip = data.wip.fillna(0)
data.isnull().sum()

#

print("..wrangling data..")

cols_num_picked = ['targeted_productivity',
                   'idle_men',
                   'no_of_style_change',
                   'smv',
                   'date_as_int',
                   'idle_time',
                   'incentive',
                   'wip']

cols_obj_picked = ['quarter',
                   'department']

y_whole_train = data.actual_productivity.values
del data['actual_productivity']

dv = DictVectorizer(sparse = False)
data_dict = data[cols_num_picked + cols_obj_picked].to_dict(orient = 'records')
X_data = dv.fit_transform(data_dict)

#

print("..training model..")

rf_fin = RandomForestRegressor(n_estimators = 160,
                           max_depth = 5,
                           min_samples_leaf = 5,
                           random_state = 1)

rf_fin.fit(X_data, y_whole_train)

bentoml.sklearn.save_model('garment_productivity_model',
                            rf_fin,
                            custom_objects={'DictVectorizer': dv})


print("..saving model..")





