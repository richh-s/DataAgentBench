code = """import json
import re

# Load all non-Python repositories
non_python_file = locals()['var_functions.query_db:26']
with open(non_python_file, 'r') as f:
    non_python_repos = json.load(f)

# Create a set for efficient lookup
non_python_repo_set = set(repo['repo_name'] for repo in non_python_repos)

# Load all README.md files (larger dataset)
readme_file = locals()['var_functions.query_db:40']
with open(readme_file, 'r') as f:
    readme_data = json.load(f)

# Filter README.md files to only those from non-Python repositories
non_python_readmes = []
for item in readme_data:
    repo_name = item['sample_repo_name']
    if repo_name in non_python_repo_set:
        non_python_readmes.append({
            'repo_name': repo_name,
            'content': item.get('content', '') or ''
        })

# Define copyright patterns - looking for actual copyright statements
copyright_patterns = [
    'copyright',
    '©',
    '(c)'
]

# Count READMEs with copyright information
copyright_count = 0
total_readmes = len(non_python_readmes)

copyright_examples = []

for readme in non_python_readmes:
    content = readme.get('content', '')
    content_lower = content.lower()
    has_copyright = False
    
    # Check for copyright patterns
    for pattern in copyright_patterns:
        if pattern == '©':
            if '©' in content:
                has_copyright = True
                break
        elif pattern in content_lower:
            has_copyright = True
            break
    
    if has_copyright:
        copyright_count += 1

result = {
    'total_non_python_readmes': total_readmes,
    'copyright_readmes': copyright_count,
    'proportion': round(copyright_count / total_readmes * 100, 1) if total_readmes > 0 else 0
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['languages', 'repos', 'licenses'], 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': [{'sample_repo_name': 'ninja-ide/ninja-ide'}, {'sample_repo_name': 'JuliaDB/MySQL.jl'}, {'sample_repo_name': '3ventic/DiscordServers'}, {'sample_repo_name': 'Maaphoo/Retr3d'}, {'sample_repo_name': 'inamiy/DebugLog'}, {'sample_repo_name': 'ravl1084/TJ2PDF'}, {'sample_repo_name': 'velveteer/mithril-boilerplate'}, {'sample_repo_name': 'jeffmo/jasmine-pit'}, {'sample_repo_name': 'marcelklehr/gulf-contenteditable'}, {'sample_repo_name': 'mozilla/oneanddone'}, {'sample_repo_name': 'CfABrigadePhiladelphia/jawn'}, {'sample_repo_name': 'guangzhuwu/p2engine'}, {'sample_repo_name': 'firebase/EventSource-Examples'}, {'sample_repo_name': 'hypriot/rpi-busybox-httpd'}, {'sample_repo_name': 'jforman/munin-graphite'}, {'sample_repo_name': 'johnpneumann/portable-maya-prefs'}, {'sample_repo_name': 'uupaa/UserAgent.js'}, {'sample_repo_name': 'rafiuske/papergram'}, {'sample_repo_name': 'sakaal/service_platform_ansible'}, {'sample_repo_name': 'rluders/phaser-skeleton'}, {'sample_repo_name': 'himanshu-soni/image-intent-handler'}, {'sample_repo_name': 'edomaru/codeigniter_multilevel_menu'}, {'sample_repo_name': 'keithwhor/cmnd'}, {'sample_repo_name': 'qt-pods/qt-pods'}, {'sample_repo_name': 'rubylit/guevara'}, {'sample_repo_name': 'jeelabs/jet'}, {'sample_repo_name': 'j-bennet/wharfee'}, {'sample_repo_name': 'jsonld-java/jsonld-java-tools'}, {'sample_repo_name': 'nictuku/stardew-rocks'}, {'sample_repo_name': 'lmammino/gulp-cozy'}, {'sample_repo_name': 'Flat/Konachan-for-Muzei'}, {'sample_repo_name': 'durka/named-block'}, {'sample_repo_name': 'blond/hash-set'}, {'sample_repo_name': 'wahern/cqueues'}, {'sample_repo_name': 'adobe-type-tools/cmap-resources'}, {'sample_repo_name': 'crossroadlabs/homebrew-tap'}, {'sample_repo_name': 'isychev93/Xamarin.Forms-Drag-and-drop-ListView'}, {'sample_repo_name': 'AutoDo/AutoDo'}, {'sample_repo_name': 'noveogroup/android-logger'}, {'sample_repo_name': 'zverok/magic_cloud'}, {'sample_repo_name': 'TelerikAcademy/TelerikAcademyPlus'}, {'sample_repo_name': 'ha/doozerd'}, {'sample_repo_name': 'Magnetme/consultant'}, {'sample_repo_name': 'blynkkk/blynk-server'}, {'sample_repo_name': 'polomoshnov/jQuery-UI-Resizable-Snap-extension'}, {'sample_repo_name': 'dikiaap/mangan'}, {'sample_repo_name': 'dblock/slack-google-bot'}, {'sample_repo_name': 'jzitelli/poolvr'}, {'sample_repo_name': 'rusty1s/koa2-rest-api'}, {'sample_repo_name': 'DUBULEE/FileCacheUtil'}, {'sample_repo_name': 'SuperID/super-cache'}, {'sample_repo_name': 'LI-COR/eddypro-engine'}, {'sample_repo_name': 'kluivers/jbw-builders'}, {'sample_repo_name': 'daemon3000/InputManager'}, {'sample_repo_name': 'Hexworks/hexameter'}, {'sample_repo_name': 'pmwkaa/serenity'}, {'sample_repo_name': 'Blizzard/omniauth-bnet'}, {'sample_repo_name': 'chrisdone/hulk'}, {'sample_repo_name': 'claudijd/c7decrypt'}, {'sample_repo_name': 'smklancher/ZeoSleepMonitor'}, {'sample_repo_name': 'mattinove/SwiftySlider'}, {'sample_repo_name': 'adafruit/Adafruit-Trinket-Gemma-Bootloader'}, {'sample_repo_name': 'winunet/Hui'}, {'sample_repo_name': 'NickolausDS/Unity-Free-Flight'}, {'sample_repo_name': 'paul999/433.92-Raspberry-Pi'}, {'sample_repo_name': 'cwilso/midi-synth'}, {'sample_repo_name': 'MaLeLabTs/RegexGenerator'}, {'sample_repo_name': 'mstevenson/AssetsWatcher'}, {'sample_repo_name': 'krishkumar/BlockParty'}, {'sample_repo_name': 'mmerian/phpcrawl'}, {'sample_repo_name': 'OfficeDev/Product-List-Code-Sample'}, {'sample_repo_name': 'chrisbarrett/emacs-refactor'}, {'sample_repo_name': 'jcinnamond/el-presenti'}, {'sample_repo_name': 'nodejs/node-gyp'}, {'sample_repo_name': 'rogpeppe/showdeps'}, {'sample_repo_name': 'DMarby/Harpia'}, {'sample_repo_name': 'derrickburns/generalized-kmeans-clustering'}, {'sample_repo_name': 'johnhamelink/exrm_deb'}, {'sample_repo_name': 'Calinou/godot-snippets'}, {'sample_repo_name': 'opinkerfi/adagios'}, {'sample_repo_name': 'devsoulwolf/ChatMessageView'}, {'sample_repo_name': 'dfletcher/tsws'}, {'sample_repo_name': 'andres-erbsen/dename'}, {'sample_repo_name': 'jconst/JCDialPad'}, {'sample_repo_name': 'yuvirajsinh/YCameraView'}, {'sample_repo_name': 'google/traceur-compiler'}, {'sample_repo_name': 'mluisbrown/Memories'}, {'sample_repo_name': 'lucaspouzac/contiperf'}, {'sample_repo_name': 'rdebath/Brainfuck'}, {'sample_repo_name': 'JMPerez/beats-audio-api'}, {'sample_repo_name': 'Nebulosus/shamir'}, {'sample_repo_name': 'brindille/brindille-component'}, {'sample_repo_name': 'sendgrid/python-http-client'}, {'sample_repo_name': 'richtr/plug.play.js'}, {'sample_repo_name': 'divmain/GitSavvy'}, {'sample_repo_name': 'JSSolutions/meteor-google-prediction'}, {'sample_repo_name': 'aceway/findX'}, {'sample_repo_name': 'VeliovGroup/Meteor-logger'}, {'sample_repo_name': 'PECE-project/pece-distro'}, {'sample_repo_name': 'kinduff/spree_reffiliate'}, {'sample_repo_name': 'varlesh/elementary-add'}, {'sample_repo_name': 'sskyy/redux-task'}, {'sample_repo_name': 'F1ReKing/wheelview'}, {'sample_repo_name': 'hosom/bro-file-extraction'}, {'sample_repo_name': 'thedeibo/ServerLoveMCPE'}, {'sample_repo_name': 'alexchamberlain/piimg'}, {'sample_repo_name': 'shenxgan/xblog'}, {'sample_repo_name': 'CESNET/owncloud-theme'}, {'sample_repo_name': 'PixarAnimationStudios/jss-api-gem'}, {'sample_repo_name': 'kittens/lerna'}, {'sample_repo_name': 'spaar/besiege-modloader'}, {'sample_repo_name': 'jbboehr/php-mustache'}, {'sample_repo_name': 'atom/node-ctags'}, {'sample_repo_name': 'radare/radeco'}, {'sample_repo_name': 'Moq/moq'}, {'sample_repo_name': 'mojeda/ServerStatus'}, {'sample_repo_name': 'otoolep/gosf-rqlite'}, {'sample_repo_name': 'laxa1986/gulp-angular-embed-templates'}, {'sample_repo_name': 'analog-nico/passport-pinterest'}, {'sample_repo_name': 'bh107/bohrium'}, {'sample_repo_name': 'xxtea/xxtea-php'}, {'sample_repo_name': 'Swader/diffbot-php-client'}, {'sample_repo_name': 'OscarES/Differential-Algebra-Tracker'}, {'sample_repo_name': 'AcyOrt/acyort'}, {'sample_repo_name': 'fdaciuk/ajax'}, {'sample_repo_name': 'rita-marylin-raquel/softbloks'}, {'sample_repo_name': 'delight-im/OpenSoccer'}, {'sample_repo_name': 'pouetnet/pouet2.0'}], 'var_functions.query_db:22': [{'total': '2774729'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:32': 2774729, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'total_non_python_readmes': 101, 'sample_repos': ['cwilso/midi-synth', 'ha/doozerd', 'devsoulwolf/ChatMessageView', 'google/traceur-compiler', 'jeffmo/jasmine-pit']}, 'var_functions.execute_python:38': {'total_non_python_readmes': 101, 'copyright_readmes': 17, 'proportion': 0.16831683168316833}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'message': 'Found 101 README files from non-Python repositories'}}

exec(code, env_args)
