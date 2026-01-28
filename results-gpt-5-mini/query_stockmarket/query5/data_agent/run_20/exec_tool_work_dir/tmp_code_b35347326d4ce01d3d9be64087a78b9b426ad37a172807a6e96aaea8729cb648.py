code = """import json
# Load the previous tool results from the provided storage keys
with open(var_call_0E5QaHvjoVMRvwUB85CQmhze, 'r') as f:
    stockinfo_records = json.load(f)
with open(var_call_djPIRwcWq4NijOTf6t11m3o0, 'r') as f:
    trade_tables = json.load(f)

# stockinfo_records contains entries with Symbol and Company Description already filtered to Market Category 'S'
# Filter to symbols present in trade_tables
trade_set = set(trade_tables)
filtered = [r for r in stockinfo_records if r['Symbol'] in trade_set]

# Prepare output structure: list of symbols and mapping to company name
symbols = [r['Symbol'] for r in filtered]
mapping = {r['Symbol']: r['Company Description'] for r in filtered}

output = {
    'symbols': symbols,
    'mapping': mapping
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_0E5QaHvjoVMRvwUB85CQmhze': 'file_storage/call_0E5QaHvjoVMRvwUB85CQmhze.json', 'var_call_djPIRwcWq4NijOTf6t11m3o0': 'file_storage/call_djPIRwcWq4NijOTf6t11m3o0.json'}

exec(code, env_args)
