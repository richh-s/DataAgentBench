code = """import json, re

# Load files
with open(var_call_DC5goInbH4wtr4Tyj3ekeUna, 'r', encoding='utf-8') as f:
    level5_data = json.load(f)
with open(var_call_GFynDXJBCT7UezxVAXkKIhAo, 'r', encoding='utf-8') as f:
    pub_data = json.load(f)

level5_symbols = set()
for r in level5_data:
    s = r.get('symbol')
    if s:
        level5_symbols.add(s.strip().upper())

# regex to extract codes from cpc field without full json parsing
code_re = re.compile(r'"code"\s*:\s*"([^"\\]+)"')

# helper to extract year

def extract_year(text):
    if not isinstance(text, str):
        return None
    for i in range(len(text)-3):
        part = text[i:i+4]
        if (part.startswith('19') or part.startswith('20')) and part.isdigit():
            return int(part)
    return None

counts = {}
min_year = 9999
max_year = 0

for rec in pub_data:
    fd = rec.get('filing_date') or ''
    year = extract_year(fd)
    if year is None:
        continue
    if year < min_year: min_year = year
    if year > max_year: max_year = year
    cpc_field = rec.get('cpc')
    if not cpc_field or not isinstance(cpc_field, str):
        continue
    for m in code_re.finditer(cpc_field):
        code = m.group(1).strip().upper()
        if len(code) < 4:
            continue
        group = code[:4]
        if not (group[0].isalpha() and group[1].isdigit() and group[2].isdigit() and group[3].isalpha()):
            continue
        if group in level5_symbols:
            counts[(group, year)] = counts.get((group, year), 0) + 1

# compute EMA
alpha = 0.2
selected = []
if counts:
    groups = sorted({g for (g,y) in counts.keys()})
    years = list(range(min_year, max_year+1))
    for g in groups:
        ema = None
        best_ema = -1.0
        best_year = None
        for y in years:
            x = counts.get((g,y), 0)
            if ema is None:
                ema = float(x)
            else:
                ema = alpha * float(x) + (1 - alpha) * ema
            if ema > best_ema:
                best_ema = ema
                best_year = y
        if best_year == 2022:
            selected.append(g)

selected = sorted(selected)
print('__RESULT__:')
print(json.dumps(selected))"""

env_args = {'var_call_DC5goInbH4wtr4Tyj3ekeUna': 'file_storage/call_DC5goInbH4wtr4Tyj3ekeUna.json', 'var_call_GFynDXJBCT7UezxVAXkKIhAo': 'file_storage/call_GFynDXJBCT7UezxVAXkKIhAo.json', 'var_call_UmhGy9Sr0LmqG1hbvew6OqLC': {'level5_count': 677, 'pub_count': 277813}}

exec(code, env_args)
