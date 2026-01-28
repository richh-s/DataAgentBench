code = """import json, re

# Load civic_docs (large result stored in a .json file path)
with open(var_call_qCd41xIxKoJWJQiltYKGVpvm, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Load funding aggregation results
with open(var_call_1JlJOdqgm0KD53xKrf9qlUMH, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Build funding map: Project_Name -> amount (int)
fund_map = {}
for rec in funding:
    name = rec.get('Project_Name')
    amt = rec.get('total_amount')
    try:
        amt_val = int(float(amt)) if amt is not None and str(amt).strip()!='' else 0
    except:
        # fallback if non-numeric
        amt_val = 0
    fund_map[name] = amt_val

# Heuristic: for each funded project, look for project name in civic docs text
# and check nearby text for both 'spring' and '2022'
matched = set()
for proj_name, amt in fund_map.items():
    if not proj_name:
        continue
    proj_lower = proj_name.lower()
    for doc in civic_docs:
        text = doc.get('text','')
        text_lower = text.lower()
        pos = text_lower.find(proj_lower)
        if pos != -1:
            # get surrounding context
            start = max(0, pos - 200)
            end = pos + len(proj_lower) + 500
            snippet = text_lower[start:end]
            if 'spring' in snippet and '2022' in snippet:
                matched.add(proj_name)
                break

# Prepare result
total_funding = sum(fund_map[p] for p in matched)
result = {
    'count': len(matched),
    'total_funding': total_funding,
    'projects': sorted(list(matched))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_EEYj4xb8xbi9hoRhPGuKInGy': ['civic_docs'], 'var_call_OEEesrF5kWcWPLVhJYfhTaUV': ['Funding'], 'var_call_qCd41xIxKoJWJQiltYKGVpvm': 'file_storage/call_qCd41xIxKoJWJQiltYKGVpvm.json', 'var_call_1JlJOdqgm0KD53xKrf9qlUMH': 'file_storage/call_1JlJOdqgm0KD53xKrf9qlUMH.json'}

exec(code, env_args)
