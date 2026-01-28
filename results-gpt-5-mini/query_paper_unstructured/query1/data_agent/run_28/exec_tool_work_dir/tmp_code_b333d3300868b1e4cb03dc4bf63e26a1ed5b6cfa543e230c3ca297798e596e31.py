code = """import json
with open(var_call_xgfwqQgmQYB90Agv1Y9V1ATM, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_5QUzNaplD2axIQspTd16liMY, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Extract food-related titles
food_titles = [d['filename'].replace('.txt','') for d in docs if 'food' in d.get('text','').lower()]

# Build a map of citation totals (from earlier grouped query)
cit_map = {c['title']: int(c['total_citations']) for c in citations}

matched = {t: cit_map.get(t, 0) for t in food_titles}

total = sum(matched.values())

output = json.dumps({"food_titles": food_titles, "matched_citations": matched, "food_domain_total_citations": total})
print('__RESULT__:')
print(output)"""

env_args = {'var_call_XjVBNCkepLGgO8Cu2OgcQVth': ['paper_docs'], 'var_call_xgfwqQgmQYB90Agv1Y9V1ATM': 'file_storage/call_xgfwqQgmQYB90Agv1Y9V1ATM.json', 'var_call_qPIPGT34vscwC1oFP3m55bwO': ['Citations', 'sqlite_sequence'], 'var_call_5QUzNaplD2axIQspTd16liMY': 'file_storage/call_5QUzNaplD2axIQspTd16liMY.json', 'var_call_pCfCVKuObEE6Dc1yNFWs13MD': {'food_domain_total_citations': 0}, 'var_call_XuokttwL8muTGeE4m7KDSLdO': {'num_docs': 5, 'num_citations_records': 259, 'num_food_docs': 3, 'sample_food_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'matched_food_titles_in_citations': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}}

exec(code, env_args)
