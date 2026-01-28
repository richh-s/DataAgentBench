code = """import json

# Load data
with open(locals()["var_functions.query_db:40"], "r") as f:
    funding = json.load(f)

with open(locals()["var_functions.query_db:5"], "r", encoding="utf-8") as f:
    civic = json.load(f)

# Find design projects
design_projs = set()
for doc in civic:
    txt = doc.get("text", "")
    if "Capital Improvement Projects (Design)" in txt:
        idx = txt.find("Capital Improvement Projects (Design)")
        section = txt[idx:idx+2500]
        for line in section.split("\n"):
            s = line.strip()
            if len(s) > 10 and "Project" in s and "fema" not in s.lower():
                design_projs.add(s)

# Match funding > 50000
matched = set()
for rec in funding:
    if int(rec["Amount"]) > 50000:
        name = rec["Project_Name"]
        base = name.split("(")[0].strip()
        if base in design_projs:
            matched.add(base)

result = {"count": len(matched)}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
