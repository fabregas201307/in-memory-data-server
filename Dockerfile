# Use the official Redis image as the base image
FROM redis:latest

# Expose Redis default port
EXPOSE 6379

# Start Redis server
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]
