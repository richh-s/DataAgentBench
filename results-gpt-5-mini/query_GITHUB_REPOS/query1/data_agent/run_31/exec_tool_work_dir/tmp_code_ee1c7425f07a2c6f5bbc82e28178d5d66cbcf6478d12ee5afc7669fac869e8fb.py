code = """import json, os
# Load non-Python repo list from previous step var_call_EIqlZdmwFYSTOJlsAQbUJcfR
data1 = var_call_EIqlZdmwFYSTOJlsAQbUJcfR
if isinstance(data1, str) and os.path.exists(data1):
    with open(data1, 'r') as f:
        nonpython_repos = json.load(f)
else:
    # try to parse if it's a JSON string
    try:
        nonpython_repos = json.loads(data1)
    except Exception:
        nonpython_repos = data1
# Load README mapping from var_call_lnd4DRaPvPckt9eONJUdX29o
data2 = var_call_lnd4DRaPvPckt9eONJUdX29o
# data2 may be a dict already or a JSON string
if isinstance(data2, str) and os.path.exists(data2):
    with open(data2, 'r') as f:
        readme_map = json.load(f)
else:
    try:
        readme_map = json.loads(data2)
    except Exception:
        readme_map = data2
# Normalize types
if isinstance(nonpython_repos, dict):
    # if mistakenly a dict with key 'repo_names'
    nonpython_list = nonpython_repos.get('repo_names', [])
else:
    nonpython_list = list(nonpython_repos)
nonpython_set = set(nonpython_list)
# readme_map expected to have keys 'repo_names' and 'has_copyright'
repo_names = readme_map.get('repo_names', [])
has_copy = readme_map.get('has_copyright', [])
readme_dict = {repo_names[i]: bool(has_copy[i]) for i in range(min(len(repo_names), len(has_copy)))}
# Intersection: repos that are non-python and have a README observed
intersect_repos = sorted([r for r in nonpython_set if r in readme_dict])
total_nonpython_with_readme = len(intersect_repos)
count_with_copyright = sum(1 for r in intersect_repos if readme_dict.get(r))
proportion = None
if total_nonpython_with_readme > 0:
    proportion = count_with_copyright / total_nonpython_with_readme
# Also provide totals
result = {
    'total_nonpython_repos_in_metadata_query': len(nonpython_list),
    'nonpython_repos_with_readme_found': total_nonpython_with_readme,
    'readmes_with_copyright_count': count_with_copyright,
    'proportion': proportion
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_o9nNR0lnbP7iyPnxPMBkLHgN': 'file_storage/call_o9nNR0lnbP7iyPnxPMBkLHgN.json', 'var_call_EIqlZdmwFYSTOJlsAQbUJcfR': 'file_storage/call_EIqlZdmwFYSTOJlsAQbUJcfR.json', 'var_call_ifdhidu4Chp0AVBiJhSHILEk': 'file_storage/call_ifdhidu4Chp0AVBiJhSHILEk.json', 'var_call_lnd4DRaPvPckt9eONJUdX29o': {'repo_names': ['3ventic/DiscordServers', 'AcyOrt/acyort', 'Ali-Razmjoo/OWASP-ZSC', 'AutoDo/AutoDo', 'Blizzard/omniauth-bnet', 'CESNET/owncloud-theme', 'Calinou/godot-snippets', 'CfABrigadePhiladelphia/jawn', 'DMarby/Harpia', 'DUBULEE/FileCacheUtil', 'F1ReKing/wheelview', 'Flat/Konachan-for-Muzei', 'Hexworks/hexameter', 'JMPerez/beats-audio-api', 'JSSolutions/meteor-google-prediction', 'JuliaDB/MySQL.jl', 'LI-COR/eddypro-engine', 'MaLeLabTs/RegexGenerator', 'Maaphoo/Retr3d', 'Magnetme/consultant', 'Moq/moq', 'Nebulosus/shamir', 'NickolausDS/Unity-Free-Flight', 'OfficeDev/Product-List-Code-Sample', 'OscarES/Differential-Algebra-Tracker', 'PECE-project/pece-distro', 'PixarAnimationStudios/jss-api-gem', 'SuperID/super-cache', 'Swader/diffbot-php-client', 'TelerikAcademy/TelerikAcademyPlus', 'VeliovGroup/Meteor-logger', 'aceway/findX', 'adafruit/Adafruit-Trinket-Gemma-Bootloader', 'adobe-type-tools/cmap-resources', 'alexchamberlain/piimg', 'analog-nico/passport-pinterest', 'andres-erbsen/dename', 'atom/node-ctags', 'bh107/bohrium', 'blond/hash-set', 'blynkkk/blynk-server', 'brindille/brindille-component', 'chrisbarrett/emacs-refactor', 'chrisdone/hulk', 'claudijd/c7decrypt', 'crossroadlabs/homebrew-tap', 'cwilso/midi-synth', 'daemon3000/InputManager', 'dblock/slack-google-bot', 'delight-im/OpenSoccer', 'derrickburns/generalized-kmeans-clustering', 'devsoulwolf/ChatMessageView', 'dfletcher/tsws', 'dikiaap/mangan', 'dineshTrivedi/angularjs-styleguide', 'divmain/GitSavvy', 'durka/named-block', 'edomaru/codeigniter_multilevel_menu', 'fdaciuk/ajax', 'firebase/EventSource-Examples', 'google/traceur-compiler', 'guangzhuwu/p2engine', 'ha/doozerd', 'himanshu-soni/image-intent-handler', 'hosom/bro-file-extraction', 'hypriot/rpi-busybox-httpd', 'inamiy/DebugLog', 'isychev93/Xamarin.Forms-Drag-and-drop-ListView', 'j-bennet/wharfee', 'jaredwilli/devtools-cheatsheet', 'jbboehr/php-mustache', 'jcinnamond/el-presenti', 'jconst/JCDialPad', 'jeelabs/jet', 'jeffmo/jasmine-pit', 'jforman/munin-graphite', 'johnhamelink/exrm_deb', 'johnpneumann/portable-maya-prefs', 'jsonld-java/jsonld-java-tools', 'jzitelli/poolvr', 'keithwhor/cmnd', 'kinduff/spree_reffiliate', 'kittens/lerna', 'kluivers/jbw-builders', 'krishkumar/BlockParty', 'laxa1986/gulp-angular-embed-templates', 'lede-project/source', 'lmammino/gulp-cozy', 'lucaspouzac/contiperf', 'marcelklehr/gulf-contenteditable', 'mattinove/SwiftySlider', 'mluisbrown/Memories', 'mmerian/phpcrawl', 'mojeda/ServerStatus', 'mozilla/oneanddone', 'mstevenson/AssetsWatcher', 'nictuku/stardew-rocks', 'ninja-ide/ninja-ide', 'nodejs/node-gyp', 'noveogroup/android-logger', 'opinkerfi/adagios', 'otoolep/gosf-rqlite', 'parro-it/is-fqdn', 'paul999/433.92-Raspberry-Pi', 'pmwkaa/serenity', 'polomoshnov/jQuery-UI-Resizable-Snap-extension', 'pouetnet/pouet2.0', 'qt-pods/qt-pods', 'radare/radeco', 'rafiuske/papergram', 'ravl1084/TJ2PDF', 'rdebath/Brainfuck', 'richtr/plug.play.js', 'rita-marylin-raquel/softbloks', 'rluders/phaser-skeleton', 'rogpeppe/showdeps', 'rubylit/guevara', 'rusty1s/koa2-rest-api', 'sakaal/service_platform_ansible', 'sendgrid/python-http-client', 'shenxgan/xblog', 'smklancher/ZeoSleepMonitor', 'spaar/besiege-modloader', 'sskyy/redux-task', 'strukturag/spreed-webrtc', 'thedeibo/ServerLoveMCPE', 'tt-acm/Spectacles.WebViewer', 'uupaa/UserAgent.js', 'varlesh/elementary-add', 'velveteer/mithril-boilerplate', 'wahern/cqueues', 'winunet/Hui', 'xxtea/xxtea-php', 'yuvirajsinh/YCameraView', 'zverok/magic_cloud'], 'has_copyright': [False, False, False, False, False, False, True, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, True, False, False, True, False, False, False, False, False, False, False, False, True, True, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}}

exec(code, env_args)
