code = """import json, re

with open(var_call_UnYOruakbLEubMPEjdnbIbFN, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_0VlHSAjA8oAeNXBPOEXNwXzf, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Collect park-related funding entries
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
    for idx, line in enumerate(lines):
        low = line.lower()
        # look for completion statements that mention 2022
        if 'completed' in low and '2022' in line:
            # search context (current and previous 3 lines) for park-related project names or 'park' keyword
            context = ' '.join(lines[max(0, idx-3): idx+1]).lower()
            if 'park' in context or any(pn in context for pn in park_names):
                for p in park_funding:
                    pname_low = p['Project_Name'].lower()
                    if pname_low in context and p['Project_Name'] not in matched_names:
                        matched.append(p)
                        matched_names.add(p['Project_Name'])
                # handle cases like 'Bluffs Park Shade Structure' where project name may be slightly different
                for p in park_funding:
                    if p['Project_Name'] in matched_names:
                        continue
                    name_low = p['Project_Name'].lower()
                    words = [w for w in re.split(r'[^a-z0-9]+', name_low) if w]
                    # require at least two words to match
                    if len(words) >= 2 and all(w in context for w in words[:2]):
                        matched.append(p)
                        matched_names.add(p['Project_Name'])

# Deduplicate and compute total
unique = {p['Project_Name']: p for p in matched}
matched_list = list(unique.values())

total = sum(p['Amount'] for p in matched_list)

result = {'matched_projects': matched_list, 'total_funding': total}

json_str = json.dumps(result)
print("----BEGIN PRINT FORMAT----")
print('print("__RESULT__:")')
print('print(' + json.dumps(json_str) + ')')
print("----END PRINT FORMAT----")"""

env_args = {'var_call_TenNsadP4ijMxU8ivUzpD1p8': [], 'var_call_E02bb2NNu0gqPdDQNnqjE30V': ['civic_docs'], 'var_call_UnYOruakbLEubMPEjdnbIbFN': 'file_storage/call_UnYOruakbLEubMPEjdnbIbFN.json', 'var_call_59Lp1s5RndrufOMad3wuudAj': ['Funding'], 'var_call_0VlHSAjA8oAeNXBPOEXNwXzf': 'file_storage/call_0VlHSAjA8oAeNXBPOEXNwXzf.json'}

exec(code, env_args)
