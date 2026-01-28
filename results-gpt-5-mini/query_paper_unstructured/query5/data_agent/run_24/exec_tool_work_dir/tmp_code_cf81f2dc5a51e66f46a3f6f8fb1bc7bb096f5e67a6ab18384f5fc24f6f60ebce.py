code = """import json, re
# Load the citations for 2020 (file path stored in var_call_ULoT7Yja3x7BR5LtpdHMT3FN)
with open(var_call_ULoT7Yja3x7BR5LtpdHMT3FN, 'r', encoding='utf-8') as f:
    citations_records = json.load(f)

# Load paper documents (file path stored in var_call_tuqqN3NpZI1xl0x9HxF4hR5u)
with open(var_call_tuqqN3NpZI1xl0x9HxF4hR5u, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# Build set of titles for papers presented at CHI by detecting 'CHI' in the text
chi_titles = set()
for doc in paper_docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    if re.search(r'\bCHI\b', text, re.IGNORECASE):
        chi_titles.add(title)

# Process citation records (they are already filtered to 2020 by the earlier query)
matched = []
total = 0
for rec in citations_records:
    title = rec.get('title')
    try:
        count = int(rec.get('citation_count', 0))
    except:
        # handle non-int
        try:
            count = int(float(rec.get('citation_count',0)))
        except:
            count = 0
    if title in chi_titles:
        matched.append({'title': title, 'citation_count': count})
        total += count

# Sort matched by citation_count desc
matched.sort(key=lambda x: x['citation_count'], reverse=True)

result = {
    'total_citations_2020_for_CHI_papers': total,
    'num_chi_papers_cited_in_2020': len(matched),
    'papers': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ULoT7Yja3x7BR5LtpdHMT3FN': 'file_storage/call_ULoT7Yja3x7BR5LtpdHMT3FN.json', 'var_call_S1gKjKKYJATqzsNixyTxNMeF': 'file_storage/call_S1gKjKKYJATqzsNixyTxNMeF.json', 'var_call_JHht0QJIKkseVC2KHr0Pw9dz': ['paper_docs'], 'var_call_tuqqN3NpZI1xl0x9HxF4hR5u': 'file_storage/call_tuqqN3NpZI1xl0x9HxF4hR5u.json'}

exec(code, env_args)
