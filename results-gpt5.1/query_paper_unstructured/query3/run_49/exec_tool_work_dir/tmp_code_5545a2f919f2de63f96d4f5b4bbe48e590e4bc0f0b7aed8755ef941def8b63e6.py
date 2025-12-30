code = """import re, json
import pandas as pd

# Load full Mongo and SQL results
with open(var_call_8Rd5WoNQsMk5blm3KO3uIBRO, 'r') as f:
    papers = json.load(f)
with open(var_call_13Dx3t0Uwcf7yTxNPgoTuT0X, 'r') as f:
    citations = json.load(f)

# Heuristic extraction of year and contribution from text
records = []
for doc in papers:
    text = doc.get('text','')
    # year: look for CHI/venue line with year, or any 19xx/20xx; take first >=2017
    years = re.findall(r'(19|20)\d{2}', text)
    pub_year = None
    for y in years:
        y_int = int(''.join(y) if isinstance(y, tuple) else y)
        if y_int >= 2017:
            pub_year = y_int
            break
    # contribution: check if "empirical" appears near words like study, evaluation, work
    contrib = None
    if re.search(r'empirical', text, re.I):
        contrib = 'empirical'
    if pub_year is None or contrib != 'empirical':
        continue
    title = re.sub(r'\.txt$', '', doc.get('filename',''))
    records.append({'title': title, 'year': pub_year, 'contribution': contrib})

papers_df = pd.DataFrame(records)

cit_df = pd.DataFrame(citations)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

merged = pd.merge(papers_df, cit_df, on='title', how='inner')

result = merged[['title','total_citations']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_8Rd5WoNQsMk5blm3KO3uIBRO': 'file_storage/call_8Rd5WoNQsMk5blm3KO3uIBRO.json', 'var_call_13Dx3t0Uwcf7yTxNPgoTuT0X': 'file_storage/call_13Dx3t0Uwcf7yTxNPgoTuT0X.json'}

exec(code, env_args)
