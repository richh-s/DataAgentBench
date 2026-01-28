code = """import json
mongo_docs=json.loads(open('/tmp/tmp9z4c2iv0.json').read())
funding_recs=json.loads(open('/tmp/tmps9c7b2d8.json').read())
d={r['Project_Name']:int(r['Amount']) for r in funding_recs}
spring=set()
for doc in mongo_docs:
    text=doc.get('text','')
    lines=text.split('\n')
    for i in range(len(lines)):
        if 'Begin Construction' in lines[i] and '2022' in lines[i]:
            for j in range(i-1,max(i-8,-1),-1):
                cand=lines[j].strip()
                if cand and cand[0]!='(' and 'Schedule' not in cand and len(cand)>5:
                    spring.add(cand)
                    break
matches=[{'name':p,'funding':d[p]} for p in spring if p in d]
cnt=len(matches)
total=sum(m['funding'] for m in matches)
result={'project_count':cnt,'total_funding':total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
