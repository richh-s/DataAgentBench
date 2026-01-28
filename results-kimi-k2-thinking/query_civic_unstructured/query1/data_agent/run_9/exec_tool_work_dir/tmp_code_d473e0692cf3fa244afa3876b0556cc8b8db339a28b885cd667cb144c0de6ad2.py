code = """import json
import re

# Load funding data
funding_file = locals()['var_functions.query_db:2']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
civic_docs_file = locals()['var_functions.query_db:8']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(funding_data)} funding records and {len(civic_docs)} civic documents")

# Filter funding > $50,000
high_funding = [f for f in funding_data if int(f['Amount']) > 50000]
print(f"Projects with funding > $50k: {len(high_funding)}")

# Create lookup for high funding projects
funding_lookup = {}
for f in high_funding:
    name = f['Project_Name'].lower().strip()
    funding_lookup[name] = {
        'Amount': int(f['Amount']),
        'Project_Name': f['Project_Name']
    }

# Parse civic docs to find capital projects with design status
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Find Capital Improvement Projects (Design) section
    if 'Capital Improvement Projects (Design)' in text:
        # Extract the section
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) < 2:
            continue
        
        design_section = parts[1]
        # Split by next major heading if it exists
        major_headings = ['Capital Improvement Projects (Construction)', 'Disaster Recovery Projects', 'Capital Improvement Projects (Not Started)']
        for heading in major_headings:
            if heading in design_section:
                design_section = design_section.split(heading)[0]
                break
        
        # Extract project names
        lines = design_section.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or len(line) < 5:
                continue
            
            # Skip common non-project lines
            skip_patterns = ['updates:', 'project schedule:', 'complete design', 'advertise', 'begin construction', 'page', 'agenda item', '(cid:', '•', '◆']
            if any(pattern in line.lower() for pattern in skip_patterns):
                continue
            
            # Skip date/season lines
            if re.match(r'^(spring|summer|fall|winter)\s+20\d{2}$', line.lower()):
                continue
            
            if re.match(r'^(q[1-4]|\d{4})$', line.lower()):
                continue
            
            # Clean the line
            clean_line = re.sub(r'\s+', ' ', line).strip()
            clean_line = re.sub(r'^[^a-zA-Z]+', '', clean_line)  # Remove leading non-letters
            clean_line = re.sub(r'[^a-zA-Z0-9\s&\-\/\(\)]$', '', clean_line)  # Remove trailing punctuation
            
            # Check if it looks like a project name (reasonable length, starts with capital letter)
            if (len(clean_line) > 10 and 
                clean_line[0].isupper() and 
                not clean_line.isupper() and  # Not all caps
                len(clean_line.split()) <= 10):  # Not too many words
                
                capital_design_projects.append(clean_line)

# Remove duplicates while preserving order
unique_projects = []
seen = set()
for proj in capital_design_projects:
    if proj.lower() not in seen:
        unique_projects.append(proj)
        seen.add(proj.lower())

print(f"Capital design projects found in documents: {len(unique_projects)}")

# Match projects with funding
matched_projects = []

for project_name in unique_projects:
    project_lower = project_name.lower()
    
    # Direct match
    if project_lower in funding_lookup:
        matched_projects.append({
            'Project_Name': project_name,
            'Amount': funding_lookup[project_lower]['Amount']
        })
    else:
        # Fuzzy matching
        for funded_name, data in funding_lookup.items():
            # Check if one contains the other
            if (project_lower in funded_name or funded_name in project_lower):
                # Additional check: avoid very generic matches
                if len(project_lower) > 15 or len(funded_name) > 15:
                    matched_projects.append({
                        'Project_Name': project_name,
                        'Amount': data['Amount']
                    })
                    break
            # Check for keyword matches on major components
            proj_words = set(project_lower.replace('(', ' ').replace(')', ' ').replace('-', ' ').split())
            fund_words = set(funded_name.replace('(', ' ').replace(')', ' ').replace('-', ' ').split())
            common_words = proj_words.intersection(fund_words)
            if len(common_words) >= 3 and len(project_lower) > 10 and len(funded_name) > 10:
                if abs(len(project_lower) - len(funded_name)) < 20:
                    matched_projects.append({
                        'Project_Name': project_name,
                        'Amount': data['Amount']
                    })
                    break

# Remove duplicates
final_projects = []
final_names = set()
for proj in matched_projects:
    if proj['Project_Name'] not in final_names:
        final_projects.append(proj)
        final_names.add(proj['Project_Name'])

print(f"Matched capital design projects with funding > $50k: {len(final_projects)}")

# Show some matches for verification
for proj in final_projects[:10]:
    print(f"  {proj['Project_Name']}: ${proj['Amount']:,}")

# Return the count
result = len(final_projects)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
