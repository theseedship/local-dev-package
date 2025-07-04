#!/usr/bin/env python3
"""Fix Supabase docker-compose.yml issues"""
import yaml
import sys

try:
    # Custom loader to preserve formatting
    class SafeLineLoader(yaml.SafeLoader):
        def construct_mapping(self, node):
            pairs = self.construct_pairs(node)
            return dict(pairs)

    # Read the file
    with open('supabase/docker/docker-compose.yml', 'r') as f:
        content = f.read()
    
    # Parse YAML
    data = yaml.load(content, Loader=SafeLineLoader)
    
    # Fix vector service security_opt
    if 'services' in data and 'vector' in data['services']:
        vector = data['services']['vector']
        if 'security_opt' in vector:
            # Ensure it's a list with unique values
            opts = vector['security_opt']
            if isinstance(opts, list):
                # Remove duplicates while preserving order
                unique_opts = []
                seen = set()
                for opt in opts:
                    if opt not in seen:
                        seen.add(opt)
                        unique_opts.append(opt)
                vector['security_opt'] = unique_opts
    
    # Write back with minimal changes
    with open('supabase/docker/docker-compose.yml', 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print("Fixed Supabase docker-compose.yml")
    
except Exception as e:
    print(f"Error: {e}")
    # If YAML approach fails, try regex approach
    print("Trying regex approach...")
    import re
    
    with open('supabase/docker/docker-compose.yml', 'r') as f:
        content = f.read()
    
    # Find and fix security_opt section
    pattern = r'(security_opt:\s*\n)((?:\s*-\s*[^\n]+\n)+)'
    
    def fix_security_opt(match):
        header = match.group(1)
        items = match.group(2)
        # Split items and remove duplicates
        lines = [line.strip() for line in items.strip().split('\n') if line.strip()]
        unique_lines = []
        seen = set()
        for line in lines:
            # Extract the value after the dash
            value = line.lstrip('- ').strip()
            if value not in seen:
                seen.add(value)
                unique_lines.append(f"      - {value}")
        return header + '\n'.join(unique_lines) + '\n'
    
    content = re.sub(pattern, fix_security_opt, content)
    
    with open('supabase/docker/docker-compose.yml', 'w') as f:
        f.write(content)
    
    print("Fixed using regex approach")