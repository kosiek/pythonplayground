# Number Generations Project

## Overview

The Number Generations project is designed play around and develop my python skills.

Don't bother looking around for anything valuable. It's public just for learning and having conversations about my experiments with others.

## Features

- **dataaccess** package: my play with various data persistence techniques.
- **numberfunc** package: designed to play with number and data manipulation algorithms.

## Getting Started

To get started with the Number Generations project, you will need to have Python installed on your system. This project is designed for Python 3.12 and above.

### Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install `poetry`, `pyenv` and `pyenv-virtualenv` utilities.
4. Run the following command to initialize the virtualenv, using project's configuration:

```bash
my_python=$(grep 'python =' pyproject.toml | awk -F '"' '{gsub(/\^/, "", $2); print $2}')
grep_flags="-Po". # Linux
[[ "$OSTYPE" =~ "darwin" ]] && grep_flags="-E" # MacOS
latest_venv=$(pyenv install --list | tr -d ' ' | grep $grep_flags "^$my_python\.\d+" | tail -1)
echo "Pulling venv @ $latest_venv..."
pyenv install $latest_venv
pyenv virtualenv $latest_venv $(cat .python-version)

# Set up poetry inside of the virtualenv:
pip3 install poetry
```

4. Install the required dependencies using Poetry:

```bash
poetry install
```

### Testing

After installing all depdendencies using `poetry install`, it should be possible to run the tests using pytest suite:

```bash
pytest
```

## Contributing

As this project is for personal goals and will be developing it in my free time, expect me to not dedicate my time for any public feedback of any kind, including but not limited to issues and/or pull requests, unless stated otherwise.

## License

MIT License

Copyright (c) [2024] [Przemysław Kośka]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
