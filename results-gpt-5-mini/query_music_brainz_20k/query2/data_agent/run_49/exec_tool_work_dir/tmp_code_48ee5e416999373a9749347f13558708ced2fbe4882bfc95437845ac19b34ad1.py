code = """import json
import os
# var_call_lcDjXSrqM6FYjP34MTn1v9rF is available in the environment
data = None
v = var_call_lcDjXSrqM6FYjP34MTn1v9rF
if isinstance(v, str) and os.path.exists(v):
    with open(v, 'r', encoding='utf-8') as f:
        data = json.load(f)
else:
    data = v

candidates = []
for r in data:
    title = (r.get('title') or '').lower()
    artist = (r.get('artist') or '').lower()
    album = (r.get('album') or '').lower()
    # conditions for matching 'Street Hype' and variations of artist
    cond_title = ('street' in title and 'hype' in title) or 'street hype' in title or 'sttreet hype' in title or 'sttreet' in title and 'hype' in title
    cond_artist = 'maginnis' in artist or 'brucqe' in artist or 'bruce maginnis' in artist or 'brucqe maginnis' in artist
    cond_album = 'groove city' in album
    if cond_title or cond_artist or cond_album:
        tid = r.get('track_id')
        # try convert to int
        try:
            tid_int = int(tid)
        except:
            # skip non-int ids
            continue
        candidates.append(tid_int)
# deduplicate
candidates = sorted(list(set(candidates)))
import json
print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_call_lcDjXSrqM6FYjP34MTn1v9rF': 'file_storage/call_lcDjXSrqM6FYjP34MTn1v9rF.json'}

exec(code, env_args)
