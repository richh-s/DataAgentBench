code = """import json, re
import pandas as pd

# Load paper docs
paper_docs_src = var_call_EmiF4ccxWmcLJ1D02sH3lx8F
if isinstance(paper_docs_src, str):
    with open(paper_docs_src, 'r', encoding='utf-8') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_src

# Load citations
cit_src = var_call_wkVRtwW8Nme5ucXFI3gDhvjb
if isinstance(cit_src, str):
    with open(cit_src, 'r', encoding='utf-8') as f:
        citations = json.load(f)
else:
    citations = cit_src

# Identify 'food' domain papers using substring match on full text
food_titles = set()
for d in paper_docs:
    text = (d.get('text') or '')
    if re.search(r'\bfood\b', text, flags=re.IGNORECASE):
        fn = d.get('filename','')
        title = re.sub(r'\.txt$', '', fn)
        food_titles.add(title)

# Sum citation_count for those titles
food_titles_lower = {t.lower(): t for t in food_titles}

total = 0
matched_records = 0
for r in citations:
    title = (r.get('title') or '')
    if title.lower() in food_titles_lower:
        try:
            total += int(r.get('citation_count') or 0)
            matched_records += 1
        except Exception:
            pass

out = {"total_citation_count": total, "food_paper_count": len(food_titles), "matched_citation_rows": matched_records}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_EmiF4ccxWmcLJ1D02sH3lx8F': 'file_storage/call_EmiF4ccxWmcLJ1D02sH3lx8F.json', 'var_call_wkVRtwW8Nme5ucXFI3gDhvjb': 'file_storage/call_wkVRtwW8Nme5ucXFI3gDhvjb.json'}

exec(code, env_args)
