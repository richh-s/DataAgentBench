code = """import json

# Get the repository list data
repo_data = locals()['var_functions.query_db:22']

# Parse the JSON data
if isinstance(repo_data, str):
    with open(repo_data, 'r') as f:
        repo_list = json.load(f)
else:
    repo_list = repo_data

# Extract all repository names
all_repos = [repo['repo_name'] for repo in repo_list]
total_repos = len(all_repos)

print(f'Total repositories found: {total_repos}')

# Create batches of repository names (DuckDB can handle reasonably large IN clauses)
batch_size = 2000  # Process 2000 repos at a time
batches = []
for i in range(0, total_repos, batch_size):
    batch = all_repos[i:i+batch_size]
    batches.append(batch)

print(f'Created {len(batches)} batches of up to {batch_size} repositories each')

# Store the batches for the next step
print('__RESULT__:')
print(json.dumps(batches))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'commit_count': '0'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'commit_count': '0'}], 'var_functions.execute_python:26': {'total_repos': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor', 'ivschukin/learning-azure', 'arrawatia/cp-docker-images', 'wolfitem/docker', 'sdgdsffdsfff/ModSecurity', 'frapposelli/govmomi', 'Grimmjowjack/google-services', 'chuangWu/butterknife', 'louwrentius/eztables', 'riddlesio/hack-man-engine', 'DavitTevanyan/word2vec', 'Siphon098/git-sync-batch', 'hitwangyu/apache-common-pool2', 'wshearn/openshift-ansible', 'javasoze/clue', 'hschema/schemaorg', 'simba518/AniEditor', 'abhgupta/kubernetes', 'enovance/puppet-tripleo', 'garana/mod_reslog', 'shiumachi/hbck-analyzer', 'wildfly-swarm/wildfly-swarm-core', 'grmartin/android-vcard', 'allancth/camel', 'wkalt/puppetdb', 'bep/killswitch', 'mark-adams/compose', 'navnorth/LR-Data', 'ShengC/remotely', 'triAGENS/guacamole', 'cavanm/apn-defaults', 'ampproject/amphtml', 'zkrejcov/drools-wb', 'bmistry13/kafka', 'googleapis/java-retail', 'kewalaka/chocolatey-packages', 'AzazelN28/din', 'ZacharyKlein/grails-isomorphic', 'automatecloud/docker-ddc-vagrant', 'Lambda3/docker-vsts-agent', 'darilek/dotvvm']}}

exec(code, env_args)
