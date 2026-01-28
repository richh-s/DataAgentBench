code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

cit = load_records(var_call_Fy5i3XczySmswFCLJNUHzFPg)
docs = load_records(var_call_wWw7duUsf4O7fGHH8JOrvdkm)

df_cit = pd.DataFrame(cit)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

def title_from_filename(fn):
    return re.sub(r'\.txt$', '', fn or '').strip()

# detect ACM source via typical copyright line / permissions / ACM DOI
acm_pat = re.compile(r'\bAssociation for Computing Machinery\b|\bACM\b|acm\.org|dx\.doi\.org/10\.1145|doi\.org/10\.1145', re.IGNORECASE)

acm_titles = set()
for d in docs:
    fn = d.get('filename')
    text = d.get('text') or ''
    if acm_pat.search(text):
        acm_titles.add(title_from_filename(fn))

# filter citations to ACM titles and compute average
mask = df_cit['title'].isin(acm_titles)
df_acm = df_cit[mask].copy()
avg = float(df_acm['citation_count'].mean()) if len(df_acm) else None

out = {
    'average_citation_count_2018_acm': avg,
    'num_acm_papers_with_2018_citations': int(len(df_acm)),
    'num_total_papers_with_2018_citations': int(len(df_cit)),
    'num_acm_titles_detected_in_docs': int(len(acm_titles))
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Fy5i3XczySmswFCLJNUHzFPg': 'file_storage/call_Fy5i3XczySmswFCLJNUHzFPg.json', 'var_call_wWw7duUsf4O7fGHH8JOrvdkm': 'file_storage/call_wWw7duUsf4O7fGHH8JOrvdkm.json'}

exec(code, env_args)
