code = """import json
import re
from pathlib import Path

contents_path = Path(var_call_jQQSgzJH4LwIFK5GGYOlnsgn)
languages_path = Path(var_call_0Egm93ckdSYZQKPTuYeDx3Ry)

with open(contents_path, 'r', encoding='utf-8') as f:
    contents = json.load(f)
with open(languages_path, 'r', encoding='utf-8') as f:
    languages = json.load(f)

swift_repo_set = set(r.get('repo_name') for r in languages if r.get('repo_name'))

def extract_count(desc):
    if not desc:
        return 1
    desc = desc.lower()
    # look for patterns
    patterns = [r"(\d+)\s*times", r"seen\s*(\d+)\s*times", r"copied\s*(\d+)\s*times", r"appearing\s*(\d+)\s*times", r"duplicated\s*(\d+)\s*times", r"appears\s*(\d+)\s*times"]
    for p in patterns:
        m = re.search(p, desc)
        if m:
            try:
                return int(m.group(1))
            except:
                pass
    # fallback: look for a number
    m = re.search(r"(\d+)", desc)
    if m:
        return int(m.group(1))
    return 1

# analyze .swift non-binary entries
records = []
for rec in contents:
    path = (rec.get('sample_path') or '')
    if not path.lower().endswith('.swift'):
        continue
    desc = rec.get('repo_data_description') or ''
    # treat as binary only if 'binary' in desc and not 'non-binary'
    if 'binary' in desc.lower() and 'non-binary' not in desc.lower():
        continue
    rid = rec.get('id')
    if not rid:
        continue
    count = extract_count(desc)
    records.append({
        'id': rid,
        'sample_repo_name': rec.get('sample_repo_name'),
        'sample_path': path,
        'copies': count,
        'repo_data_description': desc
    })

if not records:
    out = {"error": "no non-binary swift records"}
else:
    # group by id and take max copies (should be single per id in this sample)
    id_map = {}
    for r in records:
        rid = r['id']
        if rid not in id_map or r['copies']>id_map[rid]['copies']:
            id_map[rid] = r
    # find max copies
    max_copies = max(r['copies'] for r in id_map.values())
    top_ids = [r for r in id_map.values() if r['copies']==max_copies]
    # find a repository among top_ids that is in swift_repo_set
    chosen = None
    for t in top_ids:
        if t['sample_repo_name'] in swift_repo_set:
            chosen = t
            break
    # if none match, choose first top
    if not chosen and top_ids:
        chosen = top_ids[0]
    out = {
        'max_copies': max_copies,
        'top_ids_count': len(top_ids),
        'chosen': chosen,
        'top_ids': top_ids[:10]
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5KRbupHvs2wmPHCPXMMfBEDn': [], 'var_call_KK1dL8G6KJlTANfIWAh52t2G': [], 'var_call_0Egm93ckdSYZQKPTuYeDx3Ry': 'file_storage/call_0Egm93ckdSYZQKPTuYeDx3Ry.json', 'var_call_tezl9OVPxPVJjImyosaXXcQ7': 'file_storage/call_tezl9OVPxPVJjImyosaXXcQ7.json', 'var_call_Q25tp1Q7XUOgQLwg9OAIKqJf': [{'cnt': '105'}], 'var_call_OSJbegtlIVR7o1m5lEH4rMlB': [], 'var_call_jQQSgzJH4LwIFK5GGYOlnsgn': 'file_storage/call_jQQSgzJH4LwIFK5GGYOlnsgn.json', 'var_call_L7gcLuHUBgefDnEKuBDfDxtM': {'error': 'no non-binary swift files found'}, 'var_call_i8Rdzf4mKHOP9YE8Qz0Ps7P3': 'file_storage/call_i8Rdzf4mKHOP9YE8Qz0Ps7P3.json', 'var_call_ycu0WLKIRAq0v34bqmYvOkP8': [{'id': 'f2a35422a5bf04eba40c03e05adb0f15db319cf8', 'copies': '1'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'copies': '1'}, {'id': '3d42ac2c0fad831225f80a9355a196027e6ccc3e', 'copies': '1'}, {'id': 'cc4de346f66613edef22d12b73c44fc2c8834acd', 'copies': '1'}, {'id': 'c46ff203c0ab2432f4a283cb31c7912fd61467e5', 'copies': '1'}, {'id': 'd8d672966a456490723bb351997fb40fd870fee7', 'copies': '1'}, {'id': '252279b2058c226728c794eeafe89b1df59bc024', 'copies': '1'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'copies': '1'}, {'id': '1c331b4ee6bf6d47575d1ba7be047a2f2a02c394', 'copies': '1'}, {'id': 'c236a42435aa5e367f87077c802b0a77e8047faa', 'copies': '1'}, {'id': 'b32abcab564f4e4e7d409d97ba8415e9a8e59484', 'copies': '1'}, {'id': '0fe09241b77bd34943472f6cff76e71eeb03773a', 'copies': '1'}, {'id': '6488a8d4c15e8c5af390dc4ae272a9bb6e55a1e8', 'copies': '1'}, {'id': 'a452f93131f16c5ea7978582b8253046d6a36f63', 'copies': '1'}, {'id': '88a9c3190ebcf15a4343642aa4767359c4517a10', 'copies': '1'}, {'id': '2e2fe40cd35ab655dbb492b20fb7ae8aaea3e7df', 'copies': '1'}, {'id': '839b819b98b2b6a934d91229bf9d8d2f565b7855', 'copies': '1'}, {'id': '729e22ed109bea5edb4bfb6cef1fe4cf5204e564', 'copies': '1'}, {'id': 'ec6d2f9ee3d4ad887abe7e7d488c5287388c9f8b', 'copies': '1'}, {'id': '1ff86af65537e2973b533c27044763ffefd0347d', 'copies': '1'}]}

exec(code, env_args)
