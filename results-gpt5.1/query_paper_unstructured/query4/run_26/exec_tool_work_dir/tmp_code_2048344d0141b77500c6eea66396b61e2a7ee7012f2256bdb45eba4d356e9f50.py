code = """import json, re, pandas as pd

# Load full results
with open(var_call_msC6tZIuxu5X2oXpaOhVcPzq) as f:
    papers = json.load(f)
with open(var_call_lBZqkNQMJGx5TZBi20XYaAxy) as f:
    cits = json.load(f)

# Extract title (filename without .txt) and approximate year & domain from text
records = []
for doc in papers:
    title = doc.get('filename','').replace('.txt','')
    text = doc.get('text','')
    # heuristic: look for 4-digit years 20xx or 19xx; take first between 2000-2025
    years = re.findall(r"(19|20)\d{2}", text)
    pub_year = None
    for y in re.findall(r"(19\d{2}|20\d{2})", text):
        y_int = int(y)
        if 2000 <= y_int <= 2025:
            pub_year = y_int
            break
    # domain detection via keyword
    domain = 'physical activity' if re.search(r'physical activity', text, re.I) else ''
    records.append({'title': title, 'year': pub_year, 'domain': domain})

paper_df = pd.DataFrame(records)

# Filter to physical activity domain and year 2016
pa_2016 = paper_df[(paper_df['domain'] == 'physical activity') & (paper_df['year'] == 2016)]

cit_df = pd.DataFrame(cits)
# normalize types
cit_df['citation_count'] = cit_df['citation_count'].astype(int)

# compute total citations per title (all years)
cit_totals = cit_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})

result_df = pa_2016.merge(cit_totals, left_on='title', right_on='title', how='left')
result_df = result_df[['title','total_citations']].fillna(0)

result = result_df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_msC6tZIuxu5X2oXpaOhVcPzq': 'file_storage/call_msC6tZIuxu5X2oXpaOhVcPzq.json', 'var_call_lBZqkNQMJGx5TZBi20XYaAxy': 'file_storage/call_lBZqkNQMJGx5TZBi20XYaAxy.json', 'var_call_fBFQj6oiqu4d6uCCqynRhDdh': ['paper_docs']}

exec(code, env_args)
