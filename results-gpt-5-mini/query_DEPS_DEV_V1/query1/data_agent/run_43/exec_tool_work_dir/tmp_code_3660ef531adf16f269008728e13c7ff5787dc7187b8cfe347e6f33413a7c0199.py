code = """import json
import pandas as pd

pkg_path = var_call_FivGpH4t0NfQFAUPFyBGHV1V
ppv_path = var_call_41iMZj8Uk64lYGbt4pIv7PWr
pi_path = var_call_5glgSpqrtkeEL66qVt9GP4oC

with open(pkg_path, 'r', encoding='utf-8') as f:
    pkgs = json.load(f)
with open(ppv_path, 'r', encoding='utf-8') as f:
    ppvs = json.load(f)
with open(pi_path, 'r', encoding='utf-8') as f:
    pis = json.load(f)

info = {}
info['pkg_count'] = len(pkgs) if isinstance(pkgs, list) else None
info['ppv_count'] = len(ppvs) if isinstance(ppvs, list) else None
info['pi_count'] = len(pis) if isinstance(pis, list) else None

info['pkg_first_keys'] = list(pkgs[0].keys()) if isinstance(pkgs, list) and len(pkgs)>0 and isinstance(pkgs[0], dict) else None
info['ppv_first_keys'] = list(ppvs[0].keys()) if isinstance(ppvs, list) and len(ppvs)>0 and isinstance(ppvs[0], dict) else None
info['pi_first_keys'] = list(pis[0].keys()) if isinstance(pis, list) and len(pis)>0 and isinstance(pis[0], dict) else None

# Sample first records
info['pkg_sample0'] = pkgs[0] if isinstance(pkgs, list) and len(pkgs)>0 else None
info['ppv_sample0'] = ppvs[0] if isinstance(ppvs, list) and len(ppvs)>0 else None
info['pi_sample0'] = pis[0] if isinstance(pis, list) and len(pis)>0 else None

print("__RESULT__:")
print(json.dumps(info))"""

env_args = {'var_call_CJZhajwS3qMiYjKY8nUHfTm1': ['packageinfo'], 'var_call_FtqMybgYmGGAyxyivBimhT9W': ['project_info', 'project_packageversion'], 'var_call_FivGpH4t0NfQFAUPFyBGHV1V': 'file_storage/call_FivGpH4t0NfQFAUPFyBGHV1V.json', 'var_call_41iMZj8Uk64lYGbt4pIv7PWr': 'file_storage/call_41iMZj8Uk64lYGbt4pIv7PWr.json', 'var_call_5glgSpqrtkeEL66qVt9GP4oC': 'file_storage/call_5glgSpqrtkeEL66qVt9GP4oC.json'}

exec(code, env_args)
