code = """import json
import pandas as pd
import re

with open(var_call_l3PPpLM8azB2GyPcKmLRSWmP, 'r') as f:
    citations = json.load(f)
with open(var_call_LyPn518D1Z9V3O9rDu5LttwR, 'r') as f:
    papers = json.load(f)

# DataFrames
df_c = pd.DataFrame(citations)
df_p = pd.DataFrame(papers)

# Ensure citation_count numeric
df_c['citation_count'] = pd.to_numeric(df_c.get('citation_count', 0), errors='coerce').fillna(0).astype(int)

# Extract title from filename
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace(r'\.txt$', '', regex=True)
else:
    df_p['title'] = None

# Normalization function for titles
def normalize_title(t):
    if t is None:
        return ''
    s = str(t)
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    # remove punctuation except keep alnum and spaces
    s = re.sub(r"[^0-9a-z ]+", "", s)
    s = s.strip()
    return s

# Create normalized title columns
if 'title' in df_c.columns:
    df_c['title_norm'] = df_c['title'].apply(normalize_title)
else:
    df_c['title_norm'] = ['']*len(df_c)

if 'title' in df_p.columns:
    df_p['title_norm'] = df_p['title'].apply(normalize_title)
else:
    df_p['title_norm'] = ['']*len(df_p)

# Detect ACM source in paper text
if 'text' in df_p.columns:
    df_p['source_is_acm'] = df_p['text'].str.contains(r'\bacm\b', case=False, na=False) | df_p['text'].str.contains('Association for Computing Machinery', case=False, na=False)
else:
    df_p['source_is_acm'] = False

# Merge on normalized title
df_merged = pd.merge(df_c, df_p[['title','title_norm','source_is_acm']], on='title_norm', how='left', indicator=True)

# Filter merged records where source_is_acm is True
df_acm = df_merged[df_merged['source_is_acm'] == True]

matched_acm_count = int(len(df_acm))

avg = None
if matched_acm_count>0:
    avg = round(float(df_acm['citation_count'].mean()), 2)

# Prepare sample list
sample = df_acm[['title', 'citation_count']].drop_duplicates().head(20).to_dict(orient='records')

result = {
    'average_citation_count': None if avg is None else avg,
    'num_acm_citation_records_considered': matched_acm_count,
    'sample_acm_papers': sample
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_l3PPpLM8azB2GyPcKmLRSWmP': 'file_storage/call_l3PPpLM8azB2GyPcKmLRSWmP.json', 'var_call_JpdX0be34W7QvGpbBwH5EoYN': ['paper_docs'], 'var_call_LyPn518D1Z9V3O9rDu5LttwR': 'file_storage/call_LyPn518D1Z9V3O9rDu5LttwR.json', 'var_call_ot8o1VcWilpQ4hD8fqPulUQC': {'average_citation_count': None, 'num_acm_papers_considered': 0}, 'var_call_XtWWLN8dMLbtU9XrALfuOBUX': 'file_storage/call_XtWWLN8dMLbtU9XrALfuOBUX.json'}

exec(code, env_args)
