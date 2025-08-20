from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()


OPENAI_FILE_ID = "file-KVxbNSqdaXYu9fE82XF2Hm"
OPENAI_MODEL = "gpt-4.1-nano-2025-04-14"
OPENAI_TOKEN = os.environ["OPENAI_API_KEY"]
client = OpenAI()
try: 
  ft_job = client.fine_tuning.jobs.create(
  training_file=OPENAI_FILE_ID,
  model=OPENAI_MODEL
  )
  print("Fine Tune Job has been created with id ", ft_job.id)
except Exception as erreur:
    print("Erreur lors de la création du fine-tuning :", erreur) 

