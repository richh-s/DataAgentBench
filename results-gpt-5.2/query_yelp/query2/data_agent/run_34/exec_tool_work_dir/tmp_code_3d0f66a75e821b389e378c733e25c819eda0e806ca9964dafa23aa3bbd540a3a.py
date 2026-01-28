code = """import json, re, pandas as pd

def load_tool_result(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

business_records = load_tool_result(var_call_7zTbh6V4tUeyH6N2GC7yXF58)

bdf = pd.DataFrame(business_records)

# improved extraction: look for ', ST' in first ~120 chars
pat = re.compile(r",\s*([A-Z]{2})(?:\s|,|\.|\b)")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    s = desc[:200]
    m = re.search(r"\bin\s+[^,]{1,50},\s*([A-Z]{2})\b", s)
    if m:
        return m.group(1)
    m = pat.search(s)
    if m:
        return m.group(1)
    return None

bdf['state'] = bdf['description'].apply(extract_state)
counts = bdf['state'].value_counts(dropna=False).head(20)

print('__RESULT__:')
print(json.dumps({'top_state_values': counts.to_dict()}))"""

env_args = {'var_call_7zTbh6V4tUeyH6N2GC7yXF58': 'file_storage/call_7zTbh6V4tUeyH6N2GC7yXF58.json', 'var_call_EeisKdPrtiC9qFaVsr8NuUe9': 'file_storage/call_EeisKdPrtiC9qFaVsr8NuUe9.json', 'var_call_FvfNnOOuSlINA493fLZYfR3x': {'state': None, 'total_reviews_in_state': None, 'average_business_rating_in_state': None, 'num_businesses_with_reviews_used_for_avg': 0}}

exec(code, env_args)
