code = """import json, re

# Load repositories from both queries
non_python_data = []
readme_data = []

with open(locals()['var_functions.query_db:62'], 'r') as f:
    non_python_data = json.load(f)[:50]  # Load first 50

with open(locals()['var_functions.query_db:52'], 'r') as f:
    readme_data = json.load(f)[:50]  # Load first 50

# Extract repo names
non_python_repos = set([item['repo_name'] for item in non_python_data])
readme_repos = set([item['sample_repo_name'] for item in readme_data])

# Check sample data
print('Sample non-Python repos:', list(non_python_repos)[:10])
print('\nSample README repos:', list(readme_repos)[:10])

# Check if there are Python repos in the READMEs to understand data
readme_with_python = []
for readme in readme_data:
    for repo in non_python_data:
        if readme['sample_repo_name'] == repo['repo_name']:
            break
    else:
        # This README is not in our non-Python list
        if 'ninja-ide' not in readme['sample_repo_name']:  # This one is Python
            readme_with_python.append(readme['sample_repo_name'])

print('\nSome README repos not in non-Python list:', list(readme_with_python)[:10])

# Check if the README file paths are correct
print('\nSample README paths:')
for readme in readme_data[:10]:
    print(f"  {readme['sample_repo_name']} -> {readme['sample_path']}")

print('\nChecking for common repo...')
if 'rtrouton/rtrouton_scripts' in readme_repos:
    print('Found rtrouton/rtrouton_scripts in README data')
    if 'rtrouton/rtrouton_scripts' in non_python_repos:
        print('Found rtrouton/rtrouton_scripts in non-Python data (GOOD!)')
    else:
        print('NOT found rtrouton/rtrouton_scripts in non-Python data')

result = {
    'non_python_count': len(non_python_repos),
    'readme_count': len(readme_repos),
    'intersection': len(non_python_repos.intersection(readme_repos))
}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'count': 0, 'first_five': []}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': [{'repo_name': 'juliandunn/rackspacecloud'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer'}, {'repo_name': 'michaellihs/gitlab'}, {'repo_name': 'vyorkin/xftp'}, {'repo_name': 'airatshigapov/drophunter'}, {'repo_name': 'tombruijn/chef-ruby-install'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby'}, {'repo_name': 'procore/site-reliability-scripts'}, {'repo_name': 'tibastral/web_motion'}, {'repo_name': 'Haegin/stately'}, {'repo_name': 'Scripted/pandago-ruby'}, {'repo_name': 'wallywest/magnum'}, {'repo_name': 'kuleszaj/chef-an-introduction'}, {'repo_name': 'ruby-amqp/rabbitmq_http_api_client'}, {'repo_name': 'rupakg/lorry'}, {'repo_name': 'rmomogi/validator_ie'}, {'repo_name': 'MailRoute/mailroute_ruby'}, {'repo_name': 'Nordstrom/al_agents'}, {'repo_name': 'Pixelshifter/My-cloud-PoC-Ansible-Vagrant'}, {'repo_name': 'enspiresoftware/n_able_rails'}, {'repo_name': 'kynan/rbenv'}, {'repo_name': 'mbailey/openssl'}, {'repo_name': 'cloudfoundry/machete-firewall-test'}, {'repo_name': 'tomichj/operate'}, {'repo_name': 'Pisangel/stats_db_model'}, {'repo_name': 'GHKEN/pem2xml'}, {'repo_name': 'yyuu/capistrano-platform-resources'}, {'repo_name': 'dinahosting/dinaip-linux-grafica'}, {'repo_name': 'bmckinney/ebsco-eds-api-gem'}, {'repo_name': 'lord63/rb_colors'}, {'repo_name': 'jgraichen/routing_engine'}, {'repo_name': 'CroneKorkN/editable-rails'}, {'repo_name': 'tobymao/rolling_stock'}, {'repo_name': 'iSarCasm/i18n-lazy-generator'}, {'repo_name': 'kaihar4/classifieds'}, {'repo_name': 'nyankichi820/scrapper'}, {'repo_name': 'chooper/eventlog'}, {'repo_name': 'danielfree/ansible-mesos-playbook'}, {'repo_name': 'gbudiman/elfcat'}, {'repo_name': 'fuellab/bootstrap'}, {'repo_name': 'bloomyminded/chicrime'}, {'repo_name': 'anothermh/string_entropy'}, {'repo_name': 'piepieninja/AutoCraft'}, {'repo_name': 'frankhjung/ruby-xml'}, {'repo_name': 'jeqo/ansible-elastic-kibana'}, {'repo_name': 'pvdb/faraday'}, {'repo_name': 'cordata/heroku-buildpack-ruby'}, {'repo_name': 'brint/rax-wordpress-cookbook'}, {'repo_name': 'Shopify/buildkit'}, {'repo_name': 'rarenerd/train'}, {'repo_name': 'vaelen/chessboard'}, {'repo_name': 'sakura1116/jp_city_code'}, {'repo_name': 'thoughtbot/rspec-mocks'}, {'repo_name': 'equivalent/file_organizer'}, {'repo_name': 'AmitPatel-BoTreeConsulting/bliss_office'}, {'repo_name': 'kouk/vagrant-dns'}, {'repo_name': 'ignazioc/MoneyManager'}, {'repo_name': 'wallyqs/ruby-nats'}, {'repo_name': 'tsukasaoishi/unicorn-standby'}, {'repo_name': 'tsuru/homebrew-tsuru'}, {'repo_name': 'lileeyao/resque'}, {'repo_name': 'alu0100785265/prct10'}, {'repo_name': 'matschaffer/mats-tools'}, {'repo_name': 'a-suenami/dbspec'}, {'repo_name': 'tumf/gvm'}, {'repo_name': 'dinsaw/filesaverjs-rails'}, {'repo_name': 'ludovicdeluna/monads-ruby'}, {'repo_name': 'codeenigma/nagios_statuscake'}, {'repo_name': 'danielpclark/MightyString'}, {'repo_name': 'mimimalizam/haskii'}, {'repo_name': 'countir/countir-sdk-ruby'}, {'repo_name': 'cbarratt/mac_system_update'}, {'repo_name': 'pkordel/ffaker'}, {'repo_name': 'cimon-io/susanin'}, {'repo_name': 'frohoff/rails_exploits'}, {'repo_name': 'danfinn/bash-git-prompt'}, {'repo_name': 'underyx/homebrew-cask'}, {'repo_name': 'coinbase/pagerduty'}, {'repo_name': 'archan937/motion-bundler'}, {'repo_name': 'tushartuteja/first_gem'}, {'repo_name': 'dkhamsing/app_store_screenshots'}, {'repo_name': 'dthtvwls/bento'}, {'repo_name': 'Storenvy/opensky_bis'}, {'repo_name': 'darrenleeweber/aws-ops'}, {'repo_name': 'groovenauts/milc'}, {'repo_name': 'data-creative/google-sheet-reader-ruby'}, {'repo_name': 'LicaOka/reading_kanji_in_kana'}, {'repo_name': 'yepengxj/binary-buildpack'}, {'repo_name': 'bozaro/gitlab-shell'}, {'repo_name': 'Manfred/matterhorn_whymper'}, {'repo_name': 'migibert/orientdb-role'}, {'repo_name': 'smellsblue/attestify'}, {'repo_name': 'mysociety/mongoid'}, {'repo_name': 'wethu/whatsfordinner'}, {'repo_name': 'y-yagi/minitest-test_profile'}, {'repo_name': 'ongair/ig_scrape'}, {'repo_name': 'vinhnglx/weer'}, {'repo_name': 'ptsurbeleu/jekyll-theme-specs'}, {'repo_name': 'GlobalNamesArchitecture/name-spotter'}, {'repo_name': 'mateusduboli/bjn-logstash-cookbook'}], 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:64': [1000, 0, 0, 0], 'var_functions.execute_python:66': {'non_python_repos': 1000, 'total_readmes_in_non_python': 0, 'readmes_with_copyright': 0, 'readmes_without_copyright': 0, 'proportion': 0, 'percentage': 0}, 'var_functions.execute_python:70': {'non_python_repos': 1000, 'readme_in_non_python': 0, 'with_copyright': 0, 'proportion': 0, 'percentage': 0}}

exec(code, env_args)
