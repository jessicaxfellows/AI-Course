#import required libraries 
import os
from google.cloud import storage
from google.cloud import aiplatform

#set up project and region variables 
PROJECT_ID = "tensorflowproject-402323"
REGION = "us-central1"

#set the bucket name
BUCKET_NAME = "my-new-bucket-972791123"

#authenticate google cloud account
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\jessi\\Downloads\\tensorflowproject-402323-42eb5ef818fc.json"

#create cloud storage bucket 
def create_bucket(bucket_name):
    """
    Creates a cloud storage bucket with the given name.
    """
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)
    print("Bucket created:", bucket.name)

#upload dataset file to cloud storage bucket
def upload_dataset(bucket_name, dataset_path):
    """"
    Uploads a dataset file to the specified cloud storage bucket
    """
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(os.path.basename(dataset_path))
    blob.upload_from_filename(dataset_path)
    print("Dataset file uploaded to Cloud Storage")

#create tabular dataset in vertex AI
def create_tabular_dataset(bucket_name, dataset_path):
    """
    Creates a tabular dataset in vertex AI using the specified bucket and dataset file
    """
    aiplatform.init(project=PROJECT_ID, location=REGION)

    gcs_source_uri = F"gs://{bucket_name}/{os.path.basename(dataset_path)}"
    dataset = aiplatform.TabularDataset.create(display_name="my-dataset", gcs_source=gcs_source_uri)
    print("Tabular Dataset created:", dataset.display_name)

#Analyze the dataset
def analyze_dataset(bucket_name, dataset_path):
    dataset = aiplatform.TabularDataset(
        project=PROJECT_ID,
        location=REGION,
        display_name="my-dataset",
        gcs_source=f"gs://{bucket_name}/{os.path.basename(dataset_path)}"
    )
    analysis = dataset.analyze()
    print("Dataset analysis results:")
    print(analysis)

#Main function
def Main():
    """
    Main fucntion that orchestrates the steps to create the bucket,
    upload the dataset, and create the Tabular datatset
    """
    create_bucket(BUCKET_NAME)
    upload_dataset(BUCKET_NAME, r"C:\\Users\\jessi\\image_dataset.csv")
    create_tabular_dataset(BUCKET_NAME, r"C:\\Users\\jessi\\image_dataset.csv")

#execute the main function
if __name__ == "__main__":
    Main()