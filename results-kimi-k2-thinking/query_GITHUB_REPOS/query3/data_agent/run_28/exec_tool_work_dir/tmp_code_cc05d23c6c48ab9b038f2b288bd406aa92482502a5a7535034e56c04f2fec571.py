code = """import json

result_file = locals()['var_functions.query_db:5']
with open(result_file, 'r') as f:
    repo_data = json.load(f)

repo_names = [item['repo_name'] for item in repo_data]
print(f"Total repos to process: {len(repo_names)}")

# Process in batches
batch_size = 200  
batches = []
for i in range(0, len(repo_names), batch_size):
    batches.append(repo_names[i:i + batch_size])

num_batches = len(batches)
print(f"Number of batches: {num_batches}")

# For the first batch, construct the query
first_batch = batches[0]
in_clause = "'" + "','".join(first_batch) + "'"

query = f"""
SELECT COUNT(*) as commit_count
FROM commits
WHERE repo_name IN ({in_clause})
AND message IS NOT NULL
AND LENGTH(message) < 1000
AND LOWER(SUBSTR(message, 1, 6)) NOT IN ('merge', 'update', 'test')
AND LOWER(SUBSTR(message, 1, 5)) NOT IN ('merge', 'updat', 'test')
AND LOWER(SUBSTR(message, 1, 4)) NOT IN ('merg', 'upda', 'test')
AND LOWER(SUBSTR(message, 1, 3)) NOT IN ('mer', 'upd', 'tes')
"""

print(f"First 300 chars of query: {query[:300]}...")

print('__RESULT__:')
print(json.dumps({
    'total_repos': len(repo_names),
    'num_batches': num_batches,
    'first_batch_size': len(first_batch)
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {'first_batch': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor', 'ivschukin/learning-azure', 'arrawatia/cp-docker-images', 'wolfitem/docker', 'sdgdsffdsfff/ModSecurity', 'frapposelli/govmomi', 'Grimmjowjack/google-services', 'chuangWu/butterknife', 'louwrentius/eztables', 'riddlesio/hack-man-engine', 'DavitTevanyan/word2vec', 'Siphon098/git-sync-batch', 'hitwangyu/apache-common-pool2', 'wshearn/openshift-ansible', 'javasoze/clue', 'hschema/schemaorg', 'simba518/AniEditor', 'abhgupta/kubernetes', 'enovance/puppet-tripleo', 'garana/mod_reslog', 'shiumachi/hbck-analyzer', 'wildfly-swarm/wildfly-swarm-core', 'grmartin/android-vcard', 'allancth/camel', 'wkalt/puppetdb', 'bep/killswitch', 'mark-adams/compose', 'navnorth/LR-Data', 'ShengC/remotely', 'triAGENS/guacamole', 'cavanm/apn-defaults', 'ampproject/amphtml', 'zkrejcov/drools-wb', 'bmistry13/kafka', 'googleapis/java-retail', 'kewalaka/chocolatey-packages', 'AzazelN28/din', 'ZacharyKlein/grails-isomorphic', 'automatecloud/docker-ddc-vagrant', 'Lambda3/docker-vsts-agent', 'darilek/dotvvm', 'DagensNyheter/helios', 'WitchKing-Helkar/rtbkit', 'branic/manageiq', 'dwmw2/luci', 'StartupMakers/ssh-resource', 'saturnism/oauth2util', 'diogomonica/docker', 'plutoshe/taskgraph', 'ftrossbach/intro-to-dcos', 'nao20010128nao/android-build', 'adamleff/knife-vcair', 'carezone/mixpanel-iphone', 'luvit/luvi', 'rsprabery/FIN', 'dugwa/puppet-control', 'liuqijie/wind', 'proximcreation/tad-mobile', 'ekumenlabs/terminus', 'Hitcents/iOS4Unity', 'wanelo-chef/chef-bootstrap', 'choopooly/docker-grafana-graphite', 'tealover/nova', 'coolsvap/kolla', 'mikepenz/Android-Iconics', 'walrusCH/HomeMirror', 'ppletscher/BCFWstruct', 'barakmich/cayley', 'olafura/json_diff_ex', 'jinahya/jpa-metamodels-with-maven-example', 'msoftware/ContentLoadingProgressDialog', 'iQubeLabs/sdp_search_members_node', 'unixunion/vertx-dockermod', 'mtsyganov/react', 'fish-cat/piwebapi-samples', 'xuanduc939/iosched', 'chemouna/frame-gradle-plugin', 'laura-dietz/kba-y2-streameval', 'jarcec/cmd-tools', 'mrcflorian/classbook', 'cherrydocker/minos', 'Qihoo360/phptrace', '43350860/spdylearn', 'gmtahackers/deeplearning', 'is00hcw/jgroups-raft', 'olamy/archiva', 'boundary/zoocreeper', 'ThomasMarcel/gae-tomalcala-flask', 'mheon/docker', 'wowsoso/etcd', 'SourceBackups/DexHunter'], 'in_clause_example': "'jitsi/jipopro','NuGet/json-ld.net','virtualcoinclub/common','pydev/jmx_exporter','eskatos/qi4j-dev-...", 'total_batches': 1150}, 'var_functions.execute_python:12': {'total_repos': 114972}}

exec(code, env_args)
