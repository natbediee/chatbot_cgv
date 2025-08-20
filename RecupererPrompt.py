import PresenceBdd
# recuperation du prompt de la question utilisateur
PromptUser= input("Quelle est votre question ?")
# on va vérifier dans notre BDD que cette question n'a pas déjà été posée
PresenceBdd.PresenceBdd(PromptUser)
