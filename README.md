# shark

This program allows you to simulate poker games and write AI agents to play in those games.

## Why?

- Because I feel like it?
- To get experience designing a full application.
- Maybe to try out multiprocessing.
- To try out reinforcement learning agents.
- To get better at poker.

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

    Copyright 2022 Thomas Woodruff

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
