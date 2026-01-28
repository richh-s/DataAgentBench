code = """import json, os
key = 'var_functions.execute_python:42'
path = locals().get(key)
with open(path, 'r') as f:
    result = json.load(f)
query = result['query']
print('__RESULT__:')
print(json.dumps({'query_preview': query[:500], 'query_length': len(query)}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'repo_count': 114972, 'first_five': ['juliandunn/rackspacecloud', 'rupakg/lorry', 'Nordstrom/al_agents', 'fuellab/bootstrap', 'brint/rax-wordpress-cookbook']}, 'var_functions.execute_python:10': {'total_repos': 114972}, 'var_functions.execute_python:12': {'total_repos': 114972}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'repo_count': 114972, 'quoted_sample': "'juliandunn/rackspacecloud','rupakg/lorry','Nordstrom/al_agents','fuellab/bootstrap','brint/rax-wordpress-cookbook','rarenerd/train','wallyqs/ruby-nats','dthtvwls/bento','darrenleeweber/aws-ops','yepengxj/binary-buildpack','EntropyWorks/capistrano-chef-test','fhir-crucible/fhir_client','nirmal070125/vagrant-kubernetes-setup','tomduckering/mock-rpm-builder','jdutton/omnibus-collectd','gbm-bailleul/vagrant-machines','chriscowley/puppetmaster-bootstrap','criteo/cassback','saucelabs/sauce_ruby','sec"}, 'var_functions.execute_python:20': {'total_repos': 114972, 'num_batches': 58, 'batch_size': 2000}, 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.execute_python:28': {'query_prefix': "SELECT COUNT(*) as cnt FROM commits WHERE repo_name IN ('juliandunn/rackspacecloud','rupakg/lorry','Nordstrom/al_agents','fuellab/bootstrap','brint/rax-wordpress-cookbook','rarenerd/train','wallyqs/ru", 'query_suffix': "'m4kspl/scala-ssh','stdweird/aquilon') AND message IS NOT NULL AND length(message) < 1000 AND lower(subject) NOT LIKE 'merge%' AND lower(subject) NOT LIKE 'update%' AND lower(subject) NOT LIKE 'test%'", 'num_repos': 114972}, 'var_functions.execute_python:42': 'file_storage/functions.execute_python:42.json'}

exec(code, env_args)
