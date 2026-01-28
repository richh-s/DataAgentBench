code = """import json
import re

# Read the data files
with open('var_functions.query_db:0', 'r') as f:
    civic_docs_data = json.load(f)

with open('var_functions.query_db:1', 'r') as f:
    funding_data = json.load(f)

# Extract capital design projects by parsing document structure
projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Find design section
    design_match = re.search(r'Design\)(.*?)(?:Construction\)|Not Started\)|$)', 
                            text, re.DOTALL|re.IGNORECASE)
    
    if design_match:
        design_section = design_match.group(1)
        lines = design_section.split(chr(10))  # Use chr(10) for newline
        
        for line in lines:
            line = line.strip()
            # Filter for likely project names
            if (line and len(line) > 10 and len(line) < 150 and 
                not line.startswith('•') and not line.startswith('(') and
                'Page' not in line and 'cid:' not in line and
                not line.isupper() and
                line[0].isalnum()):
                
                project_name = line.strip()
                if project_name.endswith(':'):
                    project_name = project_name[:-1].strip()
                    
                # Add if not duplicate
                if not any(p['Project_Name'] == project_name for p in projects):
                    projects.append({
                        'Project_Name': project_name,
                        'status': 'design',
                        'type': 'capital'
                    })

# Create funding dictionary - clean up amounts
funding_dict = {}
for item in funding_data:
    try:
        # Convert amount to integer, handling potential string values
        amount_str = str(item['Amount']).replace(',', '').strip()
        amount = int(float(amount_str))
        funding_dict[item['Project_Name']] = amount
    except (ValueError, TypeError):
        continue

# Match projects
matched = []
for proj in projects:
    name = proj['Project_Name']
    if name in funding_dict and funding_dict[name] > 50000:
        matched.append(name)

result = {
    'count': len(matched),
    'projects': matched[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
