code = """import json, re

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_0f7yDI4ecmLKSKpoaVFu2vZD)

# find occurrences of 'Spring 2022' with spaces/newlines variants
pat = re.compile(r"Spring\s*[,\-]?\s*2022", re.IGNORECASE)
count=0
samples=[]
for d in docs:
    text=str(d.get('text',''))
    m = pat.search(text)
    if m:
        count += 1
        if len(samples)<5:
            start=max(0,m.start()-80); end=min(len(text), m.end()+80)
            samples.append(text[start:end].replace('\n','\\n'))
print('__RESULT__:')
print(json.dumps({'docs_with_spring2022':count,'samples':samples}))"""

env_args = {'var_call_0f7yDI4ecmLKSKpoaVFu2vZD': 'file_storage/call_0f7yDI4ecmLKSKpoaVFu2vZD.json', 'var_call_27VpEJXZf7UZvZlIuZtK2xrL': 'file_storage/call_27VpEJXZf7UZvZlIuZtK2xrL.json', 'var_call_WYLUmmwObGXwduLEEijbEoV5': {'spring_2022_project_count': 0, 'spring_2022_total_funding_matched': 0, 'matched_project_count': 0, 'missing_funding_project_count': 0, 'missing_projects_sample': []}, 'var_call_XLDXr8FDGIphVyw4C4Q3qfWR': {'line_hits': 0, 'samples': []}}

exec(code, env_args)
