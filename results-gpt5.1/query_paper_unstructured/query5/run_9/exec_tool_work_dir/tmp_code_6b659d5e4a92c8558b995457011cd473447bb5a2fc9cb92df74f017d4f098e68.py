code = """import json, pandas as pd

# Load full citations data
with open(var_call_yhhMiKKgiZou82BnhuCfpT04, 'r') as f:
    citations = json.load(f)

# Load full paper docs metadata
with open(var_call_GuzDNY19emLgYgduYBdr12Mq, 'r') as f:
    docs = json.load(f)

# Build dataframe for docs with inferred title and venue filter
rows = []
for d in docs:
    filename = d.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text', '')
    venue = None
    # simple heuristic: look for 'CHI ' in first 2000 chars
    header = text[:2000].upper()
    if ' CHI ' in header or "CHI '" in header or "\nCHI " in header:
        venue = 'CHI'
    rows.append({'title': title, 'venue': venue})

docs_df = pd.DataFrame(rows)
chi_titles = set(docs_df[docs_df['venue']=='CHI']['title'])

cit_df = pd.DataFrame(citations)
# ensure numeric citation_count
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'])

# filter citations to CHI papers only
chi_cit = cit_df[cit_df['title'].isin(chi_titles)]

result = int(chi_cit['citation_count'].sum())

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_yhhMiKKgiZou82BnhuCfpT04': 'file_storage/call_yhhMiKKgiZou82BnhuCfpT04.json', 'var_call_GuzDNY19emLgYgduYBdr12Mq': 'file_storage/call_GuzDNY19emLgYgduYBdr12Mq.json'}

exec(code, env_args)
