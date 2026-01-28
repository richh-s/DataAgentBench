code = """import json

funding_path = var_call_TUmevO8tahmvoGUCVw7U8Bfy
civic_path = var_call_zQkLJw2iym3t2IWOoS4vkm4o

with open(funding_path, 'r') as f:
    funding = json.load(f)
with open(civic_path, 'r') as f:
    civic = json.load(f)

park_keywords = ['park','playground','walkway','bench','shade','bluffs','paver','play']
matched = []

# prepare civic texts lower
civic_texts = [doc.get('text','').lower() for doc in civic]

for row in funding:
    pname = row.get('Project_Name','')
    amount = int(row.get('Amount',0))
    pname_low = pname.lower()
    if not any(k in pname_low for k in park_keywords):
        continue
    found = False
    # try exact match in civic texts
    for text in civic_texts:
        pos = text.find(pname_low)
        if pos != -1:
            window = text[max(0,pos-300):pos+300]
            if 'completed' in window and '2022' in window:
                matched.append({'Project_Name': pname, 'Amount': amount})
                found = True
                break
    if found:
        continue
    # try without parenthesis suffix
    if '(' in pname_low:
        base = pname_low.split('(')[0].strip()
        for text in civic_texts:
            pos = text.find(base)
            if pos != -1:
                window = text[max(0,pos-300):pos+300]
                if 'completed' in window and '2022' in window:
                    matched.append({'Project_Name': pname, 'Amount': amount})
                    found = True
                    break
    if found:
        continue

# sum amounts
total = sum(item['Amount'] for item in matched)

output = {'total_funding': total, 'matched_projects': matched}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_7F65cxkXehOP67TdCcKr94V9': ['civic_docs'], 'var_call_j7BetpNtBnPAHqOl4xBQnreH': ['Funding'], 'var_call_TUmevO8tahmvoGUCVw7U8Bfy': 'file_storage/call_TUmevO8tahmvoGUCVw7U8Bfy.json', 'var_call_zQkLJw2iym3t2IWOoS4vkm4o': 'file_storage/call_zQkLJw2iym3t2IWOoS4vkm4o.json', 'var_call_MpLMplY97suCpXCa4g3YLFuE': {'funding_len': 500, 'civic_len': 19}}

exec(code, env_args)
