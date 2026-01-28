code = """import json, re
with open(var_call_XUBy8XmuJmOI8vXHIz3v37wT, 'r') as f:
    funding = json.load(f)
with open(var_call_KPdyHGx04fGghcaHvIyfkfCj, 'r') as f:
    civic_docs = json.load(f)

texts = [d.get('text','') for d in civic_docs]
sep = chr(10)*2
combined = sep.join(texts)
combined_lower = combined.lower()

def base_name(n):
    return n.split('(')[0].strip()

park_keywords = ['park','playground','walkway','walkways','bluffs','trancas','point dume','malibu bluffs','skate park']
park_rows = []
for r in funding:
    pname = r.get('Project_Name','')
    b = base_name(pname)
    low = b.lower()
    if any(k in low for k in park_keywords):
        try:
            amt = int(r.get('Amount'))
        except:
            try:
                amt = int(float(r.get('Amount')))
            except:
                amt = 0
        park_rows.append({'orig': pname, 'base': b, 'amount': amt})

matched = set()
# check occurrences in combined text
for row in park_rows:
    b = row['base'].lower()
    if not b:
        continue
    if b in combined_lower:
        # find indices
        start_idx = 0
        while True:
            idx = combined_lower.find(b, start_idx)
            if idx==-1:
                break
            start = max(0, idx-500)
            end = min(len(combined_lower), idx+500)
            context = combined_lower[start:end]
            if 'completed' in context and '2022' in context:
                matched.add(row['base'])
                break
            # paragraph boundaries using sep
            ps = combined_lower.rfind(sep, 0, idx)
            if ps==-1:
                ps = max(0, idx-500)
            pe = combined_lower.find(sep, idx)
            if pe==-1:
                pe = min(len(combined_lower), idx+500)
            para = combined_lower[ps:pe]
            if 'completed' in para and '2022' in para:
                matched.add(row['base'])
                break
            start_idx = idx + len(b)

# scan texts for lines with completed and 2022 and look for nearby project names
for text in texts:
    lo = text.lower()
    if 'completed' in lo and '2022' in lo:
        lines = text.splitlines()
        for i,line in enumerate(lines):
            if 'completed' in line.lower() and '2022' in line.lower():
                for j in range(max(0, i-6), min(len(lines), i+1)):
                    cand = lines[j].strip()
                    if not cand:
                        continue
                    for row in park_rows:
                        if row['base'].lower() in cand.lower() or cand.lower() in row['base'].lower():
                            matched.add(row['base'])

# Prepare sum
total = 0
included = []
for r in park_rows:
    if r['base'] in matched:
        total += r['amount']
        included.append(r)

result = {
    'total_funding_completed_in_2022_for_park_projects': total,
    'matched_project_base_names': sorted(list(matched)),
    'included_rows_count': len(included)
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5hSTdGHQhXk0rZS3ZU1Xb9ji': ['civic_docs'], 'var_call_XUBy8XmuJmOI8vXHIz3v37wT': 'file_storage/call_XUBy8XmuJmOI8vXHIz3v37wT.json', 'var_call_KPdyHGx04fGghcaHvIyfkfCj': 'file_storage/call_KPdyHGx04fGghcaHvIyfkfCj.json', 'var_call_u1UJCstaxFZckB6tK05YH9m6': {'funding_len': 500, 'civic_docs_len': 5}}

exec(code, env_args)
