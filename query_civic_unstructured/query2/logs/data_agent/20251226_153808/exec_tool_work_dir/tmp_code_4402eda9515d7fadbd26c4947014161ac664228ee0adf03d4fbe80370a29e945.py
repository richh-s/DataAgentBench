code = """import json

# Load civic docs
with open(var_call_ZGxPsl3QZckLx5Aftdn8Sa0X, "r") as f:
    civic_docs = json.load(f)

# Load funding
with open(var_call_vzEtHYEO2mxMyHPnsAC47tFQ, "r") as f:
    funding_records = json.load(f)

# Build funding map
funding_map = {}
for rec in funding_records:
    name = rec.get("Project_Name")
    amt = rec.get("Amount")
    if name is None:
        continue
    try:
        val = int(amt)
    except Exception:
        try:
            val = int(float(amt))
        except Exception:
            val = 0
    funding_map[name] = funding_map.get(name, 0) + val

# Helper: find title above index
def find_title(lines, idx):
    for j in range(idx - 1, max(-1, idx - 11), -1):
        line = lines[j].strip()
        if not line:
            continue
        low = line.lower()
        if low.startswith("updates") or low.startswith("project schedule") or low.startswith("estimated schedule") or low.startswith("project description"):
            continue
        if ":" in line:
            continue
        if "capital improvement projects" in low or "disaster recovery projects" in low:
            continue
        if "agenda item" in low or "page " in low:
            continue
        if len(line) > 120:
            continue
        return line
    return None

# Find park-related projects completed in 2022
park_projects = set()
for doc in civic_docs:
    text = doc.get("text", "")
    lines = text.split("\n")
    for i, line in enumerate(lines):
        low = line.lower()
        if ("completed" in low) and ("2022" in line):
            title = find_title(lines, i)
            if not title:
                continue
            tl = title.lower()
            if ("park" in tl) or ("playground" in tl):
                park_projects.add(title)

# Match funding names
matched_funding_names = set()
for proj in park_projects:
    p_low = proj.lower()
    for fname in funding_map.keys():
        f_low = fname.lower()
        if p_low == f_low or p_low in f_low or f_low in p_low:
            matched_funding_names.add(fname)

# Sum total
total = sum(funding_map[name] for name in matched_funding_names)

result = {
    "park_completed_2022_projects": sorted(list(park_projects)),
    "matched_funding_records": sorted(list(matched_funding_names)),
    "total_funding": total
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ZGxPsl3QZckLx5Aftdn8Sa0X': 'file_storage/call_ZGxPsl3QZckLx5Aftdn8Sa0X.json', 'var_call_vzEtHYEO2mxMyHPnsAC47tFQ': 'file_storage/call_vzEtHYEO2mxMyHPnsAC47tFQ.json'}

exec(code, env_args)
