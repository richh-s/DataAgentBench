code = """import re, json, pandas as pd
from pathlib import Path

# Load full results from files
with open(var_call_psjoV1V3cV7AuSBuWs5oOtws, 'r') as f:
    papers = json.load(f)
with open(var_call_yV1ZwrxLLwy24UC8AElWO9Xt, 'r') as f:
    citations = json.load(f)

# Helper to extract year from text
YEAR_RE = re.compile(r"(19|20)\d{2}")
VENUE_RE = re.compile(r"CHI|CSCW|Ubicomp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH", re.I)

records = []
for p in papers:
    text = p.get('text','')
    # crude year: earliest year >=2017 mentioned that looks like a pub year
    years = [int(y) for y in YEAR_RE.findall(text)]
    pub_year = None
    if years:
        cand = min(years)
        if cand >= 2017:
            pub_year = cand
    # fallback: search patterns like CHI 2018 etc
    if pub_year is None:
        m = re.search(r"(CHI|CSCW|Ubicomp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+(19|20)\d{2}", text, re.I)
        if m:
            pub_year = int(re.search(r"(19|20)\d{2}", m.group(0)).group(0))
    # require empirical contribution: text contains 'empirical'
    contrib = 'empirical' if re.search(r"empirical", text, re.I) else None
    if contrib == 'empirical' and pub_year and pub_year > 2016:
        title = p.get('filename','').replace('.txt','')
        records.append({'title': title, 'year': pub_year})

emp_df = pd.DataFrame(records).drop_duplicates('title')

cit_df = pd.DataFrame(citations)
# citation totals already aggregated; ensure numeric
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

merged = emp_df.merge(cit_df, left_on='title', right_on='title', how='left')
merged = merged[['title','total_citations','year']].sort_values('title')

result = merged.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_psjoV1V3cV7AuSBuWs5oOtws': 'file_storage/call_psjoV1V3cV7AuSBuWs5oOtws.json', 'var_call_yV1ZwrxLLwy24UC8AElWO9Xt': 'file_storage/call_yV1ZwrxLLwy24UC8AElWO9Xt.json'}

exec(code, env_args)
