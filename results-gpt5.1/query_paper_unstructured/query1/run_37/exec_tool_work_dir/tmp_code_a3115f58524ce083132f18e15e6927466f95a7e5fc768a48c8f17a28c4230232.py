code = """import re, json
import pandas as pd

# Load full citation data
path_citations = var_call_WIrwnrYtxfg1dos2dQLoeLcd
with open(path_citations, 'r') as f:
    citations = json.load(f)

# Load full paper docs data
path_docs = var_call_7spOBn42Yqlu6rSBs9cULMbc
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Heuristic: identify 'food' domain papers via keywords in full text
food_keywords = [
    'food tracking', 'food journal', 'diet tracking', 'diet app', 'calorie tracking', 'calorie tracker',
    'nutrition tracking', 'nutrition app', 'dietary tracking', 'weight loss app', 'weight-loss app',
    'weight loss', 'eating habits', 'meal logging', 'meal log', 'diet diary', 'food diary',
    'nutrition diary', 'calorie counting', 'calorie counter', 'diet monitoring', 'eating behavior',
    'eating behaviours', 'eating behaviour', 'food intake', 'dietary intake', 'eating patterns'
]

food_papers = []
for d in docs:
    text = d.get('text','').lower()
    if any(k in text for k in food_keywords):
        # derive title from filename (strip .txt)
        fn = d.get('filename','')
        title = fn[:-4] if fn.lower().endswith('.txt') else fn
        food_papers.append(title)

food_papers = sorted(set(food_papers))

# Build DataFrame for citations
cf = pd.DataFrame(citations)
# citation_count may be string, convert to int
cf['citation_count'] = cf['citation_count'].astype(int)

# Filter citations whose title matches a food paper title
food_citations = cf[cf['title'].isin(food_papers)]

total_citations = int(food_citations['citation_count'].sum())

result = {
    'food_paper_titles': food_papers,
    'total_citation_count_food_domain': total_citations
}

res_json = json.dumps(result)
print('__RESULT__:')
print(res_json)"""

env_args = {'var_call_7spOBn42Yqlu6rSBs9cULMbc': 'file_storage/call_7spOBn42Yqlu6rSBs9cULMbc.json', 'var_call_WIrwnrYtxfg1dos2dQLoeLcd': 'file_storage/call_WIrwnrYtxfg1dos2dQLoeLcd.json'}

exec(code, env_args)
