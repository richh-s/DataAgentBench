code = """import json

result_file = locals()['var_functions.query_db:10']
with open(result_file, 'r') as f:
    shell_repos = json.load(f)

# Create list of repo names
repo_list = [repo['repo_name'] for repo in shell_repos]

# Build SQL query for DuckDB - use the commits table
# We'll construct an IN clause with all repo names
repo_names_str = "', '".join(repo_list)
# Remove star expression issue
query = "SELECT COUNT(*) as commit_count FROM commits "
query += "WHERE repo_name IN ('{}') ".format(repo_names_str)
query += "AND message IS NOT NULL "
query += "AND LENGTH(message) < 1000 "
query += "AND LOWER(SUBSTR(TRIM(message), 1, 5)) NOT IN ('merge', 'updat', 'test')"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'Total repos found: 114972', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': 'Total Shell repos: 6936', 'var_functions.execute_python:14': "Query: SELECT COUNT(*) as commit_count FROM commits WHERE repo_name IN ('eskatos/qi4j-dev-scripts', 'louwrentius/eztables', 'shiumachi/hbck-analyzer', 'automatecloud/docker-ddc-vagrant', 'StartupMakers/ssh-resource', 'nao20010128nao/android-build', 'maltezacharias/mailman', 'slashr00t/vagrant-ipa', 'shishir-a412ed/docker-storage-setup', 'sasthas-twp/kafkanetes', 'meltwater/puppet-beanstalkd', 'jrossi/ship', 'InfoSec812/sonarqube-docker', 's-bortolussi/spring-cloud-config-demo', 'Romke-vd-Meulen/Beethoven', 'dstrctrng/definition-lucid', 'kubernetes-sigs/windows-testing', 'wmeddie/dl4j-scala.g8', 'CloudBees-community/papertrail-clickstack', 'Ikiuchi/TP-git', 'TelekomNFV/vagrant_multisite', 'adaptivdesign/odooku', 'patocox/golang-builder', 'ashumeow/meow-cli', 'jakubholynet/docker-grafana-influxdb-cloudwatch', 'riverspiv/cloudera-director', '64b2b6d12b/spotkey', 'freedev/macosx-vbox-headless', 'stevekuznetsov/openldap', 'AlvaroPaniaguaT/Pruebas-personales', 'resin-io-projects/beast', 'dchenbecker/printutf', 'ArrowElectronics/aws-iot-device-sdk', 'abayer/hst', 'mikelasla/centos7-java8-tomcat7-docker', 'joriscode/homebrew-sbk', 'picoded/rancher-container-backup-via-cli', 'innuendonh/stunnel-docker', 'TakafumiOtake/runit-alpine', 'sven-m/thesis-specification', 'jalmansor/docker-gc', 'bestswifter/macbootstrap', 'rootcss/nutch-cassandra-docker', 'tobibo/AndroidMonkey', 'codinn/prebuilt-openssl', 'davegurnell/shapeless-workshop-scalax-2014', 'matanvr/quickstart-informatica-bdm', 'v1k0d3n/terransikube', 'sagentio/docker-mesos-kafka', 'AdmaticITServices/mongodb') AND message IS NOT NULL AND LENGTH(message) < 1000 AND LOWER(message) NOT LIKE 'merge%' AND LOWER(message) NOT LIKE 'update%' AND LOWER(message) NOT LIKE 'test%'"}

exec(code, env_args)
