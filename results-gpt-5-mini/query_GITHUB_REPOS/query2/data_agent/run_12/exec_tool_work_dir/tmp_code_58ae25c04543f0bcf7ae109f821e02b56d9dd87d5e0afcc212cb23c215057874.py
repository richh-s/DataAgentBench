code = """import json
# Access previous stored results
q_res = var_call_siwHioSVrnYnoprrhY8XRkkd
lang_res = var_call_WsP0KurOHL3NoIjF3c3437HM
repo_res = var_call_WoC5imcF5O5Uv8GC9hedZc3u

repo_name = q_res[0]['sample_repo_name']
path = q_res[0]['sample_path']
file_id = q_res[0]['id']
copies = None
# extract copies from repo_data_description
desc = q_res[0].get('repo_data_description','')
import re
m = re.search(r"(\d+)\s+times", desc)
if m:
    copies = int(m.group(1))

languages = lang_res[0]['language_description'] if lang_res else None
watch_count = int(repo_res[0]['watch_count']) if repo_res and repo_res[0]['watch_count'] is not None else None

result = {
    'repository': repo_name,
    'file_id': file_id,
    'sample_path': path,
    'copies_in_dataset': copies,
    'language_description': languages,
    'watch_count': watch_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_rpRyLsnE61cE1hAUP5ZVGwx1': [], 'var_call_2QScgCh80adt2EDhXi21HyD6': 'file_storage/call_2QScgCh80adt2EDhXi21HyD6.json', 'var_call_9iTDljG5bpRTcLRV1idvotAq': {'max_copies': 38, 'ids': ['6f4cdb70f044b0486a24a07403600cb964a02672'], 'repo_names': ['uacaps/PageMenu'], 'sample_paths': ['Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift']}, 'var_call_siwHioSVrnYnoprrhY8XRkkd': [{'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'sample_repo_name': 'uacaps/PageMenu', 'sample_path': 'Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift', 'repo_data_description': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.'}], 'var_call_WsP0KurOHL3NoIjF3c3437HM': [{'repo_name': 'uacaps/PageMenu', 'language_description': 'The codebase includes: Swift (56,461 bytes), Objective-C (51,756 bytes), Ruby (5,999 bytes).'}], 'var_call_WoC5imcF5O5Uv8GC9hedZc3u': [{'repo_name': 'uacaps/PageMenu', 'watch_count': '487'}]}

exec(code, env_args)
