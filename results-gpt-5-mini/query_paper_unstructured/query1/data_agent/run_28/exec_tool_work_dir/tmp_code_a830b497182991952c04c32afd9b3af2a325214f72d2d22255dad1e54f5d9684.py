code = """import json
# load the same files to inspect sample titles and matches
with open(var_call_xgfwqQgmQYB90Agv1Y9V1ATM, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_5QUzNaplD2axIQspTd16liMY, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build maps
titles = [d['filename'].replace('.txt','') for d in docs]
# Find docs that mention 'food'
food_docs = [d for d in docs if 'food' in d.get('text','').lower()]
food_titles = [d['filename'].replace('.txt','') for d in food_docs]

# Check which food_titles are present in citations
cit_titles = [c['title'] for c in citations]
matched = [t for t in food_titles if t in cit_titles]

result = {
    'num_docs': len(docs),
    'num_citations_records': len(citations),
    'num_food_docs': len(food_docs),
    'sample_food_titles': food_titles[:20],
    'matched_food_titles_in_citations': matched[:20]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_XjVBNCkepLGgO8Cu2OgcQVth': ['paper_docs'], 'var_call_xgfwqQgmQYB90Agv1Y9V1ATM': 'file_storage/call_xgfwqQgmQYB90Agv1Y9V1ATM.json', 'var_call_qPIPGT34vscwC1oFP3m55bwO': ['Citations', 'sqlite_sequence'], 'var_call_5QUzNaplD2axIQspTd16liMY': 'file_storage/call_5QUzNaplD2axIQspTd16liMY.json', 'var_call_pCfCVKuObEE6Dc1yNFWs13MD': {'food_domain_total_citations': 0}}

exec(code, env_args)
