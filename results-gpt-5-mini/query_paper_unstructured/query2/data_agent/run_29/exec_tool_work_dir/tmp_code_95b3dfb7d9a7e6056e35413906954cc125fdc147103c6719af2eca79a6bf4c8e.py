code = """import json
import pandas as pd
import re

with open(var_call_l3PPpLM8azB2GyPcKmLRSWmP, 'r') as f:
    citations = json.load(f)
with open(var_call_LyPn518D1Z9V3O9rDu5LttwR, 'r') as f:
    papers = json.load(f)

df_c = pd.DataFrame(citations)
df_p = pd.DataFrame(papers)

# Normalize function
def normalize_title(t):
    if t is None:
        return ''
    s = str(t)
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^0-9a-z ]+", "", s)
    s = s.strip()
    return s

# Add title from filename
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_p['title'] = None

# normalized
if 'title' in df_c.columns:
    df_c['title_norm'] = df_c['title'].apply(normalize_title)
else:
    df_c['title_norm'] = ['']*len(df_c)

df_p['title_norm'] = df_p['title'].apply(normalize_title)

set_c = set(df_c['title_norm'].unique())
set_p = set(df_p['title_norm'].unique())

intersection = set_c.intersection(set_p)

# sample sizes
sample_c_titles = df_c['title'].head(30).tolist()
sample_p_filenames = df_p['filename'].head(30).tolist()

# show up to 20 matching titles
match_examples = list(intersection)[:20]

# For matched titles, show whether paper text contains 'ACM'
matches_info = []
for tn in match_examples:
    rows = df_p[df_p['title_norm']==tn]
    has_acm = False
    titles = []
    for _,r in rows.iterrows():
        titles.append(r.get('title',''))
        text = r.get('text','')
        if isinstance(text,str) and re.search(r'\bacm\b', text, flags=re.I):
            has_acm = True
    matches_info.append({'title_norm': tn, 'paper_titles': titles, 'has_acm': has_acm})

result = {
    'num_citation_records': len(df_c),
    'num_paper_docs': len(df_p),
    'num_intersection_titles': len(intersection),
    'match_examples': matches_info,
    'sample_citation_titles_first30': sample_c_titles,
    'sample_paper_filenames_first30': sample_p_filenames
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_l3PPpLM8azB2GyPcKmLRSWmP': 'file_storage/call_l3PPpLM8azB2GyPcKmLRSWmP.json', 'var_call_JpdX0be34W7QvGpbBwH5EoYN': ['paper_docs'], 'var_call_LyPn518D1Z9V3O9rDu5LttwR': 'file_storage/call_LyPn518D1Z9V3O9rDu5LttwR.json', 'var_call_ot8o1VcWilpQ4hD8fqPulUQC': {'average_citation_count': None, 'num_acm_papers_considered': 0}, 'var_call_XtWWLN8dMLbtU9XrALfuOBUX': 'file_storage/call_XtWWLN8dMLbtU9XrALfuOBUX.json', 'var_call_jx0Rd4Uv3k2QWGB5RZGnVZmA': {'average_citation_count': None, 'num_acm_citation_records_considered': 0, 'sample_acm_papers': []}}

exec(code, env_args)
