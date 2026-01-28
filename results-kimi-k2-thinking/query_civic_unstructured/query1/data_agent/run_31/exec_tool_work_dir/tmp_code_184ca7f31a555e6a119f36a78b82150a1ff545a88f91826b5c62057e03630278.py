code = """import json

f_funding = var_functions.query_db:68
f_civic = var_functions.query_db:5

with open(f_funding) as f:
    funding = json.load(f)

with open(f_civic) as f:
    civic = json.load(f)

# Count funding projects over $50k
funding_count = 0
funding_names = []

for rec in funding:
    if int(rec['Amount']) > 50000:
        funding_count += 1
        funding_names.append(rec['Project_Name'])

# Extract design projects from civic docs
project_list = []

for doc in civic:
    if 'text' in doc:
        text = doc['text']
        if 'Capital' in text and 'Design' in text:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line and len(line) < 100:
                    lower = line.lower()
                    # Check if this looks like a project name
                    has_keywords = 'road' in lower or 'park' in lower or 'canyon' in lower
                    not_metadata = 'updates' not in lower and 'schedule' not in lower
                    if has_keywords and not_metadata:
                        project_list.append(line)

# Remove duplicates (use dict to preserve order)
unique_projects = list(dict.fromkeys(project_list))

# Simple matching: compare cleaned project names
matches = 0

for project_name in unique_projects:
    # Clean project name
    clean_proj = ''.join(c for c in project_name.lower() if c.isalpha())
    
    for fund_name in funding_names:
        # Clean funding name similarly
        clean_fund = ''.join(c for c in fund_name.lower() if c.isalpha())
        
        # Check if one contains the other
        if clean_proj in clean_fund or clean_fund in clean_proj:
            if len(clean_proj) > 5 and len(clean_fund) > 5:  # Avoid trivial matches
                matches += 1
                break

result = {'count': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs'], 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
