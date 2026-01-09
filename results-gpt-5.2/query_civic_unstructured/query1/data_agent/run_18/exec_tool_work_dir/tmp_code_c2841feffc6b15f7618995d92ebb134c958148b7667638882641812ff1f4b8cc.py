code = """import json, re

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

funding = load_records(var_call_uNEWWIgoazl4OEa45raLQHJF)
docs = load_records(var_call_EoYnjBLEIy4e8ssN5tTokANC)

funding_names = sorted({r.get('Project_Name') for r in funding if r.get('Project_Name')})
full_text = "\n".join(d.get('text','') for d in docs)


def is_design_in_docs(name):
    n = re.escape(name)
    p1 = 'Capital Improvement Projects \\(Design\\)[\\s\\S]{0,5000}\\b' + n + '\\b'
    p2 = '\\b' + n + '\\b[\\s\\S]{0,200}\\(Design\\)'
    p3 = '\\(Design\\)[\\s\\S]{0,200}\\b' + n + '\\b'
    for p in (p1,p2,p3):
        if re.search(p, full_text, flags=re.IGNORECASE):
            return True
    return False

matched = [nm for nm in funding_names if is_design_in_docs(nm)]

print('__RESULT__:')
print(json.dumps({'count': len(matched)}))"""

env_args = {'var_call_FzQfpdMuis5pWlSBX6WBYRDU': ['Funding'], 'var_call_LPLFPLfnq4ss3HNzr908cp14': ['civic_docs'], 'var_call_uNEWWIgoazl4OEa45raLQHJF': 'file_storage/call_uNEWWIgoazl4OEa45raLQHJF.json', 'var_call_EoYnjBLEIy4e8ssN5tTokANC': 'file_storage/call_EoYnjBLEIy4e8ssN5tTokANC.json'}

exec(code, env_args)
