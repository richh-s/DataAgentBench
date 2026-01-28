code = """import json
import re

# Read languages data for repos
if isinstance(locals()['var_functions.query_db:2'], str):
    with open(locals()['var_functions.query_db:2'], 'r') as f:
        languages_data = json.load(f)
else:
    languages_data = locals()['var_functions.query_db:2']

# Create a set of non-Python repos
non_python_repos = {item['repo_name'] for item in non_python_repos}

# Read README files
if isinstance(locals()['var_functions.query_db:12'], str):
    with open(locals()['var_functions.query_db:12'], 'r') as f:
        readme_files = json.load(f)
else:
    readme_files = locals()['var_functions.query_db:12']

# Check which README files are from non-Python repos
readme_non_python = []
copyright_pattern = re.compile(r'copyright|©', re.IGNORECASE)

for readme in readme_files:
    repo_name = readme['sample_repo_name']
    if repo_name in non_python_repos:
        has_copyright = bool(copyright_pattern.search(readme.get('content', '')))
        readme_non_python.append({
            'repo_name': repo_name,
            'has_copyright': has_copyright,
            'content': readme.get('content', '')
        })

# Calculate statistics
total_readme_non_python = len(readme_non_python)
copyright_count = sum(1 for r in readme_non_python if r['has_copyright'])

print('__RESULT__:')
print(json.dumps({
    'total_non_python_readmes': total_readme_non_python,
    'copyright_count': copyright_count,
    'proportion': copyright_count / total_readme_non_python if total_readme_non_python > 0 else 0,
    'details': readme_non_python
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'total_repos': '2774729'}], 'var_functions.list_db:8': ['commits', 'contents', 'files'], 'var_functions.query_db:10': [{'total_files': '202'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': ['google/libfuzzer-bot', 'chrisdone/hulk', 'yubinbai/leetcode', 'zverok/magic_cloud', 'tangrams/blocks', 'delight-im/OpenSoccer', 'CESNET/owncloud-theme', 'crossroadlabs/homebrew-tap', 'MaLeLabTs/RegexGenerator', 'Nebulosus/shamir', 'LI-COR/eddypro-engine', 'rofrischmann/fela', 'mmerian/phpcrawl', 'JMPerez/beats-audio-api', 'sendgrid/python-http-client', 'zeroc-ice/ice-demos', 'lowescott/learning-tools', 'jaredwilli/devtools-cheatsheet', 'StackStorm/st2contrib', 'kittens/lerna', 'adafruit/Adafruit-Trinket-Gemma-Bootloader', 'adobe-type-tools/cmap-resources', 'voussoir/reddit', 'xxtea/xxtea-php', 'gshopov/competitive-programming-archive', 'jsonld-java/jsonld-java-tools', 'DMarby/Harpia', 'OscarES/Differential-Algebra-Tracker', 'winunet/Hui', 'jeelabs/jet', 'smklancher/ZeoSleepMonitor', 'apache/stratos', 'blynkkk/blynk-server', 'velveteer/mithril-boilerplate', 'Elemental-IRCd/elemental-ircd', 'Microsoft/WPF-Samples', 'marcelklehr/gulf-contenteditable', 'jcoppieters/cody-samples', 'google/traceur-compiler', 'hosom/bro-file-extraction', 'daemon3000/InputManager', 'rgardler/azure-quickstart-templates', 'Microsoft/Windows-classic-samples', 'ninja-ide/ninja-ide', 'jbboehr/php-mustache', 'durka/named-block', 'varlesh/elementary-add', 'dale3h/alexa-skills-list', 'parro-it/is-fqdn', 'atom/node-ctags', 'ZenLulz/MemorySharp', 'jeffpar/pcjs', 'Moq/moq', 'j-bennet/wharfee', 'shenxgan/xblog', 'retep998/winapi-rs', 'guangzhuwu/p2engine', 'paldepind/synceddb', 'inamiy/DebugLog', 'devsoulwolf/ChatMessageView', 'airlift/airlift', 'andyhqtran/UI-Library', 'firebase/EventSource-Examples', 'Microsoft/vsts-tasks', 'fdaciuk/ajax', 'AutoDo/AutoDo', 'thedeibo/ServerLoveMCPE', 'whitepages/terraform-provider-stingray', 'qt-pods/qt-pods', 'rancher/rancher-compose', 'johnpneumann/portable-maya-prefs', 'ninibe/netlog', 'dineshTrivedi/angularjs-styleguide', 'OfficeDev/Product-List-Code-Sample', 'SuperID/super-cache', 'CfABrigadePhiladelphia/jawn', 'bh107/bohrium', 'derrickburns/generalized-kmeans-clustering', 'linux-on-ibm-z/kubernetes', 'uupaa/UserAgent.js', 'rluders/phaser-skeleton', 'alibaba/jstorm', 'jeffmo/jasmine-pit', 'supamii/QttpServer', 'keithwhor/cmnd', 'laxa1986/gulp-angular-embed-templates', 'zpz1237/NirZhihuNews', 'chrisbarrett/emacs-refactor', 'hypriot/rpi-busybox-httpd', 'Ali-Razmjoo/OWASP-ZSC', 'webpack/webpack', 'kinduff/spree_reffiliate', 'pmwkaa/serenity', 'yuvirajsinh/YCameraView', 'paf31/lambdaconf-2015', 'Magnetme/consultant', 'jcinnamond/el-presenti', 'pezy/LeetCode', 'selenith/plasmide', 'rafiuske/papergram', 'kluivers/jbw-builders', 'sakaal/service_platform_ansible', 'neophob/PixelController', 'JSSolutions/meteor-google-prediction', 'jconst/JCDialPad', 'Swader/diffbot-php-client', 'edomaru/codeigniter_multilevel_menu', 'jails-org/Demos', 'DynamoRIO/dynamorio', 'Theseus-Aegis/tac-a3-mods', 'PECE-project/pece-distro', 'tonioo/modoboa', 'lagopus/lagopus', 'JiyunTech/Kever', 'Maaphoo/Retr3d', 'rubylit/guevara', 'VeliovGroup/Meteor-logger', 'TelerikAcademy/TelerikAcademyPlus', 'zhufengnodejs/201602node_homework', 'ha/doozerd', 'claudijd/c7decrypt', 'Blizzard/omniauth-bnet', 'nictuku/stardew-rocks', 'johnhamelink/exrm_deb', 'tt-acm/Spectacles.WebViewer', 'himanshu-soni/image-intent-handler', 'isychev93/Xamarin.Forms-Drag-and-drop-ListView', 'opinkerfi/adagios', 'noveogroup/android-logger', 'mattinove/SwiftySlider', 'TelerikAcademy/SchoolAcademy', 'Download/polymer-cdn', '3ventic/DiscordServers', 'wilsonmar/oss-perf', 'rogpeppe/showdeps', 'Hexworks/hexameter', 'VirgilSecurity/virgil', 'sclorg/rhscl-dockerfiles', 'otoolep/gosf-rqlite', 'americanpanorama/panorama', 'paul999/433.92-Raspberry-Pi', 'jforman/munin-graphite', 'richtr/plug.play.js', 'hacklabr/mapasculturais', 'alexchamberlain/piimg', 'jzitelli/poolvr', 'opencog/atomspace', 'MIT-LCP/mimic-code', 'wahern/cqueues', 'radare/radeco', 'NickolausDS/Unity-Free-Flight', 'pouetnet/pouet2.0', 'spaar/besiege-modloader', 'DUBULEE/FileCacheUtil', 'rita-marylin-raquel/softbloks', 'EngoEngine/engo', 'CapsAdmin/goluwa', 'rusty1s/koa2-rest-api', 'premgane/agolo-slackbot', 'DaMSL/K3', 'mozilla/oneanddone', 'nodejs/node-gyp', 'docker-library/docs', 'hortonworks/kubernetes-yarn', 'lucaspouzac/contiperf', 'dfletcher/tsws', 'dikiaap/mangan', 'divmain/GitSavvy', 'F1ReKing/wheelview', 'AcyOrt/acyort', 'meganz/sdk', 'PixarAnimationStudios/jss-api-gem', 'swannodette/todomvc', 'rdebath/Brainfuck', 'polomoshnov/jQuery-UI-Resizable-Snap-extension', 'JuliaDB/MySQL.jl', 'lmammino/gulp-cozy', 'digibyte/digibyte', 'cwilso/midi-synth', 'mstevenson/AssetsWatcher', 'krishkumar/BlockParty', 'felladrin/runuo-custom-scripts', 'Calinou/godot-snippets', 'mojeda/ServerStatus', 'landlab/landlab', 'mluisbrown/Memories', 'sskyy/redux-task', 'ravl1084/TJ2PDF', 'dblock/slack-google-bot', 'alexandrucoman/labs', 'brindille/brindille-component', 'rtrouton/rtrouton_scripts', 'blond/hash-set', 'andres-erbsen/dename', 'Flat/Konachan-for-Muzei', 'analog-nico/passport-pinterest', 'aceway/findX', 'openhab/openhab2']}

exec(code, env_args)
