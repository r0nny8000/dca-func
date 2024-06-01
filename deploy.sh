#!/bin/bash
echo "deploy function in Azure"


# This script deploys a function in Azure. It sets variables for the resource group, location, storage account, 
# and function app. It then logs into Azure, creates a resource group, a storage account, and a function app,
# and prepares to publish the function. All these operations are performed using Azure CLI commands.

RESOURCE_GROUP=dcafuncrg
LOCATION=westeurope
STORAGE=dcafuncst
APP=dca-func

az config param-persist off

echo "login..."
az login
echo "done."

echo "create a resource group..."
az group create --name $RESOURCE_GROUP --location $LOCATION
echo "done."

echo "create a storage..."
az storage account create --name $STORAGE --location $LOCATION --resource-group $RESOURCE_GROUP --sku Standard_LRS
echo "done."

echo "create a function..."
az functionapp create --resource-group $RESOURCE_GROUP --consumption-plan-location $LOCATION --runtime python --runtime-version 3.10 --functions-version 4 --name $APP --os-type linux --storage-account $STORAGE
echo "done."

echo "publish function..."
func azure functionapp publish $APP
echo "done."

echo "config something... :-)"
az functionapp config appsettings set --name $APP --resource-group $RESOURCE_GROUP --settings AzureWebJobsFeatureFlags=EnableWorkerIndexing
echo "done."