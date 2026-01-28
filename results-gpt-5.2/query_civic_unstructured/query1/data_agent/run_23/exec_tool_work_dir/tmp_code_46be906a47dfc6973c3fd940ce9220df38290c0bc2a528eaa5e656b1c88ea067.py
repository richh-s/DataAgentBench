code = """import json, re

# load funding names
fund = var_call_nIH2g1Y7CWpxAGgLZym4ZROD
if isinstance(fund, str):
    with open(fund, 'r', encoding='utf-8') as f:
        fund = json.load(f)
fund_names = set(r['Project_Name'] for r in fund if r.get('Project_Name') is not None)

# load extracted design projects
ex = var_call_stDSPIg3DSyDPQFJ0EZpdOlr
if isinstance(ex, str):
    ex = json.loads(ex)
# we didn't store full set earlier, recompute quickly from docs file again for accuracy but with better filtering

docs = var_call_tusdBk6MktgfX48BczKJWKck
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

header_pat = re.compile(r'Capital Improvement Projects\s*\(\s*Design\s*\)', re.IGNORECASE)
stop_pat = re.compile(r'Capital Improvement Projects\s*\(\s*(Construction|Not Started)\s*\)|Disaster Recovery Projects', re.IGNORECASE)

bad_prefixes = (
    '(cid', '•', '-', 'updates', 'project schedule', 'estimated schedule', 'project description',
    'page ', 'agenda item', 'discussion', 'recommended action', 'to:', 'prepared by', 'approved by',
    'date prepared', 'meeting date', 'subject'
)

def is_project_line(ln:str)->bool:
    if not ln or len(ln)>120: return False
    low=ln.lower().strip()
    for bp in bad_prefixes:
        if low.startswith(bp):
            return False
    # reject obvious narrative/sentence fragments
    if re.search(r'\b(city|staff|council|consultant|caltrans|county)\b.*\b(will|is|are|was|were|working|submitted|awaiting)\b', low):
        return False
    if re.search(r'\b(spring|summer|fall|winter)\b\s*20\d\d', low):
        return False
    if ':' in ln:  # schedule lines
        return False
    # must contain a letter
    if not re.search(r'[A-Za-z]', ln):
        return False
    # avoid trailing comma/period
    if ln.strip().endswith(('.',',')):
        return False
    return True

projects_design=set()
for d in docs:
    text=d.get('text','') or ''
    for m in header_pat.finditer(text):
        rest=text[m.end():]
        sm=stop_pat.search(rest)
        section=rest[:sm.start()] if sm else rest
        for ln in (x.strip() for x in section.splitlines()):
            if is_project_line(ln):
                projects_design.add(ln)

# Intersect
matched = sorted(projects_design & fund_names)

print('__RESULT__:')
print(json.dumps({'count': len(matched), 'matched_sample': matched[:50]}))"""

env_args = {'var_call_eAygeFmmLDqweYUC98CP3LRU': [{'cnt': '276'}], 'var_call_tusdBk6MktgfX48BczKJWKck': 'file_storage/call_tusdBk6MktgfX48BczKJWKck.json', 'var_call_stDSPIg3DSyDPQFJ0EZpdOlr': {'design_projects_extracted_count': 154, 'sample': ['14th Council meeting bids will be rejected. The bids came in higher', '2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements', '2022-2023 budget. Upon the adoption of the budget, the revised', '2022. The Regional Board has approved the request and modified the', '2022. This project requires Caltrans approval since the work will be on', '8, 2021. This project received Caltrans approval since the work will be', '8, 2021. This project requires Caltrans approval since the work will be', 'Annual Street Maintenance', 'Bluffs Park Shade Structure', 'Caltrans for the final project approvals. Interviews were conducted with', 'Caltrans. The project is currently out to bids with bids due December', 'Canyon Road near Harbor Vista Drive and Potter Lane to determine if any', 'City will be issuing a RFQ/P for design services in the summer of 2023', 'Civic Center Stormwater Diversion Structure', 'Civic Center Water Treatment Facility Phase 2', 'Clover Heights Storm Drainage Improvements', 'Coastal Development Permit and directed the Public Works and Public', 'Commission meeting for project direction due to concerns regarding', 'Commission will then review the project in Spring 2022 before final', 'Commission will then review the project in Summer 2022 before final', 'Commission. Staff is coordinating with Caltrans for the final project', 'Council directed staff to withdraw the proposed project and associated', 'Council on March 14, 2022. Bids were opened and at the November', 'County and will be finalizing the design. The approved CDP was', 'In August, the City released a request for proposals from consultants', 'In May 2021, the Council approved funding for additional engineering', 'Individual letters were mailed to all properties within Phase 2 with their', 'Interviews were conducted with qualified consultants to provide']}, 'var_call_nIH2g1Y7CWpxAGgLZym4ZROD': 'file_storage/call_nIH2g1Y7CWpxAGgLZym4ZROD.json'}

exec(code, env_args)
