# Use the official Redis image as the base image
FROM redis:latest

# Copy custom configuration file to the image
COPY redis.conf /usr/local/etc/redis/redis.conf

# Expose Redis default port
EXPOSE 8999

# Start Redis with the custom configuration
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]
# CMD ["redis-server"]
