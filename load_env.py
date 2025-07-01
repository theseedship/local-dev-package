#!/usr/bin/env python3
"""
load_env.py - Load environment variables from .env and .env.local files

This script loads environment variables from .env first, then .env.local
.env.local values will override values from .env

Usage: 
    python load_env.py
    
Or import in other Python scripts:
    from load_env import load_environment
    load_environment()
"""

import os
import sys
from pathlib import Path

def load_env_file(filepath):
    """Load environment variables from a file."""
    if not os.path.exists(filepath):
        print(f"⚠ {filepath} not found, skipping...")
        return False
    
    print(f"Loading environment variables from {filepath}...")
    
    with open(filepath, 'r') as f:
        for line in f:
            # Skip comments and empty lines
            line = line.strip()
            if line and not line.startswith('#'):
                # Remove inline comments
                if '#' in line:
                    line = line.split('#')[0].strip()
                
                # Parse key=value
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # Remove quotes if present
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    elif value.startswith("'") and value.endswith("'"):
                        value = value[1:-1]
                    
                    # Set environment variable
                    os.environ[key] = value
    
    print(f"✓ Loaded {filepath}")
    return True

def load_environment():
    """Load environment variables from .env and .env.local files."""
    print("Loading environment variables...")
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    
    # Load .env first (base configuration)
    env_path = script_dir / '.env'
    load_env_file(env_path)
    
    # Load .env.local second (local overrides)
    env_local_path = script_dir / '.env.local'
    load_env_file(env_local_path)
    
    print("Environment variables loaded successfully!")
    print("")
    print("To use this script before running docker-compose:")
    print("  python load_env.py")
    print("  docker-compose up -d")
    print("")
    print("Or import in your Python scripts:")
    print("  from load_env import load_environment")
    print("  load_environment()")

if __name__ == "__main__":
    load_environment()