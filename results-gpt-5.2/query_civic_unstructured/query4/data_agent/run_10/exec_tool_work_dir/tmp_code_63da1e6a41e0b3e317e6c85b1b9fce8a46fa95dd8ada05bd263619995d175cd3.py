code = """import json, re
import pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_PZeGpCzqKK9GItmbLxvBqimS)
funding = load_json_maybe(var_call_R6KQ8EGMbxxtALdSfG7IqwUR)

fund_map = {r['Project_Name']: int(r['total_amount']) for r in funding if r.get('Project_Name') is not None and r.get('total_amount') is not None}

# Extract project schedule blocks: assume pattern "<Project Name>\n...\nProject Schedule:" and then lines with "Begin" and a season/year
proj_starts = {}

season_pat = re.compile(r'\b(Spring|Summer|Fall|Winter)\b\s*(\d{4})', re.IGNORECASE)
# also allow "Spring, 2023" or "Spring 2023" within same line

for d in docs:
    text = d.get('text','')
    if not text:
        continue
    # Normalize some odd chars
    t = text.replace('\r','')
    # Find all occurrences of "Project Schedule" blocks
    for m in re.finditer(r'\n(?P<name>[A-Z0-9][^\n]{2,120})\n\s*(?:\(cid:[^\n]*\)\n\s*)*(?:Updates:.*?\n|\(cid:.*?\)\s*Updates:.*?\n|\(cid:.*?\)\s*Project Updates:.*?\n|Project Updates:.*?\n|Project Description:.*?\n|\(cid:.*?\)\s*Project Description:.*?\n|\s*)*?(?:\(cid:.*?\)\s*)*Project Schedule.*?:\s*\n(?P<body>.*?)(?=\n\s*[A-Z0-9][^\n]{2,120}\n\s*(?:\(cid:|Updates:|Project Description:|Project Updates:|Project Schedule)|\Z)', t, flags=re.IGNORECASE|re.DOTALL):
        name = m.group('name').strip()
        body = m.group('body')
        # look for Begin Construction or Begin
        begin_lines = []
        for line in body.splitlines():
            if re.search(r'\bBegin\b', line, flags=re.IGNORECASE):
                begin_lines.append(line)
        start = None
        for line in begin_lines:
            sm = season_pat.search(line)
            if sm:
                start = f"{sm.group(2)}-{sm.group(1).capitalize()}"
                break
        if start is None:
            continue
        # store if not set; if multiple, keep earliest lexicographically by year then season order
        if name not in proj_starts:
            proj_starts[name] = start
        else:
            # compare
            def key(s):
                y, seas = s.split('-')
                order = {'Winter':1,'Spring':2,'Summer':3,'Fall':4}.get(seas,9)
                return (int(y), order)
            if key(start) < key(proj_starts[name]):
                proj_starts[name] = start

# Filter Spring 2022
spring2022 = [p for p, st in proj_starts.items() if st.lower() == '2022-spring']

# Sum funding for those project names that match exactly
count = len(spring2022)
total = sum(fund_map.get(p, 0) for p in spring2022)

out = {
    "projects_started_spring_2022": count,
    "total_funding": total,
    "projects": sorted(spring2022)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PZeGpCzqKK9GItmbLxvBqimS': 'file_storage/call_PZeGpCzqKK9GItmbLxvBqimS.json', 'var_call_R6KQ8EGMbxxtALdSfG7IqwUR': 'file_storage/call_R6KQ8EGMbxxtALdSfG7IqwUR.json'}

exec(code, env_args)
