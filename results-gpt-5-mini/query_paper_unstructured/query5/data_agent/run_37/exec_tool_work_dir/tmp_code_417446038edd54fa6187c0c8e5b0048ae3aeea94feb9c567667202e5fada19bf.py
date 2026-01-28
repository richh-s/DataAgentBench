code = """import json

# Load the MongoDB query result (file path stored in var_call_kVLUiqpbKeOJKwrJaSyC7OYZ)
with open(var_call_kVLUiqpbKeOJKwrJaSyC7OYZ, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# Load the SQLite query result (file path stored in var_call_KriBsfIu0WlhJ6jJITgXH3xp)
with open(var_call_KriBsfIu0WlhJ6jJITgXH3xp, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Extract titles from Mongo filenames (remove .txt)
chi_titles = set()
for doc in paper_docs:
    fn = doc.get('filename', '')
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    chi_titles.add(title)

# Match with citations for 2020 and sum
matched_papers = []
total = 0
for rec in citations:
    title = rec.get('title')
    try:
        count = int(rec.get('citation_count', 0))
    except:
        # handle non-int strings
        try:
            count = int(float(rec.get('citation_count', 0)))
        except:
            count = 0
    if title in chi_titles:
        matched_papers.append({"title": title, "citation_count": count})
        total += count

# Sort matched papers by title for consistency
matched_papers = sorted(matched_papers, key=lambda x: x['title'])

result = {
    "total_citations_2020_for_CHI_papers": total,
    "num_CHI_papers_cited_in_2020": len(matched_papers),
    "papers": matched_papers
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ybZ2HkxMxlqdEVuhpfGaDJvJ': ['paper_docs'], 'var_call_pI5zYuLsM9qBbBVfD6vIYIPB': ['Citations', 'sqlite_sequence'], 'var_call_kVLUiqpbKeOJKwrJaSyC7OYZ': 'file_storage/call_kVLUiqpbKeOJKwrJaSyC7OYZ.json', 'var_call_KriBsfIu0WlhJ6jJITgXH3xp': 'file_storage/call_KriBsfIu0WlhJ6jJITgXH3xp.json'}

exec(code, env_args)
