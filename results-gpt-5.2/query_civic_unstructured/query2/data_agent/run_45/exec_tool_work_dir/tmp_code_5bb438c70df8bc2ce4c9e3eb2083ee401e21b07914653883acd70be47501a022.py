code = """import json, pathlib, re

obj = var_call_dxEi22kLvq8oSeo1t8m5SSHb
if isinstance(obj, str):
    docs = json.loads(pathlib.Path(obj).read_text())
else:
    docs = obj

completed_park_projects=set()

for rec in docs:
    text = rec.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.search(r'\bPark\b', line, flags=re.I):
            if re.search(r'Updates:|Project Description:|Estimated Schedule:|Project Schedule:', line, flags=re.I):
                continue
            name = line.strip()
            if len(name) < 5 or len(name) > 120:
                continue
            window = "\n".join(lines[i:i+15])
            if re.search(r'\b(completed|accepted)\b', window, flags=re.I) and re.search(r'\b2022\b', window):
                completed_park_projects.add(name)

print('__RESULT__:')
print(json.dumps(sorted(completed_park_projects)))"""

env_args = {'var_call_tEb2QUBsxnJuTQFmoMn6ttnX': ['Funding'], 'var_call_iIVaQT6kP5WyVCoQ1lJTuaP0': ['civic_docs'], 'var_call_HBmVCfCZr2ZNgGuyYKXf7Yf3': 'file_storage/call_HBmVCfCZr2ZNgGuyYKXf7Yf3.json', 'var_call_dxEi22kLvq8oSeo1t8m5SSHb': 'file_storage/call_dxEi22kLvq8oSeo1t8m5SSHb.json', 'var_call_wcH0G5gICzozKFOzOjxZV2v5': 'file_storage/call_wcH0G5gICzozKFOzOjxZV2v5.json'}

exec(code, env_args)
