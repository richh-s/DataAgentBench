code = """import json

p_docs = var_call_7D8EP2WAYggkcSvlh6EUsyhx
with open(p_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# find the snippet in 01262022 file and show more context around first occurrence of 'Begin Construction: Spring 2022'
out=[]
for d in docs:
    if d.get('filename')=='malibucity_agenda__01262022-1835.txt':
        lines=d.get('text','').splitlines()
        for idx,ln in enumerate(lines):
            if 'Begin Construction: Spring 2022' in ln:
                start=max(0,idx-15); end=min(len(lines),idx+10)
                out.append("\\n".join(lines[start:end]))
                break
        break

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1EWiZF0MWHnDBQUWPaYA512M': ['Funding'], 'var_call_7D8EP2WAYggkcSvlh6EUsyhx': 'file_storage/call_7D8EP2WAYggkcSvlh6EUsyhx.json', 'var_call_gkn6QJLGZl3ts1HELo7BGVOs': 'file_storage/call_gkn6QJLGZl3ts1HELo7BGVOs.json', 'var_call_aiIe4m3TtHHVjzNjac9me70B': {'count': 0, 'total_funding': 0, 'projects_started_spring_2022': [], 'missing_funding_projects': []}, 'var_call_QJ700MNUJD7Xf1pYcyFipe3Q': [{'filename': 'malibucity_agenda__01262022-1835.txt', 'snippet': '(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n'}, {'filename': 'malibucity_agenda__01272021-1626.txt', 'snippet': '\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'}, {'filename': 'malibucity_agenda__03022021-1648.txt', 'snippet': '\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'snippet': '\n(cid:190) Project Schedule:\n\n(cid:131) Complete Final Design: Spring 2022\n(cid:131) Advertise: Summer 2022\n(cid:131) Award Contract and Begin Construction: Summer 2022\n'}, {'filename': 'malibucity_agenda__03242021-1665.txt', 'snippet': '\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'}]}

exec(code, env_args)
