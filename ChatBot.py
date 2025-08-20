import AfficherPrompt
from openai import OpenAI
from dotenv import load_dotenv
import os
import mysql.connector as mysql

def ChatBot(PromptUser) :
    load_dotenv()
    # On fait une instance sur notre modèle
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    MODEL_NAME = "ft:gpt-4.1-nano-2025-04-14:jn-formation::Bqz1DM3f"
    # Envoi des éléments au modèle
    reponse = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
        {"role": "user", "content": PromptUser}
        ]
    )
    # retour du modèle
    ReponseChat=reponse.choices[0].message.content
    AfficherPrompt.AfficherPrompt(ReponseChat)
    # maj de notre BDD avec la question de l'utilisateur et la réponse du modèle
    MajBdd(PromptUser,ReponseChat)

def MajBdd(PromptUser,Reponse) :
    questions = []
    bdd = mysql.connect(
        host='localhost',
        user='root',
        password='example',
        database='cgvbot',
        port=3306
    )
    cursor = bdd.cursor()

    query = "INSERT INTO questions (question, reponse,satisfaction) VALUES ('"+PromptUser.replace("'","")+"', '"+Reponse.replace("'","")+"','')" 
    cursor.execute(query)
    bdd.commit()

    cursor.close()
    bdd.close()