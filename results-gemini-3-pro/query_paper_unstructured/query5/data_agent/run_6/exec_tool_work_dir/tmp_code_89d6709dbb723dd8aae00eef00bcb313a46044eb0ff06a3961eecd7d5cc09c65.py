code = """import json
import re

with open(locals()['var_function-call-9485982252767693581'], 'r') as f:
    citations = json.load(f)

with open(locals()['var_function-call-18114231173969465501'], 'r') as f:
    papers = json.load(f)

citation_map = {c['title']: c['citation_count'] for c in citations}

titles_in_db = set()
for paper in papers:
    fn = paper.get('filename', '')
    if fn.endswith('.txt'):
        titles_in_db.add(fn[:-4])

common_titles = set(citation_map.keys()).intersection(titles_in_db)
print(f"Number of common titles: {len(common_titles)}")

# Print snippets for a few common papers
sample_count = 0
for paper in papers:
    fn = paper.get('filename', '')
    title = fn[:-4] if fn.endswith('.txt') else fn
    if title in common_titles:
        print(f"--- Paper: {title} ---")
        print(paper.get('text', '')[:300])
        sample_count += 1
        if sample_count >= 5:
            break

print("__RESULT__:")
print("Done")"""

env_args = {'var_function-call-9485982252767693581': 'file_storage/function-call-9485982252767693581.json', 'var_function-call-9485982252767692568': 'file_storage/function-call-9485982252767692568.json', 'var_function-call-2245160326568444986': 188, 'var_function-call-11048170535639833603': 'file_storage/function-call-11048170535639833603.json', 'var_function-call-18114231173969465501': 'file_storage/function-call-18114231173969465501.json', 'var_function-call-12581163801840341244': 0}

exec(code, env_args)
