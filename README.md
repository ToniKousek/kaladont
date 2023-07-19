# Kaladont

In this repository is a solver for a game called **kaladont**. The game is played as instructed in the [How to play](#How-to-play) heading or in this [Wikipedia article](https://en.wikipedia.org/wiki/Kaladont).

The game is my childhood game which we would play on trips. Currently it uses croatian words, to use words from a diffrent language, change the `open_file()` function in the file [solver.py](solver.py)

## Download

To download the solver:

```
git clone
```

To play:

```
cd kaladont
python solver.py
```

## How to play

The game starts with one player saying a word. After that, usually clockwise or counterclockwise, other players say a word, paying attention to the fact that the word must be a verb in the infinitive or a noun in the nominative and must not be a proper name or an invented word. The player who cannot remember the word drops out of the game. The player who first says _“Kaladont”_ when someone says a word that ends in _“ka”_ or the player who remains last is the winner

## Dictionary

The dictionary is from https://github.com/gigaly/rjecnik-hrvatskih-jezika
