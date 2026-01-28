code = """import json
import re

with open(locals()['var_function-call-9485982252767693581'], 'r') as f:
    citations = json.load(f)

with open(locals()['var_function-call-18114231173969465501'], 'r') as f:
    papers = json.load(f)

citation_map = {c['title']: c['citation_count'] for c in citations}

titles_in_db = set()
paper_map = {}
for paper in papers:
    fn = paper.get('filename', '')
    if fn.endswith('.txt'):
        t = fn[:-4]
        titles_in_db.add(t)
        paper_map[t] = paper

common_titles = set(citation_map.keys()).intersection(titles_in_db)

samples = []
for t in list(common_titles)[:5]:
    text = paper_map[t].get('text', '')[:500]
    samples.append({"title": t, "snippet": text})

result = {
    "common_titles_count": len(common_titles),
    "samples": samples
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9485982252767693581': 'file_storage/function-call-9485982252767693581.json', 'var_function-call-9485982252767692568': 'file_storage/function-call-9485982252767692568.json', 'var_function-call-2245160326568444986': 188, 'var_function-call-11048170535639833603': 'file_storage/function-call-11048170535639833603.json', 'var_function-call-18114231173969465501': 'file_storage/function-call-18114231173969465501.json', 'var_function-call-12581163801840341244': 0}

exec(code, env_args)
