code = """import json
import re
# var_call_1Bqplr3rh53ChNvtEOW1gjRS is available in storage
data = None
# If the storage variable is a filepath (string), read the file
try:
    # var_call_1Bqplr3rh53ChNvtEOW1gjRS may be a path to a .json file
    if isinstance(var_call_1Bqplr3rh53ChNvtEOW1gjRS, str):
        with open(var_call_1Bqplr3rh53ChNvtEOW1gjRS, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = var_call_1Bqplr3rh53ChNvtEOW1gjRS
except Exception as e:
    data = var_call_1Bqplr3rh53ChNvtEOW1gjRS

# Extract filenames where the text contains '2016' (publication year) and 'physical activity' already matched by query
titles = []
for doc in data:
    text = doc.get('text','')
    # check for 2016 as a year
    if re.search(r'\b2016\b', text):
        filename = doc.get('filename','')
        if filename.endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        titles.append(title)

# Remove duplicates and sort
titles = sorted(list(dict.fromkeys(titles)))

result = json.dumps(titles)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_1Bqplr3rh53ChNvtEOW1gjRS': 'file_storage/call_1Bqplr3rh53ChNvtEOW1gjRS.json'}

exec(code, env_args)
