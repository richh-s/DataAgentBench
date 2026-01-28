code = """import json

# Load the funding data (already filtered for Amount > 50000)
funding_file = var_functions.query_db:5
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load the civic documents data
civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create a map: Project_Name -> Amount for funding records > 50000
funding_map = {}
for record in funding_records:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[proj_name] = amount

# Extract capital projects with design status from civic documents
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    text_lower = text.lower()
    # Look for capital improvement projects in design phase
    if 'capital improvement projects' in text_lower:
        # Look for design status indicators in the text
        if 'design' in text_lower:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line and len(line) > 5:
                    # Skip non-project lines
                    skip_patterns = ['page', 'schedule', 'updates', 'project description', 'staff is', 'city will', 'consultant', 'completed', 'construction']
                    if any(pattern in line.lower() for pattern in skip_patterns):
                        continue
                    # If line is reasonable length and starts with capital letter or bullet
                    if (len(line) < 200 and 
                        (line[0].isupper() or line.startswith('•')) and
                        not line.startswith('202') and
                        'Page' not in line):
                        clean_name = line.replace('• ', '').strip()
                        if len(clean_name) > 5:
                            design_projects.add(clean_name)

# Count how many design projects have funding > 50000
count = 0
matched_projects = []

for design_proj in design_projects:
    # Look for matching funded project
    for funded_name, amount in funding_map.items():
        # Simple name matching - check if one contains the other
        d_lower = design_proj.lower()
        f_lower = funded_name.lower()
        
        # Check substring match
        if (d_lower in f_lower) or (f_lower in d_lower):
            # Check length similarity to reduce false positives
            if abs(len(design_proj) - len(funded_name)) < 40:
                count += 1
                matched_projects.append({
                    'project': design_proj,
                    'funded_as': funded_name,
                    'amount': amount
                })
                break

# Return the final count
result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
