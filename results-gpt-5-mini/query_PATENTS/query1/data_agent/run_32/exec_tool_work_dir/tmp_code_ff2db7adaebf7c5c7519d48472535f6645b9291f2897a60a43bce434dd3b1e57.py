code = """import json
import re
from collections import defaultdict

# Load level-5 symbols
with open(var_call_v1OtkJfTUeC5VXQY072oZ9zT, 'r', encoding='utf-8') as f:
    level5 = json.load(f)
symbols = [r['symbol'] for r in level5 if r.get('symbol')]
# Build sets by length for fast prefix matching
set_by_len = {}
lengths = set()
for s in symbols:
    l = len(s)
    lengths.add(l)
    set_by_len.setdefault(l, set()).add(s)
lengths = sorted(lengths, reverse=True)

# Prepare counts
counts = defaultdict(lambda: defaultdict(int))

year_re = re.compile(r'(19|20)\d{2}')

pubs_path = var_call_0pHvLmRFOFeI8zjaOCjRnq9R

# Stream-parse the large JSON array of publication records
with open(pubs_path, 'r', encoding='utf-8') as f:
    # skip whitespace until first '['
    ch = f.read(1)
    while ch and ch != '[':
        ch = f.read(1)
    if not ch:
        raise SystemExit('empty file')

    buf = ''
    depth = 0
    in_str = False
    esc = False
    while True:
        chunk = f.read(65536)
        if not chunk:
            break
        for c in chunk:
            # manage string state
            if c == '"' and not esc:
                in_str = not in_str
                if depth > 0:
                    buf += c
                esc = False
                continue
            if c == '\\' and in_str and not esc:
                esc = True
                if depth > 0:
                    buf += c
                continue
            if esc:
                # escaped char
                if depth > 0:
                    buf += c
                esc = False
                continue
            if not in_str:
                if c == '{':
                    depth += 1
                    buf += c
                    continue
                elif c == '}':
                    depth -= 1
                    buf += c
                    if depth == 0:
                        # end of object
                        try:
                            obj = json.loads(buf)
                        except Exception:
                            # reset buffer
                            buf = ''
                            continue
                        # process obj
                        cpc_field = obj.get('cpc')
                        filing_date = obj.get('filing_date') or ''
                        m = year_re.search(filing_date)
                        if m and cpc_field:
                            year = int(m.group(0))
                            try:
                                cpc_list = json.loads(cpc_field)
                            except Exception:
                                cpc_list = None
                            if cpc_list:
                                for item in cpc_list:
                                    code = (item.get('code') or '').strip()
                                    if not code:
                                        continue
                                    matched = None
                                    # try lengths
                                    for L in lengths:
                                        prefix = code[:L]
                                        if prefix in set_by_len.get(L, set()):
                                            matched = prefix
                                            break
                                    if matched:
                                        counts[matched][year] += 1
                        # reset buffer
                        buf = ''
                    continue
                else:
                    # separators like comma or whitespace outside objects
                    continue
            else:
                # inside string
                if depth > 0:
                    buf += c
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
