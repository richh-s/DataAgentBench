code = """import json
import pandas as pd

k_fund = "var_function-call-14443830636332700640"
k_docs = "var_function-call-14443830636332701107"

funding_path = locals()[k_fund]
docs_path = locals()[k_docs]

with open(funding_path, "r") as f:
    funding_data = json.load(f)

with open(docs_path, "r") as f:
    docs_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding["Amount"] = df_funding["Amount"].astype(float)

def clean(n):
    if "(" in n:
        parts = n.split("(")
        if parts[-1].strip().endswith(")"):
            return "(".join(parts[:-1]).strip()
    return n.strip()

proj_map = {}
for i, row in df_funding.iterrows():
    fn = row["Project_Name"]
    bn = clean(fn)
    if bn not in proj_map:
        proj_map[bn] = []
    proj_map[bn].append(row)

bases = list(proj_map.keys())

total = 0.0
seen_projs = []

for doc in docs_data:
    lines = doc["text"].split("\n")
    cur_p = None
    cur_lines = []
    
    # Identify chunks
    chunks = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        match = None
        if line in bases:
            match = line
        else:
            # Check Clean
            c = clean(line)
            if c in bases:
                match = c
        
        if match:
            if cur_p:
                chunks.append({"name": cur_p, "lines": cur_lines})
            cur_p = match
            cur_lines = []
        else:
            if cur_p:
                cur_lines.append(line)
    if cur_p:
        chunks.append({"name": cur_p, "lines": cur_lines})

    # Filter
    for chunk in chunks:
        nm = chunk["name"]
        ls = chunk["lines"]
        
        # Check start 2022
        st_2022 = False
        for l in ls:
            l_low = l.lower()
            if "begin construction" in l_low or "advertise" in l_low:
                if "2022" in l:
                    st_2022 = True
                    break
        
        if st_2022:
            # Check disaster
            is_d = False
            txt = " ".join(ls)
            d_keys = ["FEMA", "CalOES", "Disaster", "Fire", "Emergency"]
            for k in d_keys:
                if k in txt:
                    is_d = True
                    break
            
            if not is_d:
                recs = proj_map.get(nm, [])
                for r in recs:
                    if "FEMA" in r["Project_Name"] or "CalOES" in r["Project_Name"]:
                        is_d = True
                        break
            
            if is_d:
                if nm not in seen_projs:
                    seen_projs.append(nm)

# Sum
final_sum = 0.0
for nm in seen_projs:
    for r in proj_map[nm]:
        final_sum += r["Amount"]

print("__RESULT__:")
print(json.dumps({"total": final_sum, "projects": seen_projs}))"""

env_args = {'var_function-call-14443830636332701107': 'file_storage/function-call-14443830636332701107.json', 'var_function-call-14443830636332700640': 'file_storage/function-call-14443830636332700640.json'}

exec(code, env_args)
