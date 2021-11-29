# Reaction Time Cheat
With this Repository you are able to easily climb the Leaderboard of the [Bernhard-Gaul Reaktionstest](https://www.bernhard-gaul.de/spiele/reaktion/reaktion.php). Just clone the Repository and go through the Usage.

## Usage

```python
from post import postTime

# creates an object where the username is "Username" and the reactiontime equal to 0.123s
p = postTime("Username", 123)

# puts your time on the leaderboard with the help of a POST request
p.send()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Credits
I have to give credit to the [js2py](https://github.com/PiotrDabkowski/Js2Py) Project, which helped me convert the blowfish encryption file into usable Python code.
## License
[MIT](https://choosealicense.com/licenses/mit/)