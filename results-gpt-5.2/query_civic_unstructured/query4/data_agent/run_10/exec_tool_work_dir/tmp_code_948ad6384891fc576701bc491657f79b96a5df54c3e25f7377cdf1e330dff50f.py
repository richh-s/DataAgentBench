code = """import json, re

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_PZeGpCzqKK9GItmbLxvBqimS)
funding = load_json_maybe(var_call_R6KQ8EGMbxxtALdSfG7IqwUR)

fund_map = {r.get('Project_Name'): int(r.get('total_amount')) for r in funding if r.get('Project_Name') is not None and r.get('total_amount') is not None}

season_pat = re.compile(r"\\b(Spring|Summer|Fall|Winter)\\b\\s*,?\\s*(\\d{4})", re.IGNORECASE)

proj_starts = {}

skip_prefixes = (
    'page ', 'agenda item', 'to', 'prepared by', 'approved by', 'date prepared',
    'meeting date', 'subject', 'recommended action', 'discussion',
    'capital improvement projects', 'disaster recovery projects'
)

for d in docs:
    t = (d.get('text') or '').replace('\r','')
    if not t:
        continue
    lines = t.split('\n')
    last_name = None
    for line in lines:
        s = line.strip()
        if not s:
            continue
        s_low = s.lower()
        if len(s) <= 120 and ':' not in s and (not s_low.startswith(skip_prefixes)) and '(cid' not in s_low:
            if not re.match(r"^\(?cid[:\d]", s_low):
                last_name = s
        if last_name and re.search(r"\\bBegin\\b", s, flags=re.IGNORECASE):
            sm = season_pat.search(s)
            if sm:
                season = sm.group(1).capitalize()
                year = sm.group(2)
                start = year + '-' + season
                if last_name not in proj_starts:
                    proj_starts[last_name] = start
                else:
                    def key(val):
                        y, seas = val.split('-')
                        order = {'Winter':1,'Spring':2,'Summer':3,'Fall':4}.get(seas,9)
                        return (int(y), order)
                    if key(start) < key(proj_starts[last_name]):
                        proj_starts[last_name] = start

spring2022 = sorted([p for p, st in proj_starts.items() if st.lower() == '2022-spring'])
count = len(spring2022)
total = sum(fund_map.get(p, 0) for p in spring2022)

out = {"projects_started_spring_2022": count, "total_funding": total, "projects": spring2022}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PZeGpCzqKK9GItmbLxvBqimS': 'file_storage/call_PZeGpCzqKK9GItmbLxvBqimS.json', 'var_call_R6KQ8EGMbxxtALdSfG7IqwUR': 'file_storage/call_R6KQ8EGMbxxtALdSfG7IqwUR.json'}

exec(code, env_args)
