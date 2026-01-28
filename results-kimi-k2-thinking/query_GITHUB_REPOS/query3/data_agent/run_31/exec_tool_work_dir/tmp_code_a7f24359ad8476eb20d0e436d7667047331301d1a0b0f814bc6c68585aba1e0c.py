code = """import json

# Read the full repository list
file_path = 'file_storage/functions.query_db:0.json'
with open(file_path, 'r') as f:
    repo_data = json.load(f)

repo_names = [repo['repo_name'] for repo in repo_data]

# Create batches of 1000 repos each
batch_size = 1000
batches = []
for i in range(0, len(repo_names), batch_size):
    batch = repo_names[i:i+batch_size]
    batches.append(batch)

print('__RESULT__:')
print(json.dumps({
    'total_repos': len(repo_names),
    'num_batches': len(batches),
    'batch_size': batch_size,
    'first_batch_sample': batches[0][:5] if batches else []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': [{'repo_name': 'facebook/react'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'tensorflow/tensorflow'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:20': {'count': 114972, 'first_five': [{'repo_name': 'jitsi/jipopro'}, {'repo_name': 'NuGet/json-ld.net'}, {'repo_name': 'virtualcoinclub/common'}, {'repo_name': 'pydev/jmx_exporter'}, {'repo_name': 'eskatos/qi4j-dev-scripts'}]}, 'var_functions.execute_python:22': {'total_repos': 114972, 'first_10': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor'], 'sample_batch': ['disqus/python-phabricator', 'shenguoquan/netty', 'abutcher/kubernetes', 'coderanger/brix', 'pnikosis/jHTML2Md', 'opuk/puppet-devel-workshop', 'HazemKhaled/Suds', 'bineanzhou/google-guice', 'bazelbuild/rules_kotlin', 'fbladilo/testing']}}

exec(code, env_args)
