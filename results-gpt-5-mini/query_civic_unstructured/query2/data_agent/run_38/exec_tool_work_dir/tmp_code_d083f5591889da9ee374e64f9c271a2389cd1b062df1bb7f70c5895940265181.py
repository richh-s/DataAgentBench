code = """import json, re

with open(var_call_UnYOruakbLEubMPEjdnbIbFN, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_0VlHSAjA8oAeNXBPOEXNwXzf, 'r', encoding='utf-8') as f:
    funding = json.load(f)

park_funding = []
for entry in funding:
    name = entry.get('Project_Name', '')
    if 'park' in name.lower():
        try:
            amt = int(entry.get('Amount') or 0)
        except:
            try:
                amt = int(float(entry.get('Amount')))
            except:
                amt = 0
        park_funding.append({'Funding_ID': entry.get('Funding_ID'), 'Project_Name': name, 'Amount': amt})

park_names = [p['Project_Name'].lower() for p in park_funding]

matched = []
matched_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for line in lines:
        low = line.lower()
        if 'completed' in low and '2022' in line:
            if 'park' in low or any(pn in low for pn in park_names):
                for p in park_funding:
                    if p['Project_Name'].lower() in low:
                        matched.append(p)
                        matched_names.add(p['Project_Name'])
                for p in park_funding:
                    name_low = p['Project_Name'].lower()
                    if p['Project_Name'] in matched_names:
                        continue
                    words = [w for w in re.split(r'[^a-z0-9]+', name_low) if w]
                    if words and all(w in low for w in words[:3]):
                        matched.append(p)
                        matched_names.add(p['Project_Name'])

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for idx, line in enumerate(lines):
        low = line.lower()
        if 'completed' in low and '2022' in line:
            context = ' '.join(lines[max(0, idx-3): idx+1]).lower()
            for p in park_funding:
                if p['Project_Name'].lower() in context and p['Project_Name'] not in matched_names:
                    matched.append(p)
                    matched_names.add(p['Project_Name'])
            for p in park_funding:
                name_low = p['Project_Name'].lower()
                if any(phrase in context for phrase in [name_low, 'bluffs park', 'malibu park', 'legacy park']):
                    if p['Project_Name'] not in matched_names and any(w in context for w in name_low.split()[:2]):
                        matched.append(p)
                        matched_names.add(p['Project_Name'])

unique_matched = {}
for p in matched:
    unique_matched[p['Project_Name']] = p

matched_list = list(unique_matched.values())

total = sum(p['Amount'] for p in matched_list)

result = {'matched_projects': matched_list, 'total_funding': total}

print("----BEGIN PRINT FORMAT----")
print("print(\"__RESULT__:\")")
print("print('" + json.dumps(result).replace("'", "\\'") + "')")
print("----END PRINT FORMAT----")"""

env_args = {'var_call_TenNsadP4ijMxU8ivUzpD1p8': [], 'var_call_E02bb2NNu0gqPdDQNnqjE30V': ['civic_docs'], 'var_call_UnYOruakbLEubMPEjdnbIbFN': 'file_storage/call_UnYOruakbLEubMPEjdnbIbFN.json', 'var_call_59Lp1s5RndrufOMad3wuudAj': ['Funding'], 'var_call_0VlHSAjA8oAeNXBPOEXNwXzf': 'file_storage/call_0VlHSAjA8oAeNXBPOEXNwXzf.json'}

exec(code, env_args)
