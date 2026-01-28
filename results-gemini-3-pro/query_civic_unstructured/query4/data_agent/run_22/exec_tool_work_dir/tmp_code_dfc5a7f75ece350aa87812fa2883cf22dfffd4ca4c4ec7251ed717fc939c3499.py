code = """import json
import pandas as pd

k1 = "var_function-call-8904296491751843034"
with open(locals()[k1], "r") as f:
    d1 = json.load(f)
df = pd.DataFrame(d1)
df["Amount"] = pd.to_numeric(df["Amount"])

k2 = "var_function-call-8494922430906473506"
with open(locals()[k2], "r") as f:
    d2 = json.load(f)

projs = set()
for d in d2:
    txt = d.get("text", "")
    lines = txt.split("\n")
    cur = ""
    buf = ""
    for line in lines:
        line = line.strip()
        if not line: continue
        low = line.lower()
        if "page " in low: continue
        
        if "Updates:" in line or "Project Schedule:" in line:
            if buf: cur = buf
        
        if cur and "begin construction" in low:
            # check date
            if "2022" in low:
                if "spring" in low or "march" in low or "april" in low or "may" in low:
                    projs.add(cur)
        
        if "Updates:" not in line and "Project Schedule:" not in line:
            buf = line

# Calculate funding
total_funding = 0
target_list = list(projs)

for idx, row in df.iterrows():
    f_name = row["Project_Name"].strip()
    match = False
    for p in target_list:
        p_clean = p.strip()
        if p_clean.lower() == f_name.lower():
            match = True
        elif len(p_clean) > 5 and len(f_name) > 5:
            if p_clean.lower() in f_name.lower() or f_name.lower() in p_clean.lower():
                match = True
        if match: break
    
    if match:
        total_funding += row["Amount"]

print("__RESULT__:")
print(json.dumps({"count": len(projs), "funding": total_funding, "projects": list(projs)}))"""

env_args = {'var_function-call-1649366549132259120': 'file_storage/function-call-1649366549132259120.json', 'var_function-call-17157926342599850647': 'file_storage/function-call-17157926342599850647.json', 'var_function-call-8904296491751843034': 'file_storage/function-call-8904296491751843034.json', 'var_function-call-8494922430906473506': 'file_storage/function-call-8494922430906473506.json'}

exec(code, env_args)
