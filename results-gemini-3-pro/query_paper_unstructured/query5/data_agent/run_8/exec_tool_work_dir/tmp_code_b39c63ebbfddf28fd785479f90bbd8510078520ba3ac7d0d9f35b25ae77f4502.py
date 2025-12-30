code = """import json
import re

with open(locals()['var_function-call-4961661729464848456'], 'r') as f:
    citations = json.load(f)

citation_map = {c['title']: int(c['citation_count']) for c in citations}

with open(locals()['var_function-call-14263536467630025147'], 'r') as f:
    papers = json.load(f)

debug_info = []
total = 0

for paper in papers:
    title = paper.get('filename', '')[:-4]
    if title in citation_map:
        text = paper.get('text', '')
        header = text[:2000]
        if re.search(r'\bCHI\b', header) or "Conference on Human Factors in Computing Systems" in header:
            count = citation_map[title]
            debug_info.append({"title": title, "count": count})
            total += count

print(f"Total: {total}")
print("__RESULT__:")
print(json.dumps({"total": total, "papers": debug_info}))"""

env_args = {'var_function-call-4961661729464848456': 'file_storage/function-call-4961661729464848456.json', 'var_function-call-4306319526809017372': 188, 'var_function-call-9160616424066584020': 'file_storage/function-call-9160616424066584020.json', 'var_function-call-16237189493323066997': 5, 'var_function-call-14263536467630025147': 'file_storage/function-call-14263536467630025147.json', 'var_function-call-95742628409748684': 1551, 'var_function-call-6733428787577609903': 16}

exec(code, env_args)
