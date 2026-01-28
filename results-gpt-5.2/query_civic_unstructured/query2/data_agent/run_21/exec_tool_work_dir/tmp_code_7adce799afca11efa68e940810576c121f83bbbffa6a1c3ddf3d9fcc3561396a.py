code = """import json
path_docs=var_call_bRlNzZZ72IqhjANul1A5ti3D
with open(path_docs,'r',encoding='utf-8') as f:
    docs=json.load(f)
# find a doc containing 'Capital Improvement Projects'
found=None
for d in docs:
    if 'Capital Improvement Projects' in d.get('text',''):
        found=d
        break
text=found['text'] if found else docs[0]['text']
lines=text.splitlines()
# show lines that contain 'Capital Improvement'
hits=[ln for ln in lines if 'Capital Improvement' in ln]
import json as _json
print('__RESULT__:')
print(_json.dumps({'filename':found['filename'] if found else docs[0]['filename'],'hits':hits[:20]}))"""

env_args = {'var_call_EwJRJJ2BDH1bM1CyPdScGWSH': ['Funding'], 'var_call_y86nrVdqSPdR9vmjn1tZzarh': ['civic_docs'], 'var_call_bRlNzZZ72IqhjANul1A5ti3D': 'file_storage/call_bRlNzZZ72IqhjANul1A5ti3D.json', 'var_call_tSW7bYfRh9pqlIqOF2V66jZM': 'file_storage/call_tSW7bYfRh9pqlIqOF2V66jZM.json', 'var_call_9wzPbJn4pIo9IAPXQeBcNCYw': {'doc_count': 19, 'sample_keys': ['filename', 'text']}, 'var_call_EmngWz2UM1sSupaha8csJxcu': {'rows': 0, 'cols': [], 'head': []}}

exec(code, env_args)
