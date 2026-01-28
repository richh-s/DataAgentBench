code = """import json

p1 = locals()["var_function-call-5247396609485473632"]
p2 = locals()["var_function-call-633765740054289148"]

with open(p1, "r") as f:
    fd = json.load(f)

t_names = set()
for i in fd:
    if float(i["Amount"]) > 50000:
        t_names.add(i["Project_Name"].strip().lower())

with open(p2, "r") as f:
    dl = json.load(f)

res = set()
for d in dl:
    lines = d["text"].splitlines()
    mode = 0
    for l in lines:
        lc = l.strip().lower()
        if not lc: continue
        
        if "capital improvement projects (design)" in lc:
            mode = 1
            continue
        if "capital improvement projects" in lc and "(design)" not in lc:
            mode = 0
            continue
        if "disaster recovery projects" in lc:
            mode = 0
            continue
            
        if mode == 1:
            if lc in t_names:
                res.add(lc)

print("__RESULT__:")
print(json.dumps(list(res)))"""

env_args = {'var_function-call-5247396609485473632': 'file_storage/function-call-5247396609485473632.json', 'var_function-call-633765740054289148': 'file_storage/function-call-633765740054289148.json'}

exec(code, env_args)
