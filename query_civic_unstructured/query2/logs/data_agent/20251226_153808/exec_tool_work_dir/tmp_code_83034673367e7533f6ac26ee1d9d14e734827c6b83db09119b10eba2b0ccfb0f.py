code = """import json
with open(var_call_ZGxPsl3QZckLx5Aftdn8Sa0X, "r") as f:
    civic_docs = json.load(f)
# scan for lines indicating completed in 2022 and capture titles
results = []
for doc in civic_docs:
    text = doc.get("text", "")
    lines = text.split("\n")
    for i, line in enumerate(lines):
        low = line.lower()
        if ("completed" in low) and ("2022" in line):
            # find previous plausible title
            j = i - 1
            title = None
            while j >= 0 and j >= i - 10:
                cand = lines[j].strip()
                if cand:
                    cl = cand.lower()
                    if (":" in cand) or cl.startswith("updates") or cl.startswith("project schedule") or cl.startswith("estimated schedule") or cl.startswith("project description") or ("agenda item" in cl) or ("page " in cl) or (len(cand) > 120) or ("capital improvement projects" in cl) or ("disaster recovery projects" in cl):
                        pass
                    else:
                        title = cand
                        break
                j -= 1
            if title:
                results.append({"title": title, "line": line.strip()})
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_ZGxPsl3QZckLx5Aftdn8Sa0X': 'file_storage/call_ZGxPsl3QZckLx5Aftdn8Sa0X.json', 'var_call_vzEtHYEO2mxMyHPnsAC47tFQ': 'file_storage/call_vzEtHYEO2mxMyHPnsAC47tFQ.json', 'var_call_vPZiNK1ZwTOX2UZ4GF6PIA6T': {'num_docs': 5, 'num_funding': 500}}

exec(code, env_args)
