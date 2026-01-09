code = """import json, re

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

funding = load_json_maybe(var_call_9VTcyE0rwaemK7cQ94kOlwa6)
docs = load_json_maybe(var_call_qSNM8svbdwVUOUeF2YIBUzBK)

funding_map = {r['Project_Name']: int(r['total_amount']) for r in funding if r.get('Project_Name')}

# Determine disaster-related project names via keywords in name (FEMA/CalOES/CalJPIA) or appears under disaster sections.

disaster_names = set()

# name-based
for name in funding_map:
    if re.search(r'\bFEMA\b|CalOES|CalJPIA|Disaster|Woolsey|Fire', name, re.I):
        disaster_names.add(name)

# doc-based: projects appearing after 'Disaster Recovery Projects' heading until next 'Capital Improvement Projects' (or end)
for d in docs:
    text = d.get('text','') or ''
    lines = text.splitlines()
    in_disaster = False
    for ln in lines:
        if re.search(r'Disaster Recovery Projects', ln, re.I):
            in_disaster = True
            continue
        if in_disaster and re.search(r'Capital Improvement Projects', ln, re.I):
            in_disaster = False
        if in_disaster:
            s = ln.strip()
            if s in funding_map:
                disaster_names.add(s)

# Now find those with start/begin lines containing 2022 within 30 lines after occurrence in any doc
starts_re = re.compile(r'^(?:\(cid:131\)\s*)?(?:Start|Begin)\s*(?:Construction|Design)?\s*:\s*(.+?)\s*$', re.I)

started_2022 = set()
for d in docs:
    text = d.get('text','') or ''
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if ln in disaster_names:
            for j in range(i+1, min(i+35, len(lines))):
                m = starts_re.match(lines[j])
                if m and '2022' in m.group(1):
                    started_2022.add(ln)
                    break

# If no explicit start lines, also accept project names that themselves include '2022 ' prefix (started in 2022)
for name in list(disaster_names):
    if re.match(r'^2022\b', name):
        started_2022.add(name)

# Sum
selected = sorted(started_2022)
total = sum(funding_map.get(n, 0) for n in selected)

print('__RESULT__:')
print(json.dumps({'total_funding_usd': total, 'project_count': len(selected), 'projects': selected}))"""

env_args = {'var_call_9VTcyE0rwaemK7cQ94kOlwa6': 'file_storage/call_9VTcyE0rwaemK7cQ94kOlwa6.json', 'var_call_qSNM8svbdwVUOUeF2YIBUzBK': 'file_storage/call_qSNM8svbdwVUOUeF2YIBUzBK.json', 'var_call_VEb87KrIX5pu8BEnQ3XJsuii': {'total_funding_usd': 0, 'matched_disaster_projects_started_2022_count': 0, 'matched_disaster_projects_started_2022': []}, 'var_call_V3VoQYl4KFgoq7mHfZHkep3h': {'docs_with_disaster_section': 5, 'unique_funding_projects_found_in_disaster_docs': 81, 'top_projects': [['PCH Signal Synchronization System Improvements Project', 5], ['Civic Center Water Treatment Facility Phase 2', 5], ['Marie Canyon Green Streets', 5], ['PCH Median Improvements Project', 5], ['Bluffs Park Shade Structure', 5], ['Clover Heights Storm Drain', 5], ['Malibu Road Slope Repairs', 5], ['Storm Drain Master Plan', 4], ['Broad Beach Road Water Quality Infrastructure Repairs', 4], ['Corral Canyon Road Bridge Repairs', 4], ['Corral Canyon Culvert Repairs', 4], ['Trancas Canyon Park Planting and Irrigation Repairs', 4], ['Clover Heights Storm Drain (FEMA Project)', 4], ['Civic Center Way Improvements', 4], ['Encinal Canyon Road Drainage Improvements', 4], ['Trancas Canyon Park Slope Stabilization Project', 4], ['Latigo Canyon Road Roadway/Retaining Wall Improvements', 4], ['Latigo Canyon Road Culvert Repairs', 4], ['Westward Beach Road Improvements Project', 4], ['Vehicle Protection Devices', 4], ['Civic Center Stormwater Diversion Structure', 4], ['Annual Street Maintenance', 4], ['Birdview Avenue Improvements', 4], ['PCH at Trancas Canyon Road Right Turn Lane', 3], ['Malibu Bluffs Park South Walkway', 3], ['PCH Median Improvements at Paradise Cove and Zuma Beach', 3], ['Permanent Skate Park', 3], ['Storm Drain Master Plan (FEMA Project)', 3], ['Malibu Park Drainage Improvements', 3], ['Guardrail Replacement Citywide', 3]]}, 'var_call_fUIoEWCTPuDI9aht4kH1ZLn0': {'snippet': 'Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n(cid:131) Begin Construction: Fall 2023\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) On September 22, 2022, the City received four (4) construction bids\n\nand rejected all bids due to a budget shortfall\n\n(cid:131) City will work with the design consultant to review design alternatives\n\nor phasing out the project\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n\nPage 1 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Repair Project\n\n(cid:190) Updates:\n\n(cid:131) City working with consultant on the design of the shoulder repairs\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Drainage Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) Plans are under review by Fish and Wildlife and City is expecting\ncomments mid-April. This project required their review since the project\nscope falls within Zuma Canyon Creek. Army Corp. of Engineers has\ncleared the project.\n\n(cid:190) Project Schedule:\n\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nClover Heights Storm Drainage Improvements\n\n(cid:190) Updates:\n\n(cid:131) City submitted plans to CalOES for review and working with consultant\n\nto finalize plans and specifications\n\n(cid:190) Project Schedule:\n\n(cid:131) Final Design: Summer, 2023\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nLatigo Canyon Road Retaining Wall Repair Project\n\n(cid:190) Updates:\n\n(cid:131) Plans and specifications have been completed\n(cid:131) Awaiting final FEMA/CalOES approval for scope modification\n\n(cid:190) Project Schedule:\n\n(cid:131) Advertise: Spring 2023\n(cid:131) Begin Con'}}

exec(code, env_args)
