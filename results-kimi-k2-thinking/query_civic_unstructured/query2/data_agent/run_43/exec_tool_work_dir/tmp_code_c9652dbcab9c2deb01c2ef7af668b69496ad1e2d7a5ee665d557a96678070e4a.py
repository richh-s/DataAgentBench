code = """import json

# Load funding data
f_path = var_functions.query_db:5
with open(str(f_path), 'r') as f:
    funding = json.load(f)

# Load civic docs data  
c_path = var_functions.query_db:6
with open(str(c_path), 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup
funding_lookup = {item['Project_Name']: item for item in funding}

# Find park projects completed in 2022
matches = []
seen = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Look for completion in 2022
    has_2022_completion = '2022' in text and 'completed' in text.lower()
    
    if has_2022_completion:
        # Check each park project
        for pname, record in funding_lookup.items():
            if any(kw in pname.lower() for kw in ['park', 'playground']):
                if pname.lower() in text.lower() and pname not in seen:
                    matches.append({
                        'name': pname,
                        'source': record['Funding_Source'],
                        'amount': int(record['Amount'])
                    })
                    seen.add(pname)

# Calculate total
total_funding = sum(m['amount'] for m in matches)

result = {
    'total_funding': total_funding,
    'project_count': len(matches),
    'projects': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
