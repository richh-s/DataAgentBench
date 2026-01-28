code = """import json
import pandas as pd

# Load full citations result
with open(var_call_fiNuwQFvEchJkIoEC2DDE2jk, 'r') as f:
    citations = json.load(f)

# Load full paper docs result
with open(var_call_MEeUDKkqd3w5C52zWbvEg5xh, 'r') as f:
    papers = json.load(f)

cit_df = pd.DataFrame(citations)
cit_df['citation_count'] = cit_df['citation_count'].astype(int)

records = []
for doc in papers:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    header = text[:2000].upper()
    venue = None
    if 'CHI ' in header or "CHI'" in header or ' CHI,' in header or '\nCHI ' in header or ' CHI\n' in header:
        venue = 'CHI'
    records.append({'title': title, 'venue': venue})

venue_df = pd.DataFrame(records)
chi_titles = set(venue_df[venue_df['venue'] == 'CHI']['title'])
chi_citations = cit_df[cit_df['title'].isin(chi_titles)]

total_citations_2020 = int(chi_citations['citation_count'].sum())

import json as jsonlib
result = jsonlib.dumps(total_citations_2020)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_fiNuwQFvEchJkIoEC2DDE2jk': 'file_storage/call_fiNuwQFvEchJkIoEC2DDE2jk.json', 'var_call_MEeUDKkqd3w5C52zWbvEg5xh': 'file_storage/call_MEeUDKkqd3w5C52zWbvEg5xh.json'}

exec(code, env_args)
