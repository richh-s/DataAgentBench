code = """import json
import re

# Load the query result from contents
content_file = 'var_functions.query_db:80'
if isinstance(locals()[content_file], str):
    with open(locals()[content_file], 'r') as f:
        contents_data = json.load(f)
else:
    contents_data = locals()[content_file]

print(f"Contents entries retrieved: {len(contents_data)}")
print(f"Sample: {contents_data[:2]}")

# Check for copyright in these texts
total_checked = 0
with_copyright = 0
without_copyright = 0

copyright_examples = []

for entry in contents_data:
    content = entry.get('content', '')
    if content is None or content == 'None' or not isinstance(content, str):
        continue
    
    total_checked += 1
    # Look for copyright patterns
    if re.search(r'copyright', content, re.IGNORECASE):
        with_copyright += 1
        # Store first example
        if len(copyright_examples) < 3:
            copyright_examples.append({
                'repo': entry.get('repo_name'),
                'id': entry.get('id'),
                'content_preview': content[:200]
            })
    else:
        without_copyright += 1

print(f"Total checked: {total_checked}")
print(f"With copyright: {with_copyright}")
print(f"Without copyright: {without_copyright}")
print(f"Copyright examples: {copyright_examples}")

if total_checked > 0:
    proportion = with_copyright / total_checked
    print(f"Proportion with copyright: {proportion:.2%}")
else:
    proportion = 0

print('__RESULT__:')
print(json.dumps({
    'total_checked': total_checked,
    'with_copyright': with_copyright,
    'without_copyright': without_copyright,
    'proportion': proportion,
    'examples': copyright_examples
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:5': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['commits', 'contents', 'files'], 'var_functions.execute_python:10': 2774729, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'non_python_repos': 2774729, 'readme_files_total': 3086, 'readme_files_filtered': 2196, 'repos_with_readme': 1644, 'sample_repos': ['jgeboski/bitlbee-steam', 'nodesource/docker-node', 'iGEL/it', 'DaMSL/K3', 'IGS/OSDF']}, 'var_functions.execute_python:16': [{'repo_name': 'jgeboski/bitlbee-steam', 'id': '100b93820ade4c16225673b4ca62bb3ade63c313', 'path': 'README.md'}, {'repo_name': 'nodesource/docker-node', 'id': 'ff5c79602cf4f4964d15b6230c551f9d260ab007', 'path': 'centos/7/node/0.10.44/README.md'}, {'repo_name': 'iGEL/it', 'id': '9ed04c6e74db0e3606e716e64e1d7190d5027b15', 'path': 'README.md'}, {'repo_name': 'DaMSL/K3', 'id': '10f4a323a73e5da0d396326e68a7f4afb17a2356', 'path': 'tools/scripts/docker/README.md'}, {'repo_name': 'IGS/OSDF', 'id': '09bb97995c1ce09607e64ed72f9b1089e86c741f', 'path': 'node_modules/express/node_modules/depd/Readme.md'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_repos': 405, 'sample_size': 100, 'ids_to_query_count': 100, 'sample_ids': ['845dd71420cb9df094c29f0c9f9e09ca7442d6da', 'd597a191ec646f358123af42e3cf8b3413de2068', 'b5b1de32091f8bf198802bdd89cb8c7d238d257a', '785699e4010391f046b276cf5c6a15c5385e4640', '69f84df28d204371de44c37f7e41bb3dbd3a9976']}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': [], 'var_functions.query_db:28': [{'repo_name': 'cjdelisle/cjdns', 'path': 'tunnel/README.md'}, {'repo_name': 'poliastro/poliastro', 'path': 'README.rst'}, {'repo_name': 'jgeboski/bitlbee-steam', 'path': 'README.md'}, {'repo_name': 'nodesource/docker-node', 'path': 'centos/7/node/0.10.44/README.md'}, {'repo_name': 'nodesource/docker-node', 'path': 'fedora/22/node/6.1.0/README.md'}, {'repo_name': 'nodesource/docker-node', 'path': 'debian/sid/node/5.8.0/README.md'}, {'repo_name': 'nodesource/docker-node', 'path': 'debian/sid/node/0.10.40/README.md'}, {'repo_name': 'NOAA-GFDL/MOM6-examples', 'path': 'ocean_only/global/INPUT/README'}, {'repo_name': 'gregbanks/python-tabulate', 'path': 'README'}, {'repo_name': 'KDE/qca', 'path': 'certs/README'}, {'repo_name': 'QEF/q-e', 'path': 'NEB/examples/ESM_example/README'}, {'repo_name': 'QEF/q-e', 'path': 'upftools/README'}, {'repo_name': 'h2o/h2o', 'path': 'deps/mruby-dir/README.md'}, {'repo_name': 'iGEL/it', 'path': 'README.md'}, {'repo_name': 'm4b/rdr', 'path': 'README.md'}, {'repo_name': 'npm/npm', 'path': 'node_modules/node-gyp/node_modules/npmlog/README.md'}, {'repo_name': 'npm/npm', 'path': 'node_modules/read-package-json/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/README.md'}, {'repo_name': 'ojs/ojs', 'path': 'app/Resources/node_modules/uglify-js/README.md'}, {'repo_name': 'ovh/tat', 'path': 'vendor/github.com/spf13/pflag/README.md'}, {'repo_name': 'DaMSL/K3', 'path': 'tools/scripts/docker/README.md'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [], 'var_functions.query_db:34': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_repo_name': 'nwjs/chromium.src'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_repo_name': 'nwjs/chromium.src'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'sample_repo_name': 'pirapira/coq2rust'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_repo_name': 'unfiltered/unfiltered'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'sample_repo_name': 'JosefRypacek/PrimeTV'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [], 'var_functions.query_db:42': [], 'var_functions.execute_python:44': {'total_readme_files': 100, 'non_python_repos_count': 2774729, 'non_python_readme_files': 67, 'sample_ids': ['100b93820ade4c16225673b4ca62bb3ade63c313', '9ed04c6e74db0e3606e716e64e1d7190d5027b15', '5f0d4f75fdb2cf3b303d312d6898d3413fccfca7', '4e1d480f9228a40af4e3e4c507b38d593e3e588b', 'e75de9d29f2af646ae811eb662be95f7f3dc6cc2', '0329b60fe20ccf905a4f788d3853ebd08dfbf7ab', '27c3a330d6f2bc7588a5c6eb14762fc20a1a1783', 'ec5adbce44a5723719e95aaa267282d6c0e7d0e1', '60a9af5a1bbd2ed78ca7f4563c8f39370bb0b44f', '817092bcd9d85ae89a2345fc67907af0a16acde3']}, 'var_functions.execute_python:46': {'non_python_repo_count': 2774729, 'next_step': 'Query all README files and filter'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:50': {'non_python_repo_count': 10000, 'sample_repos': ['jqmp/bash', 'Velocity-/scapefs', 'arosenberger/nalloc_2.10', 'Microway/MCMS-OpenHPC-Recipe', 'droboports/ruby2']}, 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.execute_python:54': {'non_python_repos': 10000, 'readme_files_total': 1094, 'non_python_readme_files': 5, 'non_python_repos_with_readme': 5, 'sample_ids': ['fdc0089b9c16178120ecfaefb88f3df709a49396', '73d5a44f92c081002ed2e8d0d3b825a946668a86', '28607efcc9afa50de701b6cddf77eeca1e1bfe23', '7024bc36155723e6fb7aff491444ef93f43dc023', '13aae67f0133694c88f0f261352add5f6d89995a']}, 'var_functions.query_db:56': [], 'var_functions.query_db:58': [{'total_files': '524077'}], 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.execute_python:62': {'non_python_repos_sampled': 10000, 'readme_files_total': 1059, 'non_python_readme_files': 5, 'batch_file_ids': ['7024bc36155723e6fb7aff491444ef93f43dc023', '13aae67f0133694c88f0f261352add5f6d89995a', '73d5a44f92c081002ed2e8d0d3b825a946668a86', 'fdc0089b9c16178120ecfaefb88f3df709a49396', '28607efcc9afa50de701b6cddf77eeca1e1bfe23'], 'batch_repo_names': ['DandyDev/sentry-ansible-vagrant', 'blstream/sbt-search-maven-plugin', 'boombatower/docker-backup', 'ricciocri/vimrc', 'unixorn/awesome-zsh-plugins']}, 'var_functions.execute_python:64': {'total_files': 1059, 'sample_ids': ['267269c0d16b1d0524d8bcd1f69528c820003f67', '1b1528a6f48384f5dd14b8f91739311b8d2f8050', 'bf0eb0f264b432403026add25c021e9c2f967545', 'dfa72501a6d22106c7c59a2567a3543631b57fa4', '878ffd04662aed3b4fb3ca979fdae1da962bf60c', 'cecd6889e2fb5604ea1d8d527e5b94a069275902', '8f6e96325a1daea5807dc808cbdff7ea0d502300', '29348291bbf1be9dc735248a0eaffd424cfe032a', '14f8ac5f585429fb592603f00fdcb3a0560d9c80', '9b3effcb1b816b7ce267eaef6bdb426133e401c2'], 'sample_repos': ['0dayZh/bitcoin_developer_guide', '121595113/mobile-build', '2gis/nuclear-river', '314eter/atom-ocaml-indent', '84Paris/canvasvideo.js', 'A5hleyRich/wp-background-processing', 'AMDmi3/dangling_ptr', 'AdRoll/backbone.d3', 'AlessandroZ/LaZagne', 'AnUnknownMiner/FOAAS-Java']}, 'var_functions.execute_python:66': {'non_python_repos_subset': 1000, 'ready_to_query_contents': True}, 'var_functions.execute_python:68': {'readme_files_total': 1059, 'non_python_repos_count': 1000, 'non_python_readmes': 0, 'sample_repo_names': ['avatarnewyork/dockerenv_sphinx', 'antob/dotfiles', 'DragonCherry/HFSwipeView', 'zenangst/pod-swift', 'rubenmoya/dotfiles']}, 'var_functions.execute_python:70': {'repos_with_readme_count': 1059, 'batch_repos_count': 100, 'sample_repos': ['xwsoul/vim-zephir', 'mstruebing/web-s', 'lowleveldesign/diagnostics-kit', 'ZoRdAK/ota-server', 'andihit/coptermanager-arduino']}, 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.execute_python:74': {'readme_entries': 1059, 'unique_repos': 1059, 'files_to_query': 50, 'sample_file_ids': ['267269c0d16b1d0524d8bcd1f69528c820003f67', '1b1528a6f48384f5dd14b8f91739311b8d2f8050', 'bf0eb0f264b432403026add25c021e9c2f967545', 'dfa72501a6d22106c7c59a2567a3543631b57fa4', '878ffd04662aed3b4fb3ca979fdae1da962bf60c']}, 'var_functions.execute_python:76': {'artifact_repos': 1059, 'metadata_repos': 10000, 'overlap': 5, 'has_overlap': True}, 'var_functions.execute_python:78': {'filtered_readme_count': 0, 'unique_repos': 0, 'repos': []}, 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json'}

exec(code, env_args)
