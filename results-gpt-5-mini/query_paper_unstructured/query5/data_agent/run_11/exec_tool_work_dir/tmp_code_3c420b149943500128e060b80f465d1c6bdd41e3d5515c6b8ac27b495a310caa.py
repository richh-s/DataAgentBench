code = """import json
# Load the query results from storage files
with open(var_call_0ZfhXvS12b4h4CZXPqG72FA1, 'r') as f:
    citations = json.load(f)
with open(var_call_KJAN4C83G7rE0MjvRkQlWrjN, 'r') as f:
    paper_docs = json.load(f)

# Build set of paper titles from paper_docs filenames (strip .txt)
chi_titles = set()
for doc in paper_docs:
    fn = doc.get('filename', '')
    if fn and fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    # We used a Mongo filter searching for 'CHI' in text, so assume these are CHI papers
    chi_titles.add(title)

# Process citations: ensure citation_count is int
matched = []
total = 0
for rec in citations:
    title = rec.get('title')
    try:
        count = int(rec.get('citation_count', 0))
    except:
        # handle non-int
        try:
            count = int(float(rec.get('citation_count', 0)))
        except:
            count = 0
    if title in chi_titles and count > 0:
        matched.append({'title': title, 'citation_count': count})
        total += count

# Prepare result
result = {
    'total_citations': total,
    'num_chi_papers_cited': len(matched),
    'papers': matched
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0ZfhXvS12b4h4CZXPqG72FA1': 'file_storage/call_0ZfhXvS12b4h4CZXPqG72FA1.json', 'var_call_KJAN4C83G7rE0MjvRkQlWrjN': 'file_storage/call_KJAN4C83G7rE0MjvRkQlWrjN.json'}

exec(code, env_args)
