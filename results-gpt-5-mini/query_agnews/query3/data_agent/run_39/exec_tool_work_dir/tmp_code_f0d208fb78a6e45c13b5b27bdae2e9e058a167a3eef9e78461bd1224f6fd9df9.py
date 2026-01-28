code = """import json
p = var_call_MVDJ1PKo4VG1zLIop4BzFL7O
with open(p, 'r') as f:
    recs = json.load(f)
# extract article ids
ids = [int(r['article_id']) for r in recs]
print('__RESULT__:')
print(json.dumps(ids))"""

env_args = {'var_call_ms1IPeXScrnLDnXJ5N74c2Gg': 'file_storage/call_ms1IPeXScrnLDnXJ5N74c2Gg.json', 'var_call_SjyJ9WSWLyyxJHx7WHzW2nIu': 'file_storage/call_SjyJ9WSWLyyxJHx7WHzW2nIu.json', 'var_call_DqH1sQLbuczivjkb9Zjz8Jjh': 'file_storage/call_DqH1sQLbuczivjkb9Zjz8Jjh.json', 'var_call_MVDJ1PKo4VG1zLIop4BzFL7O': 'file_storage/call_MVDJ1PKo4VG1zLIop4BzFL7O.json'}

exec(code, env_args)
