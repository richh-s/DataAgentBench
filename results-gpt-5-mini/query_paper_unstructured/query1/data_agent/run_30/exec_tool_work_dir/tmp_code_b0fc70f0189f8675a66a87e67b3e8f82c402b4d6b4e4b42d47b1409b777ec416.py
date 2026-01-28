code = """import json

# Load the large results from storage file paths
with open(var_call_E2O5Mvb1fnh7e9jIuC3Rll9p, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_L9uKHTGXlKlNJKXqTmKDxqHG, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Identify titles of papers whose domain contains 'food' by substring matching
food_titles = set()
for doc in docs:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text', '') or ''
    if 'food' in title.lower() or 'food' in text.lower():
        food_titles.add(title)

# Normalize citation titles and sum citation counts for matching titles
# Build a mapping from normalized citation title -> total_citations
# Normalization: strip whitespace and surrounding quotes
def normalize(t):
    if t is None:
        return t
    t = t.strip()
    # remove surrounding double or single quotes
    if (t.startswith('"') and t.endswith('"')) or (t.startswith("'") and t.endswith("'")):
        t = t[1:-1].strip()
    return t

normalized_citations = {}
for rec in citations:
    t = rec.get('title')
    norm = normalize(t)
    try:
        c = int(rec.get('total_citations', 0))
    except:
        # handle strings with commas
        c = int(str(rec.get('total_citations', 0)).replace(',', ''))
    normalized_citations[norm] = normalized_citations.get(norm, 0) + c

# Sum citations for titles identified as food domain
total = 0
matched_titles = []
for ft in food_titles:
    norm_ft = normalize(ft)
    if norm_ft in normalized_citations:
        total += normalized_citations[norm_ft]
        matched_titles.append(norm_ft)

# Prepare output
output = {
    "total_citations_for_food": total,
    "matched_titles_count": len(matched_titles),
    "matched_titles": matched_titles
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_mC5PeYSogWmdvihaCqP6NUpn': ['paper_docs'], 'var_call_E2O5Mvb1fnh7e9jIuC3Rll9p': 'file_storage/call_E2O5Mvb1fnh7e9jIuC3Rll9p.json', 'var_call_0zeLcCDulZZ0a6WVyejPE8t2': ['Citations', 'sqlite_sequence'], 'var_call_L9uKHTGXlKlNJKXqTmKDxqHG': 'file_storage/call_L9uKHTGXlKlNJKXqTmKDxqHG.json'}

exec(code, env_args)
