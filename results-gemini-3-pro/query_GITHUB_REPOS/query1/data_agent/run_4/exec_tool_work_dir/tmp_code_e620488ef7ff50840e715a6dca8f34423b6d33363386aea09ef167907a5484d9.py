code = """import json

# Get file paths from local variables
path_repos = locals()['var_function-call-7984266211391982536']
path_readmes = locals()['var_function-call-5318616242334808465']

# Load non-python repos
with open(path_repos, 'r') as f:
    non_python_repos_list = json.load(f)

# Create set of non-python repo names
non_python_repos = set(item['repo_name'] for item in non_python_repos_list)

# Load readme data
with open(path_readmes, 'r') as f:
    readme_data = json.load(f)

# Filter for non-python repos
relevant_readmes = [
    row for row in readme_data 
    if row['sample_repo_name'] in non_python_repos
]

total_readmes = len(relevant_readmes)
copyright_readmes = sum(1 for row in relevant_readmes if str(row['has_copyright']) == '1')

if total_readmes > 0:
    proportion = copyright_readmes / total_readmes
else:
    proportion = 0

print("__RESULT__:")
print(json.dumps({
    "total_readmes": total_readmes,
    "copyright_readmes": copyright_readmes,
    "proportion": proportion
}))"""

env_args = {'var_function-call-10514252645828785134': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-11217105128405756576': 'file_storage/function-call-11217105128405756576.json', 'var_function-call-7984266211391982536': 'file_storage/function-call-7984266211391982536.json', 'var_function-call-717985874268403162': [{'sample_repo_name': 'F1ReKing/wheelview'}, {'sample_repo_name': 'hypriot/rpi-busybox-httpd'}, {'sample_repo_name': 'adafruit/Adafruit-Trinket-Gemma-Bootloader'}, {'sample_repo_name': 'rubylit/guevara'}, {'sample_repo_name': 'noveogroup/android-logger'}, {'sample_repo_name': 'dblock/slack-google-bot'}, {'sample_repo_name': 'DUBULEE/FileCacheUtil'}, {'sample_repo_name': 'SuperID/super-cache'}, {'sample_repo_name': 'kinduff/spree_reffiliate'}, {'sample_repo_name': 'mluisbrown/Memories'}, {'sample_repo_name': 'rdebath/Brainfuck'}, {'sample_repo_name': 'richtr/plug.play.js'}, {'sample_repo_name': 'rita-marylin-raquel/softbloks'}, {'sample_repo_name': 'delight-im/OpenSoccer'}, {'sample_repo_name': 'selenith/plasmide'}, {'sample_repo_name': 'apache/stratos'}, {'sample_repo_name': 'nodejs/node-gyp'}, {'sample_repo_name': 'johnhamelink/exrm_deb'}, {'sample_repo_name': 'Calinou/godot-snippets'}, {'sample_repo_name': 'chrisbarrett/emacs-refactor'}], 'var_function-call-1589189329107228874': [{'count_star()': '24286'}], 'var_function-call-5318616242334808465': 'file_storage/function-call-5318616242334808465.json'}

exec(code, env_args)
