code = """import json
# Load tool results from storage keys
with open(var_call_Q2QALnRbPR1xJQJrQBJ3lLR6, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_7tRumuCn4arG0Sax5uYfVhSC, 'r', encoding='utf-8') as f:
    chi_docs = json.load(f)

# Build set of CHI paper titles by stripping .txt
chi_titles = set()
for d in chi_docs:
    fn = d.get('filename', '')
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    chi_titles.add(title)

# Filter citations for 2020 (already filtered in SQL query) and for CHI titles
matched = []
total = 0
for rec in citations:
    title = rec.get('title')
    # some titles might have extra whitespace
    if title in chi_titles:
        try:
            count = int(rec.get('citation_count', 0))
        except:
            # if string with commas
            count = int(str(rec.get('citation_count', '0')).replace(',', ''))
        matched.append({'title': title, 'citation_count': count})
        total += count

# Sort matched by citation_count desc
matched.sort(key=lambda x: x['citation_count'], reverse=True)

result = {'papers': matched, 'total_citations_2020_for_CHI_papers': total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Q2QALnRbPR1xJQJrQBJ3lLR6': 'file_storage/call_Q2QALnRbPR1xJQJrQBJ3lLR6.json', 'var_call_S9p2vxSNb8MYkASYselYNJGN': ['paper_docs'], 'var_call_7tRumuCn4arG0Sax5uYfVhSC': 'file_storage/call_7tRumuCn4arG0Sax5uYfVhSC.json'}

exec(code, env_args)
