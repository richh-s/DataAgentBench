code = """import json
# Load data from storage-provided file paths
with open(var_call_ERG8OpRhsxXmPM88AG6uA386, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_UbAQ3qmbfvbFmUieC0isIe9S, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Build set of titles from paper_docs filenames (remove .txt)
chi_titles = set()
for d in docs:
    fname = d.get('filename', '')
    if fname.lower().endswith('.txt'):
        title = fname[:-4]
    else:
        title = fname
    chi_titles.add(title)

# Filter citation records for titles in CHI set and sum citation_count
filtered = []
for r in citations:
    t = r.get('title')
    if t in chi_titles:
        cc = r.get('citation_count')
        try:
            cc_int = int(cc)
        except:
            try:
                cc_int = int(float(cc))
            except:
                cc_int = 0
        filtered.append({'title': t, 'citation_count': cc_int})

total = sum(p['citation_count'] for p in filtered)
num = len(filtered)

result = {
    'total_citations_2020_for_CHI_papers': total,
    'num_papers': num,
    'papers': filtered
}

print("----BEGIN PRINT FORMAT----")
print("print(\"__RESULT__:\")")
print("print(json.dumps(result))")
print("----END PRINT FORMAT----")"""

env_args = {'var_call_ERG8OpRhsxXmPM88AG6uA386': 'file_storage/call_ERG8OpRhsxXmPM88AG6uA386.json', 'var_call_UbAQ3qmbfvbFmUieC0isIe9S': 'file_storage/call_UbAQ3qmbfvbFmUieC0isIe9S.json'}

exec(code, env_args)
