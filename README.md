# websocket_learning_session
basic websocket code for the leaning session - it's just the example code from [websockets quickstart](https://websockets.readthedocs.io/en/stable/howto/quickstart.html#manage-application-state) on how to manage state in the server.

# getting started

1) do the usual python virtual environment setup, e.g:

- `python3 -m venv venv`
- `source venv/bin/activate`
- make sure your vscode is looking at your new virtual env.

2) then install websockets

- `pip install websockets`

3) you'll also need to install the [LiveServer vscode extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer), or do whatever your method is to run a local html file in your browser.

4) run the server with `python3 counter.py`, it should print 'hi this is counter.py' and *not* exit.

5) run counter.html with live server or however you like. With live server you can either click 'go live' btn bottom right of vs code (make sure you have the html file selected) or right click on the html file and select 'open with live server'. This should open your browser at localhost:5500, and you should see a basic webpage.

# next steps
- go mess around with it.
- try and figure out how it works.
- think about how we can use this to implement live colab (the code I used to create the prototype is in the 'proto_code' folder in this repo. the .ts files have the code to adapt the current lca-studio-prototype code.)
- **Try and think of a better way for us to do this. There's definately other methods for getting the same result - some of them will probably be better.**
- we will run through this code quickly in the learning session to make sure everyone had a basic idea of what's going on, then we'll move on to discussing possibilities for how we can do live colab for realzies.
