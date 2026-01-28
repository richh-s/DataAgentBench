code = """import json, re
import pandas as pd

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path

cit = load_records(var_call_q5UKoConJZsr5d6LrOUBSF63)
docs = load_records(var_call_ye7wD441i8kfEhXys9Z2yenT)

df_cit = pd.DataFrame(cit)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

df_docs = pd.DataFrame(docs)
df_docs['title'] = df_docs['filename'].str.replace(r'\.txt$', '', regex=True)

def is_acm(text):
    if not isinstance(text, str):
        return False
    t = text.lower()
    return ('copyright' in t and 'acm' in t) or ('association for computing machinery' in t) or ('permissions@acm.org' in t)

df_docs['is_acm'] = df_docs['text'].map(is_acm)

df = df_cit.merge(df_docs[['title','is_acm']], on='title', how='inner')

df_acm = df[df['is_acm'] == True].copy()

avg_val = float(df_acm['citation_count'].mean()) if len(df_acm) else None
out = {
    'avg_citation_count': avg_val,
    'paper_count': int(len(df_acm)),
    'citation_year': 2018
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6xyYv3iyFVD0GbUPRn0XBn9f': [{'avg_citation_count': 'None'}], 'var_call_BcsowIr2nUI5lV1hJfhPFIcw': ['paper_docs'], 'var_call_q5UKoConJZsr5d6LrOUBSF63': 'file_storage/call_q5UKoConJZsr5d6LrOUBSF63.json', 'var_call_ye7wD441i8kfEhXys9Z2yenT': 'file_storage/call_ye7wD441i8kfEhXys9Z2yenT.json'}

exec(code, env_args)
