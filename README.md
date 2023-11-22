# Implementation of a College chat bot.  
Simple chatbot implementation which answers queries about Bennett University. 

- The implementation should be easy to follow for beginners and provide a basic understanding of chatbots.
- Customization for your own use case is super easy. Just modify `intents.json` with possible patterns and responses and re-run the training (see below for more info).

The approach is inspired by this article: [https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077](https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077).


## Installation


### Install Numpy and other dependencies
You need Tensorflow, numpy, pickle and json
 ```console
pip install tensorflow
 ```

 ```console
pip install numpy
 ```

  ```console
pip install pickle
 ```
  ```console
pip install json
 ```

You also need `nltk`:
 ```console
pip install nltk
 ```

If you get an error during the first run, you also need to install `nltk.tokenize.punkt`:
Run this once in your terminal:
 ```console
$ python
>>> import nltk
>>> nltk.download('punkt')
```

## Usage
Run
```console
python training.py
```
This will train the chatbot_model. And then run
```console
python chatbot.py
```

### Webpage
If you need to run it on webpage then install Flask
 ```console
pip install flask
 ```
Then run
 ```console
python app.py
 ``` 
You can see the webpage on http://127.0.0.1:5000/ 

## Customize
Have a look at [intents.json](intents.json). You can customize it according to your own use case. Just define a new `tag`, possible `patterns`, and possible `responses` for the chat bot. You have to re-run the training whenever this file is modified.
```console
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
```
