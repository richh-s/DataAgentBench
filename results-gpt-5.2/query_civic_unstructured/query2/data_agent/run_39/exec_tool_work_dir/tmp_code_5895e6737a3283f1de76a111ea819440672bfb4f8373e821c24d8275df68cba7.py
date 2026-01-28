code = """import json, re
import pandas as pd

def load_json(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json(var_call_ZUCDDdG0SXoMt4kmuU3viNnj)

# Find park-related projects completed in 2022 by simple pattern search
patterns = [
    r"Bluffs Park Shade Structure.*?completed[^\n]*2022",
    r"Bluffs Park.*?completed[^\n]*2022",
    r"Malibu Bluffs Park.*?completed[^\n]*2022",
    r"Park.*?completed[^\n]*2022",
    r"Playground.*?completed[^\n]*2022",
]

found=set()
for d in docs:
    text = d.get('text','')
    for pat in patterns:
        for m in re.finditer(pat, text, flags=re.I|re.S):
            snippet = m.group(0)
            # project name is up to first newline
            name = snippet.split('\n',1)[0].strip()
            # clean trailing punctuation
            name = re.sub(r"\s+$","",name)
            found.add(name)

# manual normalization for known projects from snippet variations
norm=set()
for n in found:
    # keep only known funding project names where possible
    norm.add(n)

fund = load_json(var_call_lHgXzv8V5PNkATE07UWgYxoP)
df = pd.DataFrame(fund)
df['total_amount']=pd.to_numeric(df['total_amount'])

matched=df[df['Project_Name'].isin(norm)]
total=int(matched['total_amount'].sum()) if not matched.empty else 0

out={'candidates':sorted(norm), 'matched_projects':matched['Project_Name'].tolist(), 'total_funding':total}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_33hmIpX4fm9R354cWlcPlxP0': ['Funding'], 'var_call_9hYeWZ1GktsnA3KhmBLFySCc': ['civic_docs'], 'var_call_ZUCDDdG0SXoMt4kmuU3viNnj': 'file_storage/call_ZUCDDdG0SXoMt4kmuU3viNnj.json', 'var_call_lHgXzv8V5PNkATE07UWgYxoP': 'file_storage/call_lHgXzv8V5PNkATE07UWgYxoP.json'}

exec(code, env_args)
