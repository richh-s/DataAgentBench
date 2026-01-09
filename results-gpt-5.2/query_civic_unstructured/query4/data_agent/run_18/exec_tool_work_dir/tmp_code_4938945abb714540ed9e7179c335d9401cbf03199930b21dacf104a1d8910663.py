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

begin_spring22 = re.compile(r"Begin\s+Construction\s*:\s*Spring\s*2022", re.IGNORECASE)

projects=set()
for d in docs:
    lines=[ln.strip() for ln in str(d.get('text','')).splitlines()]
    for i, ln in enumerate(lines):
        if begin_spring22.search(ln):
            # scan upward for last project title: line not empty and not starting with '(' and not containing ':' and not generic headers
            for j in range(i-1, max(-1,i-80), -1):
                cand=lines[j]
                if not cand:
                    continue
                if cand.startswith('(cid'):
                    continue
                if ':' in cand:
                    continue
                if re.search(r"Capital Improvement Projects|Disaster Projects|Disaster Recovery Projects|Project Schedule|Estimated Schedule|Updates|Project Description|Recommended Action|Discussion", cand, re.IGNORECASE):
                    continue
                projects.add(cand)
                break

# funding
missing=[]
total=0
for p in projects:
    if p in fund_map:
        total+=int(fund_map[p])
    else:
        missing.append(p)

print('__RESULT__:')
print(json.dumps({'count': len(projects), 'projects': sorted(projects), 'total_funding': int(total), 'missing': sorted(missing)[:50]}))"""

env_args = {'var_call_0f7yDI4ecmLKSKpoaVFu2vZD': 'file_storage/call_0f7yDI4ecmLKSKpoaVFu2vZD.json', 'var_call_27VpEJXZf7UZvZlIuZtK2xrL': 'file_storage/call_27VpEJXZf7UZvZlIuZtK2xrL.json', 'var_call_WYLUmmwObGXwduLEEijbEoV5': {'spring_2022_project_count': 0, 'spring_2022_total_funding_matched': 0, 'matched_project_count': 0, 'missing_funding_project_count': 0, 'missing_projects_sample': []}, 'var_call_XLDXr8FDGIphVyw4C4Q3qfWR': {'line_hits': 0, 'samples': []}, 'var_call_i92AmPWPnkGbKjl9Z3o4vfog': {'docs_with_spring2022': 4, 'samples': [' Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) The project was', 'liminate this issue.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (', 'liminate this issue.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (', 'dian Improvement\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Final Design: Spring 2022\n(cid:131) Advertise: Summer 2022\n(cid:131) Award Contract and Begin Constructio']}, 'var_call_zCqf1WbLjtYkipYn3bBW8Sx6': {'projects_started_spring_2022': [], 'project_count': 0, 'total_funding_matched': 0, 'matched_count': 0, 'missing_count': 0, 'missing_projects': []}, 'var_call_9OVRbthoX8UjJjqhxVPnzzfM': {'docs': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt'], 'count_docs': 4}, 'var_call_hGjqlEFP5FEsURnqkLtIjuvn': 'file_storage/call_hGjqlEFP5FEsURnqkLtIjuvn.json', 'var_call_O8HZvF7xT1jHmIddur0w55jj': [], 'var_call_kTWrTCuq1UhpAJxKurSBMkAE': [{'i': 50, 'ln': '(cid:131) Begin Construction: Spring 2022', 'ctx': ['(cid:190) Project Schedule:', '', '(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring 2022', '', 'PCH Median Improvements Project']}, {'i': 88, 'ln': '(cid:131) Begin Construction: Spring/Summer 2022', 'ctx': ['(cid:190) Project Schedule:', '', '(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring/Summer 2022', '', 'PCH Signal Synchronization System Improvements Project']}, {'i': 105, 'ln': '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', 'ctx': ['', '(cid:131) Complete Final Design: Spring 2022', '(cid:131) Advertise: Spring/Summer 2022', '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', '', 'Westward Beach Road Improvements Project']}, {'i': 128, 'ln': '(cid:131) Begin Construction: Summer/Winter 2022', 'ctx': ['(cid:190) Project Schedule:', '', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Summer/Winter 2022', '', 'Civic Center Water Treatment Facility Phase 2']}, {'i': 161, 'ln': '(cid:131) Begin Construction: Fall 2022', 'ctx': ['', '(cid:131) Complete Design: December 2021', '(cid:131) Advertise for Bidding: February 2022', '(cid:131) Begin Construction: Fall 2022', '', 'Bluffs Park Shade Structure']}, {'i': 178, 'ln': '(cid:131) Begin Construction: Spring 2022', 'ctx': ['(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '', 'Permanent Skate Park']}, {'i': 200, 'ln': '(cid:131) Begin Construction: To be determined', 'ctx': ['(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: To be determined', '', 'PCH at Trancas Canyon Road Right Turn Lane']}, {'i': 327, 'ln': '(cid:131) Begin Construction: Spring 2022', 'ctx': ['(cid:190) Project Schedule:', '', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: Spring 2022', '', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)']}, {'i': 341, 'ln': '(cid:131) Begin Construction: April 2022', 'ctx': ['(cid:190) Project Schedule', '', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: April 2022', '', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)']}, {'i': 352, 'ln': '(cid:131) Begin Construction: Spring 2022', 'ctx': ['(cid:190) Project Schedule:', '', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)']}, {'i': 363, 'ln': '(cid:131) Begin Construction: Spring 2022', 'ctx': ['(cid:190) Project Schedule:', '', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '', 'Storm Drain Master Plan (FEMA Project)']}, {'i': 471, 'ln': '(cid:131) Begin Construction: April 2022', 'ctx': ['(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: April 2022', '', 'Encinal Canyon Road Drainage Improvements (CalOES Project)']}, {'i': 498, 'ln': '(cid:131) Begin Construction: Fall 2022', 'ctx': ['(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Fall 2022', '', 'Westward Beach Road Shoulder Repairs (CalOES Project)']}, {'i': 516, 'ln': '(cid:131) Begin Construction: Fall 2022', 'ctx': ['(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: July 2022', '(cid:131) Begin Construction: Fall 2022', '(cid:131)', '']}], 'var_call_fQm21K0qMF7nrBbtpemhEWEi': {'projects': [], 'count': 0, 'total_funding': 0, 'missing': []}, 'var_call_KcqBuT8oB9dl0Kl51KnC9ZnG': {'count': 0, 'projects': [], 'total_funding': 0, 'missing': []}, 'var_call_kZLOMGp8XxmJZYHQEpORGrpi': {'docs_with_begin_construction_spring_2022': 0}, 'var_call_rXDfBsg2dNa7USLwW245NhXd': {'count_docs': 4, 'filenames': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt']}}

exec(code, env_args)
