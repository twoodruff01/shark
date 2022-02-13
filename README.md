# shark

This program allows you to simulate poker games and write AI agents to play in those games.

Or at least, it will...

## Why?

- Because I feel like it?
- To get experience designing a full application.
- Maybe to try out multiprocessing.
- To try out reinforcement learning agents.
- To get better at poker.

## How

- Figure out how to play poker (ie the rules) --> Online poker...
- Design Architecture
- Code...

### Development

```Bash
python -m src
```

### Testing

```Bash
pytest -c tests/pytest.ini
```

### Cleanup

```Bash
find . -type d -name '__pycache__' -exec rm -r {} \;
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
