code = """import json

# Load data from storage
mongo_key = 'var_functions.query_db:10'
funding_key = 'var_functions.query_db:22'

if mongo_key in locals():
    mongo_result = locals()[mongo_key]
else:
    mongo_result = None

if funding_key in locals():
    funding_result = locals()[funding_key]
else:
    funding_result = None

# Read files if they are paths
mongo_docs = []
funding_records = []

if mongo_result and isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        mongo_docs = json.load(f)
elif mongo_result:
    mongo_docs = mongo_result

if funding_result and isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_records = json.load(f)
elif funding_result:
    funding_records = funding_result

# Create funding map for projects over 50000
funding_map = {}
for rec in funding_records:
    name = rec.get('Project_Name')
    amount = int(rec.get('Amount', 0))
    if name and amount > 50000:
        funding_map[name] = amount

# Extract design projects from documents
design_candidates = set()
for doc in mongo_docs:
    text = doc.get('text', '')
    marker = 'Capital Improvement Projects (Design)'
    if marker in text:
        idx = text.index(marker)
        section = text[idx:idx+3000]
        for line in section.split('\n'):
            line = line.strip()
            if line and len(line) > 8:
                if not line.startswith('(') and not line.endswith(':'):
                    if 'Page' not in line and 'Item' not in line and 'Public Works' not in line:
                        design_candidates.add(line)

# Match projects
matched = []
common_words = {'road','repair','improvements','and','the','project'}
for candidate in design_candidates:
    cand_set = set(candidate.lower().split()) - common_words
    for funded, amount in funding_map.items():
        fund_set = set(funded.lower().split()) - common_words
        if len(cand_set.intersection(fund_set)) >= 2:
            if funded not in [m['name'] for m in matched]:
                matched.append({'name': funded, 'amount': amount})
                break

# Return result
result = json.dumps({'count': len(matched)})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
