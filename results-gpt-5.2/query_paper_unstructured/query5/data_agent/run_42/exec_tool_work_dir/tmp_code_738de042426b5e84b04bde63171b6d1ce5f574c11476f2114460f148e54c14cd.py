code = """import json, pandas as pd

cit_path = var_call_hBMNtLT3jpsx8aDxz65hoYIP
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)

papers_path = var_call_B7Nd9ZV7ZXGO00IJwzlralmQ
with open(papers_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)
df_p = pd.DataFrame(papers)
df_p['title'] = df_p['filename'].str.replace(r'\.txt$','', regex=True)

overlap = set(df_cit['title']).intersection(set(df_p['title']))
# show few examples
ex = sorted(list(overlap))[:20]
print('__RESULT__:')
print(json.dumps({'num_citation_titles_2020': int(df_cit['title'].nunique()), 'num_doc_titles': int(df_p['title'].nunique()), 'overlap_count': int(len(overlap)), 'overlap_examples': ex}))"""

env_args = {'var_call_hBMNtLT3jpsx8aDxz65hoYIP': 'file_storage/call_hBMNtLT3jpsx8aDxz65hoYIP.json', 'var_call_B7Nd9ZV7ZXGO00IJwzlralmQ': 'file_storage/call_B7Nd9ZV7ZXGO00IJwzlralmQ.json', 'var_call_dDvhD8Tl8825uM3qly4gYxpH': {'total_citations_2020_for_CHI_papers': 0, 'num_chi_papers_with_citations_in_2020': 0, 'num_citation_records_matched': 0}, 'var_call_UewTKYCOPDUwqVlGsi9JL9zk': 'file_storage/call_UewTKYCOPDUwqVlGsi9JL9zk.json', 'var_call_orCEe0SYk7MYRvGNjFPr46f4': {'total_citations_2020_for_CHI_papers': 0, 'num_chi_papers_with_citations_in_2020': 0, 'num_chi_papers_in_docs': 0}, 'var_call_CRBDIv3pi16k8kN7jLHyNGDv': {'sample_head': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash", 'contains_CHI_20_literal_count': 43, 'regex_CHI_20yy_count': 43, 'num_docs': 99}, 'var_call_VckDTpIJ3tGhm8ktZRwNK8EZ': {'total_citations_2020_for_CHI_papers': 0, 'num_CHI_papers_cited_in_2020': 0, 'num_CHI_papers_in_docs': 0}}

exec(code, env_args)
