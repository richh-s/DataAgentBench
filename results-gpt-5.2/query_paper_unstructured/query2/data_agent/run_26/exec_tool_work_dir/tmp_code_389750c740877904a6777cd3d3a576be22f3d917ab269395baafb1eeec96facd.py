code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

cit = load_records(var_call_0ecFVkNX2C78cA9MebSVxgQM)
docs = load_records(var_call_v8x3yy7rrDvWYpib5dHKAn0B)

cit_df = pd.DataFrame(cit)
# ensure numeric
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce')

# Build title->is_acm from docs by checking for ACM in text/copyright/permission
acm_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','',fn)
    text = d.get('text','') or ''
    if re.search(r'\bACM\b', text) or re.search(r'Association for Computing Machinery', text, re.I) or re.search(r'permissions@acm\.org', text, re.I):
        acm_titles.add(title)

acm_cit_df = cit_df[cit_df['title'].isin(acm_titles)].copy()

avg_val = float(acm_cit_df['citation_count'].mean()) if len(acm_cit_df) else None
out = {
    "average_citation_count_2018_acm": avg_val,
    "num_acm_papers_matched": int(len(acm_cit_df)),
    "num_total_papers_with_citations_2018": int(len(cit_df))
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0ecFVkNX2C78cA9MebSVxgQM': 'file_storage/call_0ecFVkNX2C78cA9MebSVxgQM.json', 'var_call_v8x3yy7rrDvWYpib5dHKAn0B': 'file_storage/call_v8x3yy7rrDvWYpib5dHKAn0B.json'}

exec(code, env_args)
