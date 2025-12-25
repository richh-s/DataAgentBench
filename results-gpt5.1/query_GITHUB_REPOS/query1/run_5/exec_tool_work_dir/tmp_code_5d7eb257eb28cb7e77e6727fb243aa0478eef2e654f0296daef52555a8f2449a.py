code = """import json, re, pandas as pd

# Load large readmes result from file
readmes_file = var_call_F7wq9aGnWgPJngW1U9fUGm5u
with open(readmes_file, 'r') as f:
    readmes = json.load(f)

# Languages result is directly a list of dicts
langs = pd.DataFrame(var_call_QiYpCqEc5SQhEYwX5twq5IWJ)
readmes_df = pd.DataFrame(readmes)

# Flag repos that mention Python in their language description
langs['has_python'] = langs['language_description'].str.contains('Python', case=False, na=False)

# Repos that do NOT use Python
non_py_repos = langs.loc[~langs['has_python'], 'repo_name'].unique()

# README.md files for non-Python repos
readmes_non_py = readmes_df[readmes_df['repo_name'].isin(non_py_repos)].copy()

# Detect copyright in README content (case-insensitive)
pattern = re.compile('copyright', re.IGNORECASE)
readmes_non_py['has_copyright'] = readmes_non_py['content'].fillna('').apply(lambda x: bool(pattern.search(x)))

if len(readmes_non_py) == 0:
    proportion = None
else:
    proportion = float(readmes_non_py['has_copyright'].mean())

result = {
    'total_non_python_readmes': int(len(readmes_non_py)),
    'proportion_with_copyright': proportion
}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_F7wq9aGnWgPJngW1U9fUGm5u': 'file_storage/call_F7wq9aGnWgPJngW1U9fUGm5u.json', 'var_call_QiYpCqEc5SQhEYwX5twq5IWJ': 'file_storage/call_QiYpCqEc5SQhEYwX5twq5IWJ.json', 'var_call_nfFeJgYJAtKGCnDujK1nduWw': [{'repo_name': 'varlesh/elementary-add'}, {'repo_name': 'sskyy/redux-task'}, {'repo_name': 'F1ReKing/wheelview'}, {'repo_name': 'hosom/bro-file-extraction'}, {'repo_name': 'thedeibo/ServerLoveMCPE'}, {'repo_name': 'alexchamberlain/piimg'}, {'repo_name': 'shenxgan/xblog'}, {'repo_name': 'CESNET/owncloud-theme'}, {'repo_name': 'PixarAnimationStudios/jss-api-gem'}, {'repo_name': 'kittens/lerna'}, {'repo_name': 'spaar/besiege-modloader'}, {'repo_name': 'jbboehr/php-mustache'}, {'repo_name': 'atom/node-ctags'}, {'repo_name': 'JSSolutions/meteor-google-prediction'}, {'repo_name': 'aceway/findX'}, {'repo_name': 'VeliovGroup/Meteor-logger'}, {'repo_name': 'PECE-project/pece-distro'}, {'repo_name': 'kinduff/spree_reffiliate'}, {'repo_name': 'ninja-ide/ninja-ide'}, {'repo_name': 'JuliaDB/MySQL.jl'}, {'repo_name': '3ventic/DiscordServers'}, {'repo_name': 'Maaphoo/Retr3d'}, {'repo_name': 'inamiy/DebugLog'}, {'repo_name': 'ravl1084/TJ2PDF'}, {'repo_name': 'velveteer/mithril-boilerplate'}, {'repo_name': 'jeffmo/jasmine-pit'}, {'repo_name': 'marcelklehr/gulf-contenteditable'}, {'repo_name': 'mozilla/oneanddone'}, {'repo_name': 'CfABrigadePhiladelphia/jawn'}, {'repo_name': 'guangzhuwu/p2engine'}, {'repo_name': 'firebase/EventSource-Examples'}, {'repo_name': 'hypriot/rpi-busybox-httpd'}, {'repo_name': 'jforman/munin-graphite'}, {'repo_name': 'johnpneumann/portable-maya-prefs'}, {'repo_name': 'mattinove/SwiftySlider'}, {'repo_name': 'adafruit/Adafruit-Trinket-Gemma-Bootloader'}, {'repo_name': 'winunet/Hui'}, {'repo_name': 'NickolausDS/Unity-Free-Flight'}, {'repo_name': 'paul999/433.92-Raspberry-Pi'}, {'repo_name': 'Hexworks/hexameter'}, {'repo_name': 'pmwkaa/serenity'}, {'repo_name': 'Blizzard/omniauth-bnet'}, {'repo_name': 'chrisdone/hulk'}, {'repo_name': 'claudijd/c7decrypt'}, {'repo_name': 'smklancher/ZeoSleepMonitor'}, {'repo_name': 'durka/named-block'}, {'repo_name': 'blond/hash-set'}, {'repo_name': 'wahern/cqueues'}, {'repo_name': 'adobe-type-tools/cmap-resources'}, {'repo_name': 'crossroadlabs/homebrew-tap'}, {'repo_name': 'isychev93/Xamarin.Forms-Drag-and-drop-ListView'}, {'repo_name': 'AutoDo/AutoDo'}, {'repo_name': 'noveogroup/android-logger'}, {'repo_name': 'zverok/magic_cloud'}, {'repo_name': 'TelerikAcademy/TelerikAcademyPlus'}, {'repo_name': 'ha/doozerd'}, {'repo_name': 'Magnetme/consultant'}, {'repo_name': 'blynkkk/blynk-server'}, {'repo_name': 'polomoshnov/jQuery-UI-Resizable-Snap-extension'}, {'repo_name': 'dikiaap/mangan'}, {'repo_name': 'dblock/slack-google-bot'}, {'repo_name': 'jzitelli/poolvr'}, {'repo_name': 'rusty1s/koa2-rest-api'}, {'repo_name': 'DUBULEE/FileCacheUtil'}, {'repo_name': 'SuperID/super-cache'}, {'repo_name': 'LI-COR/eddypro-engine'}, {'repo_name': 'kluivers/jbw-builders'}, {'repo_name': 'daemon3000/InputManager'}, {'repo_name': 'radare/radeco'}, {'repo_name': 'Moq/moq'}, {'repo_name': 'mojeda/ServerStatus'}, {'repo_name': 'otoolep/gosf-rqlite'}, {'repo_name': 'laxa1986/gulp-angular-embed-templates'}, {'repo_name': 'analog-nico/passport-pinterest'}, {'repo_name': 'bh107/bohrium'}, {'repo_name': 'jcinnamond/el-presenti'}, {'repo_name': 'nodejs/node-gyp'}, {'repo_name': 'rogpeppe/showdeps'}, {'repo_name': 'jaredwilli/devtools-cheatsheet'}, {'repo_name': 'DMarby/Harpia'}, {'repo_name': 'derrickburns/generalized-kmeans-clustering'}, {'repo_name': 'johnhamelink/exrm_deb'}, {'repo_name': 'Calinou/godot-snippets'}, {'repo_name': 'opinkerfi/adagios'}, {'repo_name': 'google/traceur-compiler'}, {'repo_name': 'mluisbrown/Memories'}, {'repo_name': 'lucaspouzac/contiperf'}, {'repo_name': 'rdebath/Brainfuck'}, {'repo_name': 'JMPerez/beats-audio-api'}, {'repo_name': 'Ali-Razmjoo/OWASP-ZSC'}, {'repo_name': 'Nebulosus/shamir'}, {'repo_name': 'brindille/brindille-component'}, {'repo_name': 'sendgrid/python-http-client'}, {'repo_name': 'richtr/plug.play.js'}, {'repo_name': 'divmain/GitSavvy'}, {'repo_name': 'devsoulwolf/ChatMessageView'}, {'repo_name': 'dfletcher/tsws'}, {'repo_name': 'andres-erbsen/dename'}, {'repo_name': 'jconst/JCDialPad'}, {'repo_name': 'yuvirajsinh/YCameraView'}, {'repo_name': 'xxtea/xxtea-php'}, {'repo_name': 'Swader/diffbot-php-client'}, {'repo_name': 'OscarES/Differential-Algebra-Tracker'}, {'repo_name': 'AcyOrt/acyort'}, {'repo_name': 'tt-acm/Spectacles.WebViewer'}, {'repo_name': 'fdaciuk/ajax'}, {'repo_name': 'rita-marylin-raquel/softbloks'}, {'repo_name': 'delight-im/OpenSoccer'}, {'repo_name': 'parro-it/is-fqdn'}, {'repo_name': 'pouetnet/pouet2.0'}, {'repo_name': 'dineshTrivedi/angularjs-styleguide'}, {'repo_name': 'jeelabs/jet'}, {'repo_name': 'j-bennet/wharfee'}, {'repo_name': 'jsonld-java/jsonld-java-tools'}, {'repo_name': 'nictuku/stardew-rocks'}, {'repo_name': 'lmammino/gulp-cozy'}, {'repo_name': 'Flat/Konachan-for-Muzei'}, {'repo_name': 'cwilso/midi-synth'}, {'repo_name': 'MaLeLabTs/RegexGenerator'}, {'repo_name': 'mstevenson/AssetsWatcher'}, {'repo_name': 'krishkumar/BlockParty'}, {'repo_name': 'mmerian/phpcrawl'}, {'repo_name': 'OfficeDev/Product-List-Code-Sample'}, {'repo_name': 'chrisbarrett/emacs-refactor'}, {'repo_name': 'uupaa/UserAgent.js'}, {'repo_name': 'rafiuske/papergram'}, {'repo_name': 'sakaal/service_platform_ansible'}, {'repo_name': 'rluders/phaser-skeleton'}, {'repo_name': 'himanshu-soni/image-intent-handler'}, {'repo_name': 'edomaru/codeigniter_multilevel_menu'}, {'repo_name': 'keithwhor/cmnd'}, {'repo_name': 'qt-pods/qt-pods'}, {'repo_name': 'rubylit/guevara'}]}

exec(code, env_args)
