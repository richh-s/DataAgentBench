code = """import json, re, pandas as pd
from pathlib import Path

# Load full README contents
path = Path(var_call_fgizS0kPckG18BszD6l8gysV)
readmes = json.loads(path.read_text())

langs = pd.DataFrame(var_call_LNOGOnNHIY96o47tpgQ3wykk)
readme_repos = pd.DataFrame(var_call_M0pFMOGQdJBtloO9VXyvipsB)

# Normalize columns
langs['repo_name'] = langs['repo_name'].str.strip()
readme_repos['sample_repo_name'] = readme_repos['sample_repo_name'].str.strip()

# Determine which repos use Python (language_description contains 'Python(' or 'Python ' case-insensitive)
python_mask = langs['language_description'].str.contains(r'Python', case=True, na=False)
python_repos = set(langs.loc[python_mask, 'repo_name'])

# Repos with README.md
repos_with_readme = set(readme_repos['sample_repo_name'])

# Repos with README that do NOT use Python
non_python_repos = sorted(repos_with_readme - python_repos)

# Build DataFrame of README contents for those repos
readmes_df = pd.DataFrame(readmes)
readmes_df['sample_repo_name'] = readmes_df['sample_repo_name'].str.strip()

non_py_readmes = readmes_df[readmes_df['sample_repo_name'].isin(non_python_repos)].copy()

# Heuristic for copyright: look for word 'copyright' or symbol '©' (case-insensitive)
pattern = re.compile(r'copyright|\u00a9|\(c\)', re.IGNORECASE)

non_py_readmes['has_copyright'] = non_py_readmes['content'].fillna('').apply(lambda t: bool(pattern.search(t)))

# Some repos might have multiple README entries; aggregate per repo (any = True if any file contains it)
agg = non_py_readmes.groupby('sample_repo_name')['has_copyright'].any().reset_index()

total = int(len(agg))
with_c = int(agg['has_copyright'].sum())
prop = with_c / total if total else None

result = {
  'total_non_python_repos_with_readme': total,
  'repos_with_copyright': with_c,
  'proportion': prop
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_fgizS0kPckG18BszD6l8gysV': 'file_storage/call_fgizS0kPckG18BszD6l8gysV.json', 'var_call_LNOGOnNHIY96o47tpgQ3wykk': 'file_storage/call_LNOGOnNHIY96o47tpgQ3wykk.json', 'var_call_M0pFMOGQdJBtloO9VXyvipsB': [{'sample_repo_name': 'JSSolutions/meteor-google-prediction'}, {'sample_repo_name': 'aceway/findX'}, {'sample_repo_name': 'VeliovGroup/Meteor-logger'}, {'sample_repo_name': 'PECE-project/pece-distro'}, {'sample_repo_name': 'kinduff/spree_reffiliate'}, {'sample_repo_name': 'varlesh/elementary-add'}, {'sample_repo_name': 'sskyy/redux-task'}, {'sample_repo_name': 'F1ReKing/wheelview'}, {'sample_repo_name': 'hosom/bro-file-extraction'}, {'sample_repo_name': 'thedeibo/ServerLoveMCPE'}, {'sample_repo_name': 'alexchamberlain/piimg'}, {'sample_repo_name': 'shenxgan/xblog'}, {'sample_repo_name': 'CESNET/owncloud-theme'}, {'sample_repo_name': 'PixarAnimationStudios/jss-api-gem'}, {'sample_repo_name': 'kittens/lerna'}, {'sample_repo_name': 'spaar/besiege-modloader'}, {'sample_repo_name': 'jbboehr/php-mustache'}, {'sample_repo_name': 'atom/node-ctags'}, {'sample_repo_name': 'ninja-ide/ninja-ide'}, {'sample_repo_name': 'JuliaDB/MySQL.jl'}, {'sample_repo_name': '3ventic/DiscordServers'}, {'sample_repo_name': 'Maaphoo/Retr3d'}, {'sample_repo_name': 'inamiy/DebugLog'}, {'sample_repo_name': 'ravl1084/TJ2PDF'}, {'sample_repo_name': 'velveteer/mithril-boilerplate'}, {'sample_repo_name': 'Hexworks/hexameter'}, {'sample_repo_name': 'pmwkaa/serenity'}, {'sample_repo_name': 'Blizzard/omniauth-bnet'}, {'sample_repo_name': 'chrisdone/hulk'}, {'sample_repo_name': 'claudijd/c7decrypt'}, {'sample_repo_name': 'smklancher/ZeoSleepMonitor'}, {'sample_repo_name': 'jeffmo/jasmine-pit'}, {'sample_repo_name': 'marcelklehr/gulf-contenteditable'}, {'sample_repo_name': 'mozilla/oneanddone'}, {'sample_repo_name': 'CfABrigadePhiladelphia/jawn'}, {'sample_repo_name': 'guangzhuwu/p2engine'}, {'sample_repo_name': 'firebase/EventSource-Examples'}, {'sample_repo_name': 'hypriot/rpi-busybox-httpd'}, {'sample_repo_name': 'jforman/munin-graphite'}, {'sample_repo_name': 'johnpneumann/portable-maya-prefs'}, {'sample_repo_name': 'uupaa/UserAgent.js'}, {'sample_repo_name': 'rafiuske/papergram'}, {'sample_repo_name': 'sakaal/service_platform_ansible'}, {'sample_repo_name': 'rluders/phaser-skeleton'}, {'sample_repo_name': 'himanshu-soni/image-intent-handler'}, {'sample_repo_name': 'edomaru/codeigniter_multilevel_menu'}, {'sample_repo_name': 'keithwhor/cmnd'}, {'sample_repo_name': 'qt-pods/qt-pods'}, {'sample_repo_name': 'rubylit/guevara'}, {'sample_repo_name': 'mattinove/SwiftySlider'}, {'sample_repo_name': 'adafruit/Adafruit-Trinket-Gemma-Bootloader'}, {'sample_repo_name': 'winunet/Hui'}, {'sample_repo_name': 'NickolausDS/Unity-Free-Flight'}, {'sample_repo_name': 'paul999/433.92-Raspberry-Pi'}, {'sample_repo_name': 'jeelabs/jet'}, {'sample_repo_name': 'j-bennet/wharfee'}, {'sample_repo_name': 'jsonld-java/jsonld-java-tools'}, {'sample_repo_name': 'nictuku/stardew-rocks'}, {'sample_repo_name': 'lmammino/gulp-cozy'}, {'sample_repo_name': 'Flat/Konachan-for-Muzei'}, {'sample_repo_name': 'jcinnamond/el-presenti'}, {'sample_repo_name': 'nodejs/node-gyp'}, {'sample_repo_name': 'rogpeppe/showdeps'}, {'sample_repo_name': 'jaredwilli/devtools-cheatsheet'}, {'sample_repo_name': 'DMarby/Harpia'}, {'sample_repo_name': 'derrickburns/generalized-kmeans-clustering'}, {'sample_repo_name': 'johnhamelink/exrm_deb'}, {'sample_repo_name': 'Calinou/godot-snippets'}, {'sample_repo_name': 'opinkerfi/adagios'}, {'sample_repo_name': 'durka/named-block'}, {'sample_repo_name': 'blond/hash-set'}, {'sample_repo_name': 'wahern/cqueues'}, {'sample_repo_name': 'adobe-type-tools/cmap-resources'}, {'sample_repo_name': 'crossroadlabs/homebrew-tap'}, {'sample_repo_name': 'isychev93/Xamarin.Forms-Drag-and-drop-ListView'}, {'sample_repo_name': 'AutoDo/AutoDo'}, {'sample_repo_name': 'noveogroup/android-logger'}, {'sample_repo_name': 'zverok/magic_cloud'}, {'sample_repo_name': 'TelerikAcademy/TelerikAcademyPlus'}, {'sample_repo_name': 'radare/radeco'}, {'sample_repo_name': 'Moq/moq'}, {'sample_repo_name': 'mojeda/ServerStatus'}, {'sample_repo_name': 'otoolep/gosf-rqlite'}, {'sample_repo_name': 'laxa1986/gulp-angular-embed-templates'}, {'sample_repo_name': 'analog-nico/passport-pinterest'}, {'sample_repo_name': 'bh107/bohrium'}, {'sample_repo_name': 'cwilso/midi-synth'}, {'sample_repo_name': 'MaLeLabTs/RegexGenerator'}, {'sample_repo_name': 'mstevenson/AssetsWatcher'}, {'sample_repo_name': 'krishkumar/BlockParty'}, {'sample_repo_name': 'mmerian/phpcrawl'}, {'sample_repo_name': 'OfficeDev/Product-List-Code-Sample'}, {'sample_repo_name': 'chrisbarrett/emacs-refactor'}, {'sample_repo_name': 'ha/doozerd'}, {'sample_repo_name': 'Magnetme/consultant'}, {'sample_repo_name': 'blynkkk/blynk-server'}, {'sample_repo_name': 'polomoshnov/jQuery-UI-Resizable-Snap-extension'}, {'sample_repo_name': 'dikiaap/mangan'}, {'sample_repo_name': 'dblock/slack-google-bot'}, {'sample_repo_name': 'jzitelli/poolvr'}, {'sample_repo_name': 'rusty1s/koa2-rest-api'}, {'sample_repo_name': 'DUBULEE/FileCacheUtil'}, {'sample_repo_name': 'SuperID/super-cache'}, {'sample_repo_name': 'LI-COR/eddypro-engine'}, {'sample_repo_name': 'kluivers/jbw-builders'}, {'sample_repo_name': 'daemon3000/InputManager'}, {'sample_repo_name': 'xxtea/xxtea-php'}, {'sample_repo_name': 'Swader/diffbot-php-client'}, {'sample_repo_name': 'OscarES/Differential-Algebra-Tracker'}, {'sample_repo_name': 'AcyOrt/acyort'}, {'sample_repo_name': 'tt-acm/Spectacles.WebViewer'}, {'sample_repo_name': 'fdaciuk/ajax'}, {'sample_repo_name': 'rita-marylin-raquel/softbloks'}, {'sample_repo_name': 'delight-im/OpenSoccer'}, {'sample_repo_name': 'parro-it/is-fqdn'}, {'sample_repo_name': 'pouetnet/pouet2.0'}, {'sample_repo_name': 'dineshTrivedi/angularjs-styleguide'}, {'sample_repo_name': 'google/traceur-compiler'}, {'sample_repo_name': 'mluisbrown/Memories'}, {'sample_repo_name': 'lucaspouzac/contiperf'}, {'sample_repo_name': 'rdebath/Brainfuck'}, {'sample_repo_name': 'JMPerez/beats-audio-api'}, {'sample_repo_name': 'Ali-Razmjoo/OWASP-ZSC'}, {'sample_repo_name': 'Nebulosus/shamir'}, {'sample_repo_name': 'brindille/brindille-component'}, {'sample_repo_name': 'sendgrid/python-http-client'}, {'sample_repo_name': 'richtr/plug.play.js'}, {'sample_repo_name': 'divmain/GitSavvy'}, {'sample_repo_name': 'devsoulwolf/ChatMessageView'}, {'sample_repo_name': 'dfletcher/tsws'}, {'sample_repo_name': 'andres-erbsen/dename'}, {'sample_repo_name': 'jconst/JCDialPad'}, {'sample_repo_name': 'yuvirajsinh/YCameraView'}]}

exec(code, env_args)
