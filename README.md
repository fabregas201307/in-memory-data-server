## Docker build & run redis server locally

```
docker build . -t my-redis-server --no-cache
docker run -it --name redis-server -p 6379:6379 my-redis-server 
```

## Use the server from local

### Install dependencies

```
conda create -y -n redis
conda activate redis
conda install pip
pip install -r requirements.txt
```

### test with server

```
conda activate redis
python test_redis_server.py
```


Data Modification Commands
Data Modification Commands can be issued individually or as a part of a transaction.


# add or update a key/value pair – overwrites existing value

PUT [key] [value]


# retrieve a value by key – retrieves latest value from all committed transactions

GET [key]


# delete a value by key

DEL [key]


Transaction Control Commands
# start a transaction

START


# commit a transaction

COMMIT


# rollback a transaction – discard changes

ROLLBACK
