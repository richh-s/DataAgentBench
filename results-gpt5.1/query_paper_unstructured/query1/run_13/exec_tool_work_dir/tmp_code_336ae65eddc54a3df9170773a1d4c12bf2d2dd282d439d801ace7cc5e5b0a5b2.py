code = """import re, json, pandas as pd

# Load previous results
paper_path = var_call_fkp6epGO6SC2NTY2r56EmduQ
cites_path = var_call_MMjGtz9TfEyGP6BGpTz3t6qV

# Read full JSON files
with open(paper_path, 'r') as f:
    paper_docs = json.load(f)
with open(cites_path, 'r') as f:
    citations = json.load(f)

# Heuristic: treat papers as in 'food' domain if their text contains ' food ' or 'diet' or 'nutrition' (case-insensitive)
food_titles = []
for doc in paper_docs:
    text = doc.get('text', '').lower()
    if re.search(r'\bfood\b', text) or re.search(r'\bdiet\b', text) or re.search(r'nutrition', text):
        filename = doc.get('filename', '')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        food_titles.append(title)

food_titles_set = set(food_titles)

# Sum citation counts for these titles
food_citations_total = 0
for row in citations:
    title = row.get('title')
    if title in food_titles_set:
        try:
            c = int(row.get('citation_count', 0))
        except (TypeError, ValueError):
            c = 0
        food_citations_total += c

result = json.dumps({"total_food_domain_citations": food_citations_total, "food_titles": sorted(list(food_titles_set))})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_fkp6epGO6SC2NTY2r56EmduQ': 'file_storage/call_fkp6epGO6SC2NTY2r56EmduQ.json', 'var_call_MMjGtz9TfEyGP6BGpTz3t6qV': 'file_storage/call_MMjGtz9TfEyGP6BGpTz3t6qV.json'}

exec(code, env_args)
