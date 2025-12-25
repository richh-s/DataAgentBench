code = """import json

# Load readme data (from the query on contents)
# var_function-call-16559173715773755267 contains the list of dicts
readme_data = locals()['var_function-call-16559173715773755267']

# Load languages data (from the query on metadata_database)
# var_function-call-1758858495758652627 contains the list of dicts
languages_data = locals()['var_function-call-1758858495758652627']
# Note: if languages_data is a file path, I should load it. 
# The previous query output said "The result is too large, so it is stored in a file."
# So I must open it.

if isinstance(languages_data, str):
    with open(languages_data, 'r') as f:
        languages_data = json.load(f)

# Create a map for repo -> uses_python
repo_uses_python = {}
for row in languages_data:
    desc = row.get('language_description', '')
    if desc and 'Python' in desc:
        repo_uses_python[row['repo_name']] = True
    else:
        repo_uses_python[row['repo_name']] = False

# Counters
non_python_total = 0
non_python_copyright = 0

missing_metadata_count = 0

for item in readme_data:
    rname = item['sample_repo_name']
    
    # If we don't have metadata for this repo, we skip it (or treat as unknown)
    # Since we queried for all repos in readme_data, we should have them unless they don't exist in metadata db.
    if rname not in repo_uses_python:
        missing_metadata_count += 1
        continue
    
    if not repo_uses_python[rname]:
        non_python_total += 1
        # Check has_copyright. It might be string "0"/"1" or int.
        has_cp = item['has_copyright']
        if str(has_cp) == '1':
            non_python_copyright += 1

print(f"Total non-Python READMEs: {non_python_total}")
print(f"Non-Python READMEs with Copyright: {non_python_copyright}")
print(f"Missing metadata: {missing_metadata_count}")

if non_python_total > 0:
    proportion = non_python_copyright / non_python_total
    print("__RESULT__:")
    print(json.dumps(proportion))
else:
    print("__RESULT__:")
    print(json.dumps(0.0))"""

