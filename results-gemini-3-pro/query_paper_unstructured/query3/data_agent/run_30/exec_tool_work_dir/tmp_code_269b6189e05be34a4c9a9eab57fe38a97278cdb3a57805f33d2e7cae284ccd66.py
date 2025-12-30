code = """import json
import re

# Load the papers
with open(locals()['var_function-call-8715248679689147439'], 'r') as f:
    papers = json.load(f)

results = []
for p in papers[:5]:
    text = p['text']
    # Find context for 'contribution'
    c_matches = [m.start() for m in re.finditer(r'contribution', text, re.IGNORECASE)]
    c_contexts = []
    for m in c_matches:
        start = max(0, m - 50)
        end = min(len(text), m + 50)
        s = text[start:end].replace('\n', ' ')
        c_contexts.append(s)
    
    # Find context for 'empirical'
    e_matches = [m.start() for m in re.finditer(r'empirical', text, re.IGNORECASE)]
    e_contexts = []
    for m in e_matches:
        start = max(0, m - 50)
        end = min(len(text), m + 50)
        s = text[start:end].replace('\n', ' ')
        e_contexts.append(s)

    results.append({
        "title": p['filename'], 
        "contribution_contexts": c_contexts,
        "empirical_contexts": e_contexts
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-12710699781919047137': 'file_storage/function-call-12710699781919047137.json', 'var_function-call-4291090424664498879': ['paper_docs'], 'var_function-call-15848114717037089156': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-6799070853489164674': 'file_storage/function-call-6799070853489164674.json', 'var_function-call-17861381846449372899': [], 'var_function-call-2694959544840446415': 'file_storage/function-call-2694959544840446415.json', 'var_function-call-8715248679689147439': 'file_storage/function-call-8715248679689147439.json'}

exec(code, env_args)
