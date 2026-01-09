code = """import json, re, pandas as pd

papers_path = var_call_B7Nd9ZV7ZXGO00IJwzlralmQ
with open(papers_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)
df_p = pd.DataFrame(papers)
head = df_p.loc[0,'text'][:300]
# quick scan counts of substring 'CHI 20'
count = sum(('CHI 20' in (t[:10000] if isinstance(t,str) else '')) for t in df_p['text'])
count2 = sum((re.search(r'CHI\s*20\d\d', (t[:12000] if isinstance(t,str) else ''), flags=re.I) is not None) for t in df_p['text'])
print('__RESULT__:')
print(json.dumps({'sample_head': head, 'contains_CHI_20_literal_count': int(count), 'regex_CHI_20yy_count': int(count2), 'num_docs': int(len(df_p))}))"""

env_args = {'var_call_hBMNtLT3jpsx8aDxz65hoYIP': 'file_storage/call_hBMNtLT3jpsx8aDxz65hoYIP.json', 'var_call_B7Nd9ZV7ZXGO00IJwzlralmQ': 'file_storage/call_B7Nd9ZV7ZXGO00IJwzlralmQ.json', 'var_call_dDvhD8Tl8825uM3qly4gYxpH': {'total_citations_2020_for_CHI_papers': 0, 'num_chi_papers_with_citations_in_2020': 0, 'num_citation_records_matched': 0}, 'var_call_UewTKYCOPDUwqVlGsi9JL9zk': 'file_storage/call_UewTKYCOPDUwqVlGsi9JL9zk.json', 'var_call_orCEe0SYk7MYRvGNjFPr46f4': {'total_citations_2020_for_CHI_papers': 0, 'num_chi_papers_with_citations_in_2020': 0, 'num_chi_papers_in_docs': 0}}

exec(code, env_args)
