code = """import json
import pandas as pd
with open(var_call_M5WB5deY7REsm7gEQ2IqlM4Q, 'r') as f:
    civic_docs = json.load(f)
# Park project names from funding (from var_call_A7DJ5BY5sUIZZa7tHdqgJt6m)
park_names = json.loads(open(var_call_A7DJ5BY5sUIZZa7tHdqgJt6m,'r').read())
relevant = set()
for doc in civic_docs:
    t = doc['text'].lower()
    if '2022' in t and 'completed' in t:
        for pn in park_names:
            if all([k in t for k in pn.lower().split()]) or pn.lower().replace('(','').replace(')','').replace('/','').replace('-','') in t.replace('(','').replace(')','').replace('/','').replace('-',''):
                relevant.add(pn)
print('__RESULT__:')
print(json.dumps(list(relevant)))"""

env_args = {'var_call_M5WB5deY7REsm7gEQ2IqlM4Q': 'file_storage/call_M5WB5deY7REsm7gEQ2IqlM4Q.json', 'var_call_Rp5VVDEy0XKOcKG6atWrw8IL': 'file_storage/call_Rp5VVDEy0XKOcKG6atWrw8IL.json', 'var_call_vvdJJZTp1wY59mJUiUhblAe7': 0, 'var_call_A7DJ5BY5sUIZZa7tHdqgJt6m': ['Bluffs Park Shade Structure', 'Bluffs Park Workout Station', 'Legacy Park Benches and Arbors Renovation', 'Legacy Park Paver Repair Project', 'Malibu Bluffs Park Roof Replacement Project', 'Malibu Bluffs Park South Walkway', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Park Drainage Improvements', 'Malibu Park Resurfacing Project', 'Malibu Park Storm Drain Repairs', 'Permanent Skate Park', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Playground', 'Trancas Canyon Park Playground Resurfacing', 'Trancas Canyon Park Slope Stabilization Project', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Trancas Canyon Park Upper and Lower Slopes Repair']}

exec(code, env_args)
