code = """import json

# Load the large query results from storage-provided file paths
with open(var_call_2VYrAcCupz0VJN0rEE3Aoj6H, 'r', encoding='utf-8') as f:
    papers = json.load(f)
with open(var_call_BFh4hp6NxxDsJfESxPqbQ8Yg, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build a mapping from title (filename without .txt) to text
title_to_text = {}
for p in papers:
    filename = p.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    title_to_text[title] = p.get('text', '') or ''

# Identify titles whose paper text contains the substring 'food' (case-insensitive)
food_titles = {title for title, text in title_to_text.items() if 'food' in text.lower()}

# Sum citation counts for citations whose title is in the food_titles set
total_citations = 0
matched_titles = set()
for c in citations:
    ctitle = c.get('title')
    # citation_count may be string; convert safely
    try:
        cc = int(c.get('citation_count') or 0)
    except:
        try:
            cc = int(float(c.get('citation_count')))
        except:
            cc = 0
    if ctitle in food_titles:
        total_citations += cc
        matched_titles.add(ctitle)

result = {
    'domain': 'food',
    'total_citations': total_citations,
    'matched_papers_count': len(matched_titles),
    'matched_titles': sorted(list(matched_titles))
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2VYrAcCupz0VJN0rEE3Aoj6H': 'file_storage/call_2VYrAcCupz0VJN0rEE3Aoj6H.json', 'var_call_BFh4hp6NxxDsJfESxPqbQ8Yg': 'file_storage/call_BFh4hp6NxxDsJfESxPqbQ8Yg.json'}

exec(code, env_args)
