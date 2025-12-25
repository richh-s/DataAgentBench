code = """import json
import re

# Load readmes
with open(locals()['var_function-call-7984024457334347274'], 'r') as f:
    readmes = json.load(f)

# Load languages
with open(locals()['var_function-call-3672632216200080800'], 'r') as f:
    languages = json.load(f)

# Create a map of repo_name -> uses_python (boolean)
repo_uses_python = {}
for entry in languages:
    name = entry['repo_name']
    desc = entry.get('language_description', '')
    if desc is None: desc = ""
    # Check if Python is mentioned
    if "Python" in desc:
        repo_uses_python[name] = True
    else:
        repo_uses_python[name] = False

# Filter readmes
non_python_readmes = []
for r in readmes:
    repo = r['sample_repo_name']
    # If we don't have language info, assume non-Python? Or skip?
    # The previous query fetched languages for ALL repos in the readme list.
    # So we should have info for all, unless they were missing from metadata db.
    # If missing, I will assume non-Python or skip?
    # Let's check if repo is in the map.
    if repo in repo_uses_python:
        if not repo_uses_python[repo]:
            non_python_readmes.append(r)
    else:
        # If not in metadata DB, maybe it was deleted or mismatch.
        # I'll exclude it to be safe, or include if I assume non-Python.
        # Usually metadata covers most. I'll exclude to be rigorous.
        pass

# Check copyright
copyright_count = 0
total_count = len(non_python_readmes)

copyright_pattern = re.compile(r'(copyright|©|\(c\))', re.IGNORECASE)

for r in non_python_readmes:
    content = r['content']
    if content and copyright_pattern.search(content):
        copyright_count += 1

proportion = 0.0
if total_count > 0:
    proportion = copyright_count / total_count

result = {
    "total_non_python_readmes": total_count,
    "copyright_count": copyright_count,
    "proportion": proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8212495443049668222': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-12519788940020729844': [{'COUNT(*)': '3325634'}], 'var_function-call-2224969264879341492': [{'COUNT(*)': '2774729'}], 'var_function-call-17264575551013979957': [{'count_star()': '24286'}], 'var_function-call-13732962816098046442': [{'sample_path': 'device/nfc/nfc.mojom'}, {'sample_path': 'net/tools/quic/synchronous_host_resolver.cc'}, {'sample_path': 'lib/cUnix.mli'}, {'sample_path': 'json4s/src/main/ls/0.6.5.json'}, {'sample_path': 'assets/images/svg/ic_menu_folder_w.svg'}, {'sample_path': 'notes/2.3.1.markdown'}, {'sample_path': '3rdParty/boost/1.61.0b1/boost/hana/monadic_fold_right.hpp'}, {'sample_path': '3rdParty/boost/1.61.0b1/boost/metaparse/v1/iterate_c.hpp'}, {'sample_path': 'java/engine/org/apache/derby/iapi/store/access/BinaryOrderable.java'}, {'sample_path': 'src/program/lwaftr/doc/benchmarks-v1.0/transient-self-test-gbps.png'}], 'var_function-call-2694315862573837520': [{'count_star()': '195'}], 'var_function-call-7984024457334347274': 'file_storage/function-call-7984024457334347274.json', 'var_function-call-11804209382094254503': ['rafiuske/papergram', 'smklancher/ZeoSleepMonitor', 'thedeibo/ServerLoveMCPE', 'jcoppieters/cody-samples', 'PECE-project/pece-distro', 'spaar/besiege-modloader', 'krishkumar/BlockParty', 'Theseus-Aegis/tac-a3-mods', 'jeelabs/jet', 'zhufengnodejs/201602node_homework', 'airlift/airlift', 'inamiy/DebugLog', 'OscarES/Differential-Algebra-Tracker', 'adobe-type-tools/cmap-resources', 'nictuku/stardew-rocks', 'jzitelli/poolvr', 'rtrouton/rtrouton_scripts', 'rubylit/guevara', 'openhab/openhab2', 'mluisbrown/Memories', 'dfletcher/tsws', 'rusty1s/koa2-rest-api', 'ninja-ide/ninja-ide', 'Maaphoo/Retr3d', 'nodejs/node-gyp', 'crossroadlabs/homebrew-tap', 'durka/named-block', 'atom/node-ctags', 'NickolausDS/Unity-Free-Flight', 'alexchamberlain/piimg', 'DUBULEE/FileCacheUtil', 'Nebulosus/shamir', 'chrisbarrett/emacs-refactor', 'himanshu-soni/image-intent-handler', 'alexandrucoman/labs', 'JMPerez/beats-audio-api', 'rogpeppe/showdeps', 'hosom/bro-file-extraction', 'paul999/433.92-Raspberry-Pi', 'AcyOrt/acyort', 'blond/hash-set', 'TelerikAcademy/TelerikAcademyPlus', 'Magnetme/consultant', 'lmammino/gulp-cozy', 'webpack/webpack', 'mattinove/SwiftySlider', 'Hexworks/hexameter', 'mstevenson/AssetsWatcher', 'xxtea/xxtea-php', 'yuvirajsinh/YCameraView', 'mmerian/phpcrawl', 'mojeda/ServerStatus', 'zpz1237/NirZhihuNews', 'linux-on-ibm-z/kubernetes', 'sendgrid/python-http-client', 'tangrams/blocks', 'Microsoft/Windows-classic-samples', 'google/traceur-compiler', 'wahern/cqueues', 'selenith/plasmide', 'Calinou/godot-snippets', 'blynkkk/blynk-server', 'ZenLulz/MemorySharp', 'marcelklehr/gulf-contenteditable', 'Download/polymer-cdn', 'paf31/lambdaconf-2015', 'JSSolutions/meteor-google-prediction', 'andres-erbsen/dename', 'alibaba/jstorm', 'DaMSL/K3', 'gshopov/competitive-programming-archive', 'hacklabr/mapasculturais', 'johnpneumann/portable-maya-prefs', 'DynamoRIO/dynamorio', 'firebase/EventSource-Examples', 'apache/stratos', 'chrisdone/hulk', 'jeffmo/jasmine-pit', 'Moq/moq', 'CfABrigadePhiladelphia/jawn', 'j-bennet/wharfee', 'radare/radeco', 'rancher/rancher-compose', 'opencog/atomspace', 'VeliovGroup/Meteor-logger', 'StackStorm/st2contrib', 'wilsonmar/oss-perf', 'laxa1986/gulp-angular-embed-templates', 'whitepages/terraform-provider-stingray', 'paldepind/synceddb', 'winunet/Hui', 'fdaciuk/ajax', 'uupaa/UserAgent.js', 'felladrin/runuo-custom-scripts', 'zverok/magic_cloud', 'jails-org/Demos', 'Microsoft/WPF-Samples', 'EngoEngine/engo', 'dale3h/alexa-skills-list', 'supamii/QttpServer', 'lowescott/learning-tools', 'Blizzard/omniauth-bnet', 'guangzhuwu/p2engine', 'isychev93/Xamarin.Forms-Drag-and-drop-ListView', 'rgardler/azure-quickstart-templates', 'F1ReKing/wheelview', 'richtr/plug.play.js', 'neophob/PixelController', 'Swader/diffbot-php-client', 'rita-marylin-raquel/softbloks', 'ravl1084/TJ2PDF', 'analog-nico/passport-pinterest', 'dblock/slack-google-bot', 'adafruit/Adafruit-Trinket-Gemma-Bootloader', 'sskyy/redux-task', 'kinduff/spree_reffiliate', 'noveogroup/android-logger', 'jforman/munin-graphite', 'mozilla/oneanddone', 'TelerikAcademy/SchoolAcademy', 'devsoulwolf/ChatMessageView', 'velveteer/mithril-boilerplate', 'ha/doozerd', 'hypriot/rpi-busybox-httpd', 'rdebath/Brainfuck', 'rluders/phaser-skeleton', 'rofrischmann/fela', 'pmwkaa/serenity', 'brindille/brindille-component', 'kluivers/jbw-builders', 'DMarby/Harpia', 'MIT-LCP/mimic-code', 'opinkerfi/adagios', 'claudijd/c7decrypt', 'Microsoft/vsts-tasks', 'hortonworks/kubernetes-yarn', 'keithwhor/cmnd', 'aceway/findX', 'premgane/agolo-slackbot', 'jsonld-java/jsonld-java-tools', '3ventic/DiscordServers', 'meganz/sdk', 'CapsAdmin/goluwa', 'JuliaDB/MySQL.jl', 'AutoDo/AutoDo', 'jcinnamond/el-presenti', 'jeffpar/pcjs', 'daemon3000/InputManager', 'sclorg/rhscl-dockerfiles', 'SuperID/super-cache', 'derrickburns/generalized-kmeans-clustering', 'ninibe/netlog', 'google/libfuzzer-bot', 'cwilso/midi-synth', 'CESNET/owncloud-theme', 'andyhqtran/UI-Library', 'dikiaap/mangan', 'otoolep/gosf-rqlite', 'PixarAnimationStudios/jss-api-gem', 'sakaal/service_platform_ansible', 'landlab/landlab', 'kittens/lerna', 'jbboehr/php-mustache', 'pezy/LeetCode', 'pouetnet/pouet2.0', 'voussoir/reddit', 'jconst/JCDialPad', 'shenxgan/xblog', 'delight-im/OpenSoccer', 'retep998/winapi-rs', 'Elemental-IRCd/elemental-ircd', 'LI-COR/eddypro-engine', 'americanpanorama/panorama', 'docker-library/docs', 'swannodette/todomvc', 'divmain/GitSavvy', 'digibyte/digibyte', 'MaLeLabTs/RegexGenerator', 'qt-pods/qt-pods', 'zeroc-ice/ice-demos', 'OfficeDev/Product-List-Code-Sample', 'varlesh/elementary-add', 'yubinbai/leetcode', 'lagopus/lagopus', 'johnhamelink/exrm_deb', 'polomoshnov/jQuery-UI-Resizable-Snap-extension', 'Flat/Konachan-for-Muzei', 'tonioo/modoboa', 'lucaspouzac/contiperf', 'bh107/bohrium', 'edomaru/codeigniter_multilevel_menu'], 'var_function-call-5446700641983300336': "'rafiuske/papergram', 'smklancher/ZeoSleepMonitor', 'thedeibo/ServerLoveMCPE', 'jcoppieters/cody-samples', 'PECE-project/pece-distro', 'spaar/besiege-modloader', 'krishkumar/BlockParty', 'Theseus-Aegis/tac-a3-mods', 'jeelabs/jet', 'zhufengnodejs/201602node_homework', 'airlift/airlift', 'inamiy/DebugLog', 'OscarES/Differential-Algebra-Tracker', 'adobe-type-tools/cmap-resources', 'nictuku/stardew-rocks', 'jzitelli/poolvr', 'rtrouton/rtrouton_scripts', 'rubylit/guevara', 'openhab/openhab2', 'mluisbrown/Memories', 'dfletcher/tsws', 'rusty1s/koa2-rest-api', 'ninja-ide/ninja-ide', 'Maaphoo/Retr3d', 'nodejs/node-gyp', 'crossroadlabs/homebrew-tap', 'durka/named-block', 'atom/node-ctags', 'NickolausDS/Unity-Free-Flight', 'alexchamberlain/piimg', 'DUBULEE/FileCacheUtil', 'Nebulosus/shamir', 'chrisbarrett/emacs-refactor', 'himanshu-soni/image-intent-handler', 'alexandrucoman/labs', 'JMPerez/beats-audio-api', 'rogpeppe/showdeps', 'hosom/bro-file-extraction', 'paul999/433.92-Raspberry-Pi', 'AcyOrt/acyort', 'blond/hash-set', 'TelerikAcademy/TelerikAcademyPlus', 'Magnetme/consultant', 'lmammino/gulp-cozy', 'webpack/webpack', 'mattinove/SwiftySlider', 'Hexworks/hexameter', 'mstevenson/AssetsWatcher', 'xxtea/xxtea-php', 'yuvirajsinh/YCameraView', 'mmerian/phpcrawl', 'mojeda/ServerStatus', 'zpz1237/NirZhihuNews', 'linux-on-ibm-z/kubernetes', 'sendgrid/python-http-client', 'tangrams/blocks', 'Microsoft/Windows-classic-samples', 'google/traceur-compiler', 'wahern/cqueues', 'selenith/plasmide', 'Calinou/godot-snippets', 'blynkkk/blynk-server', 'ZenLulz/MemorySharp', 'marcelklehr/gulf-contenteditable', 'Download/polymer-cdn', 'paf31/lambdaconf-2015', 'JSSolutions/meteor-google-prediction', 'andres-erbsen/dename', 'alibaba/jstorm', 'DaMSL/K3', 'gshopov/competitive-programming-archive', 'hacklabr/mapasculturais', 'johnpneumann/portable-maya-prefs', 'DynamoRIO/dynamorio', 'firebase/EventSource-Examples', 'apache/stratos', 'chrisdone/hulk', 'jeffmo/jasmine-pit', 'Moq/moq', 'CfABrigadePhiladelphia/jawn', 'j-bennet/wharfee', 'radare/radeco', 'rancher/rancher-compose', 'opencog/atomspace', 'VeliovGroup/Meteor-logger', 'StackStorm/st2contrib', 'wilsonmar/oss-perf', 'laxa1986/gulp-angular-embed-templates', 'whitepages/terraform-provider-stingray', 'paldepind/synceddb', 'winunet/Hui', 'fdaciuk/ajax', 'uupaa/UserAgent.js', 'felladrin/runuo-custom-scripts', 'zverok/magic_cloud', 'jails-org/Demos', 'Microsoft/WPF-Samples', 'EngoEngine/engo', 'dale3h/alexa-skills-list', 'supamii/QttpServer', 'lowescott/learning-tools', 'Blizzard/omniauth-bnet', 'guangzhuwu/p2engine', 'isychev93/Xamarin.Forms-Drag-and-drop-ListView', 'rgardler/azure-quickstart-templates', 'F1ReKing/wheelview', 'richtr/plug.play.js', 'neophob/PixelController', 'Swader/diffbot-php-client', 'rita-marylin-raquel/softbloks', 'ravl1084/TJ2PDF', 'analog-nico/passport-pinterest', 'dblock/slack-google-bot', 'adafruit/Adafruit-Trinket-Gemma-Bootloader', 'sskyy/redux-task', 'kinduff/spree_reffiliate', 'noveogroup/android-logger', 'jforman/munin-graphite', 'mozilla/oneanddone', 'TelerikAcademy/SchoolAcademy', 'devsoulwolf/ChatMessageView', 'velveteer/mithril-boilerplate', 'ha/doozerd', 'hypriot/rpi-busybox-httpd', 'rdebath/Brainfuck', 'rluders/phaser-skeleton', 'rofrischmann/fela', 'pmwkaa/serenity', 'brindille/brindille-component', 'kluivers/jbw-builders', 'DMarby/Harpia', 'MIT-LCP/mimic-code', 'opinkerfi/adagios', 'claudijd/c7decrypt', 'Microsoft/vsts-tasks', 'hortonworks/kubernetes-yarn', 'keithwhor/cmnd', 'aceway/findX', 'premgane/agolo-slackbot', 'jsonld-java/jsonld-java-tools', '3ventic/DiscordServers', 'meganz/sdk', 'CapsAdmin/goluwa', 'JuliaDB/MySQL.jl', 'AutoDo/AutoDo', 'jcinnamond/el-presenti', 'jeffpar/pcjs', 'daemon3000/InputManager', 'sclorg/rhscl-dockerfiles', 'SuperID/super-cache', 'derrickburns/generalized-kmeans-clustering', 'ninibe/netlog', 'google/libfuzzer-bot', 'cwilso/midi-synth', 'CESNET/owncloud-theme', 'andyhqtran/UI-Library', 'dikiaap/mangan', 'otoolep/gosf-rqlite', 'PixarAnimationStudios/jss-api-gem', 'sakaal/service_platform_ansible', 'landlab/landlab', 'kittens/lerna', 'jbboehr/php-mustache', 'pezy/LeetCode', 'pouetnet/pouet2.0', 'voussoir/reddit', 'jconst/JCDialPad', 'shenxgan/xblog', 'delight-im/OpenSoccer', 'retep998/winapi-rs', 'Elemental-IRCd/elemental-ircd', 'LI-COR/eddypro-engine', 'americanpanorama/panorama', 'docker-library/docs', 'swannodette/todomvc', 'divmain/GitSavvy', 'digibyte/digibyte', 'MaLeLabTs/RegexGenerator', 'qt-pods/qt-pods', 'zeroc-ice/ice-demos', 'OfficeDev/Product-List-Code-Sample', 'varlesh/elementary-add', 'yubinbai/leetcode', 'lagopus/lagopus', 'johnhamelink/exrm_deb', 'polomoshnov/jQuery-UI-Resizable-Snap-extension', 'Flat/Konachan-for-Muzei', 'tonioo/modoboa', 'lucaspouzac/contiperf', 'bh107/bohrium', 'edomaru/codeigniter_multilevel_menu'", 'var_function-call-3672632216200080800': 'file_storage/function-call-3672632216200080800.json'}

exec(code, env_args)
