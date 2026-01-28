code = """import json

# Load the query results from storage file paths
with open(var_call_wNDdvlhaY1ayY7u1Q0xNORDh, 'r') as f:
    citations = json.load(f)
with open(var_call_0Mz6MhsMfss8wuRoXlUkqyu5, 'r') as f:
    paper_docs = json.load(f)

# Build set of titles from paper_docs filenames (strip .txt)
chi_titles = set()
for doc in paper_docs:
    fn = doc.get('filename', '')
    if fn.endswith('.txt'):
        chi_titles.add(fn[:-4])
    else:
        chi_titles.add(fn)

# Sum citation_counts for citations in 2020 that match CHI titles
total = 0
matched = []
for rec in citations:
    title = rec.get('title')
    # citation_count may be string, convert safely
    try:
        c = int(rec.get('citation_count', 0))
    except:
        try:
            c = int(float(rec.get('citation_count', 0)))
        except:
            c = 0
    if title in chi_titles:
        total += c
        matched.append({'title': title, 'citation_count': c})

result = {
    'total_citations_2020_for_CHI_papers': total,
    'num_matched_papers': len(matched)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wNDdvlhaY1ayY7u1Q0xNORDh': 'file_storage/call_wNDdvlhaY1ayY7u1Q0xNORDh.json', 'var_call_PjsWTCf51FkcDYjRKQmqaXUW': ['paper_docs'], 'var_call_0Mz6MhsMfss8wuRoXlUkqyu5': 'file_storage/call_0Mz6MhsMfss8wuRoXlUkqyu5.json'}

exec(code, env_args)
