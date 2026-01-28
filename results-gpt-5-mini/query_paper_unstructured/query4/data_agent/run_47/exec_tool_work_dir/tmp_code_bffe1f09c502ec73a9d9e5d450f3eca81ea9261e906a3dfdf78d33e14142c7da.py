code = """import json, re
# Load the paper docs JSON result file path from storage variable
with open(var_call_ge3CyFMCqYeAaqjfssn5Y002, 'r', encoding='utf-8') as f:
    records = json.load(f)

papers = []
for rec in records:
    filename = rec.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text','') or ''
    top = text[:2000]
    # find first 4-digit year between 2000 and 2025 in the top part
    years = re.findall(r"(20[0-2][0-9])", top)
    year = None
    if years:
        # take the first occurrence
        year = int(years[0])
    else:
        # fallback: search for ' '16 patterns like CHI '16
        m = re.search(r"'16", top)
        if m:
            year = 2016
    # detect domain: check if 'physical activity' appears anywhere
    domain = None
    if re.search(r'physical activity', text, re.I):
        domain = 'physical activity'
    papers.append({'title': title, 'year': year, 'has_physical_activity': domain is not None})

# filter for year == 2016 and has_physical_activity
filtered = [p for p in papers if p['year']==2016 and p['has_physical_activity']]
# prepare list of titles
titles = [p['title'] for p in filtered]

output = {'titles': titles, 'count': len(titles)}
import json
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_ge3CyFMCqYeAaqjfssn5Y002': 'file_storage/call_ge3CyFMCqYeAaqjfssn5Y002.json'}

exec(code, env_args)
