# Undertale Tile Game

This is a simple tile maze where the objective is to get from the left to the right, based on Undertale.

## Rules

- Pink: you can step on this.
- Red: you cannot step on this.
- Yellow: gives you an electric shock that kills you.
- Orange: makes you smell of oranges.
- Purple: is slippery and smells of lemons; you slide over to the next tile smelling of lemons.
- Blue: piranha-infested water is unsafe when next to yellow, or when you smell of oranges (but not lemons).

## Current state

Currently, the game presents you with a 20x9 grid randomly generated, with weight given to dangerous tiles, and generates a basic path. The basic path is a sequence of up, down, or right movements.

## Potential changes to make

- More complex path generation (to allow for going left and minimize redundancy).
- Add different coloured tiles.
- Allow optional grid sizes.
- General clean-up


## To run

```
git clone https://github.com/JoStMc/undertale-tile-game
cd undertale-tile-game
chmod +x main.sh
./main.sh
```
