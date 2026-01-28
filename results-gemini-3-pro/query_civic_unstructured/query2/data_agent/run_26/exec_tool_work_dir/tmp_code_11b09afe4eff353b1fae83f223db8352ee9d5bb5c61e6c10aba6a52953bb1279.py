code = """import json

d_key = "var_function-call-14510963906005286500"
f_key = "var_function-call-14510963906005285081"

d_path = locals()[d_key]
f_path = locals()[f_key]

with open(d_path, "r") as f:
    docs = json.load(f)

with open(f_path, "r") as f:
    funds = json.load(f)

known = set()
for r in funds:
    known.add(r["Project_Name"].strip())

found = []
for doc in docs:
    lines = doc["text"].split("\n")
    curr = None
    buf = []
    for line in lines:
        s = line.strip()
        if s in known:
            if curr:
                txt = " ".join(buf).lower()
                is_park = "park" in curr.lower() or "park" in txt
                is_comp = False
                if "completed" in txt and "2022" in txt:
                    if "was completed" in txt or "completed," in txt:
                        is_comp = True
                if is_park and is_comp:
                    found.append(curr)
            curr = s
            buf = []
        else:
            if curr:
                buf.append(s)
    
    if curr:
        txt = " ".join(buf).lower()
        is_park = "park" in curr.lower() or "park" in txt
        is_comp = False
        if "completed" in txt and "2022" in txt:
             if "was completed" in txt or "completed," in txt:
                 is_comp = True
        if is_park and is_comp:
            found.append(curr)

unique = list(set(found))
total = 0
for r in funds:
    if r["Project_Name"].strip() in unique:
        total += int(r["Amount"])

print("__RESULT__:")
print(json.dumps({"projects": unique, "total": total}))"""

env_args = {'var_function-call-7656597533557058168': 'file_storage/function-call-7656597533557058168.json', 'var_function-call-7656597533557058431': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14510963906005286500': 'file_storage/function-call-14510963906005286500.json', 'var_function-call-14510963906005285081': 'file_storage/function-call-14510963906005285081.json', 'var_function-call-13072667451122930611': 500}

exec(code, env_args)
