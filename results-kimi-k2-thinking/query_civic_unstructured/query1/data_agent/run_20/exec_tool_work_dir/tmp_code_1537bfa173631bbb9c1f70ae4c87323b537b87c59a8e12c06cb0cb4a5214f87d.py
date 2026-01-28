code = """import json
import os
import re

# Load funding data
key0 = 'var_functions.query_db:0'
with open(locals()[key0], 'r') as f:
    funding_data = json.load(f)

# Load civic documents
key2 = 'var_functions.query_db:2'
with open(locals()[key2], 'r') as f:
    civic_docs = json.load(f)

# Create a set of funded project names for quick lookup
funded_names = set()
for record in funding_data:
    name = record.get('Project_Name', '')
    if name:
        funded_names.add(name)

# Search through civic documents for capital projects with design status
all_design_capital = []

for doc in civic_docs:
    text = doc.get('text', '')
    sections = re.findall(r'Capital Improvement Projects \(Design\).*?(?=(?:Capital Improvement Projects|Disaster Recovery Projects|RECOMMENDED ACTION:|$))', text, re.DOTALL | re.IGNORECASE)
    
    for section in sections:
        # Extract lines that look like project names
        lines = []
        for line in section.split('\n'):
            stripped = line.strip()
            if stripped and len(stripped) > 10 and not stripped.startswith('cid:') and not stripped.startswith('Page'):
                lower_stripped = stripped.lower()
                if not lower_stripped.startswith('updates:') and not lower_stripped.startswith('project schedule:') and not lower_stripped.startswith('complete'):
                    if 'updates:' in section[section.find(stripped):section.find(stripped)+200].lower():
                        lines.append(stripped)
        all_design_capital.extend(lines)

# Also check disaster recovery projects with design status
for doc in civic_docs:
    text = doc.get('text', '')
    sections = re.findall(r'Disaster Recovery Projects \(Design\).*?(?=(?:Disaster Recovery Projects|Capital Improvement Projects|RECOMMENDED ACTION:|$))', text, re.DOTALL | re.IGNORECASE)
    
    for section in sections:
        lines = []
        for line in section.split('\n'):
            stripped = line.strip()
            if stripped and len(stripped) > 10 and not stripped.startswith('cid:') and not stripped.startswith('Page'):
                lower_stripped = stripped.lower()
                if not lower_stripped.startswith('updates:') and not lower_stripped.startswith('project schedule:') and not lower_stripped.startswith('complete'):
                    if 'updates:' in section[section.find(stripped):section.find(stripped)+200].lower():
                        lines.append(stripped)
        all_design_capital.extend(lines)

# Clean up and normalize project names for matching
clean_matches = []
for project in all_design_capital:
    # Direct match check
    if project in funded_names:
        clean_matches.append(project)
    else:
        # Try base name match (remove parenthetical suffixes)
        base_name = re.sub(r'\s*\([^)]*\)\s*$', '', project).strip()
        for funded in funded_names:
            funded_base = re.sub(r'\s*\([^)]*\)\s*$', '', funded).strip()
            if base_name == funded_base:
                clean_matches.append(project)
                break

# Remove duplicates and count
unique_matches = list(set(clean_matches))
final_count = len(unique_matches)

result = final_count
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
