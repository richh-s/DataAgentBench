code = """import json

# Load all READMEs
# Expected format: [{"sample_repo_name": "...", "content": "..."}, ...]
with open(locals()['var_function-call-13853300728743934896'], 'r') as f:
    readmes = json.load(f)

# Load python repos
# Expected format: [{"repo_name": "..."}, ...]
with open(locals()['var_function-call-1678370770831163231'], 'r') as f:
    python_repos_data = json.load(f)
python_repos = {item['repo_name'] for item in python_repos_data}

# Filter READMEs for non-python repos
non_python_readmes = [r for r in readmes if r['sample_repo_name'] not in python_repos]

# Count READMEs with copyright
copyright_count = 0
for r in non_python_readmes:
    content = r.get('content')
    if content and 'copyright' in content.lower():
        copyright_count += 1

numerator = copyright_count
denominator = len(non_python_readmes)

print(f"Total READMEs: {len(readmes)}")
print(f"Non-python READMEs: {denominator}")
print(f"With Copyright: {numerator}")

if denominator == 0:
    result = 0.0
else:
    result = numerator / denominator

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9965432359590813433': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-10642243385388096041': 'file_storage/function-call-10642243385388096041.json', 'var_function-call-7004707044584297419': [{'COUNT(*)': '3325634'}], 'var_function-call-9639577497645477698': [{'COUNT(*)': '2774729'}], 'var_function-call-650508763090176396': [{'count(DISTINCT sample_repo_name)': '21'}], 'var_function-call-15497029972618072591': [{'count(DISTINCT sample_repo_name)': '12837'}], 'var_function-call-4312641892406524807': 'file_storage/function-call-4312641892406524807.json', 'var_function-call-15639155349712836456': [{'sample_repo_name': 'F1ReKing/wheelview'}, {'sample_repo_name': 'kinduff/spree_reffiliate'}, {'sample_repo_name': 'adafruit/Adafruit-Trinket-Gemma-Bootloader'}, {'sample_repo_name': 'noveogroup/android-logger'}, {'sample_repo_name': 'rubylit/guevara'}, {'sample_repo_name': 'chrisbarrett/emacs-refactor'}, {'sample_repo_name': 'dblock/slack-google-bot'}, {'sample_repo_name': 'DUBULEE/FileCacheUtil'}, {'sample_repo_name': 'SuperID/super-cache'}, {'sample_repo_name': 'selenith/plasmide'}, {'sample_repo_name': 'apache/stratos'}, {'sample_repo_name': 'nodejs/node-gyp'}, {'sample_repo_name': 'johnhamelink/exrm_deb'}, {'sample_repo_name': 'Calinou/godot-snippets'}, {'sample_repo_name': 'mluisbrown/Memories'}, {'sample_repo_name': 'rdebath/Brainfuck'}, {'sample_repo_name': 'richtr/plug.play.js'}, {'sample_repo_name': 'hypriot/rpi-busybox-httpd'}, {'sample_repo_name': 'rita-marylin-raquel/softbloks'}, {'sample_repo_name': 'delight-im/OpenSoccer'}, {'sample_repo_name': 'parro-it/is-fqdn'}], 'var_function-call-1678370770831163231': 'file_storage/function-call-1678370770831163231.json', 'var_function-call-8797265863494452132': 0.0019071837253655435, 'var_function-call-5673418668610958535': [{'count_star()': '277'}], 'var_function-call-10792316395022402645': [{'count_star()': '24286'}], 'var_function-call-13853300728743934896': 'file_storage/function-call-13853300728743934896.json'}

exec(code, env_args)
