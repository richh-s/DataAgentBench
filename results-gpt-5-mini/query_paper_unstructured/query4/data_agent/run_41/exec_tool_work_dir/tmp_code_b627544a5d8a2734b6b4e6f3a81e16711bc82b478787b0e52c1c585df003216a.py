code = """import json
# load the large mongo query result from storage
with open(var_call_DI1QgzAvteEOnKUxNEZimjEB, 'r') as f:
    docs = json.load(f)
# extract titles (from filename without .txt) and attempt to find year and domain from text
records = []
import re
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text','')
    # find year: look for patterns like , 2016 or 2016,
    year_match = re.search(r"\b(19|20)\d{2}\b", text)
    year = int(year_match.group(0)) if year_match else None
    # domain: check if 'physical activity' appears
    domain = None
    if re.search(r'physical activity', text, re.I):
        domain = 'physical activity'
    records.append({'title': title, 'year': year, 'domain': domain})
# filter for domain physical activity and year 2016
filtered = [r for r in records if r['domain']=='physical activity' and r['year']==2016]
# produce json
print("__RESULT__:")
print(json.dumps(filtered))"""

env_args = {'var_call_DI1QgzAvteEOnKUxNEZimjEB': 'file_storage/call_DI1QgzAvteEOnKUxNEZimjEB.json'}

exec(code, env_args)
