code = """import json

# Read commits data
with open("./file_storage/functions.query_db:64.json", "r") as f:
    commits = json.load(f)

# Read shell repos
with open("./file_storage/functions.query_db:38.json", "r") as f:
    shell_repos = json.load(f)

# Read apache repos
with open("./file_storage/functions.query_db:40.json", "r") as f:
    apache_repos = json.load(f)

# Create sets
shell_repo_names = {r["repo_name"] for r in shell_repos}
apache_repo_names = {r["repo_name"] for r in apache_repos}
target_repos = shell_repo_names & apache_repo_names

print("__RESULT__:")
print(f"Total commits: {len(commits)}")
print(f"Shell repos: {len(shell_repo_names)}")
print(f"Apache repos: {len(apache_repo_names)}")
print(f"Target repos (intersection): {len(target_repos)}")
print(f"Sample target repos: {list(target_repos)[:10]}")

# Filter commits to only those from target repos
filtered_commits = [c for c in commits if c["repo_name"] in target_repos]
print(f"Filtered commits: {len(filtered_commits)}")

# Save filtered commits for analysis
with open("./filtered_commits.json", "w") as f:
    json.dump(filtered_commits, f)"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:4': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:8': [{'repo_name': 'brandonhimpfen/Techie', 'license': 'apache-2.0'}, {'repo_name': 'mychoices/android-percent-support-extend', 'license': 'apache-2.0'}, {'repo_name': 'YY030913/start', 'license': 'apache-2.0'}, {'repo_name': 'WeiLend/WeiLend.github.io', 'license': 'apache-2.0'}, {'repo_name': 'amaj674/Blog-Site-mern-', 'license': 'apache-2.0'}, {'repo_name': 'gabrielduque/chrome-app-samples', 'license': 'apache-2.0'}, {'repo_name': 'robertwilczynski/Licensor', 'license': 'apache-2.0'}, {'repo_name': 'kinfkong/cordova-plugin-email-composer', 'license': 'apache-2.0'}, {'repo_name': 'EvgeneOskin/hello-love', 'license': 'apache-2.0'}, {'repo_name': 'ProgrammingRobotsStudyGroup/AndroidControl', 'license': 'apache-2.0'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:24': ['languages', 'repos', 'licenses'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'shell_var_type': "<class 'str'>", 'apache_var_type': "<class 'str'>", 'shell_var_value': 'var_functions.query_db:26', 'apache_var_value': 'var_functions.query_db:14'}, 'var_functions.execute_python:30': {'current_dir': '/workspace', 'json_files': ['./file_storage/functions.query_db:26.json', './file_storage/functions.query_db:14.json', './file_storage/functions.query_db:12.json', './file_storage/functions.query_db:10.json']}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'target_repos_count': 114972, 'sample_target_repos': ['leontius/wide', 'danehans/docker-nova-controller', 'schleichardt/sphere-stuff', 'color-coding/ibas.importexport', 'mezz64/home-assistant', 'siliconchris1973/picbrick', 'yl2695/spark-csv', 'apache/incubator-mxnet', 'leejir/seastar', 'TouK/nussknacker', 'rantav/reversim-summit-2015', 'Jaifar/java_ptf', 'riddopic/garcon', 'Nadyakilic/java_pft1', 'xiaguangme/demo', 'lomin/fedora_java_dev_env', 'Wessi/OpenNI', 'XieXianbin/UEditor-for-aliyun-OSS', 'michaeljoseph/sealeyes', 'TheDukeFamily/GGMultipleColumns']}, 'var_functions.execute_python:46': {'intersection_count': 114972, 'sample_repos': ['InMobi/docker-hive', 'anthonycr/AndroidAssetStudio', 'flupes/catdoor', 'hyleung/ratpack-zipkin', 'joesan/plant-simulator', 'guoranliaoran/ZXAutoLayout', 'maxtoroq/XCST', 'marcellodesales/spring-boot', 'Ciclop/Terasology', 'neilbeveridge/zuul-netty']}, 'var_functions.query_db:48': [{'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'facebook/react'}, {'repo_name': 'apple/swift'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'torvalds/linux'}], 'var_functions.query_db:50': [{'commit_count': '15016'}], 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': [{'repo_name': 'facebook/react', 'commit_count': '104'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '114'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '171'}, {'repo_name': 'apple/swift', 'commit_count': '963'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '251'}, {'repo_name': 'torvalds/linux', 'commit_count': '13413'}], 'var_functions.query_db:56': [], 'var_functions.query_db:58': [{'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'torvalds/linux'}], 'var_functions.query_db:60': [{'repo_name': 'juliandunn/rackspacecloud'}, {'repo_name': 'rupakg/lorry'}, {'repo_name': 'Nordstrom/al_agents'}, {'repo_name': 'fuellab/bootstrap'}, {'repo_name': 'brint/rax-wordpress-cookbook'}, {'repo_name': 'rarenerd/train'}, {'repo_name': 'wallyqs/ruby-nats'}, {'repo_name': 'dthtvwls/bento'}, {'repo_name': 'darrenleeweber/aws-ops'}, {'repo_name': 'yepengxj/binary-buildpack'}], 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