env_args = {'var_function-call-13677778010895943402': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-9760931169711847301': [{'COUNT(*)': '3325634'}], 'var_function-call-16478506448492513366': [{'count_star()': '524077'}], 'var_function-call-12904064769800451095': [{'count(DISTINCT repo_name)': '59686'}], 'var_function-call-4301828507115235792': [{'path': 'README.md', 'count_star()': '1059'}, {'path': 'README.rst', 'count_star()': '56'}, {'path': 'README', 'count_star()': '47'}, {'path': 'readme.md', 'count_star()': '27'}, {'path': 'README.markdown', 'count_star()': '10'}, {'path': 'docs/README.md', 'count_star()': '8'}, {'path': 'Readme.md', 'count_star()': '8'}, {'path': 'example/README.md', 'count_star()': '6'}, {'path': 'README.txt', 'count_star()': '6'}, {'path': 'drivers/staging/slicoss/README', 'count_star()': '6'}], 'var_function-call-18398660009715640193': [{'repo_name': 'waydelyle/openfund', 'has_copyright': '1'}, {'repo_name': 'briancavalier/todomvc-fab', 'has_copyright': '0'}, {'repo_name': 'rgardler/azure-quickstart-templates', 'has_copyright': '0'}, {'repo_name': 'DaMSL/K3', 'has_copyright': '0'}], 'var_function-call-1502578823372228115': ['briancavalier/todomvc-fab', 'waydelyle/openfund', 'DaMSL/K3', 'rgardler/azure-quickstart-templates'], 'var_function-call-362295928800951001': [{'count_star()': '24286'}], 'var_function-call-16623598251868077292': [{'id': '100b93820ade4c16225673b4ca62bb3ade63c313'}, {'id': '9ed04c6e74db0e3606e716e64e1d7190d5027b15'}, {'id': '5f0d4f75fdb2cf3b303d312d6898d3413fccfca7'}, {'id': '4e1d480f9228a40af4e3e4c507b38d593e3e588b'}, {'id': 'e75de9d29f2af646ae811eb662be95f7f3dc6cc2'}], 'var_function-call-16847896288229096354': [], 'var_function-call-15204758217568640510': 'file_storage/function-call-15204758217568640510.json', 'var_function-call-8376599495387671806': [{'count_star()': '204'}], 'var_function-call-16559173715773755267': 'file_storage/function-call-16559173715773755267.json', 'var_function-call-14553678717394768876': "'DynamoRIO/dynamorio', 'lagopus/lagopus', 'ninja-ide/ninja-ide', 'kluivers/jbw-builders', 'Microsoft/Windows-classic-samples', 'delight-im/OpenSoccer', 'landlab/landlab', 'laxa1986/gulp-angular-embed-templates', 'StackStorm/st2contrib', 'lowescott/learning-tools', 'mmerian/phpcrawl', 'andyhqtran/UI-Library', 'F1ReKing/wheelview', 'Elemental-IRCd/elemental-ircd', 'PECE-project/pece-distro', 'jforman/munin-graphite', 'richtr/plug.play.js', 'Theseus-Aegis/tac-a3-mods', 'AcyOrt/acyort', 'jeffmo/jasmine-pit', 'Magnetme/consultant', 'uupaa/UserAgent.js', 'linux-on-ibm-z/kubernetes', 'neophob/PixelController', 'ravl1084/TJ2PDF', 'Microsoft/WPF-Samples', 'andres-erbsen/dename', 'swannodette/todomvc', 'winunet/Hui', 'dfletcher/tsws', 'adobe-type-tools/cmap-resources', 'wilsonmar/oss-perf', 'VirgilSecurity/virgil', 'mojeda/ServerStatus', 'zpz1237/NirZhihuNews', 'chrisdone/hulk', 'keithwhor/cmnd', 'parro-it/is-fqdn', 'supamii/QttpServer', 'Blizzard/omniauth-bnet', 'JSSolutions/meteor-google-prediction', 'rogpeppe/showdeps', 'smklancher/ZeoSleepMonitor', 'isychev93/Xamarin.Forms-Drag-and-drop-ListView', 'mluisbrown/Memories', 'krishkumar/BlockParty', 'aceway/findX', 'Flat/Konachan-for-Muzei', 'rgardler/azure-quickstart-templates', 'opinkerfi/adagios', 'Moq/moq', 'CapsAdmin/goluwa', 'lucaspouzac/contiperf', 'hypriot/rpi-busybox-httpd', 'chrisbarrett/emacs-refactor', 'derrickburns/generalized-kmeans-clustering', 'yubinbai/leetcode', 'paf31/lambdaconf-2015', 'paldepind/synceddb', 'americanpanorama/panorama', 'divmain/GitSavvy', 'dineshTrivedi/angularjs-styleguide', 'jzitelli/poolvr', 'alibaba/jstorm', 'adafruit/Adafruit-Trinket-Gemma-Bootloader', 'TelerikAcademy/SchoolAcademy', 'wahern/cqueues', 'kittens/lerna', 'j-bennet/wharfee', 'marcelklehr/gulf-contenteditable', 'tt-acm/Spectacles.WebViewer', 'VeliovGroup/Meteor-logger', 'jaredwilli/devtools-cheatsheet', 'hacklabr/mapasculturais', 'airlift/airlift', 'atom/node-ctags', 'TelerikAcademy/TelerikAcademyPlus', 'jeelabs/jet', 'noveogroup/android-logger', 'otoolep/gosf-rqlite', 'Swader/diffbot-php-client', 'devsoulwolf/ChatMessageView', 'EngoEngine/engo', 'CESNET/owncloud-theme', 'pezy/LeetCode', 'google/traceur-compiler', 'rofrischmann/fela', 'SuperID/super-cache', 'Microsoft/vsts-tasks', 'hosom/bro-file-extraction', 'qt-pods/qt-pods', 'johnhamelink/exrm_deb', 'ha/doozerd', 'guangzhuwu/p2engine', 'DaMSL/K3', 'Hexworks/hexameter', 'rdebath/Brainfuck', 'CfABrigadePhiladelphia/jawn', 'daemon3000/InputManager', 'Maaphoo/Retr3d', 'rafiuske/papergram', 'rubylit/guevara', 'PixarAnimationStudios/jss-api-gem', 'selenith/plasmide', 'tangrams/blocks', 'DMarby/Harpia', 'dikiaap/mangan', 'retep998/winapi-rs', 'spaar/besiege-modloader', 'DUBULEE/FileCacheUtil', 'JuliaDB/MySQL.jl', 'google/libfuzzer-bot', 'varlesh/elementary-add', 'nictuku/stardew-rocks', 'MIT-LCP/mimic-code', 'brindille/brindille-component', 'felladrin/runuo-custom-scripts', 'dblock/slack-google-bot', 'ninibe/netlog', 'hortonworks/kubernetes-yarn', '3ventic/DiscordServers', 'bh107/bohrium', 'premgane/agolo-slackbot', 'Calinou/godot-snippets', 'alexandrucoman/labs', 'jconst/JCDialPad', 'jails-org/Demos', 'jsonld-java/jsonld-java-tools', 'webpack/webpack', 'pouetnet/pouet2.0', 'sskyy/redux-task', 'thedeibo/ServerLoveMCPE', 'pmwkaa/serenity', 'whitepages/terraform-provider-stingray', 'rancher/rancher-compose', 'ridingbytes/plone.commander', 'LI-COR/eddypro-engine', 'Ali-Razmjoo/OWASP-ZSC', 'flextry/Telerik-Academy', 'OscarES/Differential-Algebra-Tracker', 'rita-marylin-raquel/softbloks', 'blond/hash-set', 'openhab/openhab2', 'yuvirajsinh/YCameraView', 'ZenLulz/MemorySharp', 'paul999/433.92-Raspberry-Pi', 'jcoppieters/cody-samples', 'xxtea/xxtea-php', 'firebase/EventSource-Examples', 'voussoir/reddit', 'zverok/magic_cloud', 'digibyte/digibyte', 'himanshu-soni/image-intent-handler', 'velveteer/mithril-boilerplate', 'apache/stratos', 'jcinnamond/el-presenti', 'JiyunTech/Kever', 'Download/polymer-cdn', 'mozilla/oneanddone', 'cwilso/midi-synth', 'tonioo/modoboa', 'rusty1s/koa2-rest-api', 'sclorg/rhscl-dockerfiles', 'polomoshnov/jQuery-UI-Resizable-Snap-extension', 'analog-nico/passport-pinterest', 'durka/named-block', 'Nebulosus/shamir', 'zhufengnodejs/201602node_homework', 'AutoDo/AutoDo', 'JMPerez/beats-audio-api', 'sakaal/service_platform_ansible', 'NickolausDS/Unity-Free-Flight', 'dale3h/alexa-skills-list', 'sendgrid/python-http-client', 'zeroc-ice/ice-demos', 'fdaciuk/ajax', 'docker-library/docs', 'inamiy/DebugLog', 'rtrouton/rtrouton_scripts', 'jbboehr/php-mustache', 'mstevenson/AssetsWatcher', 'nodejs/node-gyp', 'claudijd/c7decrypt', 'OfficeDev/Product-List-Code-Sample', 'mattinove/SwiftySlider', 'crossroadlabs/homebrew-tap', 'opencog/atomspace', 'MaLeLabTs/RegexGenerator', 'jeffpar/pcjs', 'meganz/sdk', 'shenxgan/xblog', 'alexchamberlain/piimg', 'lmammino/gulp-cozy', 'gshopov/competitive-programming-archive', 'kinduff/spree_reffiliate', 'radare/radeco', 'edomaru/codeigniter_multilevel_menu', 'johnpneumann/portable-maya-prefs', 'rluders/phaser-skeleton', 'blynkkk/blynk-server'", 'var_function-call-1758858495758652627': 'file_storage/function-call-1758858495758652627.json'}

exec(code, env_args)
