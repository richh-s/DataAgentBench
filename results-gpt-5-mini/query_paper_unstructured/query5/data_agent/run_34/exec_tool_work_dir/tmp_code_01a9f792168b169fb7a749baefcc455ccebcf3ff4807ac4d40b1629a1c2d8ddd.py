code = """import json, re
# Load the citations query result from the provided file path
with open(var_call_2bAjaySMuMe33fCE9m2xfmXn, 'r', encoding='utf-8') as f:
    citations_data = json.load(f)

# Load the paper documents from MongoDB query result
with open(var_call_wAsr13mFxq2D2MUGPbhJu8fy, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Build a lookup for citation counts by title
citations_by_title = {}
for rec in citations_data:
    title = rec.get('title')
    try:
        count = int(rec.get('citation_count'))
    except Exception:
        # handle non-int values
        try:
            count = int(float(rec.get('citation_count')))
        except Exception:
            count = 0
    citations_by_title[title] = count

# Regex to detect CHI venue mentions
chi_re = re.compile(r"\bCHI\b", re.IGNORECASE)

# Collect CHI papers that have citation records for 2020
results = []
for doc in papers:
    filename = doc.get('filename','')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4]
    text = doc.get('text','') or ''
    if chi_re.search(text):
        if title in citations_by_title:
            results.append({'title': title, 'citation_count': citations_by_title[title]})

# Sort results by citation_count descending
results.sort(key=lambda x: x['citation_count'], reverse=True)

total = sum(r['citation_count'] for r in results)
output = {
    'num_papers': len(results),
    'total_citations_2020': total,
    'papers': results
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_eeoUlpIf6RV1DGs1dvCSwE5Y': ['paper_docs'], 'var_call_Q5cWEdrlC2DtUePUiKYJHMQa': ['Citations', 'sqlite_sequence'], 'var_call_2bAjaySMuMe33fCE9m2xfmXn': 'file_storage/call_2bAjaySMuMe33fCE9m2xfmXn.json', 'var_call_wAsr13mFxq2D2MUGPbhJu8fy': 'file_storage/call_wAsr13mFxq2D2MUGPbhJu8fy.json'}

exec(code, env_args)
