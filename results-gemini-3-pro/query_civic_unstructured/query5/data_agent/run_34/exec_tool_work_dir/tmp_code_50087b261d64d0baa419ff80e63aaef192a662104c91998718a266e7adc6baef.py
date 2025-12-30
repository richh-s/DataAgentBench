code = """import json
import pandas as pd
import re

fp = locals()['var_function-call-6570500424665690713']
dp = locals()['var_function-call-6570500424665692862']

with open(fp, 'r') as f:
    fd = json.load(f)
with open(dp, 'r') as f:
    cd = json.load(f)

projs = []
# Manual escape for regex
pat = re.compile("Begin [cC]onstruction:\\s*([A-Za-z0-9\\s]+)")

for d in cd:
    lns = [x.strip() for x in d['text'].split('\n') if x.strip()]
    curr = 'Unknown'
    for i, l in enumerate(lns):
        if 'Capital Improvement Projects' in l:
            curr = 'Capital'
        elif 'Disaster Recovery Projects' in l:
            curr = 'Disaster'
        
        if 'Updates:' in l or 'Project Description:' in l:
            if i > 0:
                name = lns[i-1]
                # Filter out obvious non-names
                if 'Projects' in name or 'Agenda' in name or 'Page' in name:
                    continue
                
                # Context
                ctx = " ".join(lns[i:i+30])
                m = pat.search(ctx)
                sd = m.group(1).strip() if m else "Unknown"
                
                typ = curr
                if 'FEMA' in name or 'CalOES' in name:
                    typ = 'Disaster'
                
                projs.append({"n": name, "t": typ, "d": sd})

# Filter
tgs = [p["n"] for p in projs if p["t"] == "Disaster" and "2022" in p["d"]]
tgs = list(set(tgs))

df = pd.DataFrame(fd)
df['Amount'] = pd.to_numeric(df['Amount'])
res = df[df['Project_Name'].isin(tgs)]['Amount'].sum()

print("__RESULT__:")
print(json.dumps({"total": int(res), "list": tgs}))"""

env_args = {'var_function-call-2007247411734305584': ['Funding'], 'var_function-call-2007247411734305063': ['civic_docs'], 'var_function-call-6570500424665690713': 'file_storage/function-call-6570500424665690713.json', 'var_function-call-6570500424665692862': 'file_storage/function-call-6570500424665692862.json'}

exec(code, env_args)
