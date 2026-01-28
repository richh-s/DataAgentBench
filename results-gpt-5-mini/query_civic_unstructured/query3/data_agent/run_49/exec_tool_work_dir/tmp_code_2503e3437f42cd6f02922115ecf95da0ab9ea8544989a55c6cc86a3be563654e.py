code = """import json
from pathlib import Path

res_path = Path(var_call_irpx1bXZZ41igRAKSKNOyulu)
with open(res_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

out = []
for r in data:
    pname = (r.get('Project_Name') or '')
    snippet = (r.get('Status_Snippet') or '')
    s = pname.lower() + '\n' + snippet.lower()
    if 'fema' in s or 'emergency' in s:
        out.append({
            'Project_Name': pname,
            'Funding_Source': r.get('Funding_Source'),
            'Amount': r.get('Amount'),
            'Status': r.get('Status_Inferred')
        })

# Deduplicate by Project_Name
seen = set()
final = []
for item in out:
    if item['Project_Name'] in seen:
        continue
    seen.add(item['Project_Name'])
    final.append(item)

print('__RESULT__:')
print(json.dumps(final, ensure_ascii=False))"""

env_args = {'var_call_bu8LPbUHDRNIbQ84TXKpVe55': 'file_storage/call_bu8LPbUHDRNIbQ84TXKpVe55.json', 'var_call_O0tyg822jhfLZAIPR1IgNBpH': 'file_storage/call_O0tyg822jhfLZAIPR1IgNBpH.json', 'var_call_irpx1bXZZ41igRAKSKNOyulu': 'file_storage/call_irpx1bXZZ41igRAKSKNOyulu.json'}

exec(code, env_args)
