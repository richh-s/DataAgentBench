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

# Create set of funded project names
funded_names = set(record.get('Project_Name', '') for record in funding_data if record.get('Project_Name'))

design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Capital Improvement Projects (Design) section
    pattern1 = 'Capital Improvement Projects (Design)'
    idx1 = text.find(pattern1)
    if idx1 >= 0:
        # Get text until next major section
        next_section_start = text.find('Capital Improvement Projects (Construction)', idx1)
        if next_section_start < 0:
            next_section_start = text.find('Disaster Recovery Projects', idx1)
        if next_section_start < 0:
            next_section_start = text.find('RECOMMENDED ACTION:', idx1)
        if next_section_start < 0:
            section_text = text[idx1:]
        else:
            section_text = text[idx1:next_section_start]
        
        # Extract project names (lines that have updates section after them)
        lines = section_text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line and len(line) > 10 and not line.startswith('cid:') and not line.startswith('Page'):
                lower_line = line.lower()
                if not lower_line.startswith('updates:') and not lower_line.startswith('project schedule:'):
                    # Check if this line is followed by updates
                    has_updates = False
                    for j in range(i+1, min(i+5, len(lines))):
                        next_line = lines[j].strip().lower()
                        if 'updates:' in next_line:
                            has_updates = True
                            break
                    if has_updates and line not in ['Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:']:
                        design_projects.append(line)
            i += 1
    
    # Look for Disaster Recovery Projects (Design) section
    pattern2 = 'Disaster Recovery Projects (Design)'
    idx2 = text.find(pattern2)
    if idx2 >= 0:
        next_section_start = text.find('Disaster Recovery Projects (Construction)', idx2)
        if next_section_start < 0:
            next_section_start = text.find('Capital Improvement Projects', idx2)
        if next_section_start < 0:
            next_section_start = text.find('RECOMMENDED ACTION:', idx2)
        if next_section_start < 0:
            section_text = text[idx2:]
        else:
            section_text = text[idx2:next_section_start]
        
        lines = section_text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line and len(line) > 10 and not line.startswith('cid:') and not line.startswith('Page'):
                lower_line = line.lower()
                if not lower_line.startswith('updates:') and not lower_line.startswith('project schedule:'):
                    has_updates = False
                    for j in range(i+1, min(i+5, len(lines))):
                        next_line = lines[j].strip().lower()
                        if 'updates:' in next_line:
                            has_updates = True
                            break
                    if has_updates and line not in ['Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:']:
                        design_projects.append(line)
            i += 1

# Match with funded projects
matches = []
for project in design_projects:
    if project in funded_names:
        matches.append(project)
    else:
        # Try matching without parenthetical suffixes
        base_name = re.sub(r'\s*\([^)]*\)\s*$', '', project).strip()
        for funded in funded_names:
            funded_base = re.sub(r'\s*\([^)]*\)\s*$', '', funded).strip()
            if base_name == funded_base:
                matches.append(project)
                break

unique_matches = list(set(matches))
count_result = len(unique_matches)
print('__RESULT__:')
print(count_result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
