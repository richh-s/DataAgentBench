code = """import json
from pathlib import Path
p = Path(var_call_dgNX2JtQN6c1wyGbWHMecPQu)
reviews = json.loads(p.read_text())
# convert businessref_ to businessid_
mapped = []
for r in reviews:
    br = r.get('business_ref')
    if br and isinstance(br, str) and br.startswith('businessref_'):
        bid = 'businessid_' + br.split('_',1)[1]
    else:
        bid = br
    try:
        rating = float(r.get('rating'))
    except:
        continue
    mapped.append({'business_id': bid, 'rating': rating})
print('__RESULT__:')
print(json.dumps({'count': len(mapped), 'sample': mapped[:10]}))"""

env_args = {'var_call_lgZkHgp6xdF60q6wisDlHU78': ['checkin', 'business'], 'var_call_8NYYAvcvcbbNpZ4xP3tTyvjV': ['review', 'tip', 'user'], 'var_call_PtZeupfw8rOKXsTtykxJxjAb': 'file_storage/call_PtZeupfw8rOKXsTtykxJxjAb.json', 'var_call_B6wib2tXTY7mz2CRmWcwGLin': 'file_storage/call_B6wib2tXTY7mz2CRmWcwGLin.json', 'var_call_YP4FE6GOpmppMtagA9lUh1Xz': 'file_storage/call_YP4FE6GOpmppMtagA9lUh1Xz.json', 'var_call_dgNX2JtQN6c1wyGbWHMecPQu': 'file_storage/call_dgNX2JtQN6c1wyGbWHMecPQu.json'}

exec(code, env_args)
