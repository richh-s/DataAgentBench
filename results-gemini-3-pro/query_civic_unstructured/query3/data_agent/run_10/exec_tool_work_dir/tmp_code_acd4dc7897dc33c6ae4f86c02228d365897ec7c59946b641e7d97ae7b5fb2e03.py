code = """import json
with open(locals()['var_function-call-14460790621414043355'], 'r') as f:
    civic_docs = json.load(f)

text = civic_docs[0]['text']
has_cid = "(cid:190)" in text
has_uni = chr(190) in text
lines = text.split(chr(10))

print("__RESULT__:")
print(json.dumps({
    "has_cid": has_cid,
    "has_uni": has_uni,
    "line_count": len(lines),
    "sample_lines": lines[:20]
}))"""

env_args = {'var_function-call-16841234129096573312': 'file_storage/function-call-16841234129096573312.json', 'var_function-call-16841234129096575269': 'file_storage/function-call-16841234129096575269.json', 'var_function-call-1647785278935459272': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-14460790621414043355': 'file_storage/function-call-14460790621414043355.json', 'var_function-call-9486973076472858679': []}

exec(code, env_args)
