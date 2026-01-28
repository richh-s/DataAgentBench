code = """import json
import pandas as pd

with open(var_call_zzK7bHkUDPkIkcg5doQqoM3J, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_9CZg5hl05BZC3LJ77dMjEb4k, 'r', encoding='utf-8') as f:
    papers = json.load(f)

df_cit = pd.DataFrame(citations)
df_pap = pd.DataFrame(papers)

df_cit['citation_count'] = pd.to_numeric(df_cit.get('citation_count', 0), errors='coerce').fillna(0).astype(int)

df_pap['title'] = df_pap['filename'].str.replace(r"\.txt$", '', regex=True)

df_merged = pd.merge(df_cit, df_pap[['title', 'text']], on='title', how='left')

# check counts
total_citations = len(df_cit)
total_papers = len(df_pap)
matched = df_merged['text'].notna().sum()
unmatched = df_merged['text'].isna().sum()

# detect 'ACM' presence
# use several variants: 'ACM', '© ACM', 'ACM' word boundary
import re

def contains_acm(s):
    if not isinstance(s, str):
        return False
    return bool(re.search(r"\bACM\b", s, flags=re.IGNORECASE)) or ('© ACM' in s) or ('\u00a9 ACM' in s)

df_merged['is_acm'] = df_merged['text'].apply(contains_acm)
acm_count = int(df_merged['is_acm'].sum())

# show samples
samples = []
for _, row in df_merged[df_merged['text'].notna()].head(10).iterrows():
    txt = row['text']
    snippet = txt[:200].replace('\n', '\\n')
    samples.append({'title': row['title'], 'citation_count': int(row['citation_count']), 'is_acm': bool(row['is_acm']), 'text_snippet': snippet})

result = {
    'total_citations_rows': int(total_citations),
    'total_paper_docs': int(total_papers),
    'matched_rows_with_text': int(matched),
    'unmatched_rows': int(unmatched),
    'acm_count_in_matched': acm_count,
    'sample_matched_rows': samples
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_DeTvufNC96JvlW2cJS5cVew7': ['paper_docs'], 'var_call_NLpSfxNXV8s4NEdNNZxjZu5X': ['Citations', 'sqlite_sequence'], 'var_call_zzK7bHkUDPkIkcg5doQqoM3J': 'file_storage/call_zzK7bHkUDPkIkcg5doQqoM3J.json', 'var_call_9CZg5hl05BZC3LJ77dMjEb4k': 'file_storage/call_9CZg5hl05BZC3LJ77dMjEb4k.json', 'var_call_CC5DmtI1pHkPuxfd41fnz36J': {'average_citation_count': None, 'num_papers_considered': 0}}

exec(code, env_args)
