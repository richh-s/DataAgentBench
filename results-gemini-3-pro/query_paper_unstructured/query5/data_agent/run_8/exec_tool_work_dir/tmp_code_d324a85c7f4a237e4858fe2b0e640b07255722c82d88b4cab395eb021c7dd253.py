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
        # Full text search
        match = re.search(r'\bCHI\b', text)
        if match:
            start = match.start()
            context = text[max(0, start-50):min(len(text), start+50)].replace('\n', ' ')
            results.append({
                "title": title,
                "index": start,
                "context": context
            })

print("__RESULT__:")
print(json.dumps(results[:5]))"""

env_args = {'var_function-call-4961661729464848456': 'file_storage/function-call-4961661729464848456.json', 'var_function-call-4306319526809017372': 188, 'var_function-call-9160616424066584020': 'file_storage/function-call-9160616424066584020.json', 'var_function-call-16237189493323066997': 5, 'var_function-call-14263536467630025147': 'file_storage/function-call-14263536467630025147.json', 'var_function-call-95742628409748684': 1551, 'var_function-call-6733428787577609903': 16, 'var_function-call-17501030019706782583': {'total': 16, 'papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 16}]}}

exec(code, env_args)
