code = """import json
import re

with open(locals()['var_function-call-10057184920144796126'], 'r') as f:
    civic_docs = json.load(f)

targets = ["Bluffs Park Workout Station", "Legacy Park Paver Repair Project"]
results = {}

for t in targets:
    results[t] = "Not Found"
    for doc in civic_docs:
        text = doc['text']
        if t in text:
            idx = text.find(t)
            context = text[idx:idx+500]
            results[t] = context.replace("\n", " ")
            break

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-10057184920144794313': 'file_storage/function-call-10057184920144794313.json', 'var_function-call-10057184920144796126': 'file_storage/function-call-10057184920144796126.json', 'var_function-call-16463367332335965304': {'total_funding': 0, 'projects': [], 'debug': []}, 'var_function-call-12562812388912151187': {'found': True, 'context': 'Bluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022. Notice of completion\n\nfiled January 2023\n\nPage 4 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) Construction was completed, January 2023\n(cid:131) Scheduled for Council acceptance on April 24, 2023\n\nBroad Beach Road Water Quality Repair\n\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nPoi'}, 'var_function-call-4420774818653847510': {'total_funding': 0, 'projects': [], 'logs': ['Checking Bluffs Park Shade Structure, is_park=False', 'Found completion in doc: Construction was completed November 2022', 'Failed to qualify. Found in docs: True, Completed 2022: True']}, 'var_function-call-15478542269899668790': {'name': 'Bluffs Park Shade Structure', 'match': 'None', 'bool': False}, 'var_function-call-5050739371739425431': {'total_funding': 21000, 'projects': [['Bluffs Park Shade Structure', 21000]]}, 'var_function-call-5078256386249604020': [{'name': 'Bluffs Park Shade Structure', 'status': 'Completed', 'year': '2022'}, {'name': 'Bluffs Park Workout Station', 'status': 'Found', 'year': None}, {'name': 'Legacy Park Paver Repair Project', 'status': 'Found', 'year': None}, {'name': 'Malibu Bluffs Park South Walkway', 'status': 'Found', 'year': None}, {'name': 'Malibu Bluffs Park South Walkway Repairs', 'status': 'Found', 'year': None}, {'name': 'Malibu Park Drainage Improvements', 'status': 'Found', 'year': None}, {'name': 'Malibu Park Storm Drain Repairs', 'status': 'Found', 'year': None}, {'name': 'Permanent Skate Park', 'status': 'Found', 'year': None}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'status': 'Found', 'year': None}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'status': 'Found', 'year': None}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'status': 'Found', 'year': None}, {'name': 'Trancas Canyon Park Playground', 'status': 'Found', 'year': None}, {'name': 'Trancas Canyon Park Slope Stabilization Project', 'status': 'Found', 'year': None}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'status': 'Found', 'year': None}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'status': 'Found', 'year': None}, {'name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'status': 'Found', 'year': None}, {'name': 'Trancas Playground Resurfacing', 'status': 'Found', 'year': None}]}

exec(code, env_args)
