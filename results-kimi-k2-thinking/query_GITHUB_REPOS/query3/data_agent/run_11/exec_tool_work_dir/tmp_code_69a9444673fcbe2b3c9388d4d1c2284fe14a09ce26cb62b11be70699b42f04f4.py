code = """import json

# Get Shell repos file
shell_repos_file = locals()['var_functions.query_db:38']
with open(shell_repos_file, 'r') as f:
    shell_repos = json.load(f)

repo_names = [repo['repo_name'] for repo in shell_repos]

# Process first batch of 50 repos
batch1 = repo_names[:50]
in_clause = "'" + "', '".join(batch1) + "'"

query = "SELECT COUNT(*) as batch_count FROM commits WHERE "
query += "repo_name IN (" + in_clause + ") AND "
query += "message IS NOT NULL AND "
query += "LENGTH(message) < 1000 AND "
query += "LOWER(TRIM(SUBSTR(message, 1, 5))) NOT IN ('merge', 'updat', 'test')"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'Total repos found: 114972', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': 'Total Shell repos: 6936', 'var_functions.execute_python:14': "Query: SELECT COUNT(*) as commit_count FROM commits WHERE repo_name IN ('eskatos/qi4j-dev-scripts', 'louwrentius/eztables', 'shiumachi/hbck-analyzer', 'automatecloud/docker-ddc-vagrant', 'StartupMakers/ssh-resource', 'nao20010128nao/android-build', 'maltezacharias/mailman', 'slashr00t/vagrant-ipa', 'shishir-a412ed/docker-storage-setup', 'sasthas-twp/kafkanetes', 'meltwater/puppet-beanstalkd', 'jrossi/ship', 'InfoSec812/sonarqube-docker', 's-bortolussi/spring-cloud-config-demo', 'Romke-vd-Meulen/Beethoven', 'dstrctrng/definition-lucid', 'kubernetes-sigs/windows-testing', 'wmeddie/dl4j-scala.g8', 'CloudBees-community/papertrail-clickstack', 'Ikiuchi/TP-git', 'TelekomNFV/vagrant_multisite', 'adaptivdesign/odooku', 'patocox/golang-builder', 'ashumeow/meow-cli', 'jakubholynet/docker-grafana-influxdb-cloudwatch', 'riverspiv/cloudera-director', '64b2b6d12b/spotkey', 'freedev/macosx-vbox-headless', 'stevekuznetsov/openldap', 'AlvaroPaniaguaT/Pruebas-personales', 'resin-io-projects/beast', 'dchenbecker/printutf', 'ArrowElectronics/aws-iot-device-sdk', 'abayer/hst', 'mikelasla/centos7-java8-tomcat7-docker', 'joriscode/homebrew-sbk', 'picoded/rancher-container-backup-via-cli', 'innuendonh/stunnel-docker', 'TakafumiOtake/runit-alpine', 'sven-m/thesis-specification', 'jalmansor/docker-gc', 'bestswifter/macbootstrap', 'rootcss/nutch-cassandra-docker', 'tobibo/AndroidMonkey', 'codinn/prebuilt-openssl', 'davegurnell/shapeless-workshop-scalax-2014', 'matanvr/quickstart-informatica-bdm', 'v1k0d3n/terransikube', 'sagentio/docker-mesos-kafka', 'AdmaticITServices/mongodb') AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(message) NOT LIKE 'merge%' AND LOWER(message) NOT LIKE 'update%' AND LOWER(message) NOT LIKE 'test%'", 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.query_db:20': [{'commit_count': '0'}], 'var_functions.execute_python:22': "First 10 repos: ['eskatos/qi4j-dev-scripts', 'louwrentius/eztables', 'shiumachi/hbck-analyzer', 'automatecloud/docker-ddc-vagrant', 'StartupMakers/ssh-resource', 'nao20010128nao/android-build', 'maltezacharias/mailman', 'slashr00t/vagrant-ipa', 'shishir-a412ed/docker-storage-setup', 'sasthas-twp/kafkanetes']", 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.query_db:26': [{'commit_count': '15016'}], 'var_functions.execute_python:30': 'Total repos: 6936', 'var_functions.execute_python:32': ['eskatos/qi4j-dev-scripts', 'louwrentius/eztables', 'shiumachi/hbck-analyzer', 'automatecloud/docker-ddc-vagrant', 'StartupMakers/ssh-resource', 'nao20010128nao/android-build', 'maltezacharias/mailman', 'slashr00t/vagrant-ipa', 'shishir-a412ed/docker-storage-setup', 'sasthas-twp/kafkanetes'], 'var_functions.query_db:34': [{'total_filtered_commits': '15016'}], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': 'Total batches needed: 113, repos: 5612'}

exec(code, env_args)
