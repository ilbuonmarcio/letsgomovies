# letsgomovies

`letsgomovies` is a Telegram Bot application in which you can see what movies are currently available in movie theaters!

## installation

- `git clone` this repository

- Create a virtual environment in which this application will run
    - e.g. using `virtualenv`, you can create one simply by typing `virtualenv venv`
      
        (`venv` is the name of the virtual environment's folder in which it will be created)

- Activate it with this command:
    - Windows: `./venv/Scripts/activate`
    - Linux/macOS: `source ./venv/bin/activate`

- Install the required libraries using `pip install -r requirements.txt`

- Create a new bot token by using Telegram's `@BotFather` and copying the bot token already created for you

- Associate the environment variable `LETSGOMOVIES_BOT_TOKEN` with the newly created bot token, e.g.:
  `LETSGOMOVIES_BOT_TOKEN=123810293812:2130412347213wdfkwqehfkqwejhfkwef` (remember to use __your__ token, this is a fake one!!!)

- Run the application by issuing the following command: `python app.py`

## support & contributions

This bot currently supports only [TheSpaceCinema.it](https://www.thespacecinema.it)'s movie list, but I'm sure it will be easy to implement other movie lists as well by the community contributions!

### License

This software is released under MIT License. See LICENSE file for more information.