code = """import json
import pandas as pd

# citations
with open(var_call_xwJY1upmut1pJPLyopTrMQnS,'r',encoding='utf-8') as f:
    cit=json.load(f)
df=pd.DataFrame(cit)
df['citation_count']=pd.to_numeric(df['citation_count'],errors='coerce').fillna(0).astype(int)

# docs titles set
with open(var_call_83MpOqyahzqLwNuseTcsNb0P,'r',encoding='utf-8') as f:
    docs=json.load(f)
titles=set([d['filename'][:-4] if d.get('filename','').lower().endswith('.txt') else d.get('filename','') for d in docs])

matched=int(df['title'].isin(titles).sum())
print('__RESULT__:')
print(json.dumps({'citations_2020_rows': int(len(df)), 'matched_titles_in_docs': matched}))"""

env_args = {'var_call_xwJY1upmut1pJPLyopTrMQnS': 'file_storage/call_xwJY1upmut1pJPLyopTrMQnS.json', 'var_call_83MpOqyahzqLwNuseTcsNb0P': 'file_storage/call_83MpOqyahzqLwNuseTcsNb0P.json', 'var_call_zgW9zjWAApz4Rsd2InxZkzdh': {'total_citations': 0, 'num_papers': 0}, 'var_call_bpG8GJcobGk6FC7r4GXH89ue': 'file_storage/call_bpG8GJcobGk6FC7r4GXH89ue.json', 'var_call_zi33BxAI2zKCTpxAMRNmL1ep': {'Ubicomp': 71, 'DIS': 2, 'null': 15, 'CSCW': 11}}

exec(code, env_args)
