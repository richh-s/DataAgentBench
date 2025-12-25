code = """import json

# Load languages
with open(locals()['var_function-call-6641205528560958104'], 'r') as f:
    languages_data = json.load(f)

# Identify non-Python repos
non_python_repos = set()
for entry in languages_data:
    repo = entry.get('repo_name')
    desc = entry.get('language_description', '')
    if repo and 'Python' not in desc:
        non_python_repos.add(repo)

# Load readmes
with open(locals()['var_function-call-918463372830487875'], 'r') as f:
    readmes_data = json.load(f)

# Filter readmes for non-Python repos
target_readmes = []
for r in readmes_data:
    repo = r.get('sample_repo_name')
    if repo in non_python_repos:
        target_readmes.append(r)

# Count copyright in target readmes
copyright_count = 0
for r in target_readmes:
    content = r.get('content')
    if content and 'copyright' in content.lower():
        copyright_count += 1

total_target = len(target_readmes)

proportion = 0.0
if total_target > 0:
    proportion = copyright_count / total_target

print("__RESULT__:")
print(json.dumps({
    "total_readmes": len(readmes_data),
    "target_readmes_count": total_target,
    "copyright_count": copyright_count,
    "proportion": proportion
}))"""

env_args = {'var_function-call-17781051738961249134': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_function-call-10725175935578534522': [{'sample_path': 'device/nfc/nfc.mojom'}, {'sample_path': 'net/tools/quic/synchronous_host_resolver.cc'}, {'sample_path': 'lib/cUnix.mli'}, {'sample_path': 'json4s/src/main/ls/0.6.5.json'}, {'sample_path': 'assets/images/svg/ic_menu_folder_w.svg'}, {'sample_path': 'notes/2.3.1.markdown'}, {'sample_path': '3rdParty/boost/1.61.0b1/boost/hana/monadic_fold_right.hpp'}, {'sample_path': '3rdParty/boost/1.61.0b1/boost/metaparse/v1/iterate_c.hpp'}, {'sample_path': 'java/engine/org/apache/derby/iapi/store/access/BinaryOrderable.java'}, {'sample_path': 'src/program/lwaftr/doc/benchmarks-v1.0/transient-self-test-gbps.png'}], 'var_function-call-6641205528560958104': 'file_storage/function-call-6641205528560958104.json', 'var_function-call-12626732441112409419': [{'count_star()': '128'}], 'var_function-call-2483615797551027872': [{'count_star()': '204'}], 'var_function-call-918463372830487875': 'file_storage/function-call-918463372830487875.json'}

exec(code, env_args)
