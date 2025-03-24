#!/bin/sh

echo "Waiting for PostgreSQL to start..."
while ! pg_isready -U postgres -h postgres -p 5432; do
    sleep 1
done

echo "Waiting for MongoDB to start..."
while ! mongo --host mongo --port 27017 --eval 'db.adminCommand("ping")' > /dev/null 2>&1; do
    sleep 1
done

echo "Waiting for Redis to start..."
while ! redis-cli -h redis -p 6379 ping > /dev/null 2>&1; do
    sleep 1
done

echo "All services are ready. Starting the application..."
exec "$@"