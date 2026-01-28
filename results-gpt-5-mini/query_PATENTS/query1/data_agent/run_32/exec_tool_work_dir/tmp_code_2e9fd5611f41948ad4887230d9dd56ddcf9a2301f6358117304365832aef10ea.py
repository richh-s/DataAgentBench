code = """import json
import re
from collections import defaultdict

# Load level-5 symbols
with open(var_call_v1OtkJfTUeC5VXQY072oZ9zT, 'r', encoding='utf-8') as f:
    level5 = json.load(f)
# Use symbols of length 4 (typical level-5 group like A01B)
symbols = [r['symbol'] for r in level5 if r.get('symbol') and len(r['symbol'])==4]
symbol_set = set(symbols)

counts = defaultdict(lambda: defaultdict(int))

year_re = re.compile(r'(19|20)\d{2}')

pubs_path = var_call_0pHvLmRFOFeI8zjaOCjRnq9R

# Stream-parse JSON array of publication objects
with open(pubs_path, 'r', encoding='utf-8') as f:
    depth = 0
    in_str = False
    esc = False
    buf = ''
    while True:
        ch = f.read(1)
        if not ch:
            break
        if ch == '"' and not esc:
            in_str = not in_str
            if depth > 0:
                buf += ch
            continue
        if ch == '\\' and in_str and not esc:
            esc = True
            if depth > 0:
                buf += ch
            continue
        if esc:
            # escaped char
            if depth > 0:
                buf += ch
            esc = False
            continue
        if not in_str:
            if ch == '{':
                depth += 1
                buf += ch
                continue
            elif ch == '}':
                depth -= 1
                buf += ch
                if depth == 0:
                    # complete object
                    try:
                        obj = json.loads(buf)
                    except Exception:
                        buf = ''
                        continue
                    cpc_field = obj.get('cpc')
                    filing_date = obj.get('filing_date') or ''
                    m = year_re.search(filing_date)
                    if m and cpc_field:
                        year = int(m.group(0))
                        # find codes via regex in cpc_field
                        try:
                            codes = re.findall(r'"code"\s*:\s*"([^"]+)"', cpc_field)
                        except Exception:
                            codes = []
                        for code in codes:
                            code = code.strip()
                            if not code:
                                continue
                            prefix = code[:4]
                            if prefix in symbol_set:
                                counts[prefix][year] += 1
                    buf = ''
                continue
            else:
                # outside object
                continue
        else:
            # inside string
            if depth > 0:
                buf += ch
            continue

# Compute EMA alpha=0.2
alpha = 0.2
result_symbols = []
for s, ycounts in counts.items():
    years = sorted(ycounts.keys())
    if not years:
        continue
    S = None
    ema_by_year = {}
    for y in years:
        c = ycounts[y]
        if S is None:
            S = c
        else:
            S = alpha * c + (1 - alpha) * S
        ema_by_year[y] = S
    best_year = max(ema_by_year.items(), key=lambda x: (x[1], x[0]))[0]
    if best_year == 2022:
        result_symbols.append(s)

result_symbols = sorted(result_symbols)
print("__RESULT__:")
print(json.dumps(result_symbols))"""

env_args = {'var_call_v1OtkJfTUeC5VXQY072oZ9zT': 'file_storage/call_v1OtkJfTUeC5VXQY072oZ9zT.json', 'var_call_0pHvLmRFOFeI8zjaOCjRnq9R': 'file_storage/call_0pHvLmRFOFeI8zjaOCjRnq9R.json'}

exec(code, env_args)
