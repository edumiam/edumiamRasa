# Edumiam Rasa

Chatbot pour Edumiam construit avec Rasa: https://rasa.com/

# Installation

1. Install Python: https://www.python.org/downloads/
1. `pip install rasa`
1. `pip install spacy`
1. `pip install prompt-toolkit==2.0.10`
1. `pip install questionary==1.4.0`
1. `python -m spacy download fr_core_news_md`
1. `python -m spacy link fr_core_news_md fr`
1. `rasa run actions` pour démarrer le serveur d'actions
1. Dans un autre terminal, `rasa shell` pour démarrer le test du chatbot