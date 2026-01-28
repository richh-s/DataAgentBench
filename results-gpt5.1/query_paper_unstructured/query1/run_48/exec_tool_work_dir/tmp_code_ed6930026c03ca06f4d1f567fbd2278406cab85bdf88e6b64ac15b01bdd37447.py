code = """import json, re, pandas as pd

# Load full results if needed
food_docs_path = var_call_M2ziD59dLpOE8QXubaepVfSw
cites_path = var_call_xvzO4YOCsfuLqTIBrVVGhcey

with open(food_docs_path, 'r') as f:
    food_docs = json.load(f)
with open(cites_path, 'r') as f:
    cites = json.load(f)

# Extract titles (filename without .txt) and try to detect 'food' domain by simple heuristic:
# here, since the query already matched 'food' in text, we will treat all these as food-domain papers.
food_titles = set()
for d in food_docs:
    fname = d.get('filename','')
    if fname.lower().endswith('.txt'):
        title = fname[:-4]
    else:
        title = fname
    food_titles.add(title.strip())

# Build dataframe of citations
cites_df = pd.DataFrame(cites)
# citation counts may be strings
cites_df['total_citations'] = cites_df['total_citations'].astype(int)

# Filter to food titles (exact match on title)
food_cites = cites_df[cites_df['title'].isin(food_titles)]

total_citations_food = int(food_cites['total_citations'].sum())

result = json.dumps(total_citations_food)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_M2ziD59dLpOE8QXubaepVfSw': 'file_storage/call_M2ziD59dLpOE8QXubaepVfSw.json', 'var_call_xvzO4YOCsfuLqTIBrVVGhcey': 'file_storage/call_xvzO4YOCsfuLqTIBrVVGhcey.json'}

exec(code, env_args)
