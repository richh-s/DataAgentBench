code = """import json, re
import pandas as pd

def load_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

cit = load_result(var_call_716txXTTK91v7II6hqFJ85pn)
docs = load_result(var_call_cphjc5O0IOLxmsCEA7Ano7hV)

cit_df = pd.DataFrame(cit)
# normalize counts to int
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# build title->is_CHI mapping from docs
chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$', '', fn)
    text = d.get('text','') or ''
    if re.search(r'\bCHI\b', text, flags=re.IGNORECASE):
        # reduce false positives by looking for common proceedings markers
        if re.search(r"\bCHI\b\s*'?\d{2}|CHI\s*\d{4}|Proceedings of the SIGCHI|SIGCHI Conference", text, flags=re.IGNORECASE):
            chi_titles.add(title)

chi_cit_df = cit_df[cit_df['title'].isin(chi_titles)].copy()

out = {
    'citation_year': 2020,
    'num_chi_papers_cited_in_2020': int(chi_cit_df['title'].nunique()),
    'total_citations_2020_for_chi_papers': int(chi_cit_df['citation_count'].sum())
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_716txXTTK91v7II6hqFJ85pn': 'file_storage/call_716txXTTK91v7II6hqFJ85pn.json', 'var_call_cphjc5O0IOLxmsCEA7Ano7hV': 'file_storage/call_cphjc5O0IOLxmsCEA7Ano7hV.json'}

exec(code, env_args)
