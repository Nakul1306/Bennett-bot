# Bennett-bot
You need to install numpy:

pip install numpy

and also install tensorflow and pickle and json:

pip install tensorflow
pip install pickle
pip install json

You also need nltk:

pip install nltk

If you get an error during the first run, you also need to install nltk.tokenize.punkt: Run this once in your terminal:

>>>import nltk

>>>nltk.download('punkt')


Run

python training.py

This will train the model of chat bot. And then run

python chatbot.py


If you need to run it in webpage then install Flask:

pip install Flask

open the webpage on:     http://127.0.0.1:5000/

Customize

Have a look at intents.json. You can customize it according to your own use case. Just define a new tag, possible patterns, and possible responses for the chat bot. You have to re-run the training whenever this file is modified.

{
  "intents": [
    {
    
      "tag": "greeting",
      
      "patterns": ["Hi", "Hey", "How are you", "Is anyone there?", "Hello", "Good day"],
      
      "responses": ["Hey :-)", "Hello, thanks for visiting", "Hi there, what can I do for you?", "Hi there, how can I help?"]
      
    },
    ...
  ]
}
