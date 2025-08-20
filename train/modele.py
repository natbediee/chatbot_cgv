from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Remplace par ton vrai job ID
job_id = "ftjob-MPrm3zTHQgeg59mQ2rBLyChf"

job = client.fine_tuning.jobs.retrieve(job_id)

# Affiche le nom du modèle fine-tuné (si terminé)
print("Nom du modèle :", job.fine_tuned_model)