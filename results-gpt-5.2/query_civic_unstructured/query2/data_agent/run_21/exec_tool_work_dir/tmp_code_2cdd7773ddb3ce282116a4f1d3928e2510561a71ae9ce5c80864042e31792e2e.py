code = """import json,re
path_docs=var_call_bRlNzZZ72IqhjANul1A5ti3D
with open(path_docs,'r',encoding='utf-8') as f:
    docs=json.load(f)
# pick a 2022 agenda doc
doc=None
for d in docs:
    if '2022' in d['filename'] and 'Capital Improvement Projects' in d['text']:
        doc=d;break
lines=[ln.strip() for ln in doc['text'].splitlines()]
# show around the design heading
idx=[i for i,ln in enumerate(lines) if 'Capital Improvement Projects (Design)' in ln][0]
seg=lines[idx:idx+40]
print('__RESULT__:')
print(json.dumps({'filename':doc['filename'],'segment':seg}))"""

env_args = {'var_call_EwJRJJ2BDH1bM1CyPdScGWSH': ['Funding'], 'var_call_y86nrVdqSPdR9vmjn1tZzarh': ['civic_docs'], 'var_call_bRlNzZZ72IqhjANul1A5ti3D': 'file_storage/call_bRlNzZZ72IqhjANul1A5ti3D.json', 'var_call_tSW7bYfRh9pqlIqOF2V66jZM': 'file_storage/call_tSW7bYfRh9pqlIqOF2V66jZM.json', 'var_call_9wzPbJn4pIo9IAPXQeBcNCYw': {'doc_count': 19, 'sample_keys': ['filename', 'text']}, 'var_call_EmngWz2UM1sSupaha8csJxcu': {'rows': 0, 'cols': [], 'head': []}, 'var_call_FZY50vlgyNKOysQy9D5bHi50': {'filename': 'malibucity_agenda_03222023-2060.txt', 'hits': ['Capital Improvement Projects and Disaster Recovery Projects Status', 'upcoming Capital Improvement Projects and Disaster Recovery Projects.', 'Fiscal Year 2022-2023 Capital Improvement Program:', 'Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']}, 'var_call_sI22QuRPBttwk9tYwUBZxNKb': {'filename': 'malibucity_agenda_03222023-2060.txt', 'segment': ['Capital Improvement Projects (Construction)', '', 'Malibu Road Slope Repairs', '', '(cid:190) Updates: Project is currently under construction', '(cid:190) Complete Construction: April 2023', '', 'Encinal Canyon Road Repairs', '', '(cid:190) Updates: Project is currently under construction', '(cid:190) Complete Construction: Summer 2023', '', 'PCH Signal Synchronization System Improvements Project', '', '(cid:190) Updates:', '', '(cid:131) On February 27, 2023, City Council awarded the contract to GMZ', '', 'Engineering, Inc.', '', '(cid:190) Project Schedule:', '', '(cid:131) Begin construction: April 2023', '(cid:131) Complete Construction: Summer 2025', '', 'Storm Drain Trash Screens Phase Two', '', '(cid:190) Updates:', '', '(cid:131) Project is currently out to bid. Bids are due on March 23, 2023.', '', '(cid:190) Project Schedule:', '', '(cid:131) Begin construction: Summer 2023', '(cid:131) Complete Construction: Summer 2023', '', 'Bluffs Park Shade Structure', '', '(cid:190) Updates: Construction was completed November 2022. Notice of completion', '', 'filed January 2023', '', 'Page 4 of 6', '', 'Agenda Item # 4.B.', '', '', '', '', '', '', '', '', '', '', '', 'Marie Canyon Green Streets', '(cid:190) Updates:', '', '(cid:131) Construction was completed, January 2023', '(cid:131) Scheduled for Council acceptance on April 24, 2023', '', 'Broad Beach Road Water Quality Repair', '', '(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '', 'Point Dume Walkway Repairs', '(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '', 'Capital Improvement Projects (Not Started)', '', 'PCH Median Improvements at Paradise Cove and Zuma Beach', '', '(cid:190) Project Description: This project was identified in the 2015 PCH Safety Study']}, 'var_call_RFX46d5pe2gZPEFO37fy8sLV': {'n': 0, 'cols': [], 'head': []}, 'var_call_MZ36piuEqlAZ2Y2dclHCnkRT': {'docs_with_capital_projects': 17, 'sample_filenames': ['malibucity_agenda_03222023-2060.txt', 'malibucity_agenda__01262022-1835.txt']}}

exec(code, env_args)
