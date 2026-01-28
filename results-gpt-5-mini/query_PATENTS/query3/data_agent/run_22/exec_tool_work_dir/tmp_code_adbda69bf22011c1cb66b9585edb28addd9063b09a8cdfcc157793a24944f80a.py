code = """import json, re
# var_call_7xqyIJkzAWq6WVNwai0HPBQs is a file path to the JSON results
path = var_call_7xqyIJkzAWq6WVNwai0HPBQs
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
pub_nums = set()
for rec in data:
    info = rec.get('Patents_info','')
    # find patterns like 'pub. number X' or 'publication number X' or 'pub. number X.'
    m = re.findall(r'pub\. number\s*([A-Z0-9\-\.]+)', info, flags=re.IGNORECASE)
    if not m:
        m = re.findall(r'publication number\s*([A-Z0-9\-\.]+)', info, flags=re.IGNORECASE)
    for x in m:
        pub_nums.add(x.strip())
# as fallback also look for patterns 'pub. number ...,' maybe with trailing characters
# Also search whole text for patterns like '[A-Z]{2}-\d+'
if not pub_nums:
    m = re.findall(r'([A-Z]{2}-\d+[A-Z0-9\-]*)', info)
    for x in m:
        pub_nums.add(x)
pub_list = sorted(pub_nums)
result = json.dumps(pub_list)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_7xqyIJkzAWq6WVNwai0HPBQs': 'file_storage/call_7xqyIJkzAWq6WVNwai0HPBQs.json'}

exec(code, env_args)
