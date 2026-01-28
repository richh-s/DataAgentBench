code = """import json, re
with open(var_call_XUBy8XmuJmOI8vXHIz3v37wT, 'r') as f:
    funding = json.load(f)
with open(var_call_KPdyHGx04fGghcaHvIyfkfCj, 'r') as f:
    civic_docs = json.load(f)

texts = [d.get('text','') for d in civic_docs]
combined = '\n\n'.join(texts)
combined_lower = combined.lower()

def base_name(n):
    return n.split('(')[0].strip()

park_keywords = ['park','playground','walkway','walkways','bluffs','trancas','point dume','malibu bluffs','playground','skate park']

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
# search by direct occurrence with nearby 'completed' and '2022'
for row in park_rows:
    b = row['base'].lower()
    if not b:
        continue
    if b in combined_lower:
        for m in re.finditer(re.escape(b), combined_lower):
            start = max(0, m.start()-300)
            end = min(len(combined_lower), m.end()+300)
            context = combined_lower[start:end]
            if 'completed' in context and '2022' in context:
                matched.add(row['base'])
                break
            # check paragraph
            ps = combined_lower.rfind('\n\n', 0, m.start())
            if ps==-1:
                ps = max(0, m.start()-500)
            pe = combined_lower.find('\n\n', m.end())
            if pe==-1:
                pe = min(len(combined_lower), m.end()+500)
            para = combined_lower[ps:pe]
            if 'completed' in para and '2022' in para:
                matched.add(row['base'])
                break

# also scan lines where 'completed' and '2022' appear and check nearby lines for project names
for text in texts:
    lo = text.lower()
    if 'completed' in lo and '2022' in lo:
        lines = text.splitlines()
        for i,l in enumerate(lines):
            if 'completed' in l.lower() and '2022' in l.lower():
                # look up to 4 lines above for project-like lines
                for j in range(max(0, i-5), i+1):
                    cand = lines[j].strip()
                    if not cand:
                        continue
                    # match against park_rows bases
                    for row in park_rows:
                        if row['base'].lower() in cand.lower() or cand.lower() in row['base'].lower():
                            matched.add(row['base'])

# Prepare sum of funding amounts for all funding rows whose base matches matched set
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
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_5hSTdGHQhXk0rZS3ZU1Xb9ji': ['civic_docs'], 'var_call_XUBy8XmuJmOI8vXHIz3v37wT': 'file_storage/call_XUBy8XmuJmOI8vXHIz3v37wT.json', 'var_call_KPdyHGx04fGghcaHvIyfkfCj': 'file_storage/call_KPdyHGx04fGghcaHvIyfkfCj.json', 'var_call_u1UJCstaxFZckB6tK05YH9m6': {'funding_len': 500, 'civic_docs_len': 5}}

exec(code, env_args)
