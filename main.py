# main.py
import mlflow 

def workflow():
  try:  
    with mlflow.start_run() as active_run:
        print("Launching 'download'")
        download_run = mlflow.run(".", "download", parameters={})
        download_run = mlflow.tracking.MlflowClient().get_run(download_run.run_id)
        

        print("Launching 'process'")
        process_run = mlflow.run(".", "process", parameters={})
        process_run = mlflow.tracking.MlflowClient().get_run(process_run.run_id)
        


        print("Launching 'inference'")
        inference_run = mlflow.run(".", "inference", parameters={})
        train_run = mlflow.tracking.MlflowClient().get_run(inference_run.run_id)
  except:
    import os 
    os.system("bash run.sh")

if __name__ == '__main__':
    workflow()
