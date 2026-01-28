code = """import json

rec = var_call_Gl046UqFvpWtQeTrHgQIy6Nz
lang = var_call_fnObT5jwJpm6DBgGS9pvaNvG

answer = {
    'repo': rec['max_records'][0]['sample_repo_name'],
    'file_id': rec['max_records'][0]['id'],
    'file_path': rec['max_records'][0]['sample_path'],
    'copies': rec['max_count'],
    'language_description': lang[0]['language_description'] if lang else None
}

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_64wtttyxZleAyJbWgZDrD4nf': ['commits', 'contents', 'files'], 'var_call_zDsFP1NQ8OcZk7QgxRMD7fVj': ['languages', 'repos', 'licenses'], 'var_call_xDzCCeBp2zeDXdbtdpOtaITh': 'file_storage/call_xDzCCeBp2zeDXdbtdpOtaITh.json', 'var_call_HgRZrr9azxaAmWmMe130BxCC': 'file_storage/call_HgRZrr9azxaAmWmMe130BxCC.json', 'var_call_Gl046UqFvpWtQeTrHgQIy6Nz': {'max_count': 38, 'max_records': [{'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'sample_repo_name': 'uacaps/PageMenu', 'sample_path': 'Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift', 'count': 38}]}, 'var_call_fnObT5jwJpm6DBgGS9pvaNvG': [{'repo_name': 'uacaps/PageMenu', 'language_description': 'The codebase includes: Swift (56,461 bytes), Objective-C (51,756 bytes), Ruby (5,999 bytes).'}]}

exec(code, env_args)
