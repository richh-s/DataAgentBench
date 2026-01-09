code = """import json
info = var_call_scQUSoQgorDdt7RRqHvv1xhe
print('__RESULT__:')
print(json.dumps(info))"""

env_args = {'var_call_iNc1jtCKZc3PmhFsHF5mVkiw': 'file_storage/call_iNc1jtCKZc3PmhFsHF5mVkiw.json', 'var_call_fssuB9N5FSr9mC6JQ02Vi5f3': 'file_storage/call_fssuB9N5FSr9mC6JQ02Vi5f3.json', 'var_call_scQUSoQgorDdt7RRqHvv1xhe': {'n_symbols': 234, 'n_chunks': 3, 'first_chunk': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}}

exec(code, env_args)
