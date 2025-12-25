code = """import json

# Load non-python repos
non_python_repos_file = locals()['var_function-call-8001171644703104223']
# It's a file path string
with open(non_python_repos_file, 'r') as f:
    non_python_repos_data = json.load(f)

non_python_repos = set(item['repo_name'] for item in non_python_repos_data)

# Load copyright repos
# This is a list in memory
copyright_repos_data = locals()['var_function-call-16395887893214215515']
copyright_repos = set(item['sample_repo_name'] for item in copyright_repos_data)

# Calculate intersection
intersection = non_python_repos.intersection(copyright_repos)

num_non_python = len(non_python_repos)
num_intersection = len(intersection)

if num_non_python == 0:
    proportion = 0
else:
    proportion = num_intersection / num_non_python

print("__RESULT__:")
print(json.dumps({
    "num_non_python": num_non_python,
    "num_intersection": num_intersection,
    "proportion": proportion
}))"""

env_args = {'var_function-call-4474284480473766713': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-8001171644703104223': 'file_storage/function-call-8001171644703104223.json', 'var_function-call-16395887893214215515': [{'sample_repo_name': 'F1ReKing/wheelview'}, {'sample_repo_name': 'kinduff/spree_reffiliate'}, {'sample_repo_name': 'hypriot/rpi-busybox-httpd'}, {'sample_repo_name': 'adafruit/Adafruit-Trinket-Gemma-Bootloader'}, {'sample_repo_name': 'rubylit/guevara'}, {'sample_repo_name': 'noveogroup/android-logger'}, {'sample_repo_name': 'dblock/slack-google-bot'}, {'sample_repo_name': 'DUBULEE/FileCacheUtil'}, {'sample_repo_name': 'SuperID/super-cache'}, {'sample_repo_name': 'nodejs/node-gyp'}, {'sample_repo_name': 'johnhamelink/exrm_deb'}, {'sample_repo_name': 'Calinou/godot-snippets'}, {'sample_repo_name': 'chrisbarrett/emacs-refactor'}, {'sample_repo_name': 'mluisbrown/Memories'}, {'sample_repo_name': 'rdebath/Brainfuck'}, {'sample_repo_name': 'richtr/plug.play.js'}, {'sample_repo_name': 'rita-marylin-raquel/softbloks'}, {'sample_repo_name': 'delight-im/OpenSoccer'}]}

exec(code, env_args)
