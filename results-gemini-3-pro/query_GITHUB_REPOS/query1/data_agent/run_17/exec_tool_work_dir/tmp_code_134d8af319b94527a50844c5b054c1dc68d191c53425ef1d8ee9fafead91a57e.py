code = """import json

# Load languages
with open(locals()['var_function-call-2946045897821113260'], 'r') as f:
    languages_data = json.load(f)

# Identify non-Python repos
non_python_repos = set()
for item in languages_data:
    desc = item.get('language_description', '')
    if desc and 'Python' not in desc:
        non_python_repos.add(item['repo_name'])

# Load contents (READMEs)
with open(locals()['var_function-call-12726813032886270267'], 'r') as f:
    readme_data = json.load(f)

print(f"Total READMEs fetched: {len(readme_data)}")

# Filter READMEs for non-Python repos
filtered_readmes = []
for item in readme_data:
    repo = item.get('sample_repo_name')
    if repo in non_python_repos:
        filtered_readmes.append(item)

print(f"READMEs in non-Python repos: {len(filtered_readmes)}")

# Count copyright
copyright_count = 0
for item in filtered_readmes:
    content = item.get('content', '')
    if content and 'copyright' in content.lower():
        copyright_count += 1

print(f"Copyright count: {copyright_count}")

proportion = 0.0
if len(filtered_readmes) > 0:
    proportion = copyright_count / len(filtered_readmes)

print("__RESULT__:")
print(json.dumps(proportion))"""

env_args = {'var_function-call-16476119959139784129': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_function-call-9280870360935075941': 'file_storage/function-call-9280870360935075941.json', 'var_function-call-2946045897821113260': 'file_storage/function-call-2946045897821113260.json', 'var_function-call-12726813032886270267': 'file_storage/function-call-12726813032886270267.json', 'var_function-call-7077201696209082913': 0.1485148514851485, 'var_function-call-11823672658332297909': [{'count(*)': '3325634'}], 'var_function-call-659506348204056119': [], 'var_function-call-3387148875032680109': [], 'var_function-call-6669671610140129786': [{'repo_name': 'nwjs/chromium.src', 'ref': 'refs/heads/nw15', 'path': 'chrome/app/theme/default_200_percent/common/textfield_top_left.png'}, {'repo_name': 'nwjs/chromium.src', 'ref': 'refs/heads/nw15', 'path': 'third_party/WebKit/Source/modules/webusb/USBIsochronousOutTransferPacket.h'}, {'repo_name': 'nwjs/chromium.src', 'ref': 'refs/heads/nw15', 'path': 'third_party/WebKit/LayoutTests/platform/win/fast/table/large-width-expected.png'}, {'repo_name': 'nwjs/chromium.src', 'ref': 'refs/heads/nw15', 'path': 'build/android/pylib/remote/device/dummy/src/org/chromium/dummy/Dummy.java'}, {'repo_name': 'nwjs/chromium.src', 'ref': 'refs/heads/nw15', 'path': 'third_party/WebKit/LayoutTests/fast/events/right-click-focus-expected.txt'}], 'var_function-call-2793475236085628657': [], 'var_function-call-12930386529216833014': [{'count_star()': '1059'}], 'var_function-call-7865152132662430789': [{'path': 'tunnel/README.md'}, {'path': 'README.rst'}, {'path': 'README.md'}, {'path': 'centos/7/node/0.10.44/README.md'}, {'path': 'fedora/22/node/6.1.0/README.md'}, {'path': 'debian/sid/node/5.8.0/README.md'}, {'path': 'debian/sid/node/0.10.40/README.md'}, {'path': 'ocean_only/global/INPUT/README'}, {'path': 'README'}, {'path': 'Breeze Dark/mimetypes/16/text-x-readme.svg'}, {'path': 'archdroid-icon-theme/Archdroid-BlueGreyDark/mimetypes/scalable/gnome-mime-text-x-readme.svg'}, {'path': 'archdroid-icon-theme/Archdroid-Blue/mimetypes/scalable/gnome-mime-text-x-readme.svg'}, {'path': 'certs/README'}, {'path': 'NEB/examples/ESM_example/README'}, {'path': 'upftools/README'}, {'path': 'deps/mruby-dir/README.md'}, {'path': 'README.md'}, {'path': 'README.md'}, {'path': 'node_modules/node-gyp/node_modules/npmlog/README.md'}, {'path': 'node_modules/read-package-json/node_modules/glob/node_modules/minimatch/node_modules/brace-expansion/README.md'}], 'var_function-call-11954241020657723413': [{'count_star()': '2743'}], 'var_function-call-4859353504599368460': [{'count_star()': '128'}], 'var_function-call-9964557943106075060': [], 'var_function-call-14557135305532381841': [{'id': '316ad972693d0355c3504729fff14287419e004d'}, {'id': 'daa40d563068ee94f01b1e87952d607a6588a589'}, {'id': '6bd679ec4ff94d8149986d49b8e789d1b4d6a44a'}, {'id': '0cfcfb70b14958a8ba30cb83808c9bcc25516969'}, {'id': 'de516c994d6cc8b7bcc1fb6bf986699fced404f6'}], 'var_function-call-17859212942430123984': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75'}], 'var_function-call-9620634410081385224': [{'count_star()': '2'}], 'var_function-call-14865391880663372200': [{'count_star()': '251'}]}

exec(code, env_args)
