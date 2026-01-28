code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

funding = load_records(var_call_YgUR6tR7zkFTdknoL5kz9DLG)
docs = load_records(var_call_ColyzPVLwrm6y70pEszOjYFI)

fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Extract project blocks under "Disaster Recovery Projects" and their Begin Construction dates
projects = {}

begin_pat = re.compile(r'\b(Begin\s+Construction|Construction\s+Start|Start\s+Construction)\s*:\s*(.+)$', re.IGNORECASE)
sched_start_pat = re.compile(r'^\s*(Project\s+Schedule|Estimated\s+Schedule)\b', re.IGNORECASE)
section_start_pat = re.compile(r'^\s*Disaster\s+Recovery\s+Projects', re.IGNORECASE)
section_end_pat = re.compile(r'^\s*(Capital\s+Improvement\s+Projects|Staff\s+has\s+also\b)', re.IGNORECASE)

for d in docs:
    t = d.get('text','') or ''
    lines = [ln.strip() for ln in t.splitlines()]
    in_disaster = False
    current_project = None
    in_schedule = False
    for ln in lines:
        if not ln:
            continue
        if section_start_pat.match(ln):
            in_disaster = True
            current_project = None
            in_schedule = False
            continue
        if in_disaster and section_end_pat.match(ln):
            in_disaster = False
            current_project = None
            in_schedule = False
            continue
        if not in_disaster:
            continue

        if sched_start_pat.match(ln):
            in_schedule = True
            continue

        # new project name when not bullet and not a known header and no colon
        if not ln.startswith('(cid') and ':' not in ln and not re.match(r'^(Updates|Project\s+Description|Discussion|Recommended\s+Action|Page\s+\d+|Agenda\s+Item)', ln, re.IGNORECASE):
            # if looks like a title and not schedule line item
            if len(ln) <= 120 and not re.match(r'^(Complete\s+Design|Advertise|Begin\s+Construction|Final\s+Design|Complete\s+Construction)\b', ln, re.IGNORECASE):
                current_project = ln
                in_schedule = False
                projects.setdefault(current_project, {'type':'disaster','st':None})
                continue

        if in_schedule and current_project:
            m = begin_pat.search(ln)
            if m:
                st = m.group(2).strip()
                # set if none
                if projects[current_project].get('st') is None:
                    projects[current_project]['st'] = st
                continue

# Filter for start year 2022
names_2022 = [n for n,info in projects.items() if info.get('st') and '2022' in info['st']]

fund_2022 = fund_df[fund_df['Project_Name'].isin(names_2022)]
total = int(fund_2022['total_amount'].sum())

out = {
    'total_funding_disaster_projects_started_2022': total,
    'num_projects': int(fund_2022.shape[0]),
    'projects': fund_2022.sort_values('Project_Name')[['Project_Name','total_amount']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YgUR6tR7zkFTdknoL5kz9DLG': 'file_storage/call_YgUR6tR7zkFTdknoL5kz9DLG.json', 'var_call_ColyzPVLwrm6y70pEszOjYFI': 'file_storage/call_ColyzPVLwrm6y70pEszOjYFI.json', 'var_call_iMOex9cPQGXibS0Ruz0oHmZx': {'total_funding_disaster_projects_started_2022': 0, 'num_projects': 0, 'projects': []}, 'var_call_uyEKkowH2QsE9w1Wg144VzsZ': {'filename': 'malibucity_agenda_03222023-2060.txt', 'snippet': '\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n(cid:131) Begin Construction: Fall 2023\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) On September 22, 2022, the City received four (4) construction bids\n\nand rejected all bids due to a budget shortfall\n\n(cid:131) City will work with the design consultant to review design alternatives\n\nor phasing out the project\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n\nPage 1 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Repair Project\n\n(cid:190) Updates:\n\n(cid:131) City working with consultant on the design of the shoulder repairs\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Drainage Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) Plans are under review by Fish and Wildlife and City is expecting\ncomments mid-April. This project required their review since the project\nscope falls within Zuma Canyon Creek. Army Corp. of Engineers has\ncleared the project.\n\n(cid:190) Project Schedule:\n\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nClover Heights Storm Drainage Improvements\n\n(cid:190) Updates:\n\n(cid:131) City submitted plans to CalOES for review and working with consultant\n\nto finalize plans and specifications\n\n(cid:190) Project Schedule:\n\n(cid:131) Final Design: Summer, 2023\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nLatigo Canyon Road Retaining Wall Repair Project\n\n(cid:190) Updates:\n\n(cid:131) Plans and specifications have been completed\n(cid:131) Awaiting final FEMA/CalOES approval for scope modification\n\n(cid:190) Project Schedule:\n\n(cid:131) Advertise: Spring 2023\n(cid:131) Begin Construction: Summer 2023\n\nStorm Drain Master Plan\n'}}

exec(code, env_args)
