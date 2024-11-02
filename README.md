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
