code = """import json, re, pandas as pd

md = var_call_r4h5LgQDHWF3Q64iJefH3ezt
if isinstance(md, str):
    with open(md, 'r', encoding='utf-8') as f:
        md = json.load(f)

# Extract likely publication year from header patterns

def pub_year(text):
    head = text[:3000]
    # common: "CHI '16" or "CHI 2016"; "UBICOMP '16" etc.
    m = re.search(r"\b(CHI|UbiComp|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*'?\s*(\d{2,4})\b", head)
    if m:
        y = m.group(2)
        if len(y)==2:
            y = int('20'+y)
        else:
            y = int(y)
        if 1980<=y<=2026:
            return y
    # ACM copyright year
    m = re.search(r"Copyright\s*(\d{4})", head, flags=re.I)
    if m:
        return int(m.group(1))
    # any year in first 1000 chars
    m = re.search(r"\b(19|20)\d{2}\b", head)
    if m:
        return int(m.group(0))
    return None

rows=[]
for d in md:
    title = d['filename'][:-4] if d['filename'].lower().endswith('.txt') else d['filename']
    y = pub_year(d.get('text','') or '')
    if y==2016:
        rows.append(title)

print('__RESULT__:')
print(json.dumps(rows))"""

env_args = {'var_call_BnFG7NMNwOlOF78McYE12CcR': 'file_storage/call_BnFG7NMNwOlOF78McYE12CcR.json', 'var_call_NGUDu0rlWfSbJltgy6x0eoxR': 'file_storage/call_NGUDu0rlWfSbJltgy6x0eoxR.json', 'var_call_TOLP2nwAyrmLYZcktKJNVLmh': [], 'var_call_r4h5LgQDHWF3Q64iJefH3ezt': 'file_storage/call_r4h5LgQDHWF3Q64iJefH3ezt.json'}

exec(code, env_args)
