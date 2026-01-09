code = """import json, re

# Load civic docs
civic_src = var_call_2t22R3UaX4Znxt0xz8fGYIAP
if isinstance(civic_src, str):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

# Load funding per project
fund_src = var_call_CAVbt0EfwT8uPhTQKJt2uLzX
if isinstance(fund_src, str):
    with open(fund_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = fund_src

fund_map = {r['Project_Name']: int(r['total_amount']) for r in funding}
project_names = sorted(fund_map.keys(), key=len, reverse=True)

pat = re.compile(r"Begin Construction:\s*Spring\s*,?\s*2022", re.IGNORECASE)

started=set()
for doc in civic_docs:
    t = doc.get('text','') or ''
    if not pat.search(t):
        continue
    for pn in project_names:
        if pn not in t:
            continue
        if re.search(re.escape(pn)+r"[\s\S]{0,2500}Begin Construction:\s*Spring\s*,?\s*2022", t, flags=re.IGNORECASE):
            started.add(pn)

count=len(started)
total=sum(fund_map.get(p,0) for p in started)

print('__RESULT__:')
print(json.dumps({"count": count, "total_funding": total, "projects": sorted(started)}))"""

env_args = {'var_call_KGer4GH8D7ZnCWgfNaReubzl': ['Funding'], 'var_call_2t22R3UaX4Znxt0xz8fGYIAP': 'file_storage/call_2t22R3UaX4Znxt0xz8fGYIAP.json', 'var_call_CAVbt0EfwT8uPhTQKJt2uLzX': 'file_storage/call_CAVbt0EfwT8uPhTQKJt2uLzX.json', 'var_call_gqCYwIbXiadWD03lxJ9pO1c8': {'projects_started_spring_2022_count': 0, 'projects_started_spring_2022_total_funding': 0, 'projects': []}, 'var_call_hsVw4mCiG6dQp2xLIQfz2jeb': {'docs_with_spring_2022': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt', 'malibucity_agenda__03242021-1665.txt', 'malibucity_agenda__04282021-1687.txt', 'malibucity_agenda__05262021-1701.txt', 'malibucity_agenda__06222022-1919.txt', 'malibucity_agenda__06232021-1714.txt', 'malibucity_agenda__07272022-1939.txt', 'malibucity_agenda__07282021-1732.txt', 'malibucity_agenda__08252021-1746.txt', 'malibucity_agenda__09222021-1765.txt', 'malibucity_agenda__10272021-1779.txt', 'malibucity_agenda__11102022-1995.txt', 'malibucity_agenda__12142021-1808.txt'], 'count': 16}, 'var_call_cCUdQoS7XMceY7cQId4wBuHF': {'filename': 'malibucity_agenda__03232022-1869.txt', 'snippets': ['ds\nshortly after final approval. If possible, the construction of this project\nwill begin in conjunction with the PCH Median Improvement\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Final Design: Spring 2022\n(cid:131) Advertise: Summer 2022\n(cid:131) Award Contract and Begin Construction: Summer 2022\n\nWestward Beach Road Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) The design plans were', 'ds on February 24, 2022. Award of contract is\n\nscheduled for the April 11, 2022 Council meeting.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: February 2022\n(cid:131) Begin Construction: Spring 2022\n\nPermanent Skate Park\n\n(cid:190) Project Description: This project includes designing and constructing a\npermanent skate park located on the Crummer/Case Court parcel adjacent\nto Malibu Bl', 'consultant over\nthe past several months to complete the engineering work, and the final\ndraft plans are expected to be completed in early 2022. The Planning\nCommission will then review the project in Spring 2022 before final\nreview by the Council.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: To be determined\n\nPage 3 of 8\n\nAgenda Item # 4.A.\n\n', 'ected to be completed in early 2022. The Planning\nCommission will then review the project in Spring 2022 before final\nreview by the Council.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: To be determined\n\nPage 3 of 8\n\nAgenda Item # 4.A.\n\n\n\n\n\n\n\n\n\nPCH at Trancas Canyon Road Right Turn Lane\n\n(cid:190) Project Description: This project consists of', 'qualified consultant. It is anticipated that the agreement will\ngo to Council in April 2022 after the Funding Agreement is issued by\nMetro.\n(cid:190) Estimated Schedule:\n\n(cid:131) Begin Design: Late Spring 2022\n\nCapital Improvement Projects (Construction)\n\nThe City does not have projects in construction at this time.\n\nCapital Improvement Projects (Not Started)\n\nVehicle Protection Devices\n\n(cid:19', '1) The project consultant prepared the specifications for the project. Staff\n\nis finalizing the bid documents.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Advertise: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)\n\n(cid:190) Updates:\n\n(cid:131) Staff is finalizing the design of this proje', ':131) Staff is also working with FEMA/CalOES to substitute the existing\n\ntimber with non-combustible materials.\n\n(cid:190) Project Schedule\n\n(cid:131) Complete Design: April 2022\n(cid:131) Advertise: Spring 2022\n(cid:131) Begin Construction: Spring 2022\n\nPage 5 of 8\n\nAgenda Item # 4.A.\n\n\n\n\n\n\n\n\n\n\n\n\nTrancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)\n\n(cid:190) Updates:\n\n(cid:', 'ES to substitute the existing\n\ntimber with non-combustible materials.\n\n(cid:190) Project Schedule\n\n(cid:131) Complete Design: April 2022\n(cid:131) Advertise: Spring 2022\n(cid:131) Begin Construction: Spring 2022\n\nPage 5 of 8\n\nAgenda Item # 4.A.\n\n\n\n\n\n\n\n\n\n\n\n\nTrancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)\n\n(cid:190) Updates:\n\n(cid:131) The project consultant has started th', 'ng and Irrigation Repairs (CalJPIA/FEMA Project)\n\n(cid:190) Updates:\n\n(cid:131) The project consultant has started the design of this project.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nTrancas Canyon Park Slope Stabilization Project (CalJPIA Project)\n\n(cid:190) Updates:\n\n(cid:131) The project consultant has started the design of', 'rk Slope Stabilization Project (CalJPIA Project)\n\n(cid:190) Updates:\n\n(cid:131) The project consultant has started the design of this project.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nStorm Drain Master Plan (FEMA Project)\n\n(cid:190) Project Description: This project is funded through a grant from FEMA after\nthe Woolsey Fire. T']}, 'var_call_4J1W85yqMBASV5Hs9wHE6soO': {'count': 0, 'total_funding': 0, 'projects': []}, 'var_call_LV9XxtMeD5ggCUnAXAvGQimc': {'count': 0, 'projects': []}, 'var_call_DD9MyFoz1JZ92eLPPQE7Ingj': {'filename': 'malibucity_agenda__03232022-1869.txt', 'matching_lines': ['(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022'], 'n': 3}, 'var_call_YMy5rRVpFKcbpI23MVldJnth': {'count': 24, 'projects': ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'PCH Median Improvements at Paradise Cove and Zuma Beach', 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project', 'Civic Center Water Treatment Facility Phase 2', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain (FEMA Project)', 'Westward Beach Road Improvements Project', 'Storm Drain Master Plan (FEMA Project)', 'Latigo Canyon Road Culvert Repairs', 'Corral Canyon Road Bridge Repairs', '2021 Annual Street Maintenance', 'Civic Center Way Improvements', 'Bluffs Park Shade Structure', 'Clover Heights Storm Drain', 'Annual Street Maintenance', 'Storm Drain Master Plan']}}

exec(code, env_args)
