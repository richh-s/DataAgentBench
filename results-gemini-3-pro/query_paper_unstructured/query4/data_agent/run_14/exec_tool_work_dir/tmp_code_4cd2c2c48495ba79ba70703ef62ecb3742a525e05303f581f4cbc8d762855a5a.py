code = """import json

with open(locals()['var_function-call-1932226808801670089'], 'r') as f:
    papers = json.load(f)

debug_info = {}
debug_info['total_papers'] = len(papers)

pa_papers = [p for p in papers if 'physical activity' in p['text'].lower()]
debug_info['pa_count'] = len(pa_papers)

sample_headers = []
for p in pa_papers[:5]:
    header = p['text'][:300].replace('\\n', ' ')
    sample_headers.append({'filename': p['filename'], 'header': header})
debug_info['sample_headers'] = sample_headers

papers_2016 = [p for p in papers if '2016' in p['text'][:1000]]
debug_info['2016_count'] = len(papers_2016)

print('__RESULT__:')
print(json.dumps(debug_info))"""

env_args = {'var_function-call-1702073112922347921': 'file_storage/function-call-1702073112922347921.json', 'var_function-call-1932226808801670089': 'file_storage/function-call-1932226808801670089.json', 'var_function-call-962751485773488507': [], 'var_function-call-7065428767618965832': 'debug_done'}

exec(code, env_args)
