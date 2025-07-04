#!/bin/bash
# Fix duplicate security_opt in Supabase docker-compose.yml
# This is a known issue with certain versions of docker-compose

# Check if the file exists
if [ -f "supabase/docker/docker-compose.yml" ]; then
    echo "Fixing Supabase docker-compose.yml..."
    
    # Create a temporary file with fixed content
    # Remove duplicate "label=disable" entries
    sed -i '/security_opt:/,/^[[:space:]]*[^[:space:]-]/{/security_opt:/!{/label=disable/d}}' supabase/docker/docker-compose.yml
    
    echo "Fixed security_opt duplicates"
fi