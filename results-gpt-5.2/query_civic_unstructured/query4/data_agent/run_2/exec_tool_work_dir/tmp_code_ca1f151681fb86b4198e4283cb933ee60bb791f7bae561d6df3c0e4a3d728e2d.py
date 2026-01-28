code = """import json, re
raw = var_call_C8L5zhLal1Zk1ENuLjD2VCfK
if isinstance(raw, str):
    with open(raw,'r',encoding='utf-8') as f:
        docs=json.load(f)
else:
    docs=raw

projects=set()
for d in docs:
    lines=d.get('text','').splitlines()
    for i,line in enumerate(lines):
        if re.search(r'Begin\s+Construction\s*:\s*Spring\s+2022', line, flags=re.I):
            name=None
            for j in range(i-1, max(-1,i-60), -1):
                s=lines[j].strip()
                if not s:
                    continue
                if re.search(r'\(cid:\d+\)', s):
                    continue
                if re.search(r'^(Updates|Project Schedule|Estimated Schedule|Project Description|Capital Improvement Projects|Disaster Projects|Disaster Recovery Projects|DISCUSSION|RECOMMENDED ACTION)', s, flags=re.I):
                    continue
                if ':' in s:
                    continue
                # likely project names have multiple words and some Title Case
                if len(s) < 8:
                    continue
                if len(s.split()) < 3:
                    continue
                # avoid sentences
                if s.endswith('.'):
                    continue
                if re.search(r'\b(is|was|are|will|anticipated|working|scheduled|sending|advertised|beginning)\b', s, flags=re.I):
                    continue
                name=s
                break
            if name:
                projects.add(name)

print('__RESULT__:')
print(json.dumps({'count':len(projects), 'projects':sorted(projects)}))"""

env_args = {'var_call_voCW34f5mhpr4lBcDrP0GdJi': ['Funding'], 'var_call_beaAEvwBIwRzy1HcSw5H4XHD': ['civic_docs'], 'var_call_sir3H7yoilAVtxp9uzAjCNCs': 'file_storage/call_sir3H7yoilAVtxp9uzAjCNCs.json', 'var_call_1OKkPLKGhwTNK2ZpwqZXJyH2': {'projects': [], 'count': 0}, 'var_call_C8L5zhLal1Zk1ENuLjD2VCfK': 'file_storage/call_C8L5zhLal1Zk1ENuLjD2VCfK.json', 'var_call_GB4hhkINGJ8gc0CO8aCtTVBu': {'projects': [], 'count': 0}, 'var_call_4ivGfXSJykhCpB8wX702xgWY': [{'filename': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__01272021-1626.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__01272021-1626.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__03022021-1648.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__03022021-1648.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__03242021-1665.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__03242021-1665.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__04282021-1687.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__04282021-1687.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__05262021-1701.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__05262021-1701.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__06232021-1714.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__06232021-1714.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__07282021-1732.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__07282021-1732.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__08252021-1746.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__08252021-1746.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__09222021-1765.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__09222021-1765.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__10272021-1779.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__10272021-1779.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__10272021-1779.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__12142021-1808.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__12142021-1808.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__12142021-1808.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__12142021-1808.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__12142021-1808.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__12142021-1808.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'filename': 'malibucity_agenda__12142021-1808.txt', 'line': '(cid:131) Begin Construction: Spring 2022'}], 'var_call_A93qVOHL43RFHIQVj0kISrSA': {'count': 14, 'projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.']}}

exec(code, env_args)
