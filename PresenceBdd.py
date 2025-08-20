import mysql.connector as mysql
import ChatBot
import AfficherPrompt

def PresenceBdd(PromptUser):   
    # connection à notre base SQJ
    bdd = mysql.connect(
        host='localhost',
        user='root',
        password='example',
        database='cgvbot',
        port=3306
    )
    # vérifier que la question n'est pas déjà présente pour éviter un appel au modèle
    cursor = bdd.cursor()
    query="SELECT reponse FROM questions where question='"+PromptUser+"'"
    cursor.execute(query)
    resultat = cursor.fetchone()
    cursor.close()
    bdd.close()
    if resultat is None :
        # Pas de résultat, on fait au modèle pour répondre à la question
        ChatBot.ChatBot(PromptUser)
    else:
        # On affiche la réponse de notre BDD
        AfficherPrompt.AfficherPrompt(resultat[0])
   