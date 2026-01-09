code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

cit = load_records(var_call_mSCECsUItAeAnhBmwB3P5Xqy)
docs = load_records(var_call_lzLQEz5GRmIyekCQwS3pQ2pJ)

cit_df = pd.DataFrame(cit)
# ensure numeric
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce')

# Extract title from filename
acm_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$', '', fn).strip()
    text = d.get('text','') or ''
    if re.search(r'\bACM\b', text) or re.search(r'Copyright\s*\d{4}\s*©\s*ACM', text, flags=re.IGNORECASE):
        acm_titles.add(title)

# Filter citations to those titles
filt = cit_df[cit_df['title'].isin(acm_titles) & cit_df['citation_count'].notna()]
avg = float(filt['citation_count'].mean()) if len(filt)>0 else None
result = {
    'average_citation_count_2018_acm': avg,
    'num_papers_matched': int(len(filt)),
    'num_acm_papers_in_corpus': int(len(acm_titles))
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_mSCECsUItAeAnhBmwB3P5Xqy': 'file_storage/call_mSCECsUItAeAnhBmwB3P5Xqy.json', 'var_call_lzLQEz5GRmIyekCQwS3pQ2pJ': 'file_storage/call_lzLQEz5GRmIyekCQwS3pQ2pJ.json'}

exec(code, env_args)
