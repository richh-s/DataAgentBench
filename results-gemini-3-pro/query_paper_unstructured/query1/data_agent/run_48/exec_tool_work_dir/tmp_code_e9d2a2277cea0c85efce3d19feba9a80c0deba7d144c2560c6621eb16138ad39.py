code = """import json

with open(locals()['var_function-call-4672195044827894195'], 'r') as f:
    papers = json.load(f)

keywords = ['food', 'eating', 'diet', 'nutrition']
hits = {}

for p in papers:
    text = p.get('text', '').lower()
    title = p.get('filename', '')
    found = [k for k in keywords if k in text]
    if found:
        hits[title] = found

print("__RESULT__:")
print(json.dumps({"total_papers": len(papers), "hits": hits}))"""

env_args = {'var_function-call-13370766090165900916': 'file_storage/function-call-13370766090165900916.json', 'var_function-call-9130405135784485262': 'file_storage/function-call-9130405135784485262.json', 'var_function-call-9265765399726123142': 'file_storage/function-call-9265765399726123142.json', 'var_function-call-4672195044827894195': 'file_storage/function-call-4672195044827894195.json', 'var_function-call-6440888066773927974': 876, 'var_function-call-1546429934820446288': {'count': 0, 'titles': []}, 'var_function-call-16718756574261419614': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt']}

exec(code, env_args)
