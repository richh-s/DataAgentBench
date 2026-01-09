code = """import json, re
import pandas as pd

docs_path = var_call_ftuRxiadPw8NoTU53pyMvgnL
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

df_docs = pd.DataFrame(docs)

# quick venue counts by detecting common venue strings in first 2000 chars
venues = ['CHI','CSCW','UBICOMP','UbiComp','DIS','PervasiveHealth','IUI','WWW','OzCHI','TEI','AH']

def detect_venue(text):
    if not isinstance(text, str):
        return None
    s = text[:3000]
    for v in venues:
        if re.search(r'\b'+re.escape(v)+r'\b', s):
            return v
    return None

df_docs['venue_guess'] = df_docs['text'].map(detect_venue)
counts = df_docs['venue_guess'].value_counts(dropna=False).head(20).to_dict()

print('__RESULT__:')
print(json.dumps(counts, ensure_ascii=False))"""

env_args = {'var_call_S9eV44n31jNAPxIgpaspiHF6': 'file_storage/call_S9eV44n31jNAPxIgpaspiHF6.json', 'var_call_ftuRxiadPw8NoTU53pyMvgnL': 'file_storage/call_ftuRxiadPw8NoTU53pyMvgnL.json', 'var_call_wXfBywdkUQjFGY95yERMt5AM': {'total_citations_2020_for_CHI_papers': 0, 'num_CHI_papers_with_citations_in_2020': 0, 'per_paper_citations_2020': []}}

exec(code, env_args)
