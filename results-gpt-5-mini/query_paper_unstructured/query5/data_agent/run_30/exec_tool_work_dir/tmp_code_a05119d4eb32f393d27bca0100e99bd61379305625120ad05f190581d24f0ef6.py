code = """import json
# Load the large citations result stored in var_call_uhZdm0NT8ktOmC9xiiiVkh8g
path = var_call_uhZdm0NT8ktOmC9xiiiVkh8g
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
# Build list of filenames and include citation counts as ints
out = []
for r in records:
    title = r.get('title')
    cc = r.get('citation_count')
    try:
        cc_int = int(cc)
    except:
        try:
            cc_int = int(float(cc))
        except:
            cc_int = None
    out.append({'title': title, 'filename': f"{title}.txt", 'citation_count': cc_int})

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_uhZdm0NT8ktOmC9xiiiVkh8g': 'file_storage/call_uhZdm0NT8ktOmC9xiiiVkh8g.json'}

exec(code, env_args)
