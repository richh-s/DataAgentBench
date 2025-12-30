code = """import json

with open(locals()['var_function-call-264858034059979045'], 'r') as f:
    citations = json.load(f)
with open(locals()['var_function-call-8351315325764085192'], 'r') as f:
    papers_list = json.load(f)

target_title = "One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App"
citation_title = next((c['title'] for c in citations if c['title'] == target_title), None)
paper_filename = next((p['filename'] for p in papers_list if target_title in p['filename']), None)

res = {}
if citation_title and paper_filename:
    constructed = citation_title + ".txt"
    res['equal'] = (constructed == paper_filename)
    res['constructed_ords'] = [ord(c) for c in constructed]
    res['filename_ords'] = [ord(c) for c in paper_filename]
    res['citation_title'] = citation_title
    res['paper_filename'] = paper_filename

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-264858034059979045': 'file_storage/function-call-264858034059979045.json', 'var_function-call-16262197769178367218': {'count': 188, 'sample_title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, 'var_function-call-2494524119581093015': 'file_storage/function-call-2494524119581093015.json', 'var_function-call-3380312142503180972': 'file_storage/function-call-3380312142503180972.json', 'var_function-call-8351315325764085192': 'file_storage/function-call-8351315325764085192.json', 'var_function-call-1959921926523090950': {'total_citations': 0, 'num_papers': 0}, 'var_function-call-8389437484024645991': 'Done', 'var_function-call-2898140987180465692': 'Done', 'var_function-call-8612993969594668577': {'total_citations': 114, 'num_papers': 2}, 'var_function-call-4793206800934394654': 'Done', 'var_function-call-14167168668467209418': {'matched': 5}, 'var_function-call-13560056867333161268': 'Done'}

exec(code, env_args)
