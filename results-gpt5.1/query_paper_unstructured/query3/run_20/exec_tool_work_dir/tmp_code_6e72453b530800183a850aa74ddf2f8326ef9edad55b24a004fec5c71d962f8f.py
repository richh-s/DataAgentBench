code = """import re, json, pandas as pd
from datetime import datetime

# Load full Mongo and SQL results
with open(var_call_TGYbbFPHmqgb3uHZSl6gk8ik, 'r') as f:
    mongo_records = json.load(f)
with open(var_call_bJyEbvyBPEUQRgwviKfvXxP9, 'r') as f:
    sql_records = json.load(f)

# Helper: extract year from text
YEAR_RE = re.compile(r'\b(19|20)\d{2}\b')

papers = []
for doc in mongo_records:
    text = doc.get('text', '') or ''
    filename = doc.get('filename', '') or ''
    # crude heuristic: look for CHI/CSCW/etc pattern lines for year, else any year
    years = [int(y) for y in YEAR_RE.findall(text) if ''.join(y).isdigit()]
    # YEAR_RE with groups returns tuples (19, xx); adjust:
    years = []
    for m in YEAR_RE.finditer(text):
        y = m.group(0)
        try:
            years.append(int(y))
        except:
            pass
    pub_year = min(years) if years else None
    title = filename.rsplit('.txt', 1)[0]
    papers.append({'title': title, 'year': pub_year, 'filename': filename})

papers_df = pd.DataFrame(papers)

# Filter for empirical contribution: already prefiltered via regex "empirical" in text
empirical_df = papers_df.copy()

# Filter for year > 2016
empirical_df = empirical_df[empirical_df['year'].notna() & (empirical_df['year'] > 2016)]

sql_df = pd.DataFrame(sql_records)
sql_df['total_citations'] = sql_df['total_citations'].astype(int)

# Join on title
merged = empirical_df.merge(sql_df, on='title', how='left')

result = merged[['title', 'total_citations']].fillna({'total_citations': 0}).to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_TGYbbFPHmqgb3uHZSl6gk8ik': 'file_storage/call_TGYbbFPHmqgb3uHZSl6gk8ik.json', 'var_call_bJyEbvyBPEUQRgwviKfvXxP9': 'file_storage/call_bJyEbvyBPEUQRgwviKfvXxP9.json'}

exec(code, env_args)
