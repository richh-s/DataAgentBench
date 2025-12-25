code = """import json

# Load all repos in contents
with open(locals()['var_function-call-4312641892406524807'], 'r') as f:
    all_repos_data = json.load(f)
all_repos = {item['sample_repo_name'] for item in all_repos_data}

# Load python repos
with open(locals()['var_function-call-1678370770831163231'], 'r') as f:
    python_repos_data = json.load(f)
python_repos = {item['repo_name'] for item in python_repos_data}

# Load target repos (repos with README copyright)
# This variable is a list, not a file path
target_repos_data = locals()['var_function-call-15639155349712836456']
target_repos = {item['sample_repo_name'] for item in target_repos_data}

# Filter for non-python repos
non_python_repos = all_repos - python_repos
matching_target_repos = target_repos.intersection(non_python_repos)

numerator = len(matching_target_repos)
denominator = len(non_python_repos)

print(f"Total repos in contents: {len(all_repos)}")
print(f"Repos using Python (in metadata): {len(python_repos)}") # This is the full list from metadata
print(f"Non-python repos in contents: {len(non_python_repos)}")
print(f"Target repos (README+Copyright): {len(target_repos)}")
print(f"Target repos excluding Python: {len(matching_target_repos)}")

if denominator == 0:
    result = 0.0
else:
    result = numerator / denominator

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9965432359590813433': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-10642243385388096041': 'file_storage/function-call-10642243385388096041.json', 'var_function-call-7004707044584297419': [{'COUNT(*)': '3325634'}], 'var_function-call-9639577497645477698': [{'COUNT(*)': '2774729'}], 'var_function-call-650508763090176396': [{'count(DISTINCT sample_repo_name)': '21'}], 'var_function-call-15497029972618072591': [{'count(DISTINCT sample_repo_name)': '12837'}], 'var_function-call-4312641892406524807': 'file_storage/function-call-4312641892406524807.json', 'var_function-call-15639155349712836456': [{'sample_repo_name': 'F1ReKing/wheelview'}, {'sample_repo_name': 'kinduff/spree_reffiliate'}, {'sample_repo_name': 'adafruit/Adafruit-Trinket-Gemma-Bootloader'}, {'sample_repo_name': 'noveogroup/android-logger'}, {'sample_repo_name': 'rubylit/guevara'}, {'sample_repo_name': 'chrisbarrett/emacs-refactor'}, {'sample_repo_name': 'dblock/slack-google-bot'}, {'sample_repo_name': 'DUBULEE/FileCacheUtil'}, {'sample_repo_name': 'SuperID/super-cache'}, {'sample_repo_name': 'selenith/plasmide'}, {'sample_repo_name': 'apache/stratos'}, {'sample_repo_name': 'nodejs/node-gyp'}, {'sample_repo_name': 'johnhamelink/exrm_deb'}, {'sample_repo_name': 'Calinou/godot-snippets'}, {'sample_repo_name': 'mluisbrown/Memories'}, {'sample_repo_name': 'rdebath/Brainfuck'}, {'sample_repo_name': 'richtr/plug.play.js'}, {'sample_repo_name': 'hypriot/rpi-busybox-httpd'}, {'sample_repo_name': 'rita-marylin-raquel/softbloks'}, {'sample_repo_name': 'delight-im/OpenSoccer'}, {'sample_repo_name': 'parro-it/is-fqdn'}], 'var_function-call-1678370770831163231': 'file_storage/function-call-1678370770831163231.json'}

exec(code, env_args)
