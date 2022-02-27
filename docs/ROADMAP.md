# Architecture

- Should aim for speed, but not at the cost of simplicity and good design.

## Agents:

- Writing an agent should be as intuitive as possible.
- Agents should be able to be timed out. Maybe each agent can be its own sub-process?
- Should output some sort of game report as a file at the end --> should be easily parseable to facilitate hyper parameter tuning via scripts (json?).

## Simulations:

- Needs to allow numerous simulations. Should be able to run several concurrent ones throuch CLI (multiprocessing).

## GUI:

- Get the backend right and this should be easier.
- Have at least a really shitty gui at the start so you don't code yourself into a corner.

## Logs:

- two options:
  1. just one log file that everything goes into. Would run into issues if you use multiprocessing for agents.
  2. A game log file, and also one log file per agent.
- can just be print statements at first, which can be converted to logs after the gui is setup.

## CLI:

- Would be nice to be able to pass command line parameters in.

## Backtesting:

- Not a priority, but if anyone else ends up using this thing, this would be a great feature.
