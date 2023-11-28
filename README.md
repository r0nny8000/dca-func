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

Or simply use poetry init inside the folder

Configuring the shell by updating the project toml with python version 3.10.*

    poetry config --list
    poetry config virtualenvs.prefer-active-python true
    pyenv versions
    pyenv install 3.10.12
    pyenv local 3.10.12
    poetry install
    poetry shell
    which python

Switched Python Interpreter in Codium in .vscode/settings.json (or using CMD+Shift+P and "Select Interpreter")

    {
        "python.defaultInterpreterPath": "/Users/me/Library/Caches/pypoetry/virtualenvs/marketdata-cli-MiIDVtXc-py3.7/bin/python"
    }

Adding azure function as dependency to poetry from requirements.txt

    poetry add azure-functions

Export Dependencies

    poetry export -f requirements.txt --output requirements.txt --without-hashes

Setup and first deployment in Azure

    az login
    az group create --name dca-func-rg --location westeurope
    az storage account create --name dcafuncst --location westeurope --resource-group dca-func-rg --sku Standard_LRS
    az functionapp create --resource-group dca-func-rg --consumption-plan-location westeurope --runtime python --runtime-version 3.10 --functions-version 4 --name dca-func-app --os-type linux --storage-account dcafuncst
    func azure functionapp publish dca-func-app
    az functionapp config appsettings set --name dca-func-app --resource-group dca-func-rg --settings AzureWebJobsFeatureFlags=EnableWorkerIndexing


Deploy to Azure

    func azure functionapp publish dca-func-app

Logs

    func azure functionapp logstream dca-func-app --browser


Downloaded and added Bitget API 
    
    git clone git@github.com:BitgetLimited/v3-bitget-api-sdk.git
    cp -r ../v3-bitget-api-sdk/bitget-python-sdk-api/bitget .

Installed requests
    
    poetry add requests


    

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


hi there
--------
