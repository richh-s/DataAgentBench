code = """import json, re, pandas as pd

# citations
with open(var_call_V9x1rudDBVpE0M5q4epF8CxZ,'r',encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# paper docs (up to 5000)
with open(var_call_KWqfqaW3GsMkUKZQir6Ax4CZ,'r',encoding='utf-8') as f:
    docs = json.load(f)

def is_acm_text(t):
    if not isinstance(t,str):
        return False
    return bool(re.search(r'Copyright\s*\d{4}\s*\u00a9\s*ACM|\bACM\s+Classification\b|\bacm\.org\b|dx\.doi\.org/10\.1145', t, flags=re.I))

acm_titles = set()
for d in docs:
    if not isinstance(d,dict):
        continue
    fn = d.get('filename')
    if not (isinstance(fn,str) and fn.endswith('.txt')):
        continue
    if is_acm_text(d.get('text')):
        acm_titles.add(fn[:-4])

# filter citations by acm titles
filt = df_cit[df_cit['title'].isin(acm_titles)].copy()
avg = float(filt['citation_count'].mean()) if len(filt) else None

out = {
    'average_citation_count_2018_for_acm_papers': avg,
    'num_acm_titles_detected_in_docs_sample': int(len(acm_titles)),
    'num_citation_records_matched': int(len(filt))
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_V9x1rudDBVpE0M5q4epF8CxZ': 'file_storage/call_V9x1rudDBVpE0M5q4epF8CxZ.json', 'var_call_9ydg5xMWa3WV5LQuGjOB9aW3': 'file_storage/call_9ydg5xMWa3WV5LQuGjOB9aW3.json', 'var_call_1zbhc3XDHJiQGMfRH2bAYeK4': 'file_storage/call_1zbhc3XDHJiQGMfRH2bAYeK4.json', 'var_call_Zp33HXUM3PPWXmvbBnto98je': {'average_citation_count_2018_for_acm_papers': None, 'num_papers_included': 0, 'assumed_all_paper_docs_are_acm': False, 'sample_acm_detection_proportion': 0}, 'var_call_KWqfqaW3GsMkUKZQir6Ax4CZ': 'file_storage/call_KWqfqaW3GsMkUKZQir6Ax4CZ.json'}

exec(code, env_args)
