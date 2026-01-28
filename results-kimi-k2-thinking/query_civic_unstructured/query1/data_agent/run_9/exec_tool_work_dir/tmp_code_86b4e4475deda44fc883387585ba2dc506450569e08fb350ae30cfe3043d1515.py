code = """import json
import re

# Load the high funding data
high_funding_file = locals()['var_functions.query_db:50']
with open(high_funding_file, 'r') as f:
    high_funding_data = json.load(f)

# Load the civic documents
civic_docs_file = locals()['var_functions.query_db:8']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for quick matching
funding_lookup = {}
for record in high_funding_data:
    project_name = record['Project_Name'].lower().strip()
    funding_lookup[project_name] = {
        'original_name': record['Project_Name'],
        'amount': int(record['Amount'])
    }

print(f"High funding projects loaded: {len(funding_lookup)}")

# Extract capital design projects from civic documents
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Look for Capital Improvement Projects (Design) section
    if 'Capital Improvement Projects (Design)' in text:
        # Extract the design section
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) < 2:
            continue
        
        design_section = parts[1]
        
        # Truncate at next major section to avoid parsing irrelevant text
        end_markers = [
            'Capital Improvement Projects (Construction)',
            'Disaster Recovery Projects',
            'Capital Improvement Projects (Not Started)',
            'DISASTER RECOVERY PROJECTS'
        ]
        
        for marker in end_markers:
            if marker in design_section:
                design_section = design_section.split(marker)[0]
                break
        
        # Parse project names line by line
        lines = design_section.split('\n')
        
        for line in lines:
            line = line.strip()
            
            # Skip empty or very short lines
            if len(line) < 8:
                continue
            
            # Skip lines that are clearly not project names
            skip_patterns = [
                'updates', 'schedule', 'complete design', 'advertise', 'construction',
                'page', 'agenda item', '(cid:', '•', '◆', '◊',
                'project schedule', 'estimated schedule', 'recommended action',
                'begin construction', 'complete construction'
            ]
            
            line_lower = line.lower()
            if any(pattern in line_lower for pattern in skip_patterns):
                continue
            
            # Check if line starts with uppercase (likely a project name)
            if line and line[0].isupper() and not line.isupper():
                # Clean up the line
                clean_line = re.sub(r'^[^a-zA-Z]*', '', line)  # Remove leading non-letters
                clean_line = re.sub(r'[^a-zA-Z0-9\s&\-\/\(\)]$', '', clean_line)  # Remove trailing punctuation
                clean_line = re.sub(r'\s+', ' ', clean_line)  # Normalize whitespace
                
                # Validate length after cleaning
                if len(clean_line) > 10:
                    capital_design_projects.append(clean_line)

print(f"Raw capital design projects found: {len(capital_design_projects)}")

# Deduplicate projects while preserving order
unique_projects = []
seen_names = set()
for proj in capital_design_projects:
    proj_lower = proj.lower()
    if proj_lower not in seen_names:
        unique_projects.append(proj)
        seen_names.add(proj_lower)

print(f"Unique capital design projects: {len(unique_projects)}")

# Match with high funding projects
matched_count = 0
matched_projects = []

for proj in unique_projects:
    proj_lower = proj.lower()
    
    # Direct match
    if proj_lower in funding_lookup:
        matched_count += 1
        matched_projects.append({
            'project_name': proj,
            'funding_amount': funding_lookup[proj_lower]['amount'],
            'funding_source': funding_lookup[proj_lower]['original_name']
        })
        continue
    
    # Try matching without parenthetical suffixes (e.g., remove "(FEMA Project)")
    base_name = re.sub(r'\s*\([^)]*\)$', '', proj).lower().strip()
    if base_name in funding_lookup:
        matched_count += 1
        matched_projects.append({
            'project_name': proj,
            'funding_amount': funding_lookup[base_name]['amount'],
            'funding_source': funding_lookup[base_name]['original_name']
        })
        continue
    
    # Try matching by checking if project name is contained in funding name
    for funded_name, data in funding_lookup.items():
        if (proj_lower in funded_name or funded_name in proj_lower) and len(proj_lower) > 15:
            matched_count += 1
            matched_projects.append({
                'project_name': proj,
                'funding_amount': data['amount'],
                'funding_source': data['original_name']
            })
            break

print(f"Matched projects with funding > $50k: {matched_count}")

# Show some examples for verification
print("Sample matches:")
for proj in matched_projects[:10]:
    print(f"  {proj['project_name']}: ${proj['funding_amount']:,}")

# Return the final count
result = matched_count
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
