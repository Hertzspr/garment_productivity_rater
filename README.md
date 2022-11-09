# garment_productivity_rater

![Capture](https://user-images.githubusercontent.com/95233522/200820662-1b560a28-442e-4ae6-9410-f1dd60264fd8.JPG)



# Description of the problem

Data sourced from: https://archive.ics.uci.edu/ml/datasets/Productivity+Prediction+of+Garment

This is an implementation of supervised learning to solve regression problem. The model used in this program is random forest. It predicts how productive the performance of garment processing can be. 

# Instructions on how to run the project

Assuming you have docker and python installed in your environment. From your terminal, do these: 
1. Pull the image from dockerhub with ```docker pull sumurpikulkargo/garment_model```
2. Run the image with ```docker run -it --rm -p 3000:3000 garment_productivity_model:oahvo5k7j6kqpxcb``` 
3. Open http://localhost:3000/ in your web browser.
4. Use the 'try it out' feature in the POST /classify InferenceAPI(JSON → JSON) to input some garment processing data to infer the productivity rate. 

![aaaa sasa](https://user-images.githubusercontent.com/95233522/200820980-9e766771-84a2-4215-84c5-f7b97b368531.JPG)

If you want to run the program directly without docker image: 
Make sure pipenv is already installed in your environment. 
1. Use ```pipenv install``` to prepare your environment to run the program.
2. Run train.py to train model with ```python train.py```.
3. Run the service to local browser ```bentoml serve service:svc```.
4. Use the 'try it out' feature in the POST /classify InferenceAPI(JSON → JSON) to input some garment processing data to infer the productivity rate. 

# File info

- bentofile.yaml: file to build bento
- garments_worker_productivity.csv: data source used to train the model
- notebook.ipynb: documentation of how I did the preprocessing, EDA, modeling, and tuning
- service.py: script to run the model on your local network
- train.py: script to train and save the final model 
