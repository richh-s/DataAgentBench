code = """import json
import re

# Get file paths
funding_path = locals()['var_functions.query_db:2']
civic_path = locals()['var_functions.query_db:8']

# Load funding data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Filter for funding > $50,000
high_funding = []
for record in funding_data:
    if int(record['Amount']) > 50000:
        high_funding.append(record)

# Build funding lookup map
funding_map = {}
for f in high_funding:
    name_lower = f['Project_Name'].lower().strip()
    funding_map[name_lower] = int(f['Amount'])

print('High funding projects map size:', len(funding_map))

# Extract capital design projects from civic docs
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    if 'Capital Improvement Projects (Design)' in text:
        # Get the design section
        design_start = text.index('Capital Improvement Projects (Design)') + len('Capital Improvement Projects (Design)')
        remaining_text = text[design_start:]
        
        # Find where the next major section starts
        next_sections = ['Capital Improvement Projects (Construction)', 'Disaster Recovery Projects', 'Capital Improvement Projects (Not Started)']
        design_section = remaining_text
        for section in next_sections:
            if section in remaining_text:
                section_idx = remaining_text.index(section)
                if section_idx < len(design_section):
                    design_section = remaining_text[:section_idx]
        
        # Parse project names from this section
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and short lines
            if len(line) < 8:
                continue
            
            # Skip lines that are clearly not project names
            skip_indicators = ['Updates', 'Schedule', 'Complete Design', 'Advertise', 'Construction', 'Page', 'Agenda Item', '(cid:', '◆', '•']
            should_skip = False
            for indicator in skip_indicators:
                if indicator in line:
                    should_skip = True
                    break
            if should_skip:
                continue
            
            # Check if line starts with uppercase (likely project name)
            if line and line[0].isupper():
                # Clean up the project name
                clean_name = re.sub(r'\s+$', '', line)
                clean_name = re.sub(r'^[^a-zA-Z]*', '', clean_name)
                if len(clean_name) > 8:
                    capital_design_projects.append(clean_name)

print('Raw capital design projects found:', len(capital_design_projects))

# Deduplicate while preserving order
deduped_projects = []
seen_names = set()
for proj in capital_design_projects:
    proj_lower = proj.lower()
    if proj_lower not in seen_names:
        deduped_projects.append(proj)
        seen_names.add(proj_lower)

print('Unique capital design projects:', len(deduped_projects))

# Match with funding
matched = []
for proj in deduped_projects:
    proj_key = proj.lower()
    if proj_key in funding_map:
        matched.append({'name': proj, 'amount': funding_map[proj_key]})

print('Matches with funding > 50k:', len(matched))

# Return just the count
result = len(matched)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
