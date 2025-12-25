code = """import json

# Load languages data
with open(locals()['var_function-call-13312192613915097450'], 'r') as f:
    languages_data = json.load(f)

# Create a set of non-Python repos
non_python_repos = set()
for entry in languages_data:
    repo = entry['repo_name']
    desc = entry.get('language_description', '')
    if desc is None:
        desc = ""
    # Check if Python is mentioned
    if "Python" not in desc:
        non_python_repos.add(repo)

# Load READMEs
with open(locals()['var_function-call-4549804856580027565'], 'r') as f:
    readmes = json.load(f)

numerator = 0
denominator = 0

for r in readmes:
    repo = r.get('sample_repo_name')
    content = r.get('content', '')
    
    # We only care about repos that we confirmed are non-Python
    # But wait, what if a repo is NOT in languages_data at all?
    # If I queried for all of them and some are missing, I should probably exclude them because I don't know their language.
    # The query `SELECT ... WHERE repo_name IN (...)` should return all matching repos.
    # If a repo is not in the result, it doesn't exist in metadata_database (or name mismatch).
    # I should check if repo is in the returned languages_data to be sure.
    
    # Check if we have language info for this repo
    # To be efficient, let's make a set of all repos returned by the language query
    all_returned_repos = set(entry['repo_name'] for entry in languages_data)
    
    if repo in all_returned_repos:
        if repo in non_python_repos:
            denominator += 1
            if "copyright" in content.lower():
                numerator += 1

proportion = 0.0
if denominator > 0:
    proportion = numerator / denominator

print("__RESULT__:")
print(json.dumps({
    "numerator": numerator,
    "denominator": denominator,
    "proportion": proportion
}))"""

