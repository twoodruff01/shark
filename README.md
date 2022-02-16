# shark

This program allows you to simulate poker games and write AI agents to play in those games.

## Why?

- Because I feel like it?
- To get experience designing a full application.
- Maybe to try out multiprocessing.
- To try out reinforcement learning agents.
- To get better at poker.

## How?

- Figure out how to play poker (ie the rules) --> Online poker...
- Design Architecture
- Code...

## Running a game

To use this software all you need is Python 3:

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

See dodo.py for build commands using doit build tool.

```bash
doit list
```

## License

Copyright © Thomas Woodruff, 2022

This file is part of shark.

Shark is free software: you can redistribute it and/or modify it under the terms of 
the GNU Affero General Public License as published by the Free Software Foundation.

Shark is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with shark. If 
not, see <https://www.gnu.org/licenses/>.
