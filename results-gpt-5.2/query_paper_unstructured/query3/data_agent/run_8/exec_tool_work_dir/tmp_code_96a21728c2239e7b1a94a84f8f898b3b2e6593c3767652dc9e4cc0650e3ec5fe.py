code = """import json

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

citations = load_json_maybe(var_call_TWhcQoF9rfbZrwClgmm2gLiO)
# show first record keys
first = citations[0] if citations else None
print('__RESULT__:')
print(json.dumps({'first_record': first, 'keys': list(first.keys()) if first else []}))"""

env_args = {'var_call_O05e4rUsZ2q39PV166J8Xky7': 'file_storage/call_O05e4rUsZ2q39PV166J8Xky7.json', 'var_call_TWhcQoF9rfbZrwClgmm2gLiO': 'file_storage/call_TWhcQoF9rfbZrwClgmm2gLiO.json', 'var_call_4VYaIeVEDqzm0Z0t4SP4ttKp': 'file_storage/call_4VYaIeVEDqzm0Z0t4SP4ttKp.json'}

exec(code, env_args)
