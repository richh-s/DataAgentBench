code = """import json, re, pandas as pd

# Load citations 2018
path_cit = var_call_V9x1rudDBVpE0M5q4epF8CxZ
with open(path_cit,'r',encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# Load all filenames
path_fn = var_call_9ydg5xMWa3WV5LQuGjOB9aW3
with open(path_fn,'r',encoding='utf-8') as f:
    fns = json.load(f)
acm_titles = set([rec['filename'][:-4] for rec in fns if isinstance(rec,dict) and isinstance(rec.get('filename'),str) and rec.get('filename').endswith('.txt')])

sample = var_call_1zbhc3XDHJiQGMfRH2bAYeK4

def is_acm_text(t):
    if not isinstance(t,str):
        return False
    return bool(re.search(r'\bACM\b', t)) and bool(re.search(r'Copyright\s*\d{4}\s*\u00a9\s*ACM|\bACM\s+Classification\b|\bacm\.org\b|dx\.doi\.org/10\.1145', t, flags=re.I))

acm_from_sample = set()
sample_titles = []
if isinstance(sample,list):
    for rec in sample:
        if not isinstance(rec,dict):
            continue
        fn = rec.get('filename')
        if isinstance(fn,str) and fn.endswith('.txt'):
            title = fn[:-4]
            sample_titles.append(title)
            if is_acm_text(rec.get('text')):
                acm_from_sample.add(title)

prop = (len(acm_from_sample) / len(sample_titles)) if sample_titles else 0
all_acm = prop > 0.8

acm_title_set = acm_titles if all_acm else acm_from_sample

mask = df_cit['title'].isin(acm_title_set)
df_f = df_cit[mask].copy()
avg = float(df_f['citation_count'].mean()) if len(df_f) else None

out = {
    'average_citation_count_2018_for_acm_papers': avg,
    'num_papers_included': int(len(df_f)),
    'assumed_all_paper_docs_are_acm': bool(all_acm),
    'sample_acm_detection_proportion': prop
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_V9x1rudDBVpE0M5q4epF8CxZ': 'file_storage/call_V9x1rudDBVpE0M5q4epF8CxZ.json', 'var_call_9ydg5xMWa3WV5LQuGjOB9aW3': 'file_storage/call_9ydg5xMWa3WV5LQuGjOB9aW3.json', 'var_call_1zbhc3XDHJiQGMfRH2bAYeK4': 'file_storage/call_1zbhc3XDHJiQGMfRH2bAYeK4.json'}

exec(code, env_args)
