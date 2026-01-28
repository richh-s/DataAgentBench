code = """import json
import pandas as pd

p_c = locals()['var_function-call-956811650377216769']
p_f = locals()['var_function-call-956811650377216698']

with open(p_c, 'r') as f: docs = json.load(f)
with open(p_f, 'r') as f: funds = json.load(f)

names = set()
newline = chr(10)
for d in docs:
    lines = d.get("text", "").split(newline)
    for i, l in enumerate(lines):
        if "Updates:" in l or "Project Description:" in l:
            name = ""
            for j in range(i-1, -1, -1):
                s = lines[j].strip()
                if s and "Page" not in s and "Agenda" not in s and "Capital" not in s:
                    name = s
                    break
            
            if not name: continue
            
            for k in range(i, min(i+20, len(lines))):
                sub = lines[k]
                if k > i and ("Updates:" in sub or "Project Description:" in sub): break
                
                # Check for Start/Begin Construction
                if "Begin Construction" in sub or "Start Construction" in sub:
                    # Check for Spring 2022 loosely
                    if "2022" in sub:
                        if "Spring" in sub or "March" in sub or "April" in sub or "May" in sub:
                            names.add(name)

df = pd.DataFrame(funds)
res = df[df["Project_Name"].isin(names)]
print("__RESULT__:")
print(json.dumps({
    "count": len(res), 
    "total": res["Amount"].astype(float).sum(),
    "projects": res["Project_Name"].tolist()
}))"""

env_args = {'var_function-call-956811650377216769': 'file_storage/function-call-956811650377216769.json', 'var_function-call-956811650377216698': 'file_storage/function-call-956811650377216698.json', 'var_function-call-13847589957581412543': {'count': 8, 'total': 492000.0}}

exec(code, env_args)
