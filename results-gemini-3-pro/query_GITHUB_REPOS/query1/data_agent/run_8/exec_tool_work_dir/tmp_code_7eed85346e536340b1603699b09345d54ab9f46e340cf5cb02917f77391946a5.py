code = """import json

# Load contents
contents_path = locals()['var_function-call-618062251630152001']
with open(contents_path, 'r') as f:
    contents_data = json.load(f)

# Load languages
languages_path = locals()['var_function-call-12261709950828954567']
with open(languages_path, 'r') as f:
    languages_data = json.load(f)

# Create a map for languages
# Normalize repo names just in case, though they should match
lang_map = {item['repo_name']: item['language_description'] for item in languages_data}

non_python_repos_count = 0
copyright_in_readme_count = 0

for item in contents_data:
    repo = item['sample_repo_name']
    content = item.get('content', '')
    
    # Check if repo is in lang_map
    if repo not in lang_map:
        # If we don't have language info, we might skip or assume no Python.
        # Given we queried for these repos, they should be there.
        # But if missing, I'll exclude to be safe, or print to debug.
        continue
        
    lang_desc = lang_map[repo]
    
    # Check if uses Python
    # "Python" could be part of a word? unlikely in this context.
    # The string format is "The codebase includes: Ruby..., Python..."
    # or "This repository is mainly written in Python..."
    # So simple substring check is likely sufficient.
    uses_python = 'python' in lang_desc.lower()
    
    if not uses_python:
        non_python_repos_count += 1
        if 'copyright' in content.lower():
            copyright_in_readme_count += 1

proportion = 0
if non_python_repos_count > 0:
    proportion = copyright_in_readme_count / non_python_repos_count

print("__RESULT__:")
print(json.dumps({
    "non_python_repos_count": non_python_repos_count,
    "copyright_in_readme_count": copyright_in_readme_count,
    "proportion": proportion
}))"""

