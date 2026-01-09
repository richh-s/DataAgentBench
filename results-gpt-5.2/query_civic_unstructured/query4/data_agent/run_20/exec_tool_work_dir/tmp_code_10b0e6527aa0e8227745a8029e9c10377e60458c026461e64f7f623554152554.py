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

projects=set()
for d in docs:
    lines=[ln.strip() for ln in d.get('text','').splitlines()]
    for i,ln in enumerate(lines):
        if 'Begin Construction:' in ln and 'Spring 2022' in ln:
            j=i-1
            name=None
            while j>=0:
                cand=lines[j]
                cl=cand.lower()
                if cand=='':
                    j-=1; continue
                if cl.startswith('(cid'):
                    j-=1; continue
                if cl.startswith('project schedule') or cl.startswith('estimated schedule') or cl.startswith('updates'):
                    j-=1; continue
                if cl.startswith('complete design') or cl.startswith('advertise'):
                    j-=1; continue
                if cl.startswith('capital improvement projects') or cl.startswith('disaster recovery projects') or cl.startswith('page '):
                    break
                name=cand
                break
            if name:
                projects.add(name)

fund_total=sum(fund_map.get(n,0) for n in projects)
missing=[n for n in projects if n not in fund_map]

out={'count': len(projects), 'total_funding': int(fund_total), 'projects': sorted(projects), 'missing_funding_projects': sorted(missing)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1EWiZF0MWHnDBQUWPaYA512M': ['Funding'], 'var_call_7D8EP2WAYggkcSvlh6EUsyhx': 'file_storage/call_7D8EP2WAYggkcSvlh6EUsyhx.json', 'var_call_gkn6QJLGZl3ts1HELo7BGVOs': 'file_storage/call_gkn6QJLGZl3ts1HELo7BGVOs.json', 'var_call_aiIe4m3TtHHVjzNjac9me70B': {'count': 0, 'total_funding': 0, 'projects_started_spring_2022': [], 'missing_funding_projects': []}, 'var_call_QJ700MNUJD7Xf1pYcyFipe3Q': [{'filename': 'malibucity_agenda__01262022-1835.txt', 'snippet': '(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n'}, {'filename': 'malibucity_agenda__01272021-1626.txt', 'snippet': '\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'}, {'filename': 'malibucity_agenda__03022021-1648.txt', 'snippet': '\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'snippet': '\n(cid:190) Project Schedule:\n\n(cid:131) Complete Final Design: Spring 2022\n(cid:131) Advertise: Summer 2022\n(cid:131) Award Contract and Begin Construction: Summer 2022\n'}, {'filename': 'malibucity_agenda__03242021-1665.txt', 'snippet': '\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'}], 'var_call_pcMvRR2z5cLSWIezzKD1HKJA': ['\nCapital Improvement Projects (Design)\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) A hydrology report was prepared and will be used to size the pre-\nmanufactured biofilters. City staff is reviewing multiple biofilter\nmanufacturers for filters that will work in the proposed project area. It is\nanticipated to have a final design by March 2022. The project will be\nadvertised for construction bids shortly after this date.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) The project was approved by the Planning Commission on September\n8, 2021. This project requires Caltrans approval since the work will be\non Pacific Coast Highway. The project reports and plans are being\nrouted through Caltrans for final approval. It is anticipated that the'], 'var_call_OndFhYINQ4UQql1RuFZ7lcWg': {'count': 0, 'total_funding': 0, 'projects': [], 'missing_funding_projects': []}, 'var_call_Z6OFXMFaqxIurdzojEvuA9kR': [], 'var_call_umixSnxr8NrP9NfTupCnr16b': {'count_docs_with_line': 13, 'filenames': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt', 'malibucity_agenda__03242021-1665.txt', 'malibucity_agenda__04282021-1687.txt', 'malibucity_agenda__05262021-1701.txt', 'malibucity_agenda__06232021-1714.txt', 'malibucity_agenda__07282021-1732.txt', 'malibucity_agenda__08252021-1746.txt', 'malibucity_agenda__09222021-1765.txt', 'malibucity_agenda__10272021-1779.txt', 'malibucity_agenda__12142021-1808.txt']}, 'var_call_xTgz3uPqrHzrpDzGRMG382ok': [{'filename': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__01272021-1626.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__03022021-1648.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__03242021-1665.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}]}

exec(code, env_args)
