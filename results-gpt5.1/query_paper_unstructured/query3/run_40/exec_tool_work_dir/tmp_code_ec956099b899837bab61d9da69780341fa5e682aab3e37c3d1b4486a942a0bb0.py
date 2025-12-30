code = """import re, json, pandas as pd

# Load full Mongo and citations results
mongo_path = var_call_2AiMU2L6CCxvngTKetwlmIda
sql_path = var_call_CbxgolmBjXmgtcykl2p4Cwtt

with open(mongo_path, 'r') as f:
    mongo_records = json.load(f)
with open(sql_path, 'r') as f:
    sql_records = json.load(f)

# Extract year from text (search for years 2017-2025) and identify empirical contribution by keyword
empirical_papers = []
for doc in mongo_records:
    text = doc.get('text', '') or ''
    # year: look for patterns like CHI 2018, 2019, (c) 2020, etc.
    years = re.findall(r'(20[1-2][0-9])', text)
    year = None
    if years:
        # choose the earliest plausible publication year >=2017
        years_int = sorted({int(y) for y in years})
        for y in years_int:
            if y >= 2017:
                year = y
                break
    # empirical contribution: look for word 'empirical' or common phrases
    if re.search(r'\bempirical\b', text, re.IGNORECASE):
        contrib = 'empirical'
    else:
        continue
    if year and year > 2016:
        title = (doc.get('filename') or '').rsplit('.txt', 1)[0]
        empirical_papers.append({'title': title, 'year': year})

# Build DataFrame for citations
cit_df = pd.DataFrame(sql_records)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

emp_df = pd.DataFrame(empirical_papers)

if emp_df.empty:
    result = []
else:
    merged = emp_df.merge(cit_df, left_on='title', right_on='title', how='left')
    merged = merged[['title', 'total_citations']].dropna(subset=['total_citations'])
    result = merged.to_dict(orient='records')

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_2AiMU2L6CCxvngTKetwlmIda': 'file_storage/call_2AiMU2L6CCxvngTKetwlmIda.json', 'var_call_CbxgolmBjXmgtcykl2p4Cwtt': 'file_storage/call_CbxgolmBjXmgtcykl2p4Cwtt.json'}

exec(code, env_args)
