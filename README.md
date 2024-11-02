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

### test with server, through python code as in test_redis_server.py

```
conda activate redis
python test_redis_server.py
```


#### add or update a key/value pair – overwrites existing value

    store.put("name", "Alice")

#### retrieve a value by key – retrieves latest value from all committed transactions

    store.get("name")

#### delete a value by key

    store.delete("favorite_color")

#### start a transaction

    store.start_transaction()

#### commit a transaction

    store.commit_transaction()


#### rollback a transaction – discard changes

    store.rollback_transaction()
