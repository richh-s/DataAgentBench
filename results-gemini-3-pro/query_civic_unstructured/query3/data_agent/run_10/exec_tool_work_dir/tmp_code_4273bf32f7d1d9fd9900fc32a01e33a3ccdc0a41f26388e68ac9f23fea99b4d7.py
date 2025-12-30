code = """import json
import re

with open(locals()['var_function-call-14460790621414043355'], 'r') as f:
    civic_docs = json.load(f)

text = civic_docs[0]['text']
lines = text.split(chr(10))

matches = []
for line in lines:
    if "Capital Improvement" in line:
        matches.append(line)

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-16841234129096573312': 'file_storage/function-call-16841234129096573312.json', 'var_function-call-16841234129096575269': 'file_storage/function-call-16841234129096575269.json', 'var_function-call-1647785278935459272': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-14460790621414043355': 'file_storage/function-call-14460790621414043355.json', 'var_function-call-9486973076472858679': [], 'var_function-call-17381857488662847818': {'has_cid': True, 'has_uni': False, 'line_count': 434, 'sample_lines': ['Public Works Commission', 'Agenda Report', '', 'Public Works', 'Commission Meeting', '03-22-23', 'Item', '4.B.', '', 'To:', '', 'Chair Dittrich and Members of the Public Works Commission', '', 'Prepared by:', '', 'Jorge Rubalcava, Senior Civil Engineer', '', 'Approved by:', '', 'Rob DuBoux, Public Works Director/City Engineer']}}

exec(code, env_args)
