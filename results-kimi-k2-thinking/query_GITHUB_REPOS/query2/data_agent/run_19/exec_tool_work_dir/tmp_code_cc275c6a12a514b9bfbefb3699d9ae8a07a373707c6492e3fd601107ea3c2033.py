code = """import json
import re

# Get the query result
data = locals()['var_functions.query_db:10']

# Debug: check what we got
print('Data type:', type(data))
print('Data length:', len(data))

# Process the data
swift_files = []
for row in data:
    desc = row['repo_data_description']
    # Check if it's binary first
    if 'binary' not in desc.lower():
        # Extract copy count using regex
        patterns = [
            r'seen (\d+) times',
            r'appearing (\d+) times', 
            r'repeated (\d+) times',
            r'duplicated (\d+) times',
            r'copied (\d+) times'
        ]
        
        copies = 0
        for pattern in patterns:
            match = re.search(pattern, desc, re.IGNORECASE)
            if match:
                copies = int(match.group(1))
                break
        
        if copies > 0:
            swift_files.append({
                'repo': row['sample_repo_name'],
                'path': row['sample_path'],
                'copies': copies
            })

# Find max copies
if swift_files:
    max_copies = max(f['copies'] for f in swift_files)
    top_files = [f for f in swift_files if f['copies'] == max_copies]
    
    result = {
        'max_copies': max_copies,
        'top_repos': list(set(f['repo'] for f in top_files)),
        'files': top_files
    }
    print('__RESULT__:')
    print(json.dumps(result, indent=2))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No suitable Swift files found in query results', 'sample': data[:2] if data else 'no data'}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': [{'repo_name': 'e-Sixt/Swen', 'language_description': 'This repository is mainly written in Swift (16,364 bytes), with additional code in Ruby (7,243 bytes), Shell (94 bytes).'}, {'repo_name': 'ApplauseOSS/Swifjection', 'language_description': 'The codebase includes: Swift (109,540 bytes), Ruby (3,068 bytes), Shell (762 bytes).'}, {'repo_name': 'vizifit/GenericPasswordRow', 'language_description': 'The codebase includes: Swift (18,238 bytes), Ruby (716 bytes), Shell (211 bytes).'}, {'repo_name': 'cxy921126/SoftSwift', 'language_description': 'The majority of the code is in Swift (1,723,695 bytes), followed by Shell (17,716 bytes), Ruby (297 bytes).'}, {'repo_name': 'cwwise/CWWeChat', 'language_description': 'While most of the project is built in Swift (585,714 bytes), it also incorporates Ruby (3,447 bytes), Shell (190 bytes).'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'device/nfc/nfc.mojom', 'repo_data_description': 'Non-binary content file (1455 bytes) seen 8 times, using sample mode 33188.'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc', 'repo_data_description': 'Non-binary content file (2743 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_repo_name': 'unfiltered/unfiltered', 'sample_path': 'json4s/src/main/ls/0.6.5.json', 'repo_data_description': 'Non-binary content file (636 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'e8b52ec203d330ee3fbf0403a4dbe4383d14b450', 'sample_repo_name': 'apache/derby', 'sample_path': 'java/engine/org/apache/derby/iapi/store/access/BinaryOrderable.java', 'repo_data_description': 'Non-binary content file (3675 bytes) seen 8 times, using sample mode 33188.'}, {'id': '26992250b2176770379cd6c7ba84ed51ce422090', 'sample_repo_name': 'perl6/nqp', 'sample_path': '3rdparty/dyncall/doc/manual/dyncall_logo.svg', 'repo_data_description': 'Non-binary content file (21851 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'da48d7c48ca7f6c4c734487af0f288a1bb9926a2', 'sample_repo_name': 'tpaviot/oce', 'sample_path': 'src/TKXSDRAW/PACKAGES', 'repo_data_description': 'Non-binary content file (43 bytes) seen 8 times, using sample mode 33188.'}, {'id': '6c6c181ae1ef4dc8d4d28e37195ca655423fc491', 'sample_repo_name': 'neeker/chromium_extract', 'sample_path': 'src/ui/display/BUILD.gn', 'repo_data_description': 'Non-binary content file (5213 bytes) seen 8 times, using sample mode 33188.'}, {'id': '67667768c0a3f7c53f81d539958ed74ef5ad6cf2', 'sample_repo_name': 'shapeshed/nodejsbook.io.examples', 'sample_path': 'hour08/example10/views/tasks/index.jade', 'repo_data_description': 'Non-binary content file (823 bytes) seen 8 times, using sample mode 33188.'}, {'id': 'a4dbfefc7a0c6008ee7214acd91afa7dcddf5a22', 'sample_repo_name': 'dyne/Tomb', 'sample_path': 'extras/gtk-tray/tomb-gtk-tray.c', 'repo_data_description': 'Non-binary content file (10764 bytes) seen 8 times, using sample mode 33188.'}, {'id': '7091eb08215c8441809949d82fe58c77c7982479', 'sample_repo_name': 'Netflix/astyanax', 'sample_path': 'astyanax-core/src/main/java/com/netflix/astyanax/connectionpool/exceptions/InterruptedOperationException.java', 'repo_data_description': 'Non-binary content file (1262 bytes) seen 8 times, using sample mode 33188.'}], 'var_functions.query_db:10': [{'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'sample_repo_name': 'slavapestov/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}, {'sample_repo_name': 'danielgindi/ios-charts', 'sample_path': 'ChartsRealm/ThirdParty/Realm/ios/RealmSwift.framework/Modules/RealmSwift.swiftmodule/i386.swiftdoc', 'repo_data_description': 'It is a binary file of 108480 bytes, repeated 11 times in the dataset under mode 33188.'}, {'sample_repo_name': 'firebase/quickstart-ios', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.'}, {'sample_repo_name': 'MakeZL/MLSwiftBasic', 'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).'}, {'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.'}, {'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 219 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'repo_data_description': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'fixed/01682-swift-parser-parsedecl.swift', 'repo_data_description': 'The dataset includes this non-binary file, 211 bytes in size and copied 15 times (mode: 33188).'}, {'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/15025-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'A 221-byte non-binary file appearing 15 times, with sample mode code 33188.'}, {'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/18368-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'The dataset includes this non-binary file, 226 bytes in size and copied 15 times (mode: 33188).'}, {'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'fixed/01847-std-function-func-swift-type-subst.swift', 'repo_data_description': 'Non-binary content file (215 bytes) seen 15 times, using sample mode 33188.'}, {'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/08505-swift-typechecker-conformstoprotocol.swift', 'repo_data_description': 'With a file size of 247 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'fixed/00118-swift-dependentgenerictyperesolver-resolvegenerictypeparamtype.swift', 'repo_data_description': 'It is a non-binary file of 306 bytes, repeated 15 times in the dataset under mode 33188.'}, {'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift', 'repo_data_description': 'This file has a size of 273 bytes, is non-binary, and appears 15 times with sample mode 33188.'}, {'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/15704-no-stacktrace.swift', 'repo_data_description': 'It is a non-binary file of 243 bytes, repeated 15 times in the dataset under mode 33188.'}, {'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/04574-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'This file has a size of 241 bytes, is non-binary, and appears 15 times with sample mode 33188.'}], 'var_functions.execute_python:12': {'error': 'No Swift files found'}}

exec(code, env_args)
