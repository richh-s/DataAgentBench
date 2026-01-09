code = """import json, pandas as pd, re
from pathlib import Path

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json') and Path(x).exists():
        return json.loads(Path(x).read_text())
    return x

cit = load_tool_result(var_call_4hemfVqDWkovK4VRG2DmaOIt)
docs = load_tool_result(var_call_2eNXeA3Z4EPdh0jYFnUfJvNi)

cit_df = pd.DataFrame(cit)
# ensure numeric
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# extract title and venue from docs
rows = []
venue_pat = re.compile(r"\b(CHI|UbiComp|UBICOMP|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\b", re.IGNORECASE)
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    m = venue_pat.search(text)
    venue = None
    if m:
        v = m.group(1)
        if v.lower() == 'ubicomp':
            venue = 'Ubicomp'
        else:
            venue = v.upper() if v.upper() in ['CHI','CSCW','DIS','WWW','IUI','TEI','AH'] else v
            if venue.lower() == 'ozchi':
                venue = 'OzCHI'
            if venue.lower() == 'pervasivehealth':
                venue = 'PervasiveHealth'
    rows.append({'title': title, 'venue': venue})

doc_df = pd.DataFrame(rows).drop_duplicates(subset=['title'])

# join
merged = cit_df.merge(doc_df, on='title', how='left')
chi = merged[merged['venue'].fillna('').str.upper()=='CHI']

total = int(chi['citation_count'].sum())
res = {
    'total_citation_count_2020_for_CHI_papers': total,
    'num_CHI_papers_with_citations_2020': int(chi.shape[0]),
    'num_citation_records_2020_total': int(cit_df.shape[0]),
    'num_citation_records_2020_matched_to_docs': int(merged['venue'].notna().sum())
}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_4hemfVqDWkovK4VRG2DmaOIt': 'file_storage/call_4hemfVqDWkovK4VRG2DmaOIt.json', 'var_call_2eNXeA3Z4EPdh0jYFnUfJvNi': 'file_storage/call_2eNXeA3Z4EPdh0jYFnUfJvNi.json'}

exec(code, env_args)
