code = """import json
import re

with open(locals()['var_function-call-7586214257055398583'], 'r') as f:
    citations = json.load(f)
with open(locals()['var_function-call-16114964338052687681'], 'r') as f:
    paper_docs = json.load(f)
paper_map = {doc['filename']: doc['text'] for doc in paper_docs}

candidates = []

for cit in citations:
    title = cit['title']
    fname = title + ".txt"
    if fname in paper_map:
        text = paper_map[fname][:2000]
        # Look for CHI
        if "CHI" in text:
             candidates.append({"title": title, "snippet": text[:200]})

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-7586214257055398583': 'file_storage/function-call-7586214257055398583.json', 'var_function-call-979778011189952116': 'Sundroid: Solar Radiation Awareness with Smartphones', 'var_function-call-8522392465021198661': 'file_storage/function-call-8522392465021198661.json', 'var_function-call-7603458929060210194': 'file_storage/function-call-7603458929060210194.json', 'var_function-call-16114964338052687681': 'file_storage/function-call-16114964338052687681.json', 'var_function-call-11680504835106074828': 114, 'var_function-call-2209278332186281583': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': '16', 'match': 'CHI 2019'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'count': '98', 'match': 'CHI 2018'}]}

exec(code, env_args)
