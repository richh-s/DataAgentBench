code = """import json, re

path = var_call_GnX6xt7hY3INOHf23HF6PI6N
with open(path, 'r') as f:
    civic_docs = json.load(f)

texts = '\n'.join(d['text'] for d in civic_docs)
lines = [l.strip() for l in texts.split('\n') if l.strip()]

completed_2022_names = set()
for i,line in enumerate(lines):
    low = line.lower()
    if 'construction was completed' in low and '2022' in line:
        for j in range(i-1, max(-1, i-6), -1):
            if 'park' in lines[j].lower():
                completed_2022_names.add(lines[j].strip())
                break

completed_2022_names = list(completed_2022_names)

path2 = var_call_5hDBo3TBIgrWNiqKfckgM8Dr
with open(path2, 'r') as f:
    funding = json.load(f)

total = 0
for rec in funding:
    pname = rec['Project_Name'].lower()
    for cname in completed_2022_names:
        cn = cname.lower()
        if pname in cn or cn in pname:
            total += int(rec['Amount'])
            break

result = {"completed_2022_park_projects": completed_2022_names, "total_funding": total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GnX6xt7hY3INOHf23HF6PI6N': 'file_storage/call_GnX6xt7hY3INOHf23HF6PI6N.json', 'var_call_5hDBo3TBIgrWNiqKfckgM8Dr': 'file_storage/call_5hDBo3TBIgrWNiqKfckgM8Dr.json'}

exec(code, env_args)
