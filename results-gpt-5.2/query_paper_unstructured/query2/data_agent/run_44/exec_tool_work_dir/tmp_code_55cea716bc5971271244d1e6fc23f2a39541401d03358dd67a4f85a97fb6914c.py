code = """import json, re

cit = var_call_zSgHJoaZqQZUtnQcB0mm6NTI
if isinstance(cit, str):
    with open(cit,'r',encoding='utf-8') as f:
        cit = json.load(f)

docs = var_call_qcuB7G45SlVxG9i3bj36sxYz
if isinstance(docs, str):
    with open(docs,'r',encoding='utf-8') as f:
        docs = json.load(f)

# build map title->is_acm using broader heuristics
acm_titles=set()
for d in docs:
    fn=d.get('filename','')
    title=fn[:-4] if fn.lower().endswith('.txt') else fn
    text=(d.get('text') or '')
    if re.search(r'\bACM\b', text):
        acm_titles.add(title)

cit_titles=set(r.get('title') for r in cit)
inter = list(cit_titles.intersection(acm_titles))

out={"num_docs":len(docs),"num_cit2018":len(cit),"num_acm_docs_broad":len(acm_titles),"intersection":len(inter),"sample_intersection":inter[:20],"sample_cit_titles":list(cit_titles)[:20]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zSgHJoaZqQZUtnQcB0mm6NTI': 'file_storage/call_zSgHJoaZqQZUtnQcB0mm6NTI.json', 'var_call_qcuB7G45SlVxG9i3bj36sxYz': 'file_storage/call_qcuB7G45SlVxG9i3bj36sxYz.json', 'var_call_aUTFjBLjkcJmBNm89MdmCkb7': {'average_citation_count_2018_for_acm_papers': None, 'acm_papers_with_2018_citations_matched': 0}}

exec(code, env_args)
