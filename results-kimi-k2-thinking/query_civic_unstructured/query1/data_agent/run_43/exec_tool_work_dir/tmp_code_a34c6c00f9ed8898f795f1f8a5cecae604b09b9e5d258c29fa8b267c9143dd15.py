code = """import json

# Load data
funding = json.load(open(var_functions.query_db:5))
docs = json.load(open(var_functions.query_db:6))

# Build funding map by name
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding}

# Extract design projects
all_design_projects = set()
for doc in docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and 8 < len(line) < 150:
                if 'Design' in line or ('Design' in text[max(0,text.find(line)):text.find(line)+300]):
                    all_design_projects.add(line)

# Count matches with funding > 50000
count = 0
for design_proj in all_design_projects:
    for funded_name, amount in funding_map.items():
        if amount > 50000:
            # Check name similarity
            d_lower = design_proj.lower()
            f_lower = funded_name.lower()
            if d_lower in f_lower or f_lower in d_lower:
                length_diff = abs(len(design_proj) - len(funded_name))
                if length_diff < 30:
                    count += 1
                    break

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
