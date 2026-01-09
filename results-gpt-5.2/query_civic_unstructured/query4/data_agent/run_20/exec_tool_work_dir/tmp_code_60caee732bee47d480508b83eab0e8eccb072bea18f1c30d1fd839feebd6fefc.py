code = """import json, re
import pandas as pd

p_docs = var_call_7D8EP2WAYggkcSvlh6EUsyhx
with open(p_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

p_fund = var_call_gkn6QJLGZl3ts1HELo7BGVOs
with open(p_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'])
fund_map = dict(zip(fund_df['Project_Name'], fund_df['Total_Amount']))

begin_pat = re.compile(r"Begin Construction:\s*Spring\s*2022", re.IGNORECASE)

projects=set()
for d in docs:
    lines=[ln.strip() for ln in d.get('text','').splitlines()]
    for i,ln in enumerate(lines):
        if begin_pat.search(ln):
            # search backward for most recent non-bullet, non-parenthetical line (likely project header)
            name=None
            for j in range(i-1, -1, -1):
                cand=lines[j].strip()
                cl=cand.lower()
                if cand=='':
                    continue
                if cand.startswith('('):
                    continue
                if cl.startswith('project schedule') or cl.startswith('estimated schedule') or cl.startswith('updates') or cl.startswith('project description'):
                    continue
                if cl.startswith('complete design') or cl.startswith('complete final design') or cl.startswith('advertise') or cl.startswith('award contract'):
                    continue
                if cl.startswith('capital improvement projects') or cl.startswith('disaster recovery projects') or cl.startswith('discussion') or cl.startswith('recommended action') or cl.startswith('page '):
                    break
                # heuristic: project names are title case and not sentences; skip if ends with '.'
                if cand.endswith('.'):
                    continue
                # also skip if looks like a sentence (contains ' is ')
                if ' is ' in cl or ' are ' in cl or ' will ' in cl:
                    continue
                name=cand
                break
            if name:
                projects.add(name)

fund_total=sum(fund_map.get(n,0) for n in projects)
missing=[n for n in projects if n not in fund_map]

out={'count': len(projects), 'total_funding': int(fund_total), 'projects': sorted(projects), 'missing_funding_projects': sorted(missing)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1EWiZF0MWHnDBQUWPaYA512M': ['Funding'], 'var_call_7D8EP2WAYggkcSvlh6EUsyhx': 'file_storage/call_7D8EP2WAYggkcSvlh6EUsyhx.json', 'var_call_gkn6QJLGZl3ts1HELo7BGVOs': 'file_storage/call_gkn6QJLGZl3ts1HELo7BGVOs.json', 'var_call_aiIe4m3TtHHVjzNjac9me70B': {'count': 0, 'total_funding': 0, 'projects_started_spring_2022': [], 'missing_funding_projects': []}, 'var_call_QJ700MNUJD7Xf1pYcyFipe3Q': [{'filename': 'malibucity_agenda__01262022-1835.txt', 'snippet': '(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n'}, {'filename': 'malibucity_agenda__01272021-1626.txt', 'snippet': '\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'}, {'filename': 'malibucity_agenda__03022021-1648.txt', 'snippet': '\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'snippet': '\n(cid:190) Project Schedule:\n\n(cid:131) Complete Final Design: Spring 2022\n(cid:131) Advertise: Summer 2022\n(cid:131) Award Contract and Begin Construction: Summer 2022\n'}, {'filename': 'malibucity_agenda__03242021-1665.txt', 'snippet': '\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'}], 'var_call_pcMvRR2z5cLSWIezzKD1HKJA': ['\nCapital Improvement Projects (Design)\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) A hydrology report was prepared and will be used to size the pre-\nmanufactured biofilters. City staff is reviewing multiple biofilter\nmanufacturers for filters that will work in the proposed project area. It is\nanticipated to have a final design by March 2022. The project will be\nadvertised for construction bids shortly after this date.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) The project was approved by the Planning Commission on September\n8, 2021. This project requires Caltrans approval since the work will be\non Pacific Coast Highway. The project reports and plans are being\nrouted through Caltrans for final approval. It is anticipated that the'], 'var_call_OndFhYINQ4UQql1RuFZ7lcWg': {'count': 0, 'total_funding': 0, 'projects': [], 'missing_funding_projects': []}, 'var_call_Z6OFXMFaqxIurdzojEvuA9kR': [], 'var_call_umixSnxr8NrP9NfTupCnr16b': {'count_docs_with_line': 13, 'filenames': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt', 'malibucity_agenda__03242021-1665.txt', 'malibucity_agenda__04282021-1687.txt', 'malibucity_agenda__05262021-1701.txt', 'malibucity_agenda__06232021-1714.txt', 'malibucity_agenda__07282021-1732.txt', 'malibucity_agenda__08252021-1746.txt', 'malibucity_agenda__09222021-1765.txt', 'malibucity_agenda__10272021-1779.txt', 'malibucity_agenda__12142021-1808.txt']}, 'var_call_xTgz3uPqrHzrpDzGRMG382ok': [{'filename': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__01272021-1626.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__03022021-1648.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__03242021-1665.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}], 'var_call_n6vdXR1AmEkCgVU95XBzz0c8': {'count': 14, 'total_funding': 87000, 'projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'anticipated to have a final design by March 2022. The project will be', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'missing_funding_projects': ['Fire.', 'anticipated to have a final design by March 2022. The project will be', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.']}, 'var_call_zHD1jbmTw0opfHFvkdexnJR2': {'count': 14, 'total_funding': 87000, 'projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'anticipated to have a final design by March 2022. The project will be', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'missing_funding_projects': ['Fire.', 'anticipated to have a final design by March 2022. The project will be', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.']}, 'var_call_6NUOQfw4ZFQBHTmSn8Du7rEw': None, 'var_call_Nm4eXkl93ZQK2jgtWO1fE4Hn': [{'filename': 'malibucity_agenda__01262022-1835.txt', 'prev': ['manufactured biofilters. City staff is reviewing multiple biofilter', 'manufacturers for filters that will work in the proposed project area. It is', 'anticipated to have a final design by March 2022. The project will be', 'advertised for construction bids shortly after this date.', '', '(cid:190) Project Schedule:', '', '(cid:131) Complete Design: March 2022']}, {'filename': 'malibucity_agenda__01272021-1626.txt', 'prev': ['', '(cid:190) Project Description: This project consists of repairing the existing storm', 'drain on Latigo Canyon Road located approximately 2,500 feet from PCH', 'that was damaged by the Woolsey Fire.', '', '(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: Winter 2021']}, {'filename': 'malibucity_agenda__03022021-1648.txt', 'prev': ['', '(cid:190) Project Description: This project consists of repairing the existing storm', 'drain on Latigo Canyon Road located approximately 2,500 feet from PCH', 'that was damaged by the Woolsey Fire.', '', '(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: Winter 2021']}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'prev': ['', '(cid:131) Staff received bids on February 24, 2022. Award of contract is', '', 'scheduled for the April 11, 2022 Council meeting.', '', '(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: February 2022']}, {'filename': 'malibucity_agenda__03242021-1665.txt', 'prev': ['', '(cid:190) Project Description: This project consists of repairing the existing storm', 'drain on Latigo Canyon Road located approximately 2,500 feet from PCH', 'that was damaged by the Woolsey Fire.', '', '(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: Winter 2021']}]}

exec(code, env_args)
