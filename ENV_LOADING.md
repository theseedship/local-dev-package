# Environment Variables Loading

This project supports a two-tier environment variable system that allows you to maintain base configuration in `.env` while keeping local overrides in `.env.local`.

## How It Works

1. **Base Configuration** (`.env`): Contains default values and shared configuration
2. **Local Overrides** (`.env.local`): Contains local/personal overrides that won't be committed to git

Variables defined in `.env.local` will override those in `.env`.

## Usage Methods

### Method 1: Using the Docker Compose Wrapper (Recommended)

Use the `dc.sh` wrapper script instead of `docker-compose` directly:

```bash
# Start services
./dc.sh up -d

# View logs
./dc.sh logs -f

# Stop services
./dc.sh down
```

The wrapper automatically loads both `.env` and `.env.local` before running docker-compose.

### Method 2: Using start_services.py

The `start_services.py` script automatically loads both environment files:

```bash
python start_services.py --profile cpu
```

### Method 3: Manual Loading (Bash)

Source the load script before running docker-compose:

```bash
source ./load-env.sh
docker-compose up -d
```

### Method 4: Manual Loading (Python)

Use in your Python scripts:

```python
from load_env import load_environment

# Load environment variables
load_environment()

# Now use os.environ as usual
import os
print(os.environ.get('POSTGRES_PASSWORD'))
```

## Setting Up Local Overrides

1. Copy the example file:
   ```bash
   cp .env.local.example .env.local
   ```

2. Edit `.env.local` with your local settings:
   ```bash
   # Example: Override database password for local development
   POSTGRES_PASSWORD=my-local-password
   
   # Example: Use different ports locally
   KONG_HTTP_PORT=8001
   ```

3. The `.env.local` file is already in `.gitignore`, so your local settings won't be committed.

## Best Practices

1. **Never commit `.env.local`** - It's for local/personal settings only
2. **Keep sensitive data in `.env.local`** - Passwords, API keys, etc.
3. **Document required variables** - Update `.env.example` with new required variables
4. **Use descriptive names** - Make it clear what each variable does

## Troubleshooting

### Environment variables not loading?

1. Check file permissions:
   ```bash
   ls -la .env .env.local
   ```

2. Verify the scripts are executable:
   ```bash
   chmod +x load-env.sh load_env.py dc.sh
   ```

3. Check for syntax errors in your `.env` files:
   - Each line should be `KEY=value`
   - No spaces around the `=` sign
   - Quote values with spaces: `KEY="value with spaces"`

### Docker Compose not seeing variables?

Make sure you're using one of the loading methods above. Docker Compose doesn't automatically load `.env.local` - only `.env`.

## Example .env.local

```bash
# Development database credentials
POSTGRES_PASSWORD=localdev123
JWT_SECRET=local-development-jwt-secret-with-at-least-32-characters

# Local service URLs
API_EXTERNAL_URL=http://localhost:8000
SITE_URL=http://localhost:3000

# Disable email confirmation for local dev
ENABLE_EMAIL_AUTOCONFIRM=true

# Use local SMTP server
SMTP_HOST=localhost
SMTP_PORT=1025
```