code = """import json

# Load Repos
with open(locals()['var_function-call-9963890437017406524'], 'r') as f:
    repo_data = json.load(f)

# Load Commits
with open(locals()['var_function-call-17402463240102202561'], 'r') as f:
    commit_data = json.load(f)

repos_metadata = set(r['repo_name'] for r in repo_data)
repos_artifacts = set(c['repo_name'] for c in commit_data)

intersection = repos_metadata.intersection(repos_artifacts)

print("__RESULT__:")
print(json.dumps({
    "metadata_count": len(repos_metadata),
    "artifacts_count": len(repos_artifacts),
    "intersection_count": len(intersection),
    "sample_metadata": list(repos_metadata)[:5],
    "sample_artifacts": list(repos_artifacts)[:5]
}))"""

env_args = {'var_function-call-13088382630648990338': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-13088382630648991249': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-10504877886590857824': 'file_storage/function-call-10504877886590857824.json', 'var_function-call-15916807321362983497': 114972, 'var_function-call-18020883217836689134': [{'count_star()': '17976'}], 'var_function-call-17402463240102202561': 'file_storage/function-call-17402463240102202561.json', 'var_function-call-8639217337742392574': 0, 'var_function-call-16831755247236410667': [], 'var_function-call-9963890437017406524': 'file_storage/function-call-9963890437017406524.json', 'var_function-call-6990610626592161565': 0}

exec(code, env_args)
