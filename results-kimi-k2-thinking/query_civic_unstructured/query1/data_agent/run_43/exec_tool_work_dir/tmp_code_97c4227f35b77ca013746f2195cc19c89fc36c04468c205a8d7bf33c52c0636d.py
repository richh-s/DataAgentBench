code = """import json

# Load the data
funding_file = var_functions.query_db:5
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

civic_file = var_functions.query_db:6
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding map
funding_by_project = {}
for item in funding_records:
    funding_by_project[item['Project_Name']] = int(item['Amount'])

# Find design capital projects from documents
projects_in_design = set()
for doc in civic_docs:
    text = doc.get('text', '')
    # Look for capital improvement projects section
    if 'Capital Improvement Projects' in text:
        # Find design projects through simple pattern matching
        for line in text.split('\n'):
            line = line.strip()
            # Skip empty and very short lines
            if len(line) < 5:
                continue
            # Skip meta lines
            if 'Page' in line or 'Schedule' in line or 'Updates' in line:
                continue
            # Check if this project mentions design in following context
            pos = text.find(line)
            context = text[pos:pos+400]
            if 'Design' in context:
                # This is likely a design project
                clean_name = line.strip('• ').strip()
                if len(clean_name) > 10 and len(clean_name) < 200:
                    projects_in_design.add(clean_name)

# Count matches with funding > 50000
match_count = 0
for design_project in projects_in_design:
    for funded_project, amount in funding_by_project.items():
        if amount > 50000:
            # Basic name matching
            d_name = design_project.lower()
            f_name = funded_project.lower()
            # Check if one is substring of another
            if d_name.find(f_name) >= 0 or f_name.find(d_name) >= 0:
                # Check length similarity to avoid false matches
                if abs(len(design_project) - len(funded_project)) < 40:
                    match_count += 1
                    break

result = {'count': match_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
