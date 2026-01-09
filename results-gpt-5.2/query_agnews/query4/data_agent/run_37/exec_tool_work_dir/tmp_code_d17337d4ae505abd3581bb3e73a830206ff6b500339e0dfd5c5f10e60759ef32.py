code = """import json
path = var_call_FmJhJrOrS0709JNaQihRMxEW
with open(path,'r') as f:
    data = json.load(f)
article_ids = data['article_ids']
# chunk into groups of 800 to keep query size manageable
chunks = [article_ids[i:i+800] for i in range(0,len(article_ids),800)]
out = {'n_chunks': len(chunks), 'chunk_sizes': [len(c) for c in chunks[:5]], 'first_chunk': chunks[0]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_SsrtNrU5YEv5reKQ65A55cPa': 'file_storage/call_SsrtNrU5YEv5reKQ65A55cPa.json', 'var_call_FmJhJrOrS0709JNaQihRMxEW': 'file_storage/call_FmJhJrOrS0709JNaQihRMxEW.json'}

exec(code, env_args)
