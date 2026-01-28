code = """import json

# Get sample repos from metadata_database
repo_data = locals()['var_functions.query_db:22']
if isinstance(repo_data, str):
    with open(repo_data, 'r') as f:
        metadata_repos = json.load(f)
else:
    metadata_repos = repo_data

metadata_repo_names = set([repo['repo_name'] for repo in metadata_repos])
print(f'Total repos in metadata_database: {len(metadata_repo_names)}')

# Get repos from artifacts_database commits table
artifacts_data = locals()['var_functions.query_db:32']
artifacts_repo_names = set([repo['repo_name'] for repo in artifacts_data])
print(f'Repos in artifacts_database sample: {artifacts_repo_names}')

# Check for any overlap
overlap = metadata_repo_names.intersection(artifacts_repo_names)
print(f'Overlap between databases: {len(overlap)} repos')
if overlap:
    print(f'Overlapping repos: {list(overlap)[:10]}')

print('__RESULT__:')
print(json.dumps({
    'metadata_repos': len(metadata_repo_names),
    'artifacts_sample_repos': len(artifacts_repo_names),
    'overlap': len(overlap),
    'sample_overlap': list(overlap)[:5] if overlap else []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'commit_count': '0'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'commit_count': '0'}], 'var_functions.execute_python:26': {'total_repos': 114972, 'sample_repos': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor', 'ivschukin/learning-azure', 'arrawatia/cp-docker-images', 'wolfitem/docker', 'sdgdsffdsfff/ModSecurity', 'frapposelli/govmomi', 'Grimmjowjack/google-services', 'chuangWu/butterknife', 'louwrentius/eztables', 'riddlesio/hack-man-engine', 'DavitTevanyan/word2vec', 'Siphon098/git-sync-batch', 'hitwangyu/apache-common-pool2', 'wshearn/openshift-ansible', 'javasoze/clue', 'hschema/schemaorg', 'simba518/AniEditor', 'abhgupta/kubernetes', 'enovance/puppet-tripleo', 'garana/mod_reslog', 'shiumachi/hbck-analyzer', 'wildfly-swarm/wildfly-swarm-core', 'grmartin/android-vcard', 'allancth/camel', 'wkalt/puppetdb', 'bep/killswitch', 'mark-adams/compose', 'navnorth/LR-Data', 'ShengC/remotely', 'triAGENS/guacamole', 'cavanm/apn-defaults', 'ampproject/amphtml', 'zkrejcov/drools-wb', 'bmistry13/kafka', 'googleapis/java-retail', 'kewalaka/chocolatey-packages', 'AzazelN28/din', 'ZacharyKlein/grails-isomorphic', 'automatecloud/docker-ddc-vagrant', 'Lambda3/docker-vsts-agent', 'darilek/dotvvm']}, 'var_functions.execute_python:28': 'file_storage/functions.execute_python:28.json', 'var_functions.query_db:30': [], 'var_functions.query_db:32': [{'repo_name': 'facebook/react'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}], 'var_functions.query_db:34': [{'total_commits': '17976'}]}

exec(code, env_args)
