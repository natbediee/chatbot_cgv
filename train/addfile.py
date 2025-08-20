from openai import OpenAI 
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_TOKEN = os.environ["OPENAI_API_KEY"]
INPUT_FILE = "train.jsonl" 
client = OpenAI(api_key=OPENAI_TOKEN) 
file = client.files.create( 
file=open(INPUT_FILE, "rb"), 
purpose="fine-tune" 
)
print("Fine id",file.id)