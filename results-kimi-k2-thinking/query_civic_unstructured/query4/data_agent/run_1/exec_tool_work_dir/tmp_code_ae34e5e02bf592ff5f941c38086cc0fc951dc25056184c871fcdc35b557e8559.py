code = """import json
import re
from datetime import datetime

# Read the full MongoDB result from the file
file_path = var_functions.query_db:5
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Found {len(civic_docs)} documents")

# Let's extract project information by looking for patterns
# Look for project names and dates in the text
projects = []

# Pattern to match project names - they often appear at the start of lines
# Common patterns: "Project Name\n", "Project Name\n(cid:190) Updates:", etc.
project_patterns = [
    r'([A-Z][a-zA-Z\s&\-\(\)0-9]+?)(?:\n\(cid:190\)|\n\(cid:131\)|\nProject Schedule|\n\(cid:190\) Updates:|\n\(cid:190\) Project Description:|$)',
    r'(?:2022\s+)?([A-Z][a-zA-Z\s&\-\(\)0-9]+?)(?:\n\(cid:190\)|\n\(cid:131\)|\nProject Schedule|\n\(cid:190\) Updates:|\n\(cid:190\) Project Description:|$)'
]

# Date patterns to look for
spring_2022_patterns = [
    r'2022[-\s]Spring',
    r'2022[-\s]March', 
    r'2022[-\s]April',
    r'2022[-\s]May',
    r'2022[-\s]03',
    r'2022[-\s]04', 
    r'2022[-\s]05'
]

for doc in civic_docs[:10]:  # Process first 10 docs to see patterns
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    print(f"\n=== Document: {filename} ===")
    print(f"Text preview (first 500 chars): {text[:500]}")
    
    # Look for Spring 2022 projects more directly
    # Search for lines that mention 2022 and projects
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if any(pattern in line for pattern in ['2022']):
            # Look at context around this line
            context_start = max(0, i-3)
            context_end = min(len(lines), i+3)
            context = '\n'.join(lines[context_start:context_end])
            print(f"Found 2022 reference: {line}")
            print(f"Context: {context[:200]}")

print("\n=== Analysis complete ===")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
