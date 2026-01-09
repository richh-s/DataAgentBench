code = """import json, re
import pandas as pd

with open(var_call_E3A3KNZAloQm34K4K1JvVvyY,'r') as f:
    funding=json.load(f)
df_f=pd.DataFrame(funding)
df_f['Amount']=pd.to_numeric(df_f['Amount'], errors='coerce').fillna(0).astype(int)

with open(var_call_tvobrBCauIeEF7HgXhjZu1Qp,'r') as f:
    docs=json.load(f)

header=re.compile(r'^Disaster Projects', re.I)
begin=re.compile(r'Begin Construction:.*2022|Begin Design:.*2022|Award Contract and Begin Construction:.*2022', re.I)

projects=set()
for d in docs:
    lines=[ln.strip() for ln in d.get('text','').splitlines()]
    in_dis=False
    last_title=None
    for s in lines:
        if header.search(s):
            in_dis=True
            last_title=None
            continue
        if not in_dis:
            continue
        if re.match(r'^(Page\s+\d+\s+of\s+\d+|Agenda Item)', s) or not s:
            continue
        # detect titles: no colon, contains Project or parentheses or Road/Park/Drain etc, and not starting with (cid
        if (':' not in s) and (not s.startswith('(cid')):
            if len(s)<140 and re.search(r'(Project|\(|Road|Park|Drain|Canyon|Bridge|Guardrail|Warning|Storm|Fire|FEMA|CalOES|CalJPIA)', s):
                if not re.match(r'^(Updates|Project Schedule|Estimated Schedule|Project Description|Completion Date)\b', s, re.I):
                    last_title=s
        if begin.search(s) and last_title:
            projects.add(last_title)

matched=df_f[df_f['Project_Name'].isin(projects)].groupby('Project_Name', as_index=False)['Amount'].sum()

total=int(matched['Amount'].sum()) if not matched.empty else 0

print('__RESULT__:')
print(json.dumps({'total_funding_amount_usd': total,'num_projects_started_2022': len(projects),'projects_started_2022': sorted(projects),'matched_projects': matched.sort_values('Project_Name').to_dict(orient='records')}))"""

