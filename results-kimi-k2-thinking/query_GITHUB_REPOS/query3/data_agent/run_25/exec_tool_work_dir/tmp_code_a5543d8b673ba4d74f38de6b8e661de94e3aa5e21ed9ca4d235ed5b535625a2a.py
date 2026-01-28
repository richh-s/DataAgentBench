code = """import json
import os

# Try to access the correct variable based on the key name pattern
# The result of query_db call id 22 is stored in var_functions.query_db:22
# But we need to use the variable name with the full key
result_var = locals().get('var_functions.query_db:22')
if result_var:
    if isinstance(result_var, str) and result_var.endswith('.json'):
        # If it's a file path, load it
        with open(result_var, 'r') as f:
            repos = json.load(f)
    else:
        # Otherwise it's the data directly
        repos = result_var
    
    # Extract repo names
    repo_names = [item['repo_name'] for item in repos]
    total_repos = len(repo_names)
    
    # For performance, let's limit to the first 100 repos first
    # We can batch process if needed
    first_batch = repo_names[:100]
    
    print('__RESULT__:')
    print(json.dumps({
        'total_repos': total_repos,
        'first_batch': first_batch
    }))
else:
    # Check what variables are actually available
    available_vars = [k for k in locals().keys() if 'query_db' in k]
    print('__RESULT__:')
    print(json.dumps({'error': 'Variable not found', 'available': available_vars}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:5': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_functions.query_db:6': [{'repo_name': 'jitsi/jipopro', 'language_description': 'The majority of the code is in Java (137,502 bytes), followed by HTML (2,371 bytes), JavaScript (2,187 bytes), Shell (755 bytes).', 'license': 'apache-2.0'}, {'repo_name': 'NuGet/json-ld.net', 'language_description': 'The codebase includes: C# (425,267 bytes), PowerShell (2,088 bytes), ApacheConf (1,276 bytes).', 'license': 'apache-2.0'}, {'repo_name': 'virtualcoinclub/common', 'language_description': 'While most of the project is built in Java (31,960 bytes), it also incorporates Shell (99 bytes).', 'license': 'apache-2.0'}, {'repo_name': 'pydev/jmx_exporter', 'language_description': 'While most of the project is built in Java (65,290 bytes), it also incorporates Shell (1,232 bytes).', 'license': 'apache-2.0'}, {'repo_name': 'eskatos/qi4j-dev-scripts', 'language_description': 'This repository is mainly written in Shell (3,622 bytes).', 'license': 'apache-2.0'}, {'repo_name': 'doximity/docker-redis', 'language_description': 'The codebase includes: Shell (258 bytes).', 'license': 'apache-2.0'}, {'repo_name': 'raghavkarol/dotfiles', 'language_description': 'The majority of the code is in Emacs Lisp (12,794,633 bytes), followed by C (7,829,374 bytes), Common Lisp (1,331,974 bytes), Scheme (135,143 bytes), Python (48,430 bytes), Elixir (43,695 bytes), Ruby (27,753 bytes), JavaScript (14,323 bytes), YASnippet (14,292 bytes), Standard ML (9,321 bytes), Makefile (6,406 bytes), Shell (5,825 bytes), HTML (131 bytes).', 'license': 'apache-2.0'}, {'repo_name': 'Microsoft/TypeScript', 'language_description': 'The codebase includes: TypeScript (139,268,941 bytes), JavaScript (202,322 bytes), Dockerfile (6,254 bytes), Shell (53 bytes).', 'license': 'apache-2.0'}, {'repo_name': 'romelperez/conky-command', 'language_description': 'The majority of the code is in Lua (615 bytes), followed by Shell (202 bytes).', 'license': 'apache-2.0'}, {'repo_name': 'NorthernMan54/homebridge-wssensor', 'language_description': 'The majority of the code is in Lua (162,628 bytes), followed by JavaScript (44,031 bytes), Shell (746 bytes).', 'license': 'apache-2.0'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': []}

exec(code, env_args)
