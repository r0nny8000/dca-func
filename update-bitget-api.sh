#!/bin/bash

echo "delete old api"

rm -rf bitget
rm -rf v3-bitget-api-sdk-master
rm master.tar.gz

echo "get folder from git..."

wget "https://github.com/BitgetLimited/v3-bitget-api-sdk/archive/master.tar.gz"

echo "extract..."

tar -xf master.tar.gz

echo "copy api..."

cp -r v3-bitget-api-sdk-master/bitget-python-sdk-api/bitget .

echo "clean up..."

rm -rf v3-bitget-api-sdk-master
rm master.tar.gz