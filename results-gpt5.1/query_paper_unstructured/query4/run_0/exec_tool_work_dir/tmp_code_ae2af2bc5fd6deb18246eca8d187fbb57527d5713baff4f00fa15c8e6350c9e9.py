code = """import re, json, pandas as pd

# Load full Mongo and SQL results
with open(var_call_WP5wkczVqlcHGYSKRbUvSjmQ, 'r') as f:
    mongo_records = json.load(f)
with open(var_call_qMOPXmmESQcksob1CmjhgtMQ, 'r') as f:
    citation_records = json.load(f)

# Extract year and domain heuristically from text
papers = []
for doc in mongo_records:
    text = doc.get('text', '')
    # Year: look for 2016 explicitly in the header lines
    year = None
    m = re.search(r"\b2016\b", text[:2000])
    if m:
        year = 2016
    # Domain: check if 'physical activity' appears
    domain = 'physical activity' if re.search(r"physical activity", text, re.I) else None
    if year == 2016 and domain == 'physical activity':
        title = doc.get('filename', '').rsplit('.txt', 1)[0]
        papers.append({'title': title, 'year': year, 'domain': domain})

# Build dataframe of citations
cit_df = pd.DataFrame(citation_records)
# citation counts may be strings
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

# Join and aggregate total citations per title for the matched papers
papers_df = pd.DataFrame(papers)
if not papers_df.empty:
    merged = papers_df.merge(cit_df, on='title', how='left')
    result_df = merged.groupby('title', as_index=False)['total_citations'].sum()
    result = result_df.to_dict(orient='records')
else:
    result = []

res_str = json.dumps(result)
print("__RESULT__:")
print(res_str)"""

env_args = {'var_call_WP5wkczVqlcHGYSKRbUvSjmQ': 'file_storage/call_WP5wkczVqlcHGYSKRbUvSjmQ.json', 'var_call_qMOPXmmESQcksob1CmjhgtMQ': 'file_storage/call_qMOPXmmESQcksob1CmjhgtMQ.json'}

exec(code, env_args)
