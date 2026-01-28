code = """import json; mkey='var_functions.query_db:42'; fkey='var_functions.query_db:4'; mongo_path=locals()[mkey]; funding_path=locals()[fkey]; mongo_docs=json.load(open(mongo_path)); funding_recs=json.load(open(funding_path)); d={r['Project_Name']:int(r['Amount']) for r in funding_recs}; spring=set()
for doc in mongo_docs:
    text=doc.get('text',''); lines=text.split('\n'); 
    for i in range(len(lines)):
        if 'Begin Construction' in lines[i] and '2022' in lines[i]:
            for j in range(i-1,max(i-8,-1),-1):
                cand=lines[j].strip()
                if cand and cand[0]!='(' and 'Schedule' not in cand and len(cand)>5:
                    spring.add(cand); break
matches=[{'name':p,'funding':d[p]} for p in spring if p in d]; count=len(matches); total=sum(m['funding'] for m in matches)
print('__RESULT__:')
print(json.dumps({'count':count,'total_funding':total}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
