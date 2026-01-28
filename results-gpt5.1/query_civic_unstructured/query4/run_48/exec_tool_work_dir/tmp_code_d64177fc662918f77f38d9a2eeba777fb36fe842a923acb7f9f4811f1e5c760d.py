code = """import re, json, pandas as pd

# Load full civic docs from file
with open(var_call_Xadzzg5GJM5LpLRfAtzp7ib8, 'r') as f:
    civic_docs = json.load(f)

# Load funding table records
funding_records = var_call_IrMDoqi62u4A4hE2QevOHgkH

spring_2022_projects = set()
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        name = line.strip()
        if not name:
            continue
        for rec in funding_records:
            pname = rec['Project_Name']
            if pname in name or name in pname:
                context = '\n'.join(lines[i:i+10])
                if re.search(r'Begin (Construction|Design):\s*Spring 2022', context) or re.search(r'Start(?:s|ed)?:\s*Spring 2022', context):
                    spring_2022_projects.add(pname)

spring_funding = [rec for rec in funding_records if rec['Project_Name'] in spring_2022_projects]

count_projects = len({rec['Project_Name'] for rec in spring_funding})

total_funding = sum(int(rec['Amount']) for rec in spring_funding) if spring_funding else 0

result = {"num_projects_started_spring_2022": count_projects, "total_funding_spring_2022": total_funding}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Xadzzg5GJM5LpLRfAtzp7ib8': 'file_storage/call_Xadzzg5GJM5LpLRfAtzp7ib8.json', 'var_call_IrMDoqi62u4A4hE2QevOHgkH': 'file_storage/call_IrMDoqi62u4A4hE2QevOHgkH.json'}

exec(code, env_args)
