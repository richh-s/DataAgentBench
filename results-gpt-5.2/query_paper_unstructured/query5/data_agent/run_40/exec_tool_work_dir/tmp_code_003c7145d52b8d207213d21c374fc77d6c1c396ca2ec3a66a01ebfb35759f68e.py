code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

cit = load_records(var_call_0hvZYWNzDy3iqrylut7ycEik)
docs = load_records(var_call_UaE8dgtnbDsQe1W7LMuL6zgu)

cit_df = pd.DataFrame(cit)
# normalize types
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# build set of CHI titles from docs by detecting venue in text
chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = (d.get('text') or '')
    if re.search(r'\bCHI\b\s*(?:\’|\'|)\d{2}', text):
        chi_titles.add(title)
    elif re.search(r'\bCHI\s*\d{4}\b', text):
        chi_titles.add(title)
    elif re.search(r'\b(?:Proceedings of the )?SIGCHI\b', text, flags=re.IGNORECASE):
        chi_titles.add(title)
    elif re.search(r'\bCHI\s*\'?\d{2}\b', text):
        chi_titles.add(title)

# filter citations to CHI titles and sum total
chi_cit_df = cit_df[cit_df['title'].isin(chi_titles)].copy()

total_citations = int(chi_cit_df['citation_count'].sum())

out = {
    "total_citations_2020_for_CHI_papers": total_citations,
    "num_CHI_papers_cited_in_2020": int(chi_cit_df['title'].nunique()),
    "note": "CHI papers identified by regex matches for CHI/SIGCHI in full text; joined to 2020 citation records by title==filename minus .txt"
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0hvZYWNzDy3iqrylut7ycEik': 'file_storage/call_0hvZYWNzDy3iqrylut7ycEik.json', 'var_call_UaE8dgtnbDsQe1W7LMuL6zgu': 'file_storage/call_UaE8dgtnbDsQe1W7LMuL6zgu.json'}

exec(code, env_args)
