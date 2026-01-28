code = """import json

# Get the shell+apache repos from storage
file_path_var = 'var_functions.query_db:14'
file_path = locals()[file_path_var]

with open(file_path, 'r') as f:
    shell_apache_repos = json.load(f)

# Get available repos in commits table from storage
commits_repos_var = 'var_functions.query_db:32'
commits_repos = locals()[commits_repos_var]

shell_apache_repo_names = set(repo['repo_name'] for repo in shell_apache_repos)
commits_repo_names = set(repo['repo_name'] for repo in commits_repos)

# Find intersection
common_repos = shell_apache_repo_names.intersection(commits_repo_names)

print("__RESULT__:")
print(json.dumps({
    'shell_apache_total': len(shell_apache_repo_names),
    'commits_total': len(commits_repo_names),
    'common_repos': list(common_repos),
    'common_count': len(common_repos)
}))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': "'jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor', 'ivschukin/learning-azure', 'arrawatia/cp-docker-images', 'wolfitem/docker', 'sdgdsffdsfff/ModSecurity', 'frapposelli/govmomi', 'Grimmjowjack/google-services', 'chuangWu/butterknife', 'louwrentius/eztables', 'riddlesio/hack-man-engine', 'DavitTevanyan/word2vec', 'Siphon098/git-sync-batch', 'hitwangyu/apache-common-pool2', 'wshearn/openshift-ansible', 'javasoze/clue', 'hschema/schemaorg', 'simba518/AniEditor', 'abhgupta/kubernetes', 'enovance/puppet-tripleo', 'garana/mod_reslog', 'shiumachi/hbck-analyzer', 'wildfly-swarm/wildfly-swarm-core', 'grmartin/android-vcard', 'allancth/camel', 'wkalt/puppetdb', 'bep/killswitch', 'mark-adams/compose', 'navnorth/LR-Data', 'ShengC/remotely', 'triAGENS/guacamole', 'cavanm/apn-defaults', 'ampproject/amphtml', 'zkrejcov/drools-wb', 'bmistry13/kafka', 'googleapis/java-retail', 'kewalaka/chocolatey-packages', 'AzazelN28/din', 'ZacharyKlein/grails-isomorphic', 'automatecloud/docker-ddc-vagrant', 'Lambda3/docker-vsts-agent', 'darilek/dotvvm', 'DagensNyheter/helios', 'WitchKing-Helkar/rtbkit', 'branic/manageiq', 'dwmw2/luci', 'StartupMakers/ssh-resource', 'saturnism/oauth2util', 'diogomonica/docker', 'plutoshe/taskgraph', 'ftrossbach/intro-to-dcos', 'nao20010128nao/android-build', 'adamleff/knife-vcair', 'carezone/mixpanel-iphone', 'luvit/luvi', 'rsprabery/FIN', 'dugwa/puppet-control', 'liuqijie/wind', 'proximcreation/tad-mobile', 'ekumenlabs/terminus', 'Hitcents/iOS4Unity', 'wanelo-chef/chef-bootstrap', 'choopooly/docker-grafana-graphite', 'tealover/nova', 'coolsvap/kolla', 'mikepenz/Android-Iconics', 'walrusCH/HomeMirror', 'ppletscher/BCFWstruct', 'barakmich/cayley', 'olafura/json_diff_ex', 'jinahya/jpa-metamodels-with-maven-example', 'msoftware/ContentLoadingProgressDialog', 'iQubeLabs/sdp_search_members_node', 'unixunion/vertx-dockermod', 'mtsyganov/react', 'fish-cat/piwebapi-samples', 'xuanduc939/iosched', 'chemouna/frame-gradle-plugin', 'laura-dietz/kba-y2-streameval', 'jarcec/cmd-tools', 'mrcflorian/classbook', 'cherrydocker/minos', 'Qihoo360/phptrace', '43350860/spdylearn', 'gmtahackers/deeplearning', 'is00hcw/jgroups-raft', 'olamy/archiva', 'boundary/zoocreeper', 'ThomasMarcel/gae-tomalcala-flask', 'mheon/docker', 'wowsoso/etcd', 'SourceBackups/DexHunter'", 'var_functions.query_db:22': [], 'var_functions.query_db:24': [{'total_commits': '0'}], 'var_functions.query_db:26': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_functions.query_db:28': [], 'var_functions.execute_python:30': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor', 'ivschukin/learning-azure', 'arrawatia/cp-docker-images', 'wolfitem/docker', 'sdgdsffdsfff/ModSecurity', 'frapposelli/govmomi', 'Grimmjowjack/google-services', 'chuangWu/butterknife', 'louwrentius/eztables', 'riddlesio/hack-man-engine', 'DavitTevanyan/word2vec'], 'var_functions.query_db:32': [{'repo_name': 'facebook/react'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}]}

exec(code, env_args)
