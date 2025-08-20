# EcomLegal : Assistant CGV pour MonEshop

## 📖 Résumé
Ce projet est un **Proof of Concept (POC)** visant à démontrer la faisabilité d’un assistant virtuel capable de répondre automatiquement aux questions sur les **Conditions Générales de Vente (CGV)** d’un site e-commerce.  
Le système combine :  
- une base de données SQLite pour stocker les questions/réponses et les logs,  
- un appel à un modèle OpenAI **fine-tuné** sur un corpus de CGV,  
- une interface simple en console Python pour tester le workflow.  

L’objectif pédagogique est de comprendre le cycle complet d’un projet IA en entreprise : **pré-prompting, fine-tuning, intégration, enregistrement des résultats et restitution**.

---

## 📑 Sommaire
1. [Objectif](#-objectif)  
2. [Architecture du projet](#-architecture-du-projet)  
3. [Organigramme](#-organigramme)  
4. [Installation](#-installation)  
5. [Utilisation](#-utilisation)  
6. [Fine-tuning du modèle](#-fine-tuning-du-modèle)  
7. [Ressources](#-ressources)  
8. [Auteur](#-auteur)  

---

## 🎯 Objectif
Automatiser la réponse aux questions juridiques courantes (paiement, rétractation, livraison, garantie, données personnelles) à partir des CGV de l’entreprise **MonEshop**.

---

## 📂 Architecture du projet

- `RecupererPrompt.py` : saisie utilisateur (console).  
- `PresenceBdd.py` : vérifie si la question existe déjà en base.  
- `ChatBot.py` : envoie la requête au modèle OpenAI si nouvelle question.  
- `AfficherPrompt.py` : affiche la réponse et gère la satisfaction utilisateur.  
- `data/` : scripts SQL de création de la table `logs`.  
- `train/` : données JSONL pour le fine-tuning.  
- `finetuning/` : scripts `addfile.py` et `finetuning.py`.  
- `.gitignore` : ignore `data/**` sauf `docker-compose.yml`.  

---

## 🗂 Organigramme
L’organigramme complet de l’algorithme se trouve dans :  

`documentations/organigramme.png`

---

## 🛠 Installation

### Prérequis
- Python 3.10+  
- Environnement virtuel (`venv`)  
- Clé API OpenAI  
- SQLite (local) ou Adminer (optionnel en Docker)

### Étapes
```bash
git clone https://github.com/natbediee/chatbot_cgv.git
cd chatbot_cgv
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```
Configuration

Un fichier .env.template est fourni. Copiez-le en .env puis renseignez votre clé API OpenAI :
```
OPENAI_API_KEY=sk-xxxx
```
Initialiser la base de données :
```bash
sqlite3 data/gestions_vol.db < data/gestions_vol.sql
```
## 🚀 Utilisation

Lancer le script principal :
```
python3 RecupererPrompt.py
```
- Si la question est connue → réponse immédiate.

- Sinon → envoi à l’API OpenAI, réponse stockée dans la base puis affichée.
  
## 📊 Fine-tuning du modèle

Préparer train/train.jsonl.

Uploader avec :

python finetuning/addfile.py


Lancer l’entraînement :

python finetuning/finetuning.py


Récupérer le nom du modèle fine-tuné (ex. ft:gpt-4.1-nano-2025-04-14:mon_projet_01:abcdef) et l’utiliser dans ChatBot.py.

## 📚 Ressources

- Guide officiel OpenAI Fine-Tuning

- Documentation SQLite

## ✍️ Auteur

Projet réalisé par Nathalie Bédiée et Gael Maiano
dans le cadre de la formation Développeur IA – ISEN Brest.
