code = """import re, json
import pandas as pd

# Load full results if they are file paths
paper_docs = var_call_RbDiujD3YvdlVynEbLPvRhiN
if isinstance(paper_docs, str):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)

citations = var_call_uTeqKL4zmSbdq7J31uvHj6Yg
if isinstance(citations, str):
    with open(citations, 'r') as f:
        citations = json.load(f)

# Identify 'food' domain papers: heuristic search for domain indicators in text
food_titles = []
for doc in paper_docs:
    text_lower = doc.get('text', '').lower()
    # heuristic: mention of food-specific tracking or diet keywords
    if any(k in text_lower for k in [' food ', ' diet ', ' dietary ', ' calorie', 'nutrition', 'nutritional', 'eating habit', 'meal logging', 'food journal']):
        title = doc.get('filename', '').replace('.txt', '')
        if title:
            food_titles.append(title)

food_titles = list(set(food_titles))

# Sum citations for these titles
cit_df = pd.DataFrame(citations)
# ensure numeric
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

if food_titles:
    total_citations = int(cit_df[cit_df['title'].isin(food_titles)]['citation_count'].sum())
else:
    total_citations = 0

result = {"food_titles": food_titles, "total_citations": total_citations}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_RbDiujD3YvdlVynEbLPvRhiN': 'file_storage/call_RbDiujD3YvdlVynEbLPvRhiN.json', 'var_call_uTeqKL4zmSbdq7J31uvHj6Yg': 'file_storage/call_uTeqKL4zmSbdq7J31uvHj6Yg.json'}

exec(code, env_args)
