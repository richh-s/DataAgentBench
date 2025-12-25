code = """import json
import re

# Load the result from the previous query
with open(locals()['var_function-call-16311214670039386027'], 'r') as f:
    repos_data = json.load(f)

# Function to check if 'Shell' is a language (excluding PowerShell)
# The format is like "... Ruby (123 bytes), Shell (456 bytes)..."
# We look for "Shell (" and ensure it's not "PowerShell ("
def uses_shell(desc):
    if not desc:
        return False
    # Check for "Shell (" but verify it's not preceded by characters that make it another language
    # Assuming "Shell" is the name used by GitHub for standard shell scripts.
    # regex: word boundary or start of string + Shell + space + (
    return re.search(r'(?:^|[\s,])Shell\s*\(', desc) is not None

# Filter repos
target_repos = [r['repo_name'] for r in repos_data if uses_shell(r['language_description'])]

print("__RESULT__:")
print(json.dumps(target_repos))"""

env_args = {'var_function-call-18351094842040007428': ['languages', 'repos', 'licenses'], 'var_function-call-15111763840125797643': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-10355730482054082399': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-16311214670039386027': 'file_storage/function-call-16311214670039386027.json'}

exec(code, env_args)
