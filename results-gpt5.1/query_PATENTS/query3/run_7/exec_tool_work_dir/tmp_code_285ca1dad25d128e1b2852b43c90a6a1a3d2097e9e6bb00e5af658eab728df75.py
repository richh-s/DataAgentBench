code = """import json, pandas as pd
import os

path = var_call_n4V8UNccRkuupBzCXO9gjH41
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Extract publication_number of UNIV CALIFORNIA patents from Patents_info
import re

def extract_pubnum(text):
    m = re.search(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', text)
    if m:
        return m.group(1)
    m = re.search(r'publication number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', text)
    if m:
        return m.group(1)
    return None

uc_pubs = df['Patents_info'].apply(extract_pubnum).dropna().unique().tolist()

result = json.dumps({"uc_publication_numbers": uc_pubs})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_TgiczeIG8IbC3AHgD6egu7ty': [], 'var_call_n4V8UNccRkuupBzCXO9gjH41': 'file_storage/call_n4V8UNccRkuupBzCXO9gjH41.json'}

exec(code, env_args)
