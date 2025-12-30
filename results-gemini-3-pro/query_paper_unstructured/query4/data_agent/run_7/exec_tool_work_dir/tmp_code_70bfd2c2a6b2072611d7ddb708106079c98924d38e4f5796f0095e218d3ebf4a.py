code = """import json

with open(locals()['var_function-call-13906461946553771185'], 'r') as f:
    paper_docs = json.load(f)

info = []
for doc in paper_docs:
    info.append({
        "filename": doc.get('filename'),
        "header": doc.get('text', '')[:100]
    })

print("__RESULT__:")
print(json.dumps(info))"""

env_args = {'var_function-call-5218844926592326471': ['paper_docs'], 'var_function-call-5218844926592327304': ['Citations', 'sqlite_sequence'], 'var_function-call-3045611188522186041': 'file_storage/function-call-3045611188522186041.json', 'var_function-call-13906461946553771185': 'file_storage/function-call-13906461946553771185.json', 'var_function-call-3552239526712038918': 'file_storage/function-call-3552239526712038918.json', 'var_function-call-12956520315501172365': {}, 'var_function-call-11308566918737790029': 'debug_done', 'var_function-call-4610303297687271524': {'total_docs': 5, 'count_2016': 0, 'count_phys': 2, 'intersection': [], 'sample_header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}}

exec(code, env_args)
