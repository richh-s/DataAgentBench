code = """import json

# Load funding data
funding_path = var_functions.query_db:5
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents
civic_path = var_functions.query_db:6
with open(civic_path, 'r') as f:
    civic_documents = json.load(f)

# Create funding lookup
funding_by_name = {}
for rec in funding_records:
    funding_by_name[rec.get('Project_Name')] = int(rec.get('Amount'))

# Find design projects in capital section
design_capital_projects = set()
for doc in civic_documents:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text:
        # Look for sections mentioning Design
        sections = text.split('\n')
        for line in sections:
            line = line.strip()
            if line and len(line) > 10:
                # Skip meta lines
                if any(x in line for x in ['Page', 'Schedule', 'Updates', 'Project Description', 'RECOMMENDED ACTION']):
                    continue
                if line.startswith('202'):
                    continue
                
                # Check context for design status
                idx = text.find(line)
                context = text[idx:idx+300]
                if 'Design' in context:
                    design_capital_projects.add(line)

# Match with funding and count > 50000
matches = 0
for project in design_capital_projects:
    for funded_name, amount in funding_by_name.items():
        if amount > 50000:
            # Check name similarity
            p_lower = project.lower()
            f_lower = funded_name.lower()
            
            if p_lower in f_lower or f_lower in p_lower:
                # Length similarity check
                if abs(len(project) - len(funded_name)) < 30:
                    matches += 1
                    break

result = {'count': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
