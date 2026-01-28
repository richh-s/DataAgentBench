code = """import json
import re

# Read the contents data from file
contents_file = var_functions.query_db:22
with open(contents_file, 'r') as f:
    contents = json.load(f)

# Parse repo_data_description to extract copy counts
max_copies = 0
swift_files = []

for item in contents:
    # Check if it's a Swift file
    if not item['sample_path'].endswith('.swift'):
        continue
        
    desc = item['repo_data_description'].lower()
    
    # Skip binary files
    if 'binary' in desc:
        continue
        
    # Extract copy count
    copies_match = re.search(r'(?:copied|duplicated|appearing|repeated|seen) (\d+) times?', desc)
    if copies_match:
        copies = int(copies_match.group(1))
        if copies > max_copies:
            max_copies = copies
            swift_files = [item]
        elif copies == max_copies:
            swift_files.append(item)

print('__RESULT__:')
print(json.dumps({
    'max_copies': max_copies,
    'files': swift_files,
    'total_swift_files': len([item for item in contents if item['sample_path'].endswith('.swift')])
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:9': [{'repo_name': 'e-Sixt/Swen', 'language_description': 'This repository is mainly written in Swift (16,364 bytes), with additional code in Ruby (7,243 bytes), Shell (94 bytes).'}, {'repo_name': 'ApplauseOSS/Swifjection', 'language_description': 'The codebase includes: Swift (109,540 bytes), Ruby (3,068 bytes), Shell (762 bytes).'}, {'repo_name': 'vizifit/GenericPasswordRow', 'language_description': 'The codebase includes: Swift (18,238 bytes), Ruby (716 bytes), Shell (211 bytes).'}, {'repo_name': 'cxy921126/SoftSwift', 'language_description': 'The majority of the code is in Swift (1,723,695 bytes), followed by Shell (17,716 bytes), Ruby (297 bytes).'}, {'repo_name': 'cwwise/CWWeChat', 'language_description': 'While most of the project is built in Swift (585,714 bytes), it also incorporates Ruby (3,447 bytes), Shell (190 bytes).'}, {'repo_name': 'Apemb/Compass', 'language_description': 'The codebase includes: Swift (33,632 bytes), Shell (711 bytes), Ruby (434 bytes).'}, {'repo_name': 'toggl/superday', 'language_description': 'The majority of the code is in Swift (747,765 bytes), followed by Ruby (3,949 bytes), Shell (393 bytes).'}, {'repo_name': 'malcommac/SwiftDate', 'language_description': 'While most of the project is built in Swift (419,579 bytes), it also incorporates Ruby (767 bytes), Shell (169 bytes).'}, {'repo_name': 'chronotruck/CTKFlagPhoneNumber', 'language_description': 'While most of the project is built in Swift (87,439 bytes), it also incorporates Ruby (2,165 bytes), Shell (65 bytes).'}, {'repo_name': 'zendobk/SwiftUtils', 'language_description': 'While most of the project is built in Swift (71,711 bytes), it also incorporates Shell (3,156 bytes), Ruby (3,009 bytes).'}, {'repo_name': 'binarylevel/Riseset', 'language_description': 'The codebase includes: Swift (55,000 bytes), Ruby (533 bytes), Shell (193 bytes).'}, {'repo_name': 'Raizlabs/Anchorage', 'language_description': 'This repository is mainly written in Swift (99,834 bytes), with additional code in Ruby (6,219 bytes), Shell (5,846 bytes).'}, {'repo_name': 'mweibel/esrscan', 'language_description': 'While most of the project is built in Swift (46,819 bytes), it also incorporates Ruby (761 bytes), Shell (102 bytes).'}, {'repo_name': 'magmajo/nmagma-ios', 'language_description': 'The codebase includes: Swift (8,672 bytes), Ruby (6,468 bytes), Shell (1,308 bytes).'}, {'repo_name': 'elpassion/el-space-ios', 'language_description': 'While most of the project is built in Swift (366,580 bytes), it also incorporates Ruby (11,529 bytes), Shell (132 bytes).'}, {'repo_name': 'steveholt55/BLJGameButton', 'language_description': 'While most of the project is built in Swift (6,873 bytes), it also incorporates Ruby (577 bytes), Shell (28 bytes).'}, {'repo_name': 'truemetal/vapor-2-heroku-auth-template', 'language_description': 'This repository is mainly written in Swift (11,040 bytes), with additional code in Ruby (880 bytes), Shell (304 bytes).'}, {'repo_name': 'DenHeadless/DTCollectionViewManager', 'language_description': 'The codebase includes: Swift (264,900 bytes), Ruby (9,909 bytes), Shell (724 bytes).'}, {'repo_name': 'fizx/jane', 'language_description': 'The codebase includes: Swift (36,767 bytes), Ruby (6,457 bytes), Shell (1,823 bytes).'}, {'repo_name': 'ostatnicky/kancional-ios', 'language_description': 'While most of the project is built in Swift (147,485 bytes), it also incorporates Ruby (422 bytes), Shell (74 bytes).'}], 'var_functions.execute_python:12': ['e-Sixt/Swen', 'ApplauseOSS/Swifjection', 'vizifit/GenericPasswordRow', 'cxy921126/SoftSwift', 'Apemb/Compass', 'toggl/superday', 'binarylevel/Riseset', 'Raizlabs/Anchorage', 'magmajo/nmagma-ios', 'truemetal/vapor-2-heroku-auth-template', 'DenHeadless/DTCollectionViewManager', 'fizx/jane'], 'var_functions.query_db:14': [], 'var_functions.query_db:16': [{'sample_repo_name': 'practicalswift/swift-compiler-crashes'}, {'sample_repo_name': 'tapouillo/BMGlyphLabelSwift'}, {'sample_repo_name': 'larryhou/swift'}, {'sample_repo_name': 'domenicosolazzo/practice-swift'}, {'sample_repo_name': 'gscalzo/FlappySwift'}, {'sample_repo_name': 'iosdevzone/IDZSwiftCommonCrypto'}, {'sample_repo_name': 'mbalex99/FirebaseRxSwiftExtensions'}, {'sample_repo_name': 'nschum/SwiftHamcrest'}, {'sample_repo_name': 'richeterre/SwiftGoal'}, {'sample_repo_name': 'PureSwift/Cacao'}, {'sample_repo_name': 'swift-lang/swift-k'}, {'sample_repo_name': 'jubinjacob19/CustomCalendarSwift'}, {'sample_repo_name': 'onekiloparsec/SwiftAA'}, {'sample_repo_name': 'mattinove/SwiftySlider'}, {'sample_repo_name': 'Keyflow/CountryPicker-iOS-Swift'}, {'sample_repo_name': 'ktmswzw/FeelingClientBySwift'}, {'sample_repo_name': 'facebook/swift'}, {'sample_repo_name': 'groovelab/SwiftBBS'}, {'sample_repo_name': 'tinysun212/swift-windows'}, {'sample_repo_name': 'ReSwift/CounterExample-Navigation-TimeTravel'}, {'sample_repo_name': 'IQUII/swift-social-login'}, {'sample_repo_name': 'TheDarkCode/Example-Swift-Apps'}, {'sample_repo_name': 'SwiftGGTeam/SwiftGGAppServer'}, {'sample_repo_name': 'onmyway133/Github.swift'}, {'sample_repo_name': 'therealglazou/quaxe-for-swift'}, {'sample_repo_name': 'k0nserv/SwiftTracer'}, {'sample_repo_name': 'MakeZL/MLSwiftBasic'}, {'sample_repo_name': 'SwiftAndroid/swift'}, {'sample_repo_name': 'PureSwift/SwiftFoundation'}, {'sample_repo_name': 'rugheid/Swift-MathEagle'}, {'sample_repo_name': 'mitsuse/autocomplete-swift'}, {'sample_repo_name': 'cdtschange/SwiftMKit'}, {'sample_repo_name': 'apple/swift'}, {'sample_repo_name': 'ruipfcosta/SwiftyWalkthrough'}, {'sample_repo_name': 'yichizhang/JCTiledScrollView_Swift'}, {'sample_repo_name': 'xiaoguoai/ec-dev-swift'}, {'sample_repo_name': 'woooowen/Top4Swift'}, {'sample_repo_name': 'slavapestov/swift'}, {'sample_repo_name': 'delba/SwiftyOAuth'}, {'sample_repo_name': 'openstack/swift'}, {'sample_repo_name': 'apple/swift-corelibs-foundation'}, {'sample_repo_name': 'swift-nav/libswiftnav'}, {'sample_repo_name': 'getsentry/sentry-swift'}, {'sample_repo_name': 'ricardorauber/iOS-Swift'}, {'sample_repo_name': 'JigarM/Swift-Tutorials'}, {'sample_repo_name': 'vtfuture/SwiftClient'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