env_args = {'var_function-call-15783456895619002105': ['languages', 'repos', 'licenses'], 'var_function-call-15783456895619001812': ['commits', 'contents', 'files'], 'var_function-call-6182409942289176379': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-6886523166819188166': [{'cnt': '2774729'}], 'var_function-call-9666328473966321472': [{'sample_path': 'device/nfc/nfc.mojom'}, {'sample_path': 'net/tools/quic/synchronous_host_resolver.cc'}, {'sample_path': 'lib/cUnix.mli'}, {'sample_path': 'json4s/src/main/ls/0.6.5.json'}, {'sample_path': 'assets/images/svg/ic_menu_folder_w.svg'}, {'sample_path': 'notes/2.3.1.markdown'}, {'sample_path': '3rdParty/boost/1.61.0b1/boost/hana/monadic_fold_right.hpp'}, {'sample_path': '3rdParty/boost/1.61.0b1/boost/metaparse/v1/iterate_c.hpp'}, {'sample_path': 'java/engine/org/apache/derby/iapi/store/access/BinaryOrderable.java'}, {'sample_path': 'src/program/lwaftr/doc/benchmarks-v1.0/transient-self-test-gbps.png'}], 'var_function-call-4234828658188929615': [{'count_star()': '128'}], 'var_function-call-5465217869787282476': [{'count_star()': '133'}], 'var_function-call-4549804856580027565': 'file_storage/function-call-4549804856580027565.json', 'var_function-call-9269858179231061703': ['ninja-ide/ninja-ide', 'cwilso/midi-synth', 'ha/doozerd', 'devsoulwolf/ChatMessageView', 'google/traceur-compiler', 'jeffmo/jasmine-pit', 'radare/radeco', 'jcinnamond/el-presenti', 'durka/named-block', 'MaLeLabTs/RegexGenerator', 'blond/hash-set', 'uupaa/UserAgent.js', 'Magnetme/consultant', 'rafiuske/papergram', 'wahern/cqueues', 'Hexworks/hexameter', 'xxtea/xxtea-php', 'JSSolutions/meteor-google-prediction', 'JuliaDB/MySQL.jl', 'varlesh/elementary-add', 'blynkkk/blynk-server', 'sakaal/service_platform_ansible', '3ventic/DiscordServers', 'sskyy/redux-task', 'jeelabs/jet', 'Swader/diffbot-php-client', 'mluisbrown/Memories', 'lucaspouzac/contiperf', 'mattinove/SwiftySlider', 'polomoshnov/jQuery-UI-Resizable-Snap-extension', 'dfletcher/tsws', 'marcelklehr/gulf-contenteditable', 'F1ReKing/wheelview', 'pmwkaa/serenity', 'nodejs/node-gyp', 'Moq/moq', 'adafruit/Adafruit-Trinket-Gemma-Bootloader', 'aceway/findX', 'Blizzard/omniauth-bnet', 'rluders/phaser-skeleton', 'mozilla/oneanddone', 'dikiaap/mangan', 'CfABrigadePhiladelphia/jawn', 'hosom/bro-file-extraction', 'Maaphoo/Retr3d', 'andres-erbsen/dename', 'dblock/slack-google-bot', 'jconst/JCDialPad', 'chrisdone/hulk', 'winunet/Hui', 'adobe-type-tools/cmap-resources', 'crossroadlabs/homebrew-tap', 'NickolausDS/Unity-Free-Flight', 'OscarES/Differential-Algebra-Tracker', 'isychev93/Xamarin.Forms-Drag-and-drop-ListView', 'rdebath/Brainfuck', 'himanshu-soni/image-intent-handler', 'mstevenson/AssetsWatcher', 'j-bennet/wharfee', 'AcyOrt/acyort', 'rogpeppe/showdeps', 'AutoDo/AutoDo', 'JMPerez/beats-audio-api', 'inamiy/DebugLog', 'fdaciuk/ajax', 'jzitelli/poolvr', 'thedeibo/ServerLoveMCPE', 'guangzhuwu/p2engine', 'rusty1s/koa2-rest-api', 'DUBULEE/FileCacheUtil', 'VeliovGroup/Meteor-logger', 'claudijd/c7decrypt', 'alexchamberlain/piimg', 'SuperID/super-cache', 'PECE-project/pece-distro', 'paul999/433.92-Raspberry-Pi', 'jsonld-java/jsonld-java-tools', 'noveogroup/android-logger', 'nictuku/stardew-rocks', 'edomaru/codeigniter_multilevel_menu', 'shenxgan/xblog', 'LI-COR/eddypro-engine', 'zverok/magic_cloud', 'rita-marylin-raquel/softbloks', 'mojeda/ServerStatus', 'yuvirajsinh/YCameraView', 'firebase/EventSource-Examples', 'otoolep/gosf-rqlite', 'keithwhor/cmnd', 'kluivers/jbw-builders', 'TelerikAcademy/TelerikAcademyPlus', 'delight-im/OpenSoccer', 'lmammino/gulp-cozy', 'Nebulosus/shamir', 'daemon3000/InputManager', 'brindille/brindille-component', 'laxa1986/gulp-angular-embed-templates', 'krishkumar/BlockParty', 'hypriot/rpi-busybox-httpd', 'DMarby/Harpia', 'CESNET/owncloud-theme', 'sendgrid/python-http-client', 'ravl1084/TJ2PDF', 'richtr/plug.play.js', 'PixarAnimationStudios/jss-api-gem', 'qt-pods/qt-pods', 'analog-nico/passport-pinterest', 'kittens/lerna', 'mmerian/phpcrawl', 'spaar/besiege-modloader', 'derrickburns/generalized-kmeans-clustering', 'johnhamelink/exrm_deb', 'jforman/munin-graphite', 'rubylit/guevara', 'Flat/Konachan-for-Muzei', 'smklancher/ZeoSleepMonitor', 'Calinou/godot-snippets', 'jbboehr/php-mustache', 'johnpneumann/portable-maya-prefs', 'OfficeDev/Product-List-Code-Sample', 'chrisbarrett/emacs-refactor', 'pouetnet/pouet2.0', 'divmain/GitSavvy', 'kinduff/spree_reffiliate', 'velveteer/mithril-boilerplate', 'atom/node-ctags', 'bh107/bohrium', 'opinkerfi/adagios'], 'var_function-call-9694367017610863978': "SELECT repo_name, language_description FROM languages WHERE repo_name IN ('ninja-ide/ninja-ide', 'cwilso/midi-synth', 'ha/doozerd', 'devsoulwolf/ChatMessageView', 'google/traceur-compiler', 'jeffmo/jasmine-pit', 'radare/radeco', 'jcinnamond/el-presenti', 'durka/named-block', 'MaLeLabTs/RegexGenerator', 'blond/hash-set', 'uupaa/UserAgent.js', 'Magnetme/consultant', 'rafiuske/papergram', 'wahern/cqueues', 'Hexworks/hexameter', 'xxtea/xxtea-php', 'JSSolutions/meteor-google-prediction', 'JuliaDB/MySQL.jl', 'varlesh/elementary-add', 'blynkkk/blynk-server', 'sakaal/service_platform_ansible', '3ventic/DiscordServers', 'sskyy/redux-task', 'jeelabs/jet', 'Swader/diffbot-php-client', 'mluisbrown/Memories', 'lucaspouzac/contiperf', 'mattinove/SwiftySlider', 'polomoshnov/jQuery-UI-Resizable-Snap-extension', 'dfletcher/tsws', 'marcelklehr/gulf-contenteditable', 'F1ReKing/wheelview', 'pmwkaa/serenity', 'nodejs/node-gyp', 'Moq/moq', 'adafruit/Adafruit-Trinket-Gemma-Bootloader', 'aceway/findX', 'Blizzard/omniauth-bnet', 'rluders/phaser-skeleton', 'mozilla/oneanddone', 'dikiaap/mangan', 'CfABrigadePhiladelphia/jawn', 'hosom/bro-file-extraction', 'Maaphoo/Retr3d', 'andres-erbsen/dename', 'dblock/slack-google-bot', 'jconst/JCDialPad', 'chrisdone/hulk', 'winunet/Hui', 'adobe-type-tools/cmap-resources', 'crossroadlabs/homebrew-tap', 'NickolausDS/Unity-Free-Flight', 'OscarES/Differential-Algebra-Tracker', 'isychev93/Xamarin.Forms-Drag-and-drop-ListView', 'rdebath/Brainfuck', 'himanshu-soni/image-intent-handler', 'mstevenson/AssetsWatcher', 'j-bennet/wharfee', 'AcyOrt/acyort', 'rogpeppe/showdeps', 'AutoDo/AutoDo', 'JMPerez/beats-audio-api', 'inamiy/DebugLog', 'fdaciuk/ajax', 'jzitelli/poolvr', 'thedeibo/ServerLoveMCPE', 'guangzhuwu/p2engine', 'rusty1s/koa2-rest-api', 'DUBULEE/FileCacheUtil', 'VeliovGroup/Meteor-logger', 'claudijd/c7decrypt', 'alexchamberlain/piimg', 'SuperID/super-cache', 'PECE-project/pece-distro', 'paul999/433.92-Raspberry-Pi', 'jsonld-java/jsonld-java-tools', 'noveogroup/android-logger', 'nictuku/stardew-rocks', 'edomaru/codeigniter_multilevel_menu', 'shenxgan/xblog', 'LI-COR/eddypro-engine', 'zverok/magic_cloud', 'rita-marylin-raquel/softbloks', 'mojeda/ServerStatus', 'yuvirajsinh/YCameraView', 'firebase/EventSource-Examples', 'otoolep/gosf-rqlite', 'keithwhor/cmnd', 'kluivers/jbw-builders', 'TelerikAcademy/TelerikAcademyPlus', 'delight-im/OpenSoccer', 'lmammino/gulp-cozy', 'Nebulosus/shamir', 'daemon3000/InputManager', 'brindille/brindille-component', 'laxa1986/gulp-angular-embed-templates', 'krishkumar/BlockParty', 'hypriot/rpi-busybox-httpd', 'DMarby/Harpia', 'CESNET/owncloud-theme', 'sendgrid/python-http-client', 'ravl1084/TJ2PDF', 'richtr/plug.play.js', 'PixarAnimationStudios/jss-api-gem', 'qt-pods/qt-pods', 'analog-nico/passport-pinterest', 'kittens/lerna', 'mmerian/phpcrawl', 'spaar/besiege-modloader', 'derrickburns/generalized-kmeans-clustering', 'johnhamelink/exrm_deb', 'jforman/munin-graphite', 'rubylit/guevara', 'Flat/Konachan-for-Muzei', 'smklancher/ZeoSleepMonitor', 'Calinou/godot-snippets', 'jbboehr/php-mustache', 'johnpneumann/portable-maya-prefs', 'OfficeDev/Product-List-Code-Sample', 'chrisbarrett/emacs-refactor', 'pouetnet/pouet2.0', 'divmain/GitSavvy', 'kinduff/spree_reffiliate', 'velveteer/mithril-boilerplate', 'atom/node-ctags', 'bh107/bohrium', 'opinkerfi/adagios')", 'var_function-call-13312192613915097450': 'file_storage/function-call-13312192613915097450.json'}

exec(code, env_args)
