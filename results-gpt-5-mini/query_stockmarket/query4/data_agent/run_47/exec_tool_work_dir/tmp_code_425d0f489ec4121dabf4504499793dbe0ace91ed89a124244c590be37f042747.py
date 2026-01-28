code = """import json, re
# load the large results from previous tool calls
with open(var_call_FWakvmR4YjyTiHO7Rp6IYgVa, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_Te8y2lY6KAqLs0XOa1kUpbGb, 'r') as f:
    trade_tables = json.load(f)

# Build set of trade table symbols
trade_set = set(trade_tables)

# Filter stockinfo for Listing Exchange = 'N' was already done in the query that produced stockinfo
# But double-check presence of ETF field
candidates = []
pattern = re.compile(r"\b(is|is an|is a|specializes in|specializes|provides|offers|operates|focusing|focuses|serving|serves|providing|that|which)\b", re.IGNORECASE)
for rec in stockinfo:
    sym = rec.get('Symbol')
    etf = rec.get('ETF')
    desc = rec.get('Company Description') or ''
    if etf and etf.strip().upper() == 'N' and sym in trade_set:
        # extract company name heuristically
        m = pattern.search(desc)
        if m:
            name = desc[:m.start()].strip().strip(',')
        else:
            # fallback: up to first period
            if '.' in desc:
                name = desc.split('.',1)[0].strip()
            else:
                name = desc.strip()
        if not name:
            name = desc
        candidates.append({'Symbol': sym, 'Name': name})

# sort candidates by symbol for deterministic ordering
candidates = sorted(candidates, key=lambda x: x['Symbol'])

result = json.dumps(candidates)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_FWakvmR4YjyTiHO7Rp6IYgVa': 'file_storage/call_FWakvmR4YjyTiHO7Rp6IYgVa.json', 'var_call_Te8y2lY6KAqLs0XOa1kUpbGb': 'file_storage/call_Te8y2lY6KAqLs0XOa1kUpbGb.json'}

exec(code, env_args)
