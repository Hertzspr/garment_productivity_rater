# garment_productivity_rater


# Description of the problem

Data sourced from: https://archive.ics.uci.edu/ml/datasets/Productivity+Prediction+of+Garment

This is an implementation of supervised learning to solve regression problem. The model used in this program after exploration in notebook.ipynb is random tree. It predicts how productive the performance of garment processing can be. 

# Instructions on how to run the project

Assuming you have docker and python installed in your environment. From your terminal, do these: 
1. Pull the image from dockerhub with ```docker pull sumurpikulkargo/garment_model```
2. Run the image with ```docker run -it --rm -p 3000:3000 garment_productivity_model:latest``` 
3. Open http://localhost:3000/ in your web browser.
4. Use the 'try it out' feature in the POST /classify InferenceAPI(JSON → JSON) to input some garment processing data to infer the productivity rate. 
