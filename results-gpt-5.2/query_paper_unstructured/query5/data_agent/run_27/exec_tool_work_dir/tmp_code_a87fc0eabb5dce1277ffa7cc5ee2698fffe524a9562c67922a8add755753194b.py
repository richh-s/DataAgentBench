code = """import json, re
import pandas as pd

def load_records(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

cit = load_records(var_call_p2RQmWkMzvuW6aa23YZbC8mo)
docs = load_records(var_call_a8Iy7QA36ZbfyOMfhfzUDIFc)

cit_df = pd.DataFrame(cit)
# normalize citation_count
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# extract title from docs filename
paper_df = pd.DataFrame(docs)
paper_df['title'] = paper_df['filename'].str.replace(r'\.txt$', '', regex=True)

# infer venue from text using regex
venue_re = re.compile(r"\bCHI\s*'\d{2}\b|\bCHI\s*\d{4}\b|\bPROCEEDINGS OF THE SIGCHI\b|\bSIGCHI\b|\bCHI\b")

def is_chi(text):
    if not isinstance(text, str):
        return False
    # require a strong signal: CHI 'YY or SIGCHI proceedings
    if re.search(r"\bCHI\s*'\d{2}\b", text):
        return True
    if re.search(r"PROCEEDINGS OF THE SIGCHI", text, flags=re.IGNORECASE):
        return True
    # fallback: 'CHI' near ACM (to avoid generic chi)
    if re.search(r"\bCHI\b", text) and re.search(r"\bACM\b", text):
        return True
    return False

paper_df['is_chi'] = paper_df['text'].apply(is_chi)
chi_titles = set(paper_df.loc[paper_df['is_chi'], 'title'])

chi_cit_df = cit_df[cit_df['title'].isin(chi_titles)].copy()

# total citation counts across all CHI papers cited in 2020
result = {
    'total_citations_2020_for_CHI_papers': int(chi_cit_df['citation_count'].sum()),
    'num_CHI_papers_cited_in_2020': int(chi_cit_df['title'].nunique())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_p2RQmWkMzvuW6aa23YZbC8mo': 'file_storage/call_p2RQmWkMzvuW6aa23YZbC8mo.json', 'var_call_a8Iy7QA36ZbfyOMfhfzUDIFc': 'file_storage/call_a8Iy7QA36ZbfyOMfhfzUDIFc.json'}

exec(code, env_args)
