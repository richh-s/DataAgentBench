code = """import json
import pandas as pd
k1 = "var_function-call-13970698935459151877"
k2 = "var_function-call-13579203068557831030"
f_path = locals()[k1]
d_path = locals()[k2]
with open(f_path, "r") as f: funding = json.load(f)
with open(d_path, "r") as f: docs = json.load(f)
df = pd.DataFrame(funding)
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce").fillna(0)
grp = df.groupby("Project_Name")["Amount"].sum()
funded = set(grp[grp > 50000].index)
design = set()
for d in docs:
    active = False
    for l in d["text"].split("\n"):
        l = l.strip()
        if "Capital Improvement Projects" in l:
            if "Design" in l: active = True
            else: active = False
            continue
        if "Disaster Recovery Projects" in l:
            active = False
            continue
        if active:
            if not l: continue
            if l.startswith("(") or l.startswith("Updates") or l.startswith("Project"): continue
            if l.startswith("Page") or l.startswith("Agenda"): continue
            if l.startswith("Complete") or l.startswith("Advertise") or l.startswith("Begin"): continue
            design.add(l)
matches = design.intersection(funded)
print("__RESULT__:")
print(json.dumps({"count": len(matches), "matches": list(matches)}))"""

env_args = {'var_function-call-13970698935459151877': 'file_storage/function-call-13970698935459151877.json', 'var_function-call-13579203068557831030': 'file_storage/function-call-13579203068557831030.json'}

exec(code, env_args)
