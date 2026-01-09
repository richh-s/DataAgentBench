code = """import json

p_docs = var_call_7D8EP2WAYggkcSvlh6EUsyhx
with open(p_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# extract exact line strings containing Begin Construction and Spring 2022 from first few docs
res=[]
for d in docs:
    for ln in d.get('text','').splitlines():
        if 'Begin Construction' in ln and 'Spring 2022' in ln:
            res.append({'filename': d.get('filename'), 'line': ln})
            break
    if len(res)>=5:
        break

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_1EWiZF0MWHnDBQUWPaYA512M': ['Funding'], 'var_call_7D8EP2WAYggkcSvlh6EUsyhx': 'file_storage/call_7D8EP2WAYggkcSvlh6EUsyhx.json', 'var_call_gkn6QJLGZl3ts1HELo7BGVOs': 'file_storage/call_gkn6QJLGZl3ts1HELo7BGVOs.json', 'var_call_aiIe4m3TtHHVjzNjac9me70B': {'count': 0, 'total_funding': 0, 'projects_started_spring_2022': [], 'missing_funding_projects': []}, 'var_call_QJ700MNUJD7Xf1pYcyFipe3Q': [{'filename': 'malibucity_agenda__01262022-1835.txt', 'snippet': '(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n'}, {'filename': 'malibucity_agenda__01272021-1626.txt', 'snippet': '\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'}, {'filename': 'malibucity_agenda__03022021-1648.txt', 'snippet': '\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'snippet': '\n(cid:190) Project Schedule:\n\n(cid:131) Complete Final Design: Spring 2022\n(cid:131) Advertise: Summer 2022\n(cid:131) Award Contract and Begin Construction: Summer 2022\n'}, {'filename': 'malibucity_agenda__03242021-1665.txt', 'snippet': '\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'}], 'var_call_pcMvRR2z5cLSWIezzKD1HKJA': ['\nCapital Improvement Projects (Design)\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) A hydrology report was prepared and will be used to size the pre-\nmanufactured biofilters. City staff is reviewing multiple biofilter\nmanufacturers for filters that will work in the proposed project area. It is\nanticipated to have a final design by March 2022. The project will be\nadvertised for construction bids shortly after this date.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) The project was approved by the Planning Commission on September\n8, 2021. This project requires Caltrans approval since the work will be\non Pacific Coast Highway. The project reports and plans are being\nrouted through Caltrans for final approval. It is anticipated that the'], 'var_call_OndFhYINQ4UQql1RuFZ7lcWg': {'count': 0, 'total_funding': 0, 'projects': [], 'missing_funding_projects': []}, 'var_call_Z6OFXMFaqxIurdzojEvuA9kR': [], 'var_call_umixSnxr8NrP9NfTupCnr16b': {'count_docs_with_line': 13, 'filenames': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt', 'malibucity_agenda__03242021-1665.txt', 'malibucity_agenda__04282021-1687.txt', 'malibucity_agenda__05262021-1701.txt', 'malibucity_agenda__06232021-1714.txt', 'malibucity_agenda__07282021-1732.txt', 'malibucity_agenda__08252021-1746.txt', 'malibucity_agenda__09222021-1765.txt', 'malibucity_agenda__10272021-1779.txt', 'malibucity_agenda__12142021-1808.txt']}}

exec(code, env_args)
