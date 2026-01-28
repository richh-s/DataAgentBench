code = """import json

# Get the file paths from the stored variables
funding_path = str(var_functions.query_db:5)
civic_path = str(var_functions.query_db:6)

# Load the data
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup map
funding_amounts = {}
for record in funding_records:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_amounts[proj_name] = amount

# Extract capital projects with design status
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
        
    # Look for capital improvement projects sections
    if 'Capital Improvement Projects' in text and 'Design' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if not line or len(line) < 5:
                continue
                
            # Skip obvious non-project lines
            skip_terms = ['page', 'schedule', 'updates', 'project description', 'staff is', 'city will', 'consultant']
            if any(term in line.lower() for term in skip_terms):
                continue
                
            if line.startswith('202') or 'Page' in line:
                continue
                
            # If line looks like a project name, add it
            if len(line) < 200 and (line[0].isupper() or line.startswith('•')):
                clean_name = line.replace('• ', '').replace('○ ', '').strip()
                if len(clean_name) > 8:
                    design_projects.add(clean_name)

# Count design projects with funding > 50000
count = 0
for design_proj in design_projects:
    for funded_name, amount in funding_amounts.items():
        if amount > 50000:
            # Check if project names match (substring)
            d_lower = design_proj.lower()
            f_lower = funded_name.lower()
            
            if (d_lower in f_lower) or (f_lower in d_lower):
                # Check length similarity to reduce false matches
                if abs(len(design_proj) - len(funded_name)) < 40:
                    count += 1
                    break

result = json.dumps({'count': count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
