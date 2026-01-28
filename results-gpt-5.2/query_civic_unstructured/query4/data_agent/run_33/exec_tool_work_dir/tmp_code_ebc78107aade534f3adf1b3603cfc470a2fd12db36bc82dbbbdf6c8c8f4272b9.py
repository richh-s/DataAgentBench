code = """import json, re, pandas as pd

# load funding aggregated
funding_src = var_call_Fo6sRnoivg5KAI728SwLRLqD
if isinstance(funding_src, str) and funding_src.endswith('.json'):
    with open(funding_src,'r',encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = funding_src

# load civic docs
civic_src = var_call_pPdtFx212Fr122zoatWud929
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    with open(civic_src,'r',encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

project_names = [r['Project_Name'] for r in funding]

# helper: determine if project started in Spring 2022 based on text near 'Project Schedule'/'Begin' lines
spring_re = re.compile(r"\bSpring\s*[, ]*2022\b", re.IGNORECASE)

def started_spring_2022(text, pname):
    # find occurrences of pname and check a window after it for begin/start construction or schedule lines with Spring 2022
    for m in re.finditer(re.escape(pname), text):
        window = text[m.start(): m.start()+1500]
        if spring_re.search(window):
            # ensure it's tied to begin/start (construction/advertise) if possible
            if re.search(r"\b(Begin|Start)\b.*\b(Spring\s*[, ]*2022)\b", window, re.IGNORECASE):
                return True
            # accept if schedule section contains Spring 2022 and mentions begin construction/start
            if re.search(r"Project Schedule|Estimated Schedule|Schedule", window, re.IGNORECASE) and re.search(r"Begin Construction|Start", window, re.IGNORECASE):
                return True
    return False

started = set()
for doc in civic_docs:
    text = doc.get('text','')
    # quick filter for docs mentioning Spring 2022
    if 'Spring 2022' not in text and 'SPRING 2022' not in text and 'spring 2022' not in text:
        continue
    for pname in project_names:
        if pname in started:
            continue
        if pname in text and started_spring_2022(text, pname):
            started.add(pname)

# Sum funding for these started projects
funding_map = {r['Project_Name']: int(r['total_amount']) for r in funding}
count = len(started)
total = sum(funding_map.get(p,0) for p in started)

out = {"projects_started_spring_2022": count, "total_funding": total, "project_names": sorted(started)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_xDJtFUKt5EMdP9katRSsc5nH': 'file_storage/call_xDJtFUKt5EMdP9katRSsc5nH.json', 'var_call_Fo6sRnoivg5KAI728SwLRLqD': 'file_storage/call_Fo6sRnoivg5KAI728SwLRLqD.json', 'var_call_pPdtFx212Fr122zoatWud929': 'file_storage/call_pPdtFx212Fr122zoatWud929.json'}

exec(code, env_args)
