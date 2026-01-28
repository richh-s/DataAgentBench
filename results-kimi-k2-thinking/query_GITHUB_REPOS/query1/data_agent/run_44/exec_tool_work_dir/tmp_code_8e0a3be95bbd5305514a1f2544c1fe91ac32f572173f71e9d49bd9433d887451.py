code = """import json
import re

# Load the readme data from the file
with open(locals()['var_functions.query_db:22'], 'r') as f:
    readme_data = json.load(f)

# Take a random sample of READMEs available and classify them
sample_size = min(500, len(readme_data))
readmes_with_python = 0
readmes_without_python = 0
total_valid_readmes = 0

repos_with_copyright = []
repos_without_copyright = []

for i, readme in enumerate(readme_data[:sample_size]):
    content = readme.get('content', '')
    if content and content != 'None':
        total_valid_readmes += 1
        
        # Check if this appears to be Python-related
        has_python = False
        python_indicators = ['python', 'pyqt', 'django', 'flask', 'pip', 'numpy', 'pandas']
        
        for indicator in python_indicators:
            if re.search(indicator, content, re.IGNORECASE):
                has_python = True
                break
        
        if has_python:
            readmes_with_python += 1
        else:
            readmes_without_python += 1
            
            # Check for copyright in non-Python repos
            if re.search(r'copyright', content, re.IGNORECASE):
                repos_with_copyright.append(readme['sample_repo_name'])
            else:
                repos_without_copyright.append(readme['sample_repo_name'])

result = {
    'total_sampled': sample_size,
    'valid_readmes': total_valid_readmes,
    'python_readmes': readmes_with_python,
    'non_python_readmes': readmes_without_python,
    'non_python_with_copyright': len(repos_with_copyright),
    'non_python_without_copyright': len(repos_without_copyright),
    'proportion': len(repos_with_copyright) / readmes_without_python if readmes_without_python > 0 else 0,
    'sample_copyright_repos': repos_with_copyright[:10],
    'sample_no_copyright_repos': repos_without_copyright[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_repos': 3325634, 'non_python_repos': 2774729, 'sample_non_python': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}, 'var_functions.execute_python:14': {'total_readmes_checked': 0, 'readmes_with_copyright': 0, 'sample_copyright_repos': []}, 'var_functions.execute_python:16': {'total_readmes_sampled': 100, 'readmes_with_content': 97, 'readmes_with_copyright': 7, 'copyright_percent': 7.216494845360824, 'sample_copyright_repos': ['selenith/plasmide', 'apache/stratos', 'id-Software/Quake-III-Arena', 'espadrine/opera', 'svn2github/chromium-depot-tools', 'mluisbrown/Memories', 'F1ReKing/wheelview']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:24': {'total_non_python_readmes': 0, 'readmes_with_copyright': 0, 'readmes_without_copyright': 0, 'proportion': 0, 'percentage': 0, 'sample_repos_with_copyright': []}, 'var_functions.execute_python:26': {'total_readme_repos': 268, 'total_non_python_repos': 50000, 'common_repos_count': 0, 'sample_common_repos': [], 'sample_readme_repos': ['rtrouton/rtrouton_scripts', 'DynamoRIO/dynamorio', 'ninja-ide/ninja-ide', 'sclorg/rhscl-dockerfiles', 'cwilso/midi-synth', 'pezy/LeetCode', 'opencog/atomspace', 'retep998/winapi-rs', 'ha/doozerd', 'JiyunTech/Kever'], 'sample_non_python_repos': ['nraboy/ng-cordova-oauth', 'this-week-in/pinboard-client', 'oroca/SkyRover_Projects', 'ericmittelhammer/NNViz', 'skyujilong/ImgLazyLoader', 'shangaslammi/haskeroids', 'nz-social-investment-unit/social_investment_analytical_layer', 'aur-archive/aafigure', 'wenshin/clearflux', 'bhargavkumar040/android-source-browsing.platform--external--bison']}}

exec(code, env_args)
