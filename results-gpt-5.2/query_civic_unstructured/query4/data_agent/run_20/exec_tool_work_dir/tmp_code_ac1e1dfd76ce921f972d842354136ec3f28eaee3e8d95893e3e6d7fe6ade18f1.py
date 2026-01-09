code = """import json

p_docs = var_call_7D8EP2WAYggkcSvlh6EUsyhx
with open(p_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# count lines that include both 'Begin Construction' and 'Spring 2022'
ct=0
files=[]
for d in docs:
    for ln in d.get('text','').splitlines():
        if 'Begin Construction' in ln and 'Spring 2022' in ln:
            ct+=1
            files.append(d.get('filename'))
            break

print('__RESULT__:')
print(json.dumps({'count_docs_with_line': ct, 'filenames': files[:20]}))"""

env_args = {'var_call_1EWiZF0MWHnDBQUWPaYA512M': ['Funding'], 'var_call_7D8EP2WAYggkcSvlh6EUsyhx': 'file_storage/call_7D8EP2WAYggkcSvlh6EUsyhx.json', 'var_call_gkn6QJLGZl3ts1HELo7BGVOs': 'file_storage/call_gkn6QJLGZl3ts1HELo7BGVOs.json', 'var_call_aiIe4m3TtHHVjzNjac9me70B': {'count': 0, 'total_funding': 0, 'projects_started_spring_2022': [], 'missing_funding_projects': []}, 'var_call_QJ700MNUJD7Xf1pYcyFipe3Q': [{'filename': 'malibucity_agenda__01262022-1835.txt', 'snippet': '(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n'}, {'filename': 'malibucity_agenda__01272021-1626.txt', 'snippet': '\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'}, {'filename': 'malibucity_agenda__03022021-1648.txt', 'snippet': '\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'snippet': '\n(cid:190) Project Schedule:\n\n(cid:131) Complete Final Design: Spring 2022\n(cid:131) Advertise: Summer 2022\n(cid:131) Award Contract and Begin Construction: Summer 2022\n'}, {'filename': 'malibucity_agenda__03242021-1665.txt', 'snippet': '\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'}], 'var_call_pcMvRR2z5cLSWIezzKD1HKJA': ['\nCapital Improvement Projects (Design)\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) A hydrology report was prepared and will be used to size the pre-\nmanufactured biofilters. City staff is reviewing multiple biofilter\nmanufacturers for filters that will work in the proposed project area. It is\nanticipated to have a final design by March 2022. The project will be\nadvertised for construction bids shortly after this date.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) The project was approved by the Planning Commission on September\n8, 2021. This project requires Caltrans approval since the work will be\non Pacific Coast Highway. The project reports and plans are being\nrouted through Caltrans for final approval. It is anticipated that the'], 'var_call_OndFhYINQ4UQql1RuFZ7lcWg': {'count': 0, 'total_funding': 0, 'projects': [], 'missing_funding_projects': []}, 'var_call_Z6OFXMFaqxIurdzojEvuA9kR': []}

exec(code, env_args)
