#!/bin/sh

docker network create my-network


docker run --name postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=test -d -e POSTGRES_USER=postgres -p 5436:5432 --network my-network postgres

docker build -t testapp ./app

docker run --network my-network testapp



