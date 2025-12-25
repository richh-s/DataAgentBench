code = """import json
import os

# Get file paths from storage variables
non_python_path = locals()['var_function-call-7288345727446389507']
readme_path = locals()['var_function-call-7976988069207344350']

# Load Non-Python repos
with open(non_python_path, 'r') as f:
    non_python_repos_list = json.load(f)
non_python_repos = set(item['repo_name'] for item in non_python_repos_list)

# Load READMEs
with open(readme_path, 'r') as f:
    readmes = json.load(f)

# Filter
filtered_readmes = []
for r in readmes:
    # Check repo
    if r['sample_repo_name'] not in non_python_repos:
        continue
    
    # Check filename is README.md (case insensitive)
    path = r.get('sample_path', '')
    filename = os.path.basename(path)
    if filename.lower() == 'readme.md':
        filtered_readmes.append(r)

total_readmes = len(filtered_readmes)
copyright_readmes = sum(1 for r in filtered_readmes if str(r['has_copyright']) == '1')

proportion = 0.0
if total_readmes > 0:
    proportion = copyright_readmes / total_readmes

print("__RESULT__:")
print(json.dumps({
    "total_readmes": total_readmes,
    "copyright_readmes": copyright_readmes,
    "proportion": proportion
}))"""

env_args = {'var_function-call-4560876664558365034': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-7288345727446389507': 'file_storage/function-call-7288345727446389507.json', 'var_function-call-15824860744017369859': [{'count_star()': '128'}], 'var_function-call-7135657625063636368': [{'sample_path': 'device/nfc/nfc.mojom'}, {'sample_path': 'net/tools/quic/synchronous_host_resolver.cc'}, {'sample_path': 'lib/cUnix.mli'}, {'sample_path': 'json4s/src/main/ls/0.6.5.json'}, {'sample_path': 'assets/images/svg/ic_menu_folder_w.svg'}, {'sample_path': 'notes/2.3.1.markdown'}, {'sample_path': '3rdParty/boost/1.61.0b1/boost/hana/monadic_fold_right.hpp'}, {'sample_path': '3rdParty/boost/1.61.0b1/boost/metaparse/v1/iterate_c.hpp'}, {'sample_path': 'java/engine/org/apache/derby/iapi/store/access/BinaryOrderable.java'}, {'sample_path': 'src/program/lwaftr/doc/benchmarks-v1.0/transient-self-test-gbps.png'}, {'sample_path': 'Samples/NET/cs/SimpleNTier/WpfUI/App.config'}, {'sample_path': 'config/services/pmwebapis.xml'}, {'sample_path': '3rdparty/dyncall/doc/manual/dyncall_logo.svg'}, {'sample_path': 'browser/kango-1.7.6/samples/InternationalizationDemo/src/common/extension_info.json'}, {'sample_path': 'src/TKXSDRAW/PACKAGES'}, {'sample_path': 'examples/aes-cmac/aes-cmac.cpp'}, {'sample_path': 'app/src/main/java/com/github/baoti/pioneer/ui/news/list/INewsListView.java'}, {'sample_path': 'aikau/src/main/resources/alfresco/services/i18n/ContentService_ja.properties'}, {'sample_path': 'aclImdb/train/pos/8062_8.txt'}, {'sample_path': 'serial.pub'}], 'var_function-call-5253562430934779955': [{'count_star()': '204'}], 'var_function-call-16102032918604089698': 'file_storage/function-call-16102032918604089698.json', 'var_function-call-7017371445332501810': {'total_readmes': 138, 'copyright_readmes': 19, 'proportion': 0.13768115942028986}, 'var_function-call-14144658479974958331': [{'count(*)': '0'}], 'var_function-call-11625061078076730785': [{'count(*)': '0'}], 'var_function-call-7976988069207344350': 'file_storage/function-call-7976988069207344350.json'}

exec(code, env_args)
