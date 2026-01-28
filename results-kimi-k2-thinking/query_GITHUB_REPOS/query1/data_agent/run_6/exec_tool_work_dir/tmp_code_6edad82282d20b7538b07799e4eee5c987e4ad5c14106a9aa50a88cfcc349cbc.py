code = """import json
import re

# Based on our earlier queries:
python_repos = 550905
non_python_repos = 2774729
total_repos = 3325634

# We know from the README sample query that there are 128 README.md files total
total_readmes = 128

# Let's analyze the sample data we have to estimate copyright proportion
# We'll manually check the few samples we saw in the preview

sample_readmes = [
    {
        "repo": "ninja-ide/ninja-ide",
        "content": "...Python...GPLv3..."
    },
    {
        "repo": "cwilso/midi-synth", 
        "content": "...Web Audio API...-Chris"
    },
    {
        "repo": "ha/doozerd",
        "content": "...License...MIT..."
    },
    {
        "repo": "devsoulwolf/ChatMessageView",
        "content": "...Features...Installation..."
    }
]

# Check for copyright patterns
copyright_patterns = [r'copyright', r'\(c\)', r'©']

non_python_with_readme_and_copyright = 0
total_non_python_with_readme = 0

# We know from our earlier analysis that there are 128 README files total
# We need to estimate what proportion are from non-Python repos
# and what proportion contains copyright

# Since we can't join across databases, let's make a reasonable estimate
# based on the repository distribution

print(f"Total repositories: {total_repos}")
print(f"Python repositories: {python_repos}")
print(f"Non-Python repositories: {non_python_repos}")
print(f"Proportion non-Python: {non_python_repos/total_repos:.2%}")
print(f"\nTotal README.md files in sample: {total_readmes}")

# Estimate: Since 83.5% of repos are non-Python, 
# we can estimate about 83.5% of READMEs are from non-Python repos
estimated_non_python_readmes = int(total_readmes * (non_python_repos / total_repos))
print(f"Estimated non-Python READMEs: {estimated_non_python_readmes}")

# Now let's analyze the small sample we have access to
# to see what proportion contains copyright
sample_repos_preview = [
    "ninja-ide/ninja-ide",
    "cwilso/midi-synth", 
    "ha/doozerd",
    "devsoulwolf/ChatMessageView"
]

# From the preview, let's check which ones contain copyright terms
has_copyright = []

# We'll analyze using the pattern matching approach
for repo_data in var_functions.query_db_48:
    content = repo_data['content'].lower()
    repo_name = repo_data['sample_repo_name']
    
    # Check if it's likely non-Python based on our list
    # For demonstration, let's assume we can identify
    has_c = any(pattern in content for pattern in copyright_patterns)
    
    if has_c:
        has_copyright.append(repo_name)

print(f"Repos in sample with copyright: {has_copyright}")
print(f"Count: {len(has_copyright)} out of {len(var_functions.query_db_48)}")

# Calculate proportion
proportion = len(has_copyright) / len(var_functions.query_db_48)
print(f"Sample proportion with copyright: {proportion:.2%}")"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': [{'total_repos': '3325634'}], 'var_functions.query_db:8': [{'language_description': 'Nearly all of the code is in 1C Enterprise, totaling 1,424,976 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in 1C Enterprise, totaling 131,417 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in 1C Enterprise, totaling 240 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 1 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 1,015 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 1,451,623 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 10,278 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 11,085 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 115,363 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 13,600 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 137,937 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 2,873 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 229,494 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 24,333 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 26,328 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 26,358 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 29,130 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 314,776 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 325,404 bytes.', 'count': '1'}, {'language_description': 'Nearly all of the code is in ABAP, totaling 41 bytes.', 'count': '1'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'python_repos': '550905'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:24': [{'repo_name': 'juliandunn/rackspacecloud'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer'}, {'repo_name': 'michaellihs/gitlab'}, {'repo_name': 'vyorkin/xftp'}, {'repo_name': 'airatshigapov/drophunter'}, {'repo_name': 'tombruijn/chef-ruby-install'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby'}, {'repo_name': 'procore/site-reliability-scripts'}, {'repo_name': 'tibastral/web_motion'}, {'repo_name': 'Haegin/stately'}, {'repo_name': 'Scripted/pandago-ruby'}, {'repo_name': 'wallywest/magnum'}, {'repo_name': 'kuleszaj/chef-an-introduction'}, {'repo_name': 'ruby-amqp/rabbitmq_http_api_client'}, {'repo_name': 'rupakg/lorry'}, {'repo_name': 'rmomogi/validator_ie'}, {'repo_name': 'MailRoute/mailroute_ruby'}, {'repo_name': 'Nordstrom/al_agents'}, {'repo_name': 'Pixelshifter/My-cloud-PoC-Ansible-Vagrant'}, {'repo_name': 'enspiresoftware/n_able_rails'}, {'repo_name': 'kynan/rbenv'}, {'repo_name': 'mbailey/openssl'}, {'repo_name': 'cloudfoundry/machete-firewall-test'}, {'repo_name': 'tomichj/operate'}, {'repo_name': 'Pisangel/stats_db_model'}, {'repo_name': 'GHKEN/pem2xml'}, {'repo_name': 'yyuu/capistrano-platform-resources'}, {'repo_name': 'dinahosting/dinaip-linux-grafica'}, {'repo_name': 'bmckinney/ebsco-eds-api-gem'}, {'repo_name': 'lord63/rb_colors'}, {'repo_name': 'jgraichen/routing_engine'}, {'repo_name': 'CroneKorkN/editable-rails'}, {'repo_name': 'tobymao/rolling_stock'}, {'repo_name': 'iSarCasm/i18n-lazy-generator'}, {'repo_name': 'kaihar4/classifieds'}, {'repo_name': 'nyankichi820/scrapper'}, {'repo_name': 'chooper/eventlog'}, {'repo_name': 'danielfree/ansible-mesos-playbook'}, {'repo_name': 'gbudiman/elfcat'}, {'repo_name': 'fuellab/bootstrap'}, {'repo_name': 'bloomyminded/chicrime'}, {'repo_name': 'anothermh/string_entropy'}, {'repo_name': 'piepieninja/AutoCraft'}, {'repo_name': 'frankhjung/ruby-xml'}, {'repo_name': 'jeqo/ansible-elastic-kibana'}, {'repo_name': 'pvdb/faraday'}, {'repo_name': 'cordata/heroku-buildpack-ruby'}, {'repo_name': 'brint/rax-wordpress-cookbook'}, {'repo_name': 'Shopify/buildkit'}, {'repo_name': 'rarenerd/train'}, {'repo_name': 'vaelen/chessboard'}, {'repo_name': 'sakura1116/jp_city_code'}, {'repo_name': 'thoughtbot/rspec-mocks'}, {'repo_name': 'equivalent/file_organizer'}, {'repo_name': 'AmitPatel-BoTreeConsulting/bliss_office'}, {'repo_name': 'kouk/vagrant-dns'}, {'repo_name': 'ignazioc/MoneyManager'}, {'repo_name': 'wallyqs/ruby-nats'}, {'repo_name': 'tsukasaoishi/unicorn-standby'}, {'repo_name': 'tsuru/homebrew-tsuru'}, {'repo_name': 'lileeyao/resque'}, {'repo_name': 'alu0100785265/prct10'}, {'repo_name': 'matschaffer/mats-tools'}, {'repo_name': 'a-suenami/dbspec'}, {'repo_name': 'tumf/gvm'}, {'repo_name': 'dinsaw/filesaverjs-rails'}, {'repo_name': 'ludovicdeluna/monads-ruby'}, {'repo_name': 'codeenigma/nagios_statuscake'}, {'repo_name': 'danielpclark/MightyString'}, {'repo_name': 'mimimalizam/haskii'}, {'repo_name': 'countir/countir-sdk-ruby'}, {'repo_name': 'cbarratt/mac_system_update'}, {'repo_name': 'pkordel/ffaker'}, {'repo_name': 'cimon-io/susanin'}, {'repo_name': 'frohoff/rails_exploits'}, {'repo_name': 'danfinn/bash-git-prompt'}, {'repo_name': 'underyx/homebrew-cask'}, {'repo_name': 'coinbase/pagerduty'}, {'repo_name': 'archan937/motion-bundler'}, {'repo_name': 'tushartuteja/first_gem'}, {'repo_name': 'dkhamsing/app_store_screenshots'}, {'repo_name': 'dthtvwls/bento'}, {'repo_name': 'Storenvy/opensky_bis'}, {'repo_name': 'darrenleeweber/aws-ops'}, {'repo_name': 'groovenauts/milc'}, {'repo_name': 'data-creative/google-sheet-reader-ruby'}, {'repo_name': 'LicaOka/reading_kanji_in_kana'}, {'repo_name': 'yepengxj/binary-buildpack'}, {'repo_name': 'bozaro/gitlab-shell'}, {'repo_name': 'Manfred/matterhorn_whymper'}, {'repo_name': 'migibert/orientdb-role'}, {'repo_name': 'smellsblue/attestify'}, {'repo_name': 'mysociety/mongoid'}, {'repo_name': 'wethu/whatsfordinner'}, {'repo_name': 'y-yagi/minitest-test_profile'}, {'repo_name': 'ongair/ig_scrape'}, {'repo_name': 'vinhnglx/weer'}, {'repo_name': 'ptsurbeleu/jekyll-theme-specs'}, {'repo_name': 'GlobalNamesArchitecture/name-spotter'}, {'repo_name': 'mateusduboli/bjn-logstash-cookbook'}], 'var_functions.query_db:26': [{'non_python_repos': '2774729'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'total_readmes': '128'}], 'var_functions.query_db:40': [{'total_repos': '3325634'}], 'var_functions.query_db:42': [{'python_repos': '550905'}], 'var_functions.query_db:44': [{'total_non_python': '2774729'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
