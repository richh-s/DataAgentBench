code = """import json
import pandas as pd

with open(var_call_zzK7bHkUDPkIkcg5doQqoM3J, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_9CZg5hl05BZC3LJ77dMjEb4k, 'r', encoding='utf-8') as f:
    papers = json.load(f)

df_cit = pd.DataFrame(citations)
df_pap = pd.DataFrame(papers)

# Normalize citation_count
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)
else:
    df_cit['citation_count'] = 0

# Extract title from filename
if 'filename' in df_pap.columns:
    df_pap['title'] = df_pap['filename'].str.replace(r"\\.txt$", '', regex=True)
else:
    df_pap['title'] = None

# Merge on title
df_merged = pd.merge(df_cit, df_pap[['title', 'text']], on='title', how='left')

# Detect ACM in text using multiple checks
import re

def detect_acm(s):
    if not isinstance(s, str):
        return False
    if re.search(r"\\bACM\\b", s, flags=re.IGNORECASE):
        return True
    if '\u00a9' in s and re.search(r"ACM", s, flags=re.IGNORECASE):
        return True
    if '©' in s and re.search(r"ACM", s, flags=re.IGNORECASE):
        return True
    return False

# Apply detection
df_merged['is_acm'] = df_merged['text'].apply(detect_acm)

# Stats
total_citations = int(len(df_cit))
total_papers = int(len(df_pap))
matched = int(df_merged['text'].notna().sum())
unmatched = int(df_merged['text'].isna().sum())
acm_count = int(df_merged['is_acm'].sum())

# Samples of matched rows
samples = []
for _, row in df_merged[df_merged['text'].notna()].head(20).iterrows():
    txt = row['text']
    snippet = (txt[:200].replace('\n', ' ')) if isinstance(txt, str) else None
    samples.append({'title': row['title'], 'citation_count': int(row['citation_count']), 'is_acm': bool(row['is_acm']), 'text_snippet': snippet})

result = {
    'total_citations_rows': total_citations,
    'total_paper_docs': total_papers,
    'matched_rows_with_text': matched,
    'unmatched_rows': unmatched,
    'acm_count_in_matched': acm_count,
    'sample_matched_rows': samples
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_DeTvufNC96JvlW2cJS5cVew7': ['paper_docs'], 'var_call_NLpSfxNXV8s4NEdNNZxjZu5X': ['Citations', 'sqlite_sequence'], 'var_call_zzK7bHkUDPkIkcg5doQqoM3J': 'file_storage/call_zzK7bHkUDPkIkcg5doQqoM3J.json', 'var_call_9CZg5hl05BZC3LJ77dMjEb4k': 'file_storage/call_9CZg5hl05BZC3LJ77dMjEb4k.json', 'var_call_CC5DmtI1pHkPuxfd41fnz36J': {'average_citation_count': None, 'num_papers_considered': 0}}

exec(code, env_args)
