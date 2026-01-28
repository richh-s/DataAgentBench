code = """# Filter repositories with Shell language from the query results
shell_repos = [
    {"repo_name": r["repo_name"], "language": "Shell", "bytes_shell": 0} 
    for r in var_functions.query_db_4
]

# Extract Shell bytes from language_description
import re
for i, r in enumerate(var_functions.query_db_4):
    desc = r["language_description"]
    desc_lower = desc.lower()
    if "shell" in desc_lower:
        # Find numbers associated with Shell
        matches = re.findall(r'[Ss]hell[^\d]*\(([\d,]+)\s*bytes\)', desc)
        if matches:
            shell_bytes = int(matches[0].replace(",", ""))
            shell_repos[i]["bytes_shell"] = shell_bytes
        else:
            # Alternative patterns
            matches2 = re.findall(r'([Ss]hell[^\d]*)\(([\d,]+)\s*bytes\)', desc)
            if matches2:
                shell_bytes = int(matches2[0][1].replace(",", ""))
                shell_repos[i]["bytes_shell"] = shell_bytes

shell_repos[:10]"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:4': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}]}

exec(code, env_args)
