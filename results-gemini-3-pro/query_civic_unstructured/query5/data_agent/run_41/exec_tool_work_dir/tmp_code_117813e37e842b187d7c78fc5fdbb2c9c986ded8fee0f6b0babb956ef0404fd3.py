code = """import json
import pandas as pd

p1 = locals()["var_function-call-14443830636332700640"]
p2 = locals()["var_function-call-14443830636332701107"]

with open(p1, "r") as f:
    d1 = json.load(f)
with open(p2, "r") as f:
    d2 = json.load(f)

df = pd.DataFrame(d1)
df["Amount"] = df["Amount"].astype(float)

def get_base(n):
    if "(" in n:
        ps = n.split("(")
        if ps[-1].strip().endswith(")"):
            return "(".join(ps[:-1]).strip()
    return n.strip()

pmap = {}
for i, r in df.iterrows():
    b = get_base(r["Project_Name"])
    if b not in pmap:
        pmap[b] = []
    pmap[b].append(r)

bases = list(pmap.keys())

projs = []
for d in d2:
    txt = d["text"]
    lns = txt.splitlines()
    cp = None
    cblk = []

    for l in lns:
        l = l.strip()
        if not l:
            continue

        m = None
        if l in bases:
            m = l
        else:
            cb = get_base(l)
            if cb in bases:
                m = cb

        if m:
            if cp:
                projs.append({"n": cp, "b": cblk})
            cp = m
            cblk = []
        else:
            if cp:
                cblk.append(l)
    if cp:
        projs.append({"n": cp, "b": cblk})

found = []
for p in projs:
    nm = p["n"]
    ls = p["b"]

    st22 = False
    for l in ls:
        ll = l.lower()
        if "begin construction" in ll or "advertise" in ll:
            if "2022" in l:
                st22 = True
                break

    if st22:
        is_d = False
        full = " ".join(ls)
        if "FEMA" in full or "CalOES" in full or "Disaster" in full:
            is_d = True

        if not is_d:
            for r in pmap[nm]:
                if "FEMA" in r["Project_Name"] or "CalOES" in r["Project_Name"]:
                    is_d = True
                    break

        if is_d:
            if nm not in found:
                found.append(nm)

tot = 0.0
for nm in found:
    for r in pmap[nm]:
        tot += r["Amount"]

print("__RESULT__:")
print(json.dumps({"t": tot, "p": found}))"""

env_args = {'var_function-call-14443830636332701107': 'file_storage/function-call-14443830636332701107.json', 'var_function-call-14443830636332700640': 'file_storage/function-call-14443830636332700640.json'}

exec(code, env_args)
