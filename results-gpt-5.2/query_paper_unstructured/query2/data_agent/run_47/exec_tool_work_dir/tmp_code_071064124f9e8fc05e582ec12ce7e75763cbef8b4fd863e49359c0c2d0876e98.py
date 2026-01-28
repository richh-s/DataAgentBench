code = """import json, re
import pandas as pd

# Load citations 2018 (may be in file)
cit = var_call_YEbrbbUT5z1umTWg3q9uYJuZ
if isinstance(cit, str):
    with open(cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)

papers = var_call_aPDlcR6AAmmLM0L70NLjBlaU
if isinstance(papers, str):
    with open(papers, 'r', encoding='utf-8') as f:
        papers = json.load(f)

cit_df = pd.DataFrame(cit)
if cit_df.empty:
    avg = None
else:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce')

# Build map title -> is_acm based on text containing ACM copyright / ACM
acm_titles = set()
for d in papers:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    # Heuristic for ACM: presence of "© ACM" or "Copyright" with ACM or "ACM" venue header
    if re.search(r'©\s*ACM|\bACM\b', text):
        acm_titles.add(title)

acm_cit_df = cit_df[cit_df['title'].isin(acm_titles)].copy()
avg = float(acm_cit_df['citation_count'].mean()) if not acm_cit_df.empty else None
out = {
    "citation_year": 2018,
    "publisher": "ACM",
    "average_citation_count": avg,
    "num_papers_matched": int(acm_cit_df['title'].nunique()) if not acm_cit_df.empty else 0,
    "num_citation_records_matched": int(len(acm_cit_df))
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YEbrbbUT5z1umTWg3q9uYJuZ': 'file_storage/call_YEbrbbUT5z1umTWg3q9uYJuZ.json', 'var_call_aPDlcR6AAmmLM0L70NLjBlaU': 'file_storage/call_aPDlcR6AAmmLM0L70NLjBlaU.json'}

exec(code, env_args)
