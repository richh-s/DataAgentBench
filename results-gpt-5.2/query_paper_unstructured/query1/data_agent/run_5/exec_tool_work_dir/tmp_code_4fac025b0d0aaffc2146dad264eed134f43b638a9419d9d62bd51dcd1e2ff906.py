code = """import json, re

paper_src = var_call_qlij76grcCeuq92SF3OyvQaK
if isinstance(paper_src, str) and paper_src.endswith('.json'):
    with open(paper_src, 'r', encoding='utf-8') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_src

# check counts for substring matches
pat_food = re.compile('food', re.IGNORECASE)
pat_word = re.compile(r'\bfood\b', re.IGNORECASE)
count_sub = 0
count_word = 0
for d in paper_docs:
    t = d.get('text','') or ''
    if pat_food.search(t):
        count_sub += 1
    if pat_word.search(t):
        count_word += 1

print('__RESULT__:')
print(json.dumps({'docs_total': len(paper_docs), 'docs_with_food_substring': count_sub, 'docs_with_food_word': count_word}))"""

env_args = {'var_call_qlij76grcCeuq92SF3OyvQaK': 'file_storage/call_qlij76grcCeuq92SF3OyvQaK.json', 'var_call_BLXzIIiiRKVAkMbcS5KNzqhC': 'file_storage/call_BLXzIIiiRKVAkMbcS5KNzqhC.json', 'var_call_rAwBrbTILgcpD5rfVWamikis': {'total_citation_count_food_domain': 0, 'food_paper_count': 0}, 'var_call_Xlb5LHiHoJTfh7q0QqMfvhQP': 'file_storage/call_Xlb5LHiHoJTfh7q0QqMfvhQP.json'}

exec(code, env_args)
