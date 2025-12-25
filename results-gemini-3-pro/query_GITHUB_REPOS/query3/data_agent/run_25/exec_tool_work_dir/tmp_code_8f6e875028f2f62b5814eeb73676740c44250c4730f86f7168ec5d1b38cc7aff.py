code = """import json

file_path_repos = locals()['var_function-call-16274142036252595144']
with open(file_path_repos, 'r') as f:
    target_repos_list = json.load(f)

target_repos = set(r['repo_name'] for r in target_repos_list)

print(f"tensorflow/tensorflow in list: {'tensorflow/tensorflow' in target_repos}")
print(f"apple/swift in list: {'apple/swift' in target_repos}")

print("__RESULT__:")
print(json.dumps({"tf_in": 'tensorflow/tensorflow' in target_repos, "swift_in": 'apple/swift' in target_repos}))"""

env_args = {'var_function-call-16274142036252595144': 'file_storage/function-call-16274142036252595144.json', 'var_function-call-17664574478091059843': {'count': 114972, 'examples': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_function-call-9584374500621073620': [{'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}], 'var_function-call-15611622135160010404': {'total_commits': 1077}, 'var_function-call-10123982761667715657': [{'repo_name': 'facebook/react'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'tensorflow/tensorflow'}], 'var_function-call-14129857903622178469': 'file_storage/function-call-14129857903622178469.json'}

exec(code, env_args)
