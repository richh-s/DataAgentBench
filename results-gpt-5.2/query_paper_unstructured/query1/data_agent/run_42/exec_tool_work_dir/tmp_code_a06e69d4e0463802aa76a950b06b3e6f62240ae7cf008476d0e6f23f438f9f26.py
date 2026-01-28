code = """import json, re
import pandas as pd

# load citations
path = var_call_GFaRgoMWZGQ8aYF3F9XrBEdu
with open(path,'r',encoding='utf-8') as f:
    citations = json.load(f)

# load mongo docs (food mentions) and classify domain=food if metadata says so
mongo_path = var_call_HdjmkiUmSZxfsR4qbye8zVog
with open(mongo_path,'r',encoding='utf-8') as f:
    docs = json.load(f)

food_titles=set()
patterns=[
    re.compile(r'(?im)^\s*domain\s*:\s*.*\bfood\b'),
    re.compile(r'(?im)^\s*domains\s*:\s*.*\bfood\b'),
    re.compile(r'(?im)^\s*research\s*domain\s*:\s*.*\bfood\b'),
]
for d in docs:
    text=d.get('text','')
    if any(p.search(text) for p in patterns):
        fn=d.get('filename','')
        title=fn[:-4] if fn.lower().endswith('.txt') else fn
        food_titles.add(title)

# sum citations for those titles

total=0
for r in citations:
    if r['title'] in food_titles:
        try:
            total += int(r['citation_count'])
        except:
            pass

out=json.dumps({"total_citation_count": total, "num_food_papers": len(food_titles)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_GFaRgoMWZGQ8aYF3F9XrBEdu': 'file_storage/call_GFaRgoMWZGQ8aYF3F9XrBEdu.json', 'var_call_WQ1k5Zwje43RwLI3G9Gmcixu': [], 'var_call_HdjmkiUmSZxfsR4qbye8zVog': 'file_storage/call_HdjmkiUmSZxfsR4qbye8zVog.json'}

exec(code, env_args)
