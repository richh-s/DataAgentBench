code = """import json

top_repos = [
    "torvalds/linux",
    "apple/swift",
    "twbs/bootstrap",
    "Microsoft/vscode",
    "facebook/react"
]

repo_names_str = ', '.join([f"'{name}'" for name in top_repos])

query = f"SELECT repo_name, language_description FROM languages WHERE repo_name IN ({repo_names_str});"

print("__RESULT__:")
print(json.dumps({"query": query}))"""

env_args = {'var_function-call-2340926761176457406': 'file_storage/function-call-2340926761176457406.json', 'var_function-call-13863585805078690205': 'file_storage/function-call-13863585805078690205.json', 'var_function-call-8689555944964674122': 'file_storage/function-call-8689555944964674122.json', 'var_function-call-3767942551275076807': [], 'var_function-call-8917675196223738767': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-2689555683014066056': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-8429983972344603568': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-17346842645571104268': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
