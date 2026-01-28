code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_0f7yDI4ecmLKSKpoaVFu2vZD)
fund = load_json_maybe(var_call_27VpEJXZf7UZvZlIuZtK2xrL)
fund_df = pd.DataFrame.from_records(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

begin_spring22 = re.compile(r"Begin\s+Construction\s*:\s*Spring\s*2022\b", re.IGNORECASE)

projects=set()
for d in docs:
    text=str(d.get('text',''))
    lines=[ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if begin_spring22.search(ln):
            # project name typically appears in preceding non-empty line that isn't schedule/update label
            j=i-1
            while j>=0 and not lines[j]:
                j-=1
            # if we are inside schedule, back up until blank line then take preceding non-empty as title
            name=None
            for k in range(j, max(-1,j-40), -1):
                if not lines[k]:
                    m=k-1
                    while m>=0 and not lines[m]:
                        m-=1
                    if m>=0:
                        cand=lines[m]
                        # filter out labels
                        if not re.search(r"Project Schedule|Estimated Schedule|Updates|Project Updates|Project Description|RECOMMENDED ACTION|DISCUSSION", cand, re.IGNORECASE):
                            name=cand
                    break
            if name is None and j>=0:
                name=lines[j]
            if name and not name.lower().startswith('(cid'):
                projects.add(name)

# funding total
missing=[]
total=0
for p in projects:
    if p in fund_map:
        total += int(fund_map[p])
    else:
        missing.append(p)

print('__RESULT__:')
print(json.dumps({'count': len(projects), 'projects': sorted(projects), 'total_funding': int(total), 'missing': sorted(missing)[:30]}))"""

env_args = {'var_call_0f7yDI4ecmLKSKpoaVFu2vZD': 'file_storage/call_0f7yDI4ecmLKSKpoaVFu2vZD.json', 'var_call_27VpEJXZf7UZvZlIuZtK2xrL': 'file_storage/call_27VpEJXZf7UZvZlIuZtK2xrL.json', 'var_call_WYLUmmwObGXwduLEEijbEoV5': {'spring_2022_project_count': 0, 'spring_2022_total_funding_matched': 0, 'matched_project_count': 0, 'missing_funding_project_count': 0, 'missing_projects_sample': []}, 'var_call_XLDXr8FDGIphVyw4C4Q3qfWR': {'line_hits': 0, 'samples': []}, 'var_call_i92AmPWPnkGbKjl9Z3o4vfog': {'docs_with_spring2022': 4, 'samples': [' Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) The project was', 'liminate this issue.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (', 'liminate this issue.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (', 'dian Improvement\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Final Design: Spring 2022\n(cid:131) Advertise: Summer 2022\n(cid:131) Award Contract and Begin Constructio']}, 'var_call_zCqf1WbLjtYkipYn3bBW8Sx6': {'projects_started_spring_2022': [], 'project_count': 0, 'total_funding_matched': 0, 'matched_count': 0, 'missing_count': 0, 'missing_projects': []}, 'var_call_9OVRbthoX8UjJjqhxVPnzzfM': {'docs': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt'], 'count_docs': 4}, 'var_call_hGjqlEFP5FEsURnqkLtIjuvn': 'file_storage/call_hGjqlEFP5FEsURnqkLtIjuvn.json', 'var_call_O8HZvF7xT1jHmIddur0w55jj': [], 'var_call_kTWrTCuq1UhpAJxKurSBMkAE': [{'i': 50, 'ln': '(cid:131) Begin Construction: Spring 2022', 'ctx': ['(cid:190) Project Schedule:', '', '(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring 2022', '', 'PCH Median Improvements Project']}, {'i': 88, 'ln': '(cid:131) Begin Construction: Spring/Summer 2022', 'ctx': ['(cid:190) Project Schedule:', '', '(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring/Summer 2022', '', 'PCH Signal Synchronization System Improvements Project']}, {'i': 105, 'ln': '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', 'ctx': ['', '(cid:131) Complete Final Design: Spring 2022', '(cid:131) Advertise: Spring/Summer 2022', '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', '', 'Westward Beach Road Improvements Project']}, {'i': 128, 'ln': '(cid:131) Begin Construction: Summer/Winter 2022', 'ctx': ['(cid:190) Project Schedule:', '', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Summer/Winter 2022', '', 'Civic Center Water Treatment Facility Phase 2']}, {'i': 161, 'ln': '(cid:131) Begin Construction: Fall 2022', 'ctx': ['', '(cid:131) Complete Design: December 2021', '(cid:131) Advertise for Bidding: February 2022', '(cid:131) Begin Construction: Fall 2022', '', 'Bluffs Park Shade Structure']}, {'i': 178, 'ln': '(cid:131) Begin Construction: Spring 2022', 'ctx': ['(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '', 'Permanent Skate Park']}, {'i': 200, 'ln': '(cid:131) Begin Construction: To be determined', 'ctx': ['(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: To be determined', '', 'PCH at Trancas Canyon Road Right Turn Lane']}, {'i': 327, 'ln': '(cid:131) Begin Construction: Spring 2022', 'ctx': ['(cid:190) Project Schedule:', '', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: Spring 2022', '', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)']}, {'i': 341, 'ln': '(cid:131) Begin Construction: April 2022', 'ctx': ['(cid:190) Project Schedule', '', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: April 2022', '', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)']}, {'i': 352, 'ln': '(cid:131) Begin Construction: Spring 2022', 'ctx': ['(cid:190) Project Schedule:', '', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)']}, {'i': 363, 'ln': '(cid:131) Begin Construction: Spring 2022', 'ctx': ['(cid:190) Project Schedule:', '', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '', 'Storm Drain Master Plan (FEMA Project)']}, {'i': 471, 'ln': '(cid:131) Begin Construction: April 2022', 'ctx': ['(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: April 2022', '', 'Encinal Canyon Road Drainage Improvements (CalOES Project)']}, {'i': 498, 'ln': '(cid:131) Begin Construction: Fall 2022', 'ctx': ['(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Fall 2022', '', 'Westward Beach Road Shoulder Repairs (CalOES Project)']}, {'i': 516, 'ln': '(cid:131) Begin Construction: Fall 2022', 'ctx': ['(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: July 2022', '(cid:131) Begin Construction: Fall 2022', '(cid:131)', '']}], 'var_call_fQm21K0qMF7nrBbtpemhEWEi': {'projects': [], 'count': 0, 'total_funding': 0, 'missing': []}}

exec(code, env_args)
