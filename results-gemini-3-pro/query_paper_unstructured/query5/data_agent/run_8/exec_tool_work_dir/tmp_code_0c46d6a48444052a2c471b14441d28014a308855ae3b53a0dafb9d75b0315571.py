code = """import json
import re

with open(locals()['var_function-call-4961661729464848456'], 'r') as f:
    citations = json.load(f)
citation_map = {c['title']: int(c['citation_count']) for c in citations}

with open(locals()['var_function-call-14263536467630025147'], 'r') as f:
    papers = json.load(f)

results = []
for paper in papers:
    title = paper.get('filename', '')[:-4]
    if title in citation_map:
        text = paper.get('text', '')
        # Check specific phrase
        if "Conference on Human Factors in Computing Systems" in text:
             results.append({"title": title, "match": "Full Name"})
        elif re.search(r'CHI \d{4}', text):
             results.append({"title": title, "match": "CHI Year"})
        elif re.search(r'\bCHI\b', text):
             results.append({"title": title, "match": "CHI word"})

print(f"Found {len(results)} matches.")
print("__RESULT__:")
print(json.dumps(results[:5]))"""

env_args = {'var_function-call-4961661729464848456': 'file_storage/function-call-4961661729464848456.json', 'var_function-call-4306319526809017372': 188, 'var_function-call-9160616424066584020': 'file_storage/function-call-9160616424066584020.json', 'var_function-call-16237189493323066997': 5, 'var_function-call-14263536467630025147': 'file_storage/function-call-14263536467630025147.json', 'var_function-call-95742628409748684': 1551, 'var_function-call-6733428787577609903': 16, 'var_function-call-17501030019706782583': {'total': 16, 'papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 16}]}, 'var_function-call-5225444022116205832': []}

exec(code, env_args)
