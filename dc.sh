#!/bin/bash
# dc.sh - Docker Compose wrapper that loads .env and .env.local
#
# This script automatically loads environment variables from .env and .env.local
# before running docker-compose commands
#
# Usage: ./dc.sh [docker-compose arguments]
# Example: ./dc.sh up -d
#          ./dc.sh logs -f
#          ./dc.sh down

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Change to script directory
cd "$SCRIPT_DIR"

# Source the load-env.sh script
source ./load-env.sh

# Pass all arguments to docker-compose
docker-compose "$@"