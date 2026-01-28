code = """import json
# load results
top = var_call_hIlkSt0w17NFomu1OILFXnym
repo_meta = var_call_2p86dX1gDU9TkWQZDDu29GZt
sample_repos = var_call_8ABBmlci92esT5mb1Vk0E4Q8

# Build final answer data
result = {
    'file_id': top['top_files'][0]['id'],
    'file_path': top['top_files'][0]['sample_path'],
    'file_copies': top['top_files'][0]['copies'],
    'sample_repo_name': top['top_files'][0]['sample_repo_name'],
    'repo_watch_count': int(repo_meta[0]['watch_count']) if repo_meta else None
}

import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uIqHw6orIQTDDOyGowdNMRgh': 'file_storage/call_uIqHw6orIQTDDOyGowdNMRgh.json', 'var_call_UpL3MbiJCKJtLwGqt9WjyYHN': 'file_storage/call_UpL3MbiJCKJtLwGqt9WjyYHN.json', 'var_call_YIFV3dT5woYOTesJwbU1GoXI': [{'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'copies': '1'}, {'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copies': '1'}], 'var_call_hIlkSt0w17NFomu1OILFXnym': {'max_copies': 38, 'top_files': [{'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'sample_repo_name': 'uacaps/PageMenu', 'sample_path': 'Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift', 'copies': 38, 'repo_data_description': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.'}]}, 'var_call_2p86dX1gDU9TkWQZDDu29GZt': [{'repo_name': 'uacaps/PageMenu', 'watch_count': '487'}], 'var_call_8ABBmlci92esT5mb1Vk0E4Q8': [{'sample_repo_name': 'uacaps/PageMenu'}]}

exec(code, env_args)
