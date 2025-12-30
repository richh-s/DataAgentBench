code = """import json

key_name = 'var_function-call-1660175416261696799'
file_path = locals()[key_name]

with open(file_path, 'r') as f:
    papers = json.load(f)

headers = []
for p in papers:
    headers.append({
        'filename': p['filename'],
        'header': p['text'][:300]
    })

print('__RESULT__:')
print(json.dumps(headers))"""

env_args = {'var_function-call-8186241074131223286': ['paper_docs'], 'var_function-call-8186241074131224069': ['Citations', 'sqlite_sequence'], 'var_function-call-11444584410328735250': 'file_storage/function-call-11444584410328735250.json', 'var_function-call-1660175416261696799': 'file_storage/function-call-1660175416261696799.json', 'var_function-call-11009971784847056933': [], 'var_function-call-17654094565186069482': {'total_papers': 5, 'count_2016_in_header': 0, 'count_pa_in_text': 4, 'examples_2016': [], 'examples_pa': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali']}}

exec(code, env_args)
