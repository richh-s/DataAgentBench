code = """import re, json
import pandas as pd

# Load full citation aggregates
path_citations = var_call_Ii9WxpOjhlm7MooyAdxhXyUY
with open(path_citations, 'r') as f:
    citations = json.load(f)

# Load paper docs (preview already filtered by regex physical activity + 2016 approximated via text regex earlier)
path_docs = var_call_mQwdajnSJbDogZlDZoFB2x5g
with open(path_docs, 'r') as f:
    docs = json.load(f)

records = []
for d in docs:
    text = d.get('text', '')
    # extract year: look for 2016
    year_match = re.search(r'20(\d{2})', text)
    year = int(year_match.group(0)) if year_match else None
    # domain physical activity (already filtered, but double-check)
    if 'physical activity' in text.lower() and year == 2016:
        title = d.get('filename', '').replace('.txt', '')
        records.append({'title': title, 'year': year})

# join with citations
df_papers = pd.DataFrame(records)
df_cit = pd.DataFrame(citations)
if not df_papers.empty:
    df = df_papers.merge(df_cit, left_on='title', right_on='title', how='left')
    df = df[['title', 'total_citations']]
    df['total_citations'] = df['total_citations'].astype(float).fillna(0).astype(int)
    result = df.to_dict(orient='records')
else:
    result = []

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_mQwdajnSJbDogZlDZoFB2x5g': 'file_storage/call_mQwdajnSJbDogZlDZoFB2x5g.json', 'var_call_Ii9WxpOjhlm7MooyAdxhXyUY': 'file_storage/call_Ii9WxpOjhlm7MooyAdxhXyUY.json'}

exec(code, env_args)
