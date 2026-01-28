code = """import json

# Load funding data
with open(locals()['var_functions.query_db:42']) as f:
    funding_records = json.load(f)

# Build funding lookup by project name
funding_dict = {}
for rec in funding_records:
    proj_name = rec.get('Project_Name', '')
    amount = int(str(rec.get('Amount', 0)))
    if proj_name and amount > 0:
        funding_dict[proj_name] = funding_dict.get(proj_name, 0) + amount

# Load and analyze civic documents to find Spring 2022 projects
with open(locals()['var_functions.query_db:52']) as f:
    civic_docs = json.load(f)

# Spring 2022 project names
spring_2022_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 5 or len(line) > 100:
            continue
        
        # Skip non-project headers
        skip_words = ['page', 'agenda', 'item', 'public works', 'commission', 'prepared', 'approved', 'date', 'subject', 'discussion', 'recommended action']
        if any(word in line.lower() for word in skip_words):
            continue
        
        # Look for lines that might be project names with 2022 spring context
        if line[0].isupper() and '2022' in line:
            if any(month in line.lower() for month in ['march', 'april', 'may', 'spring']):
                spring_2022_names.add(line)
        
        # Also check next few lines for spring 2022 schedule
        if line[0].isupper():
            context = ' '.join(lines[i:i+8]).lower()
            if '2022' in context and ('spring' in context or 'march' in context or 'april' in context or 'may' in context):
                if not any(word in line.lower() for word in ['updates', 'schedule', 'status', 'description']):
                    spring_2022_names.add(line)

# Deduplicate and clean
spring_2022_names = list(set(spring_2022_names))

# Match with funding and calculate totals
count = 0
total = 0

for proj in spring_2022_names:
    # Direct match
    if proj in funding_dict:
        count += 1
        total += funding_dict[proj]
        continue
    
    # Try base project name (without parenthetical suffixes)
    base_name = proj.split(' (')[0]
    for funded_proj in funding_dict:
        if funded_proj.startswith(base_name):
            count += 1
            total += funding_dict[funded_proj]
            break

result = {'spring_2022_project_count': count, 'total_funding_dollars': total}
print('__RESULT__:')
print(json.dumps(result))}"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_documents': 5, 'status': 'loaded'}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'funding_records': 500, 'civic_documents': 5, 'status': 'data_loaded'}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'civic_docs_loaded': 5, 'funding_records_loaded': 500, 'status': 'ready_to_process'}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'funding_records': 500, 'civic_documents': 3}, 'var_functions.list_db:50': ['civic_docs'], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
