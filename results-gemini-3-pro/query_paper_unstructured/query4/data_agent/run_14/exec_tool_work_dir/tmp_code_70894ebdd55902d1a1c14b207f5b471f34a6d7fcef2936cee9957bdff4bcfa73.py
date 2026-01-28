code = """import json

with open(locals()['var_function-call-1932226808801670089'], 'r') as f:
    papers = json.load(f)

print('Total papers: ' + str(len(papers)))

pa_papers = [p for p in papers if 'physical activity' in p['text'].lower()]
print('Papers with physical activity: ' + str(len(pa_papers)))

print('Sample headers of PA papers:')
for p in pa_papers[:5]:
    print('--- ' + p['filename'] + ' ---')
    print(p['text'][:300].replace('\n', ' '))

print('__RESULT__:')
print(json.dumps('debug_done'))"""

env_args = {'var_function-call-1702073112922347921': 'file_storage/function-call-1702073112922347921.json', 'var_function-call-1932226808801670089': 'file_storage/function-call-1932226808801670089.json', 'var_function-call-962751485773488507': []}

exec(code, env_args)
