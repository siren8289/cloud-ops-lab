#!/bin/bash
set -euo pipefail

docker compose up -d --build

echo "Waiting for API to be ready..."
for i in {1..10}; do
  if curl -sf http://127.0.0.1:8000/health > /dev/null; then
    break
  fi
  sleep 1
done

curl --fail http://127.0.0.1:8000/health
echo ""
echo "Deploy OK"
