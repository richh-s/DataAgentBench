code = """import json
import re

p_name = "Bluffs Park Shade Structure"
match = re.search(r'\bpark\b|\bplayground\b', p_name, re.IGNORECASE)
print("__RESULT__:")
print(json.dumps({"name": p_name, "match": str(match), "bool": bool(match)}))"""

env_args = {'var_function-call-10057184920144794313': 'file_storage/function-call-10057184920144794313.json', 'var_function-call-10057184920144796126': 'file_storage/function-call-10057184920144796126.json', 'var_function-call-16463367332335965304': {'total_funding': 0, 'projects': [], 'debug': []}, 'var_function-call-12562812388912151187': {'found': True, 'context': 'Bluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022. Notice of completion\n\nfiled January 2023\n\nPage 4 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) Construction was completed, January 2023\n(cid:131) Scheduled for Council acceptance on April 24, 2023\n\nBroad Beach Road Water Quality Repair\n\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nPoi'}, 'var_function-call-4420774818653847510': {'total_funding': 0, 'projects': [], 'logs': ['Checking Bluffs Park Shade Structure, is_park=False', 'Found completion in doc: Construction was completed November 2022', 'Failed to qualify. Found in docs: True, Completed 2022: True']}}

exec(code, env_args)
