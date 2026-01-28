code = """import json

# Read funding data
funding_file = var_functions.query_db:6
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Filter for funding > 50000
high_funding = [item for item in funding_data if int(item['Amount']) > 50000]

# Read civic documents
civic_file = var_functions.query_db:5
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Extract projects with design status from documents
design_capital_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    # Look for design section
    design_section_start = text.find('Capital Improvement Projects (Design)')
    if design_section_start > -1:
        design_section = text[design_section_start:]
        # Find where this section ends (next major heading)
        next_section = design_section.find('\n\nCapital Improvement Projects (')
        if next_section > -1:
            design_section = design_section[:next_section]
        
        # Extract lines that are likely project names (not bullet points, not empty)
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            if (line and 
                not line.startswith('Capital Improvement Projects') and 
                not line.startswith('(') and
                not line.startswith('To:') and
                not line.startswith('From:')):
                # Simple heuristic: if line doesn't end with punctuation and isn't too short
                if len(line) > 10 and not line.endswith('.') and not line.endswith(':'):
                    design_capital_projects.append(line)

# Remove duplicates
design_capital_projects = list(set(design_capital_projects))

# Count matches with high funding
match_count = 0
for project_name in design_capital_projects:
    for funding_item in high_funding:
        funding_name = funding_item['Project_Name']
        if (project_name == funding_name or 
            funding_name.startswith(project_name + ' ')):
            match_count += 1
            break

print('__RESULT__:')
print(json.dumps(match_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