env_args = {'var_function-call-635540268662005592': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_function-call-12586103944774157143': [{'count_star()': '128'}], 'var_function-call-2629973700177860370': [{'count(*)': '400000'}], 'var_function-call-12517068520592709827': [{'count_star()': '1059'}], 'var_function-call-7390425068396862096': [{'count_star()': '133'}], 'var_function-call-618062251630152001': 'file_storage/function-call-618062251630152001.json', 'var_function-call-11796946363227963827': ['ninja-ide/ninja-ide', 'cwilso/midi-synth', 'ha/doozerd', 'devsoulwolf/ChatMessageView', 'google/traceur-compiler', 'jeffmo/jasmine-pit', 'radare/radeco', 'jcinnamond/el-presenti', 'durka/named-block', 'MaLeLabTs/RegexGenerator', 'blond/hash-set', 'uupaa/UserAgent.js', 'Magnetme/consultant', 'rafiuske/papergram', 'wahern/cqueues', 'Hexworks/hexameter', 'xxtea/xxtea-php', 'JSSolutions/meteor-google-prediction', 'JuliaDB/MySQL.jl', 'varlesh/elementary-add', 'blynkkk/blynk-server', 'sakaal/service_platform_ansible', '3ventic/DiscordServers', 'sskyy/redux-task', 'jeelabs/jet', 'Swader/diffbot-php-client', 'mluisbrown/Memories', 'lucaspouzac/contiperf', 'mattinove/SwiftySlider', 'polomoshnov/jQuery-UI-Resizable-Snap-extension', 'dfletcher/tsws', 'marcelklehr/gulf-contenteditable', 'F1ReKing/wheelview', 'pmwkaa/serenity', 'nodejs/node-gyp', 'Moq/moq', 'adafruit/Adafruit-Trinket-Gemma-Bootloader', 'aceway/findX', 'Blizzard/omniauth-bnet', 'rluders/phaser-skeleton', 'mozilla/oneanddone', 'dikiaap/mangan', 'CfABrigadePhiladelphia/jawn', 'hosom/bro-file-extraction', 'Maaphoo/Retr3d', 'andres-erbsen/dename', 'dblock/slack-google-bot', 'jconst/JCDialPad', 'chrisdone/hulk', 'winunet/Hui', 'adobe-type-tools/cmap-resources', 'crossroadlabs/homebrew-tap', 'NickolausDS/Unity-Free-Flight', 'OscarES/Differential-Algebra-Tracker', 'isychev93/Xamarin.Forms-Drag-and-drop-ListView', 'rdebath/Brainfuck', 'himanshu-soni/image-intent-handler', 'mstevenson/AssetsWatcher', 'j-bennet/wharfee', 'AcyOrt/acyort', 'rogpeppe/showdeps', 'AutoDo/AutoDo', 'JMPerez/beats-audio-api', 'tt-acm/Spectacles.WebViewer', 'inamiy/DebugLog', 'fdaciuk/ajax', 'jzitelli/poolvr', 'thedeibo/ServerLoveMCPE', 'guangzhuwu/p2engine', 'rusty1s/koa2-rest-api', 'DUBULEE/FileCacheUtil', 'VeliovGroup/Meteor-logger', 'claudijd/c7decrypt', 'alexchamberlain/piimg', 'SuperID/super-cache', 'PECE-project/pece-distro', 'paul999/433.92-Raspberry-Pi', 'jsonld-java/jsonld-java-tools', 'noveogroup/android-logger', 'nictuku/stardew-rocks', 'edomaru/codeigniter_multilevel_menu', 'shenxgan/xblog', 'LI-COR/eddypro-engine', 'zverok/magic_cloud', 'Ali-Razmjoo/OWASP-ZSC', 'rita-marylin-raquel/softbloks', 'mojeda/ServerStatus', 'yuvirajsinh/YCameraView', 'firebase/EventSource-Examples', 'otoolep/gosf-rqlite', 'keithwhor/cmnd', 'kluivers/jbw-builders', 'TelerikAcademy/TelerikAcademyPlus', 'delight-im/OpenSoccer', 'lmammino/gulp-cozy', 'Nebulosus/shamir', 'jaredwilli/devtools-cheatsheet', 'daemon3000/InputManager', 'brindille/brindille-component', 'laxa1986/gulp-angular-embed-templates', 'krishkumar/BlockParty', 'hypriot/rpi-busybox-httpd', 'DMarby/Harpia', 'CESNET/owncloud-theme', 'sendgrid/python-http-client', 'ravl1084/TJ2PDF', 'richtr/plug.play.js', 'PixarAnimationStudios/jss-api-gem', 'qt-pods/qt-pods', 'analog-nico/passport-pinterest', 'kittens/lerna', 'mmerian/phpcrawl', 'parro-it/is-fqdn', 'spaar/besiege-modloader', 'derrickburns/generalized-kmeans-clustering', 'johnhamelink/exrm_deb', 'jforman/munin-graphite', 'rubylit/guevara', 'Flat/Konachan-for-Muzei', 'smklancher/ZeoSleepMonitor', 'Calinou/godot-snippets', 'jbboehr/php-mustache', 'johnpneumann/portable-maya-prefs', 'OfficeDev/Product-List-Code-Sample', 'chrisbarrett/emacs-refactor', 'pouetnet/pouet2.0', 'divmain/GitSavvy', 'kinduff/spree_reffiliate', 'velveteer/mithril-boilerplate', 'atom/node-ctags', 'bh107/bohrium', 'opinkerfi/adagios', 'dineshTrivedi/angularjs-styleguide'], 'var_function-call-13690932329695390107': "SELECT repo_name, language_description FROM languages WHERE repo_name IN ('ninja-ide/ninja-ide', 'cwilso/midi-synth', 'ha/doozerd', 'devsoulwolf/ChatMessageView', 'google/traceur-compiler', 'jeffmo/jasmine-pit', 'radare/radeco', 'jcinnamond/el-presenti', 'durka/named-block', 'MaLeLabTs/RegexGenerator', 'blond/hash-set', 'uupaa/UserAgent.js', 'Magnetme/consultant', 'rafiuske/papergram', 'wahern/cqueues', 'Hexworks/hexameter', 'xxtea/xxtea-php', 'JSSolutions/meteor-google-prediction', 'JuliaDB/MySQL.jl', 'varlesh/elementary-add', 'blynkkk/blynk-server', 'sakaal/service_platform_ansible', '3ventic/DiscordServers', 'sskyy/redux-task', 'jeelabs/jet', 'Swader/diffbot-php-client', 'mluisbrown/Memories', 'lucaspouzac/contiperf', 'mattinove/SwiftySlider', 'polomoshnov/jQuery-UI-Resizable-Snap-extension', 'dfletcher/tsws', 'marcelklehr/gulf-contenteditable', 'F1ReKing/wheelview', 'pmwkaa/serenity', 'nodejs/node-gyp', 'Moq/moq', 'adafruit/Adafruit-Trinket-Gemma-Bootloader', 'aceway/findX', 'Blizzard/omniauth-bnet', 'rluders/phaser-skeleton', 'mozilla/oneanddone', 'dikiaap/mangan', 'CfABrigadePhiladelphia/jawn', 'hosom/bro-file-extraction', 'Maaphoo/Retr3d', 'andres-erbsen/dename', 'dblock/slack-google-bot', 'jconst/JCDialPad', 'chrisdone/hulk', 'winunet/Hui', 'adobe-type-tools/cmap-resources', 'crossroadlabs/homebrew-tap', 'NickolausDS/Unity-Free-Flight', 'OscarES/Differential-Algebra-Tracker', 'isychev93/Xamarin.Forms-Drag-and-drop-ListView', 'rdebath/Brainfuck', 'himanshu-soni/image-intent-handler', 'mstevenson/AssetsWatcher', 'j-bennet/wharfee', 'AcyOrt/acyort', 'rogpeppe/showdeps', 'AutoDo/AutoDo', 'JMPerez/beats-audio-api', 'tt-acm/Spectacles.WebViewer', 'inamiy/DebugLog', 'fdaciuk/ajax', 'jzitelli/poolvr', 'thedeibo/ServerLoveMCPE', 'guangzhuwu/p2engine', 'rusty1s/koa2-rest-api', 'DUBULEE/FileCacheUtil', 'VeliovGroup/Meteor-logger', 'claudijd/c7decrypt', 'alexchamberlain/piimg', 'SuperID/super-cache', 'PECE-project/pece-distro', 'paul999/433.92-Raspberry-Pi', 'jsonld-java/jsonld-java-tools', 'noveogroup/android-logger', 'nictuku/stardew-rocks', 'edomaru/codeigniter_multilevel_menu', 'shenxgan/xblog', 'LI-COR/eddypro-engine', 'zverok/magic_cloud', 'Ali-Razmjoo/OWASP-ZSC', 'rita-marylin-raquel/softbloks', 'mojeda/ServerStatus', 'yuvirajsinh/YCameraView', 'firebase/EventSource-Examples', 'otoolep/gosf-rqlite', 'keithwhor/cmnd', 'kluivers/jbw-builders', 'TelerikAcademy/TelerikAcademyPlus', 'delight-im/OpenSoccer', 'lmammino/gulp-cozy', 'Nebulosus/shamir', 'jaredwilli/devtools-cheatsheet', 'daemon3000/InputManager', 'brindille/brindille-component', 'laxa1986/gulp-angular-embed-templates', 'krishkumar/BlockParty', 'hypriot/rpi-busybox-httpd', 'DMarby/Harpia', 'CESNET/owncloud-theme', 'sendgrid/python-http-client', 'ravl1084/TJ2PDF', 'richtr/plug.play.js', 'PixarAnimationStudios/jss-api-gem', 'qt-pods/qt-pods', 'analog-nico/passport-pinterest', 'kittens/lerna', 'mmerian/phpcrawl', 'parro-it/is-fqdn', 'spaar/besiege-modloader', 'derrickburns/generalized-kmeans-clustering', 'johnhamelink/exrm_deb', 'jforman/munin-graphite', 'rubylit/guevara', 'Flat/Konachan-for-Muzei', 'smklancher/ZeoSleepMonitor', 'Calinou/godot-snippets', 'jbboehr/php-mustache', 'johnpneumann/portable-maya-prefs', 'OfficeDev/Product-List-Code-Sample', 'chrisbarrett/emacs-refactor', 'pouetnet/pouet2.0', 'divmain/GitSavvy', 'kinduff/spree_reffiliate', 'velveteer/mithril-boilerplate', 'atom/node-ctags', 'bh107/bohrium', 'opinkerfi/adagios', 'dineshTrivedi/angularjs-styleguide')", 'var_function-call-12261709950828954567': 'file_storage/function-call-12261709950828954567.json'}

exec(code, env_args)
