code = """import json, os
keyRepos = 'var_functions.query_db:5'
pathRepos = locals().get(keyRepos)
# Load repo list
with open(pathRepos, 'r') as f:
    repos = json.load(f)
repo_names = [rec['repo_name'] for rec in repos]
batch_size = 1500  # adjust if needed
batches = [repo_names[i:i+batch_size] for i in range(0, len(repo_names), batch_size)]
queries = []
for batch in batches:
    # escape single quotes in repo names for SQL
    escaped = [name.replace("'", "''") for name in batch]
    in_clause = ','.join(f"'{name}'" for name in escaped)
    query = f"SELECT COUNT(*) as cnt FROM commits WHERE repo_name IN ({in_clause}) AND message IS NOT NULL AND length(message) < 1000 AND lower(subject) NOT LIKE 'merge%' AND lower(subject) NOT LIKE 'update%' AND lower(subject) NOT LIKE 'test%'"
    queries.append(query)
# Output queries list
print('__RESULT__:')
print(json.dumps({'num_batches': len(batches), 'queries': queries[:2], 'sample_batch_size': len(batches[0]) if batches else 0}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'repo_count': 114972, 'first_five': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook']}, 'var_functions.execute_python:10': {'total_repos': 114972}, 'var_functions.execute_python:12': {'total_repos': 114972}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'repo_count': 114972, 'quoted_sample': "'juliandunn/rackspacecloud','rupakg/lorry','Nordstrom/al_agents','fuellab/bootstrap','brint/rax-wordpress-cookbook','rarenerd/train','wallyqs/ruby-nats','dthtvwls/bento','darrenleeweber/aws-ops','yepengxj/binary-buildpack','EntropyWorks/capistrano-chef-test','fhir-crucible/fhir_client','nirmal070125/vagrant-kubernetes-setup','tomduckering/mock-rpm-builder','jdutton/omnibus-collectd','gbm-bailleul/vagrant-machines','chriscowley/puppetmaster-bootstrap','criteo/cassback','saucelabs/sauce_ruby','sec"}, 'var_functions.execute_python:20': {'total_repos': 114972, 'num_batches': 58, 'batch_size': 2000}}

exec(code, env_args)
