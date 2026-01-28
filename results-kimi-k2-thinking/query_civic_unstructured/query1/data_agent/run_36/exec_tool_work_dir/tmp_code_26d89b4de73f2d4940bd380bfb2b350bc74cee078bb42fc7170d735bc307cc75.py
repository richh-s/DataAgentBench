code = """import json

# Load funding data
funding_file = var_functions.query_db:4
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Filter for funding > $50,000
high_funding = []
for record in funding_data:
    try:
        amount = int(record.get('Amount', 0))
        if amount > 50000:
            high_funding.append(record)
    except:
        pass

print('Funding records over $50,000:', len(high_funding))

# Now let's examine the civic documents more carefully
# Load civic docs
civic_file = var_functions.query_db:16
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Civic documents to process:', len(civic_docs))

# Extract project names from the civic document text
design_project_names = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_design_section = False
    for i, line in enumerate(lines):
        line_lower = line.lower().strip()
        
        # Check if we're entering the design section
        if 'capital improvement projects (design)' in line_lower:
            in_design_section = True
            continue
        
        if in_design_section:
            # Check if we're exiting the design section
            if 'capital improvement projects (construction)' in line_lower:
                break
            if 'capital improvement projects (not started)' in line_lower:
                break
            if 'disaster recovery projects' in line_lower:
                break
            
            # Skip empty lines and common headers
            if not line.strip():
                continue
            if any(skip in line_lower for skip in ['updates:', 'project schedule', 'subject:', 'recommended action', 'date prepared', 'cid:']):
                continue
            if line.strip() in ['•', '●', '■', '□']:
                continue
                
            # Look for project names - they're usually followed by project details
            if i + 1 < len(lines):
                next_line = lines[i+1].lower().strip()
                if 'updates:' in next_line or 'project schedule' in next_line or next_line.startswith('('):
                    project_name = line.strip()
                    if len(project_name) > 5:
                        # Remove any leading numbers/symbols
                        project_name = project_name.lstrip('0123456789.-•●■□ ')
                        if project_name:
                            design_project_names.append(project_name)

print('Design projects found:', len(design_project_names))
for name in design_project_names[:15]:
    print('  -', name)

# Now match with funding records
matches = []
for design_name in design_project_names:
    design_lower = design_name.lower()
    for fund in high_funding:
        fund_name = fund['Project_Name'].lower()
        
        # Check for match (similar names)
        if (design_lower == fund_name or 
            design_lower in fund_name or 
            fund_name in design_lower):
            matches.append({
                'project': design_name,
                'funding_name': fund['Project_Name'],
                'amount': int(fund['Amount'])
            })
            break
        else:
            # Check word overlap for multi-word names
            design_words = set(design_lower.split())
            fund_words = set(fund_name.split())
            # If they share at least 3 meaningful words, it's likely a match
            if len(design_words.intersection(fund_words)) >= 3:
                matches.append({
                    'project': design_name,
                    'funding_name': fund['Project_Name'],
                    'amount': int(fund['Amount'])
                })
                break

# Count unique projects
unique_projects = []
project_names_seen = set()
for match in matches:
    if match['project'] not in project_names_seen:
        unique_projects.append(match)
        project_names_seen.add(match['project'])

print('\nMatching projects with funding > $50,000:', len(unique_projects))

result = {
    'count': len(unique_projects)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
