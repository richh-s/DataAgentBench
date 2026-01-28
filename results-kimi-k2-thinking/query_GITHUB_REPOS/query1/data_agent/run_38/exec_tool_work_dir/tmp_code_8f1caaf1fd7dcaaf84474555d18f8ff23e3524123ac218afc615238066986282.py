code = """import json

# Load the language data to identify non-Python repositories
languages_file = locals()['var_functions.query_db:16']

with open(languages_file, 'r') as f:
    languages = json.load(f)

# Identify repositories that do NOT use Python
non_python_repos = []
for row in languages:
    desc = row.get('language_description', '').lower()
    if 'python' not in desc:
        non_python_repos.append(row['repo_name'])

# Load the README.md files from artifacts database
readme_file = locals()['var_functions.query_db:22']

with open(readme_file, 'r') as f:
    readme_files = json.load(f)

# Filter README files for non-Python repositories
non_python_readmes = []
for readme in readme_files:
    if readme.get('sample_repo_name') in non_python_repos:
        non_python_readmes.append(readme)

result = {
    'non_python_repos_count': len(non_python_repos),
    'total_readmes_count': len(readme_files),
    'non_python_readmes_count': len(non_python_readmes)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.execute_python:5': ['languages', 'repos', 'licenses'], 'var_functions.query_db:9': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:10': ['commits', 'contents', 'files'], 'var_functions.execute_python:14': {'non_python_count': 2774729, 'sample_repos': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately', 'Scripted/pandago-ruby', 'wallywest/magnum', 'kuleszaj/chef-an-introduction', 'ruby-amqp/rabbitmq_http_api_client', 'rupakg/lorry', 'rmomogi/validator_ie', 'MailRoute/mailroute_ruby', 'Nordstrom/al_agents', 'Pixelshifter/My-cloud-PoC-Ansible-Vagrant', 'enspiresoftware/n_able_rails', 'kynan/rbenv', 'mbailey/openssl', 'cloudfoundry/machete-firewall-test', 'tomichj/operate', 'Pisangel/stats_db_model', 'GHKEN/pem2xml', 'yyuu/capistrano-platform-resources', 'dinahosting/dinaip-linux-grafica', 'bmckinney/ebsco-eds-api-gem', 'lord63/rb_colors', 'jgraichen/routing_engine', 'CroneKorkN/editable-rails', 'tobymao/rolling_stock', 'iSarCasm/i18n-lazy-generator', 'kaihar4/classifieds', 'nyankichi820/scrapper', 'chooper/eventlog', 'danielfree/ansible-mesos-playbook', 'gbudiman/elfcat', 'fuellab/bootstrap', 'bloomyminded/chicrime', 'anothermh/string_entropy', 'piepieninja/AutoCraft', 'frankhjung/ruby-xml', 'jeqo/ansible-elastic-kibana', 'pvdb/faraday', 'cordata/heroku-buildpack-ruby', 'brint/rax-wordpress-cookbook', 'Shopify/buildkit', 'rarenerd/train', 'vaelen/chessboard', 'sakura1116/jp_city_code', 'thoughtbot/rspec-mocks', 'equivalent/file_organizer', 'AmitPatel-BoTreeConsulting/bliss_office', 'kouk/vagrant-dns', 'ignazioc/MoneyManager', 'wallyqs/ruby-nats', 'tsukasaoishi/unicorn-standby', 'tsuru/homebrew-tsuru', 'lileeyao/resque', 'alu0100785265/prct10', 'matschaffer/mats-tools', 'a-suenami/dbspec', 'tumf/gvm', 'dinsaw/filesaverjs-rails', 'ludovicdeluna/monads-ruby', 'codeenigma/nagios_statuscake', 'danielpclark/MightyString', 'mimimalizam/haskii', 'countir/countir-sdk-ruby', 'cbarratt/mac_system_update', 'pkordel/ffaker', 'cimon-io/susanin', 'frohoff/rails_exploits', 'danfinn/bash-git-prompt', 'underyx/homebrew-cask', 'coinbase/pagerduty', 'archan937/motion-bundler', 'tushartuteja/first_gem', 'dkhamsing/app_store_screenshots', 'dthtvwls/bento', 'Storenvy/opensky_bis', 'darrenleeweber/aws-ops', 'groovenauts/milc', 'data-creative/google-sheet-reader-ruby', 'LicaOka/reading_kanji_in_kana', 'yepengxj/binary-buildpack', 'bozaro/gitlab-shell', 'Manfred/matterhorn_whymper', 'migibert/orientdb-role', 'smellsblue/attestify', 'mysociety/mongoid', 'wethu/whatsfordinner', 'y-yagi/minitest-test_profile', 'ongair/ig_scrape', 'vinhnglx/weer', 'ptsurbeleu/jekyll-theme-specs', 'GlobalNamesArchitecture/name-spotter', 'mateusduboli/bjn-logstash-cookbook'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
