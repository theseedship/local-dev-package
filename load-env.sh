#!/bin/bash
# load-env.sh - Load environment variables from .env and .env.local files
#
# This script loads environment variables from .env first, then .env.local
# .env.local values will override values from .env
# Usage: source ./load-env.sh

# Function to load environment file
load_env_file() {
    local env_file="$1"
    if [ -f "$env_file" ]; then
        echo "Loading environment variables from $env_file..."
        # Export variables while handling comments and empty lines
        while IFS= read -r line || [ -n "$line" ]; do
            # Skip comments and empty lines
            if [[ ! "$line" =~ ^[[:space:]]*# ]] && [[ -n "$line" ]]; then
                # Remove inline comments and trim whitespace
                line=$(echo "$line" | sed 's/#.*$//' | xargs)
                if [[ -n "$line" ]]; then
                    export "$line"
                fi
            fi
        done < "$env_file"
        echo "✓ Loaded $env_file"
    else
        echo "⚠ $env_file not found, skipping..."
    fi
}

# Main execution
echo "Loading environment variables..."

# Load .env first (base configuration)
load_env_file ".env"

# Load .env.local second (local overrides)
load_env_file ".env.local"

echo "Environment variables loaded successfully!"
echo ""
echo "To use this script before running docker-compose:"
echo "  source ./load-env.sh"
echo "  docker-compose up -d"