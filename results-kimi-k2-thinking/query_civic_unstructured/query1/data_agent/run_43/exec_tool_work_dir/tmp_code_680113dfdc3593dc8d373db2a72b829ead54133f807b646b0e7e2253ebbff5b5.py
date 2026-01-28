code = """import json

# Load the data from the JSON files
with open(str(var_functions.query_db:5), 'r') as f:
    funding_records = json.load(f)

with open(str(var_functions.query_db:6), 'r') as f:
    civic_docs = json.load(f)

# Build a dictionary mapping project names to their funding amounts
funding_amounts = {}
for record in funding_records:
    funding_amounts[record['Project_Name']] = int(record['Amount'])

# Find all capital projects with design status from the civic documents
design_capital_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Check if this document mentions capital improvement projects
    if 'Capital Improvement Projects' in text:
        # Search for design status projects by scanning the text
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 5:
                # Look for design status in the context
                context_start = text.find(line)
                if context_start >= 0:
                    context_end = min(context_start + 300, len(text))
                    context = text[context_start:context_end]
                    if 'Design' in context:
                        # Add as a design project
                        clean_name = line.replace('•', '').replace('○', '').strip()
                        if len(clean_name) > 8:
                            design_capital_projects.add(clean_name)

# Count design projects that have funding greater than $50,000
count = 0
for proj_name in design_capital_projects:
    for funded_name, amount in funding_amounts.items():
        if amount > 50000:
            # Check if the project names match closely
            p_lower = proj_name.lower()
            f_lower = funded_name.lower()
            if (p_lower in f_lower) or (f_lower in p_lower):
                # Check length similarity to avoid false matches
                if abs(len(proj_name) - len(funded_name)) < 40:
                    count += 1
                    break

# Return just the count in JSON format
result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
