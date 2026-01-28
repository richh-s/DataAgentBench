code = """import json, re, pandas as pd

# Load the large results from previous query_db calls
with open(var_call_jHSiOWOHwnSpyCQ50XZw1l5e, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)
with open(var_call_ppzE5Yv8StwF7ET15Xy2Exuz, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Process paper documents
records = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text', '') or ''
    # Extract first year occurrence (between 1900 and 2026)
    years = re.findall(r'\b(19|20)\d{2}\b', text)
    # The above returns only the first two digits; better find full matches
    full_years = re.findall(r'\b(?:19|20)\d{2}\b', text)
    year = None
    if full_years:
        try:
            year = int(full_years[0])
        except:
            year = None
    # Contribution: check substring 'empirical' in text
    contribution_empirical = False
    if 'empirical' in text.lower():
        contribution_empirical = True
    records.append({'title': title, 'year': year, 'empirical': contribution_empirical})

# Convert to DataFrame
df_papers = pd.DataFrame(records)
# Filter for empirical contribution and year > 2016
df_filtered = df_papers[(df_papers['empirical'] == True) & (df_papers['year'].notnull()) & (df_papers['year'] > 2016)]

# Process citations
# citations is list of dicts with 'title' and 'total_citations'
for c in citations:
    # Normalize keys
    if 'total_citations' in c:
        try:
            c['total_citations'] = int(c['total_citations'])
        except:
            try:
                c['total_citations'] = int(float(c['total_citations']))
            except:
                c['total_citations'] = None

# Create DataFrame for citations
df_cite = pd.DataFrame(citations)
# Merge on title
df_merged = pd.merge(df_filtered, df_cite, on='title', how='left')

# Prepare result list
result_list = []
for _, row in df_merged.iterrows():
    total = row.get('total_citations', None)
    # If missing, set to 0
    if total is None or (isinstance(total, float) and pd.isna(total)):
        total = 0
    try:
        total = int(total)
    except:
        total = 0
    result_list.append({'title': row['title'], 'total_citations': total, 'year': int(row['year'])})

# Sort by total_citations descending
result_list = sorted(result_list, key=lambda x: x['total_citations'], reverse=True)

import json
print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_call_jHSiOWOHwnSpyCQ50XZw1l5e': 'file_storage/call_jHSiOWOHwnSpyCQ50XZw1l5e.json', 'var_call_ppzE5Yv8StwF7ET15Xy2Exuz': 'file_storage/call_ppzE5Yv8StwF7ET15Xy2Exuz.json'}

exec(code, env_args)
