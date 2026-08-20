import os
import sys
import pandas as pd
import numpy as np
import mlflow
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
from mlflow.models.signature import infer_signature
import mlflow.sklearn
import logging


logging.basicConfig(level=logging.WARN)
logger=logging.getLogger(__name__)

def eval_metrics(actual,pred):
    rmse=np.sqrt(mean_squared_error(actual,pred))
    mae=mean_absolute_error(actual,pred)
    r2=r2_score(actual,pred)
    
    return rmse,mae,r2

if __name__=="__main__":
    
    # Read dataset
    csv_url = "https://raw.githubusercontent.com/mlflow/mlflow-example/master/wine-quality.csv"    
    try:
        data = pd.read_csv(csv_url)
    except Exception as e:
        logger.exception("Unable to download the data")
        
    
    # Split the data
    train,test=train_test_split(data)
    
    train_x=train.drop(["quality"],axis=1)
    test_x=test.drop(["quality"],axis=1)
    train_y=train[["quality"]]
    test_y=test[["quality"]]
    
    alpha=float(sys.argv[1]) if len(sys.argv)>1 else 0.5
    l1=float(sys.argv[2]) if len(sys.argv)>2 else 0.5
    
    # For the remote server
    remote_server="http://ec2-3-235-160-36.compute-1.amazonaws.com:5000/"
    mlflow.set_tracking_uri(remote_server)
    
    with mlflow.start_run():
        lr=ElasticNet(alpha=alpha,l1_ratio=l1,random_state=42)
        lr.fit(train_x,train_y)
    
        predicted=lr.predict(test_x)
        (rmse,mae,r2)=eval_metrics(test_y,predicted)    
        print(f"Alpha: {alpha}, L1 ration: {l1}")
        print(f"RMSE: {rmse}")
        print(f"MAE: {mae}")
        print(f"R2: {r2}")
        
        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1)
        
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)
        
        
        tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme
        if tracking_url_type_store!="file":
            mlflow.sklearn.log_model(
                lr,"model",registered_model_name="ElasticSearchWineModel"
            )
        else:
            mlflow.sklearn.log_model(
                lr,"model"
            )
        