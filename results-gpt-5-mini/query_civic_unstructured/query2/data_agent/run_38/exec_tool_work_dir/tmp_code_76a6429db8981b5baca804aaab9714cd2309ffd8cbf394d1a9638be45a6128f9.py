code = """import json

with open(var_call_NA88C4XHCJKJMABe2rto4ZPR, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_0VlHSAjA8oAeNXBPOEXNwXzf, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# find park-related funding entries
park_funding = []
for e in funding:
    name = e.get('Project_Name', '')
    if 'park' in name.lower():
        try:
            amt = int(e.get('Amount') or 0)
        except:
            try:
                amt = int(float(e.get('Amount') or 0))
            except:
                amt = 0
        park_funding.append({'Funding_ID': e.get('Funding_ID'), 'Project_Name': name, 'Amount': amt})

# find which of these were completed in 2022 per civic docs
matched = {}
for doc in civic_docs:
    text = doc.get('text', '').lower()
    if 'completed' in text and '2022' in text:
        for p in park_funding:
            if p['Project_Name'].lower() in text:
                matched[p['Project_Name']] = p

matched_list = list(matched.values())

total = sum(p['Amount'] for p in matched_list)

result = {'matched_projects': matched_list, 'total_funding': total}

# Print in required format
print("----BEGIN PRINT FORMAT----")
print('print("__RESULT__:")')
print('print(' + json.dumps(result) + ')')
print("----END PRINT FORMAT----")"""

env_args = {'var_call_TenNsadP4ijMxU8ivUzpD1p8': [], 'var_call_E02bb2NNu0gqPdDQNnqjE30V': ['civic_docs'], 'var_call_UnYOruakbLEubMPEjdnbIbFN': 'file_storage/call_UnYOruakbLEubMPEjdnbIbFN.json', 'var_call_59Lp1s5RndrufOMad3wuudAj': ['Funding'], 'var_call_0VlHSAjA8oAeNXBPOEXNwXzf': 'file_storage/call_0VlHSAjA8oAeNXBPOEXNwXzf.json', 'var_call_02yV89ZKEa3F4LTyYQnWZOec': [], 'var_call_NA88C4XHCJKJMABe2rto4ZPR': 'file_storage/call_NA88C4XHCJKJMABe2rto4ZPR.json'}

exec(code, env_args)
