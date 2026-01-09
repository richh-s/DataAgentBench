code = """import json, re
import pandas as pd

def load_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_maybe(var_call_L877EdMqfxzsRCNCQG8IpBq0)
fund = load_maybe(var_call_xtWYo2xVnMka23KfmOEIPr76)

# Build funding lookup
fund_df = pd.DataFrame(fund)
if len(fund_df)==0:
    fund_df = pd.DataFrame(columns=['Project_Name','total_amount'])
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
funding_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

# Known project names from funding table; use for extraction by presence in text.
project_names = sorted(funding_map.keys(), key=len, reverse=True)

# Identify projects that started in Spring 2022. We treat "started" as having schedule line like
# "Begin Construction: Spring 2022" or "Begin Design: Spring 2022" (or similar), explicitly Spring 2022.
start_patterns = [
    re.compile(r'Begin\\s+Construction\\s*:\\s*(?:Spring\\s+2022|Spring\\/Summer\\s+2022|Spring\\s+of\\s+2022)', re.IGNORECASE),
    re.compile(r'Award\\s+Contract\\s+and\\s+Begin\\s+Construction\\s*:\\s*(?:Spring\\s+2022|Spring\\/Summer\\s+2022)', re.IGNORECASE),
    re.compile(r'Begin\\s+Design\\s*:\\s*(?:Spring\\s+2022)', re.IGNORECASE),
    re.compile(r'Start\\s*(?:Date)?\\s*:\\s*(?:Spring\\s+2022)', re.IGNORECASE),
]

spring2022_projects = set()
for d in docs:
    text = d.get('text','')
    if not any(p.search(text) for p in start_patterns):
        continue
    # Candidate lines containing Spring 2022 and Begin
    # For robustness: if doc contains begin spring 2022 somewhere, find which project sections include it
    # We'll locate occurrences and then backtrack to nearest preceding project name (from funding list) within window.
    # But easiest: scan for each project name presence AND nearby begin spring 2022.
    for pn in project_names:
        if pn not in text:
            continue
        # Find all occurrences of pn
        for m in re.finditer(re.escape(pn), text):
            start = max(0, m.start()-800)
            end = min(len(text), m.end()+800)
            window = text[start:end]
            if any(p.search(window) for p in start_patterns):
                spring2022_projects.add(pn)
                break

# Summarize
count_projects = len(spring2022_projects)
total_funding = int(sum(funding_map.get(p,0) for p in spring2022_projects))

result = {
    "count_projects_started_spring_2022": count_projects,
    "total_funding_amount_usd": total_funding,
    "projects": sorted(list(spring2022_projects))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_L877EdMqfxzsRCNCQG8IpBq0': 'file_storage/call_L877EdMqfxzsRCNCQG8IpBq0.json', 'var_call_xtWYo2xVnMka23KfmOEIPr76': 'file_storage/call_xtWYo2xVnMka23KfmOEIPr76.json'}

exec(code, env_args)
