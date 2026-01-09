code = """import json, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

cit2018 = load_records(var_call_MFgjaIswaHg2MsC4lsCLekcf)
acm_docs = load_records(var_call_8NwmXgl4jHUuLMpzTqqwwFa3)

cit_df = pd.DataFrame(cit2018)
# ensure numeric
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce')

acm_titles = pd.Series([d.get('filename','') for d in acm_docs]).str.replace(r'\.txt$','', regex=True)
acm_set = set(acm_titles.tolist())

acm_cit_df = cit_df[cit_df['title'].isin(acm_set)].copy()

avg_citations = float(acm_cit_df['citation_count'].mean()) if len(acm_cit_df) else None
out = {
    'average_citation_count_2018_for_acm_papers': avg_citations,
    'num_acm_papers_with_citations_in_2018': int(len(acm_cit_df)),
    'num_total_papers_with_citations_in_2018': int(len(cit_df))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_MFgjaIswaHg2MsC4lsCLekcf': 'file_storage/call_MFgjaIswaHg2MsC4lsCLekcf.json', 'var_call_8NLUEjD4DRFc78Oea8npygS9': 'file_storage/call_8NLUEjD4DRFc78Oea8npygS9.json', 'var_call_8NwmXgl4jHUuLMpzTqqwwFa3': 'file_storage/call_8NwmXgl4jHUuLMpzTqqwwFa3.json'}

exec(code, env_args)
