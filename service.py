# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 00:25:55 2022

@author: husad
"""

import bentoml
from bentoml.io import JSON
from pydantic import BaseModel

class GarmentProductivity(BaseModel):
  targeted_productivity: float
  idle_men: int
  no_of_style_change: int
  smv: float
  date_as_int: int
  idle_time: float
  incentive: int
  wip: float
  quarter: str
  department: str

# Pull the model as model reference (it pulls all the associate metadata of the model)
model_ref = bentoml.sklearn.get('garment_productivity_model:latest')

# Call DictVectorizer object using model reference
dv = model_ref.custom_objects['DictVectorizer']

# Create the model runner (it can also scale the model separately)
model_runner = model_ref.to_runner()

# Create the service 'garment_productivy_model' and pass the model
svc = bentoml.Service('garment_productivity_model',
                      runners = [model_runner])


# Define an endpoint on the BentoML service
@svc.api(input = JSON(pydantic_model = GarmentProductivity),
         output = JSON()) # decorate endpoint
async def classify(garment_data):
    garment_data_dict = garment_data.dict()
    vector = dv.transform(garment_data_dict)
    prediction = await model_runner.predict.async_run(vector)
    print(prediction)
    result = prediction

    if result < 0.9: 
      return {"status": "High productivity!"}
    elif result < 0.5:
      return {"status": "WARNING! LOW PRODUCTIVITY"}
    else:
      return {"status": "Normal Productivity!"}
	
    
    

















