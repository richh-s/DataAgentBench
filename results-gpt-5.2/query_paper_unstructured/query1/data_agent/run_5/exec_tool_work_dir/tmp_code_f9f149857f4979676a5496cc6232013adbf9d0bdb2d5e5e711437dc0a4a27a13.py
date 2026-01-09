code = """import json, re

# load full docs
paper_src = var_call_qcgrcWz2ch5uSdwJGAIgjAOs
if isinstance(paper_src, str) and paper_src.endswith('.json'):
    with open(paper_src, 'r', encoding='utf-8') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_src

cit_src = var_call_BLXzIIiiRKVAkMbcS5KNzqhC
if isinstance(cit_src, str) and cit_src.endswith('.json'):
    with open(cit_src, 'r', encoding='utf-8') as f:
        cit_rows = json.load(f)
else:
    cit_rows = cit_src

# food detection substring
pat = re.compile(r'food', re.IGNORECASE)
food_titles=set()
for d in paper_docs:
    if pat.search(d.get('text','') or ''):
        fn=d.get('filename','') or ''
        title = fn[:-4] if fn.lower().endswith('.txt') else fn
        food_titles.add(title)

# sum citations for those titles
cit_sum=0
match_rows=0
for r in cit_rows:
    if r.get('title') in food_titles:
        try:
            cit_sum += int(r.get('citation_count') or 0)
            match_rows += 1
        except Exception:
            pass

print('__RESULT__:')
print(json.dumps({'food_papers': len(food_titles), 'matched_citation_rows': match_rows, 'total_citation_count': cit_sum}))"""

env_args = {'var_call_qlij76grcCeuq92SF3OyvQaK': 'file_storage/call_qlij76grcCeuq92SF3OyvQaK.json', 'var_call_BLXzIIiiRKVAkMbcS5KNzqhC': 'file_storage/call_BLXzIIiiRKVAkMbcS5KNzqhC.json', 'var_call_rAwBrbTILgcpD5rfVWamikis': {'total_citation_count_food_domain': 0, 'food_paper_count': 0}, 'var_call_Xlb5LHiHoJTfh7q0QqMfvhQP': 'file_storage/call_Xlb5LHiHoJTfh7q0QqMfvhQP.json', 'var_call_wOJLNRygSDAaJuAlS58Oze34': {'docs_total': 5, 'docs_with_food_substring': 3, 'docs_with_food_word': 0}, 'var_call_qcgrcWz2ch5uSdwJGAIgjAOs': 'file_storage/call_qcgrcWz2ch5uSdwJGAIgjAOs.json'}

exec(code, env_args)
