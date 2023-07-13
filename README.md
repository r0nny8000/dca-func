DCA-FUNC
========





What I did
----------

Created Git Repo online and checked out

    git clone git@github.com:r0nny8000/dca-func.git

Init Azure Function

    func init dca-func --python -m V2

Renamed the folder to 

    cd ..
    mv dca-func dca-func-origin


Init Poetry with a new folder

    poetry new dca-func

Moved the original files to the new folder

    mv dca-func-origin/* dca-func/
    mv dca-func-origin/.* dca-func/

Now Git, Azure and Poetry are initiated

Or simply use

    poetry init 

inside the folder



Getting started
---------------
Install pyenv

    brew install pyenv

Install python version supported by azure 

    pyenv versions
    pyenv install 3.10.12
    pyenv local 3.10.12

Checkout this project and use [Poetry](https://python-poetry.org).

Install dependencies

    poetry install

Execute

    poetry shell
    cry/cry.py

or

    poetry run python cry/cry.py

Install a new module 

    poetry add <module>
    poetry add -D pylint

Build and Install locally

    poetry build
    pip install dist/workstream-0.1.0.tar.gz

Config VSCodium
---------------

In this folder run 
    
    poetry shell
    which python

or

    poetry env info

to get the full path to the Pipenv's virtualenv. This is something like 

    /Users/me/Library/Caches/pypoetry/virtualenvs/marketdata-cli-MiIDVtXc-py3.7

Press Cmd+Shift+P and search for "Select Interpreter". Press enter, and select any of the suggested interpreters and a .vscode directory will be created inside your project root. It contains a settings.json. Edit this file and set python.pythonPath to the virtualenv path and add /bin/python at the end.

    {
        "python.defaultInterpreterPath": "/Users/me/Library/Caches/pypoetry/virtualenvs/marketdata-cli-MiIDVtXc-py3.7/bin/python"
    }

