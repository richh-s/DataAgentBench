code = """import json
import pandas as pd

fp = locals()["var_function-call-6570500424665690713"]
dp = locals()["var_function-call-6570500424665692862"]

with open(fp, "r") as f:
    fd = json.load(f)
with open(dp, "r") as f:
    cd = json.load(f)

projects = []
for d in cd:
    lines = d["text"].splitlines()
    curr = "Unknown"
    for i, l in enumerate(lines):
        l = l.strip()
        if not l: continue
        
        if "Capital Improvement Projects" in l:
            curr = "Capital"
        elif "Disaster Recovery Projects" in l:
            curr = "Disaster"
            
        if "Updates:" in l:
            # Find name
            name = "Unknown"
            # Look backwards for non-empty line
            k = i - 1
            while k >= 0:
                if lines[k].strip():
                    name = lines[k].strip()
                    break
                k -= 1
            
            # Find date in next lines
            st_date = "Unknown"
            # Simple scan
            for j in range(i, min(i+20, len(lines))):
                sl = lines[j].strip()
                if "Begin Construction:" in sl or "Begin construction:" in sl:
                    st_date = sl
                    break
            
            typ = curr
            if "FEMA" in name or "CalOES" in name:
                typ = "Disaster"
            
            projects.append({"n": name, "t": typ, "d": st_date})

# Filter
tgs = []
for p in projects:
    if p["t"] == "Disaster" and "2022" in p["d"]:
        tgs.append(p["n"])

tgs = list(set(tgs))

df = pd.DataFrame(fd)
df["Amount"] = pd.to_numeric(df["Amount"])
res = df[df["Project_Name"].isin(tgs)]["Amount"].sum()

print("__RESULT__:")
print(json.dumps({"total": int(res), "list": tgs}))"""

env_args = {'var_function-call-2007247411734305584': ['Funding'], 'var_function-call-2007247411734305063': ['civic_docs'], 'var_function-call-6570500424665690713': 'file_storage/function-call-6570500424665690713.json', 'var_function-call-6570500424665692862': 'file_storage/function-call-6570500424665692862.json'}

exec(code, env_args)
