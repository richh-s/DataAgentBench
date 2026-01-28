code = """import json
with open(var_call_ERG8OpRhsxXmPM88AG6uA386, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_UbAQ3qmbfvbFmUieC0isIe9S, 'r', encoding='utf-8') as f:
    docs = json.load(f)

chi_titles = set()
for d in docs:
    fname = d.get('filename', '')
    if fname.lower().endswith('.txt'):
        title = fname[:-4]
    else:
        title = fname
    chi_titles.add(title)

filtered = []
for r in citations:
    t = r.get('title')
    if t in chi_titles:
        try:
            cc_int = int(r.get('citation_count', 0))
        except:
            try:
                cc_int = int(float(r.get('citation_count', 0)))
            except:
                cc_int = 0
        filtered.append({'title': t, 'citation_count': cc_int})

total = sum(p['citation_count'] for p in filtered)
num = len(filtered)
result = {'total_citations_2020_for_CHI_papers': total, 'num_papers': num, 'papers': filtered}

# Print exactly in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ERG8OpRhsxXmPM88AG6uA386': 'file_storage/call_ERG8OpRhsxXmPM88AG6uA386.json', 'var_call_UbAQ3qmbfvbFmUieC0isIe9S': 'file_storage/call_UbAQ3qmbfvbFmUieC0isIe9S.json'}

exec(code, env_args)
