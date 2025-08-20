import PresenceBdd

def main():

    # recuperation du prompt de la question utilisateur
    PromptUser= input("Quelle est votre question ?")
    if not PromptUser:
            print("Aucune question saisie.")
            return
    # on va vérifier dans notre BDD que cette question n'a pas déjà été posée
    PresenceBdd.PresenceBdd(PromptUser)

if __name__ == "__main__":
    main()