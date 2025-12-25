code = """import json

# Get file paths
readme_path = locals()['var_function-call-17198880352755658305']
# Wait, previous result was just the json output. I need the list from previous run or reload.
# I'll just reuse the code logic to get the filtered list.

non_python_path = locals()['var_function-call-7288345727446389507']
readme_path = locals()['var_function-call-7976988069207344350']

with open(non_python_path, 'r') as f:
    non_python_repos_list = json.load(f)
non_python_repos = set(item['repo_name'] for item in non_python_repos_list)

with open(readme_path, 'r') as f:
    readmes = json.load(f)

import os
filtered_readmes = []
for r in readmes:
    if r['sample_repo_name'] in non_python_repos:
        path = r.get('sample_path', '')
        if os.path.basename(path).lower() == 'readme.md':
            filtered_readmes.append(r)

# Check for multiple READMEs per repo
repo_counts = {}
for r in filtered_readmes:
    repo = r['sample_repo_name']
    repo_counts[repo] = repo_counts.get(repo, 0) + 1

duplicates = [r for r, c in repo_counts.items() if c > 1]

# Calculate Repo-level proportion just in case
unique_repos_with_readme = len(repo_counts)
unique_repos_with_copyright = 0
for repo in repo_counts:
    # Check if ANY readme for this repo has copyright
    repo_readmes = [r for r in filtered_readmes if r['sample_repo_name'] == repo]
    if any(str(r['has_copyright']) == '1' for r in repo_readmes):
        unique_repos_with_copyright += 1

proportion_file = 0
if len(filtered_readmes) > 0:
    proportion_file = sum(1 for r in filtered_readmes if str(r['has_copyright']) == '1') / len(filtered_readmes)

proportion_repo = 0
if unique_repos_with_readme > 0:
    proportion_repo = unique_repos_with_copyright / unique_repos_with_readme

print("__RESULT__:")
print(json.dumps({
    "duplicates": len(duplicates),
    "proportion_file": proportion_file,
    "proportion_repo": proportion_repo,
    "count_files": len(filtered_readmes),
    "count_repos": unique_repos_with_readme
}))"""

env_args = {'var_function-call-4560876664558365034': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-7288345727446389507': 'file_storage/function-call-7288345727446389507.json', 'var_function-call-15824860744017369859': [{'count_star()': '128'}], 'var_function-call-7135657625063636368': [{'sample_path': 'device/nfc/nfc.mojom'}, {'sample_path': 'net/tools/quic/synchronous_host_resolver.cc'}, {'sample_path': 'lib/cUnix.mli'}, {'sample_path': 'json4s/src/main/ls/0.6.5.json'}, {'sample_path': 'assets/images/svg/ic_menu_folder_w.svg'}, {'sample_path': 'notes/2.3.1.markdown'}, {'sample_path': '3rdParty/boost/1.61.0b1/boost/hana/monadic_fold_right.hpp'}, {'sample_path': '3rdParty/boost/1.61.0b1/boost/metaparse/v1/iterate_c.hpp'}, {'sample_path': 'java/engine/org/apache/derby/iapi/store/access/BinaryOrderable.java'}, {'sample_path': 'src/program/lwaftr/doc/benchmarks-v1.0/transient-self-test-gbps.png'}, {'sample_path': 'Samples/NET/cs/SimpleNTier/WpfUI/App.config'}, {'sample_path': 'config/services/pmwebapis.xml'}, {'sample_path': '3rdparty/dyncall/doc/manual/dyncall_logo.svg'}, {'sample_path': 'browser/kango-1.7.6/samples/InternationalizationDemo/src/common/extension_info.json'}, {'sample_path': 'src/TKXSDRAW/PACKAGES'}, {'sample_path': 'examples/aes-cmac/aes-cmac.cpp'}, {'sample_path': 'app/src/main/java/com/github/baoti/pioneer/ui/news/list/INewsListView.java'}, {'sample_path': 'aikau/src/main/resources/alfresco/services/i18n/ContentService_ja.properties'}, {'sample_path': 'aclImdb/train/pos/8062_8.txt'}, {'sample_path': 'serial.pub'}], 'var_function-call-5253562430934779955': [{'count_star()': '204'}], 'var_function-call-16102032918604089698': 'file_storage/function-call-16102032918604089698.json', 'var_function-call-7017371445332501810': {'total_readmes': 138, 'copyright_readmes': 19, 'proportion': 0.13768115942028986}, 'var_function-call-14144658479974958331': [{'count(*)': '0'}], 'var_function-call-11625061078076730785': [{'count(*)': '0'}], 'var_function-call-7976988069207344350': 'file_storage/function-call-7976988069207344350.json', 'var_function-call-17198880352755658305': {'total_readmes': 138, 'copyright_readmes': 19, 'proportion': 0.13768115942028986}}

exec(code, env_args)
