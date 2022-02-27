# shark

This program will at some point hopefully allow you to simulate poker games and write AI agents to play in those games.

## Running a game

To run a game all you need is Python 3:

```bash
python -m src
```

## Development

For development this project uses ```virtualenv``` for its Python environment, ```expect``` for coloured terminal output, ```pytest``` as a testing framework, and ```doit``` as a build tool.

To get started:

```bash
sudo apt install expect
virtualenv env
source env/bin/activate
pip install pytest doit
```

See dodo.py for development commands using doit build tool.

```bash
doit list
```

## Why?

- Because I feel like it?
- To get experience designing my own application.
- Maybe to try out multiprocessing.
- To try out reinforcement learning agents.
- To get better at poker.

## License

Copyright 2022 Thomas Woodruff

Licensed under the Apache License, Version 2.0 