env_args = {'var_call_cguj2JY470StqtvTJdpADgC5': ['Funding'], 'var_call_E3A3KNZAloQm34K4K1JvVvyY': 'file_storage/call_E3A3KNZAloQm34K4K1JvVvyY.json', 'var_call_JESPpTsMF7CJnZLezqHiSbmp': 'file_storage/call_JESPpTsMF7CJnZLezqHiSbmp.json', 'var_call_jtmPqoYIzrjKo9fcalJWNbHi': {'total_funding_amount_usd': 0, 'num_disaster_projects_started_2022_with_funding_match': 0, 'matched_projects': [], 'extracted_disaster_projects_started_2022': [], 'num_extracted_disaster_projects_started_2022': 0}, 'var_call_tvobrBCauIeEF7HgXhjZu1Qp': 'file_storage/call_tvobrBCauIeEF7HgXhjZu1Qp.json', 'var_call_tJzkUAZC0U6FljVuIHL5Zb4r': {'total_funding_amount_usd': 0, 'projects_started_2022': [], 'matched_projects': []}, 'var_call_QlDZ95qcwba9mOGHz6EZeCrk': {'snippet': 'Disaster Projects (Design)\n\nBroad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)\n\n(cid:190) Updates:\n\n(cid:131) The project consultant prepared the specifications for the project. Staff\n\nis finalizing the bid documents.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: February 2022\n(cid:131) Begin Construction: Spring 2022\n\nLatigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)\n\n(cid:190) Updates:\n\n(cid:131) Staff is finalizing the design of this project.\n(cid:131) Staff is also working with FEMA/CalOES to substitute the existing\n\ntimber with non-combustible materials.\n\n(cid:190) Project Schedule\n\n(cid:131) Complete Design: February 2022\n(cid:131) Begin Construction: April 2022\n\nTrancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)\n\n(cid:190) Updates:\n\n(cid:131) The project consultant has started the design of this project.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Spring 2022\n\nTrancas Canyon Park Slope Stabilization Project (CalJPIA Project)\n\n(cid:190) Updates:\n\n(cid:131) The project consultant has started the design of this project.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Spring 2022\n\nStorm Drain Master Plan (FEMA Project)\n\nPage 5 of 8\n\nAgenda Item # 4.A.\n\n\n\n\n\n\n\n\n\n\n(cid:190) Project Description: This project will be funded through a grant from FEMA\nafter the Woolsey Fire. The City will create a complete inventory of storm\ndrains, culverts, debris basins, manholes, and other drainage structures\nwithin the City.\n\n(cid:190) Updates: Council approved an agreement in December for design services.\n\nA kick-off meeting was held in late December.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Completion Date: Spring 2022\n\nGuardrail Replacement Citywide (FEMA Project)\n\n(cid:190) Project Description: This project consisted of replacing the damaged\n\nguardrail throughout the City as a result of the Woolsey Fire.\n\nCorral Canyon Road Bridge Repairs (FEMA Project)\n\n(cid:190) Project Description: This project consisted of replacing fire damaged existing\nfencing and repairing the damaged embankment adjacent to the bridge.\n\nCorral Canyon Culvert Repairs (FEMA Project)\n\n(cid:190) Project Description: This project has been cancelled as it could not get FEMA\n\napproval.\n\n(cid:190)\n\nBirdview Avenue Improvements (CalOES Project)\n(cid:190) Updates: This project was\nincluded\n\nin\n\nthe Malibu Park Drainage\n\nImprovement.\n\nMalibu Park Drainage Improvements\n\n(cid:190) Updates: The Contractor completed the repairs to storm drains on Cuthbert\nRoad, Morning View Drive, Busch Drive, Harvester Road and Birdview\nAvenue. This project is scheduled to be accepted by the Council at the\nJanuary 24, 2022 meeting.\n\nClover Heights Storm Drain (FEMA Project)\n\n(cid:190) Project Description: This project consists of design and construction of a few\nstorm drains on Clover Heights. The existing storm drain facility ends at '}, 'var_call_BnZrI6jTz2SUaFj76XZ93wjH': {'total_funding_amount_usd': 0, 'num_projects': 0, 'projects_started_2022': [], 'matched_projects': []}, 'var_call_X1pRZIM4gUK4oEesl0bhXboa': [], 'var_call_okjQ2o8N9Fb2N8ZMR6sLapOk': {'count': 14, 'contexts': ['(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n', '(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring/Summer 2022\n', '\n(cid:131) Complete Final Design: Spring 2022\n(cid:131) Advertise: Spring/Summer 2022\n(cid:131) Award Contract and Begin Construction: Spring/Summer 2022\n', '(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer/Winter 2022\n', '\n(cid:131) Complete Design: December 2021\n(cid:131) Advertise for Bidding: February 2022\n(cid:131) Begin Construction: Fall 2022\n', '(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Spring 2022\n', '(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: To be determined\n', '(cid:190) Project Schedule:\n\n(cid:131) Complete Design: February 2022\n(cid:131) Begin Construction: Spring 2022\n', '(cid:190) Project Schedule\n\n(cid:131) Complete Design: February 2022\n(cid:131) Begin Construction: April 2022\n', '(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Spring 2022\n']}, 'var_call_LQw9JOZSDzzrCmXfuWXrCS65': [{'project': 'is finalizing the bid documents.', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'project': 'timber with non-combustible materials.', 'line': '(cid:131) Begin Construction: April 2022'}, {'project': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'project': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'project': 'beginning in April 2022.', 'line': '(cid:131) Begin Construction: April 2022'}, {'project': 'started and is anticipated to be completed by the Spring of 2022.', 'line': '(cid:131) Begin Construction: Fall 2022'}, {'project': 'beginning in Fall 2022.', 'line': '(cid:131) Begin Construction: Fall 2022'}]}

exec(code, env_args)
