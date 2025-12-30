code = """import json
import pandas as pd

# Load full citations result
with open(var_call_fiNuwQFvEchJkIoEC2DDE2jk, 'r') as f:
    citations = json.load(f)

# Load full paper docs result
with open(var_call_MEeUDKkqd3w5C52zWbvEg5xh, 'r') as f:
    papers = json.load(f)

# Build dataframe for citations
cit_df = pd.DataFrame(citations)
# normalize types
cit_df['citation_count'] = cit_df['citation_count'].astype(int)

# Build mapping from title to venue by scanning text for CHI/Ubicomp/etc. Here we only need CHI.
records = []
for doc in papers:
    filename = doc.get('filename','')
    text = doc.get('text','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # crude venue detection: look for "CHI" near top of paper
    header = text[:2000].upper()
    venue = None
    if 'CHI ' in header or "CHI'" in header or ' CHI,' in header or '\nCHI ' in header or ' CHI\n' in header:
        venue = 'CHI'
    # store even if venue is None for possible future use
    records.append({'title': title, 'venue': venue})

venue_df = pd.DataFrame(records)

# filter to CHI papers
chi_titles = set(venue_df[venue_df['venue']=='CHI']['title'])

# filter citations to those titles
chi_citations = cit_df[cit_df['title'].isin(chi_titles)]

total_citations_2020 = int(chi_citations['citation_count'].sum())

import json as jsonlib
result = jsonlib.dumps(total_citations_2020)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_fiNuwQFvEchJkIoEC2DDE2jk': 'file_storage/call_fiNuwQFvEchJkIoEC2DDE2jk.json', 'var_call_MEeUDKkqd3w5C52zWbvEg5xh': 'file_storage/call_MEeUDKkqd3w5C52zWbvEg5xh.json'}

exec(code, env_args)
