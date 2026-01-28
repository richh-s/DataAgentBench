code = """# Build a comprehensive query for a sample of non-Python repos
import json
import random

# Read the full languages data
lang_data_file = locals()['var_functions.query_db:5']
with open(lang_data_file, 'r') as f:
    languages_data = json.load(f)

# Filter repositories that do NOT use Python
non_python_repos = []
for repo in languages_data:
    language_desc = repo['language_description'].lower()
    if 'python' not in language_desc:
        non_python_repos.append(repo['repo_name'])

# Take a random sample of 1000 repos for analysis
sample_size = 1000
random_sample = random.sample(non_python_repos, min(sample_size, len(non_python_repos)))

# Build the SQL query
sample_repos_quoted = [f"'{repo}'" for repo in random_sample]
sample_repos_str = ", ".join(sample_repos_quoted)

# This query will fetch README.md content for our sample
query = """
SELECT 
    sample_repo_name, 
    content,
    CASE 
        WHEN content IS NULL OR content = '' THEN 'no_readme'
        WHEN lower(content) LIKE '%copyright%' OR 
             content LIKE '%\\u00a9%' OR 
             content LIKE '%(c)%' OR 
             lower(content) LIKE '%all rights reserved%' THEN 'has_copyright'
        ELSE 'no_copyright'
    END as copyright_status
FROM contents 
WHERE sample_path = 'README.md' 
    AND sample_repo_name IN (""" + sample_repos_str + ")"

print('__RESULT__:')
print(json.dumps({
    'total_non_python_repos': len(non_python_repos),
    'sample_size': len(random_sample),
    'query_preview': query[:500]
}))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'total_repos': 3325634, 'non_python_repos_count': 2774729, 'sample_non_python_repos': ['juliandunn/rackspacecloud', 'xMarkusSpringerx/coloranalyzer', 'michaellihs/gitlab', 'vyorkin/xftp', 'airatshigapov/drophunter', 'tombruijn/chef-ruby-install', 'SenseTecnic/stsplatform-lib-ruby', 'procore/site-reliability-scripts', 'tibastral/web_motion', 'Haegin/stately']}, 'var_functions.query_db:12': [], 'var_functions.execute_python:14': {'total_non_python_repos': 2774729, 'sample_size': 5000, 'sample_repos': ['rajat4493/powershell', 'TingSyuanWang/ReactSimpleBlog', 'nelodvn/restzero', 'garora/number2text', 'SmarkSeven/WaveSwipeRefreshLayout', 'Sitback/helm', 'vailum/ResponsiveImage', 'lzkjyang/LearnPython3.6', 'wtflucas/Luna', 'nvcleemp/square', 'ouonline/myhashmap', 'maroekun/go-setlock', 'osgi-forks/spring-osgi', 'iota-arbitrage/iota-arbitrage.github.com', 'steve1rm/chatbar', 'oldwo/sudoku', 'DerekMarcinyshyn/source', 'AlexSteele/stratos', 'botanicus/dm-is-serialized', 'AlexRib/Suru']}, 'var_functions.execute_python:16': {'total_repos': 3325634, 'non_python_repos_count': 2774729, 'python_repos_count': 550905, 'sample_python_repos': []}, 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.execute_python:22': {'total_non_python_repos': 2774729, 'sample_size': 1000, 'sample_repos_for_query': "'TheGranolaman/NodeJSSamples', 'parasoft/SOAtestToMTM', 'PaymentSuite/PagosOnlineBundle', 'LazyClutch/LCGraffitiImageView', 'vogelsgesang/messageformat.codemirror', 'jiyuren/Conquer', 'bennage/pundit', 'unimapper/get-started', 'iMyon/charts4bmoe', 'jovanovicivan/clojuretabs', 'victor-shepardson/nonlinear-oscbank', 'mb-dev/mbdev-core-server', 'HenriqueLacerda/DesignPatterns', 'tojason/burning-rock', 'sdk-group/iris-service-terminal', 'Hexmedia/Crontab', 'backupbrain/joke-a-day-glassware-php', 'we"}, 'var_functions.execute_python:24': {'query': "SELECT sample_repo_name, content FROM contents WHERE sample_path = 'README.md' AND sample_repo_name IN ('radzserg/stw_chat', 'jeffersonmourak/gameCast', 'studiocaramia/Citrus', 'gsamat/russian-firewall', 'timothylong/kindling', 'dpaspa/dfp', 'whitefusionhq/swift-for-ruby-and-js-devs', 'benching/rathena', 'layer-x/layerx-commons', 'yanlili1992/coolweather', 'nicolasblancom/MVCStarterKit', 'RoomController/RoomController', 'jockofcode/randr', 'wwwtyro/procedural.js', 'hassox/black', 'keyboardsurfer/btt-android-studio-config', 'rizzza/scripts', 'bcchapman/TiBountyHunterExample', 'nickkolok/tex-lint', 'hileon/sugarcrm-lang-pack-zh_cn', 'marlam/pmdsim', 'ANierbeck/Karaf-Vertx', 'lastaflute/lasta-mixer2', 'malenkiki/palette', 'robmass94/hacker-news-enhancements', 'masterweb121/php-telegram-bot', 'yuByte/NVActivityIndicatorView', 'makkura/electron_halloween', 'tameeshB/client-side-file-encrypt-gsoc', 'eddiewebb/newrelic_java_apache_mod_status_plugin', 'mschinis/ember-cli-segmentio', 'ksanaforge/testbump', 'pvign/gh-search', 'joellebechara/supermarche', 'mitrikyle/text-to-event', 'UzmaFarheen/ITMO544-app', 'wordpresspluginexpert/full-screen-responsive-background', 'GLeemanLee/FloatCellDemo', 'k3nn7/advent-of-code-clojure', 'SummerBlack/MasterServer', 'travelping/xliffer', 'fge/jsonschema2pojo', 'smartapant/ionic2-reddit-reader', 'TyrealGray/BurstPaparazzi', 'rootdevelop/clibs', 'rasmuskl/AssemblyInvoker', 'ToxicTree/StorageAPI_Editor', 'benhowdle89/Adaptive-Backgrounds', 'per-lennartsson/flashmessage', 'ddossot/loggErL')", 'sample_count': 50, 'first_few_repos': ['radzserg/stw_chat', 'jeffersonmourak/gameCast', 'studiocaramia/Citrus', 'gsamat/russian-firewall', 'timothylong/kindling']}, 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json'}

exec(code, env_args)
