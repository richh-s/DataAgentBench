code = """import json
# Load storage files
with open(var_call_ZGxPsl3QZckLx5Aftdn8Sa0X, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_vzEtHYEO2mxMyHPnsAC47tFQ, 'r') as f:
    funding_records = json.load(f)

# Build funding map and select park-related names
funding_map = {}
park_names = set()
for rec in funding_records:
    name = rec.get('Project_Name')
    amt = rec.get('Amount')
    if not name:
        continue
    try:
        val = int(amt)
    except Exception:
        try:
            val = int(float(amt))
        except Exception:
            val = 0
    funding_map[name] = funding_map.get(name, 0) + val
    low = name.lower()
    if ('park' in low) or ('playground' in low):
        park_names.add(name)

# Prepare docs text in lower-case
docs_texts = [doc.get('text', '') for doc in civic_docs]
texts_lower = [t.lower() for t in docs_texts]

# Find park projects completed in 2022 by proximity search
completed_2022_names = set()
for pname in park_names:
    p_low = pname.lower()
    for t_low in texts_lower:
        idx = t_low.find(p_low)
        if idx != -1:
            # define context window around name occurrence
            start = max(0, idx - 400)
            end = min(len(t_low), idx + 400)
            context = t_low[start:end]
            if ('completed' in context) and ('2022' in context):
                completed_2022_names.add(pname)
                break

# Sum funding amounts for matched names
total = sum(funding_map[name] for name in completed_2022_names)

result = {
    'park_completed_2022_projects': sorted(list(completed_2022_names)),
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ZGxPsl3QZckLx5Aftdn8Sa0X': 'file_storage/call_ZGxPsl3QZckLx5Aftdn8Sa0X.json', 'var_call_vzEtHYEO2mxMyHPnsAC47tFQ': 'file_storage/call_vzEtHYEO2mxMyHPnsAC47tFQ.json', 'var_call_vPZiNK1ZwTOX2UZ4GF6PIA6T': {'num_docs': 5, 'num_funding': 500}}

exec(code, env_args)
