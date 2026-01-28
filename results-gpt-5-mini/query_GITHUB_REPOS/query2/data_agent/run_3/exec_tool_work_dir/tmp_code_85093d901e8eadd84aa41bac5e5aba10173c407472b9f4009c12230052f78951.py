code = """import json, re
# load the query_db result stored in a file path variable
path = var_call_zyBa8RDtW3ddvCAcDjzNMBIA
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

rows = []
for r in data:
    desc = r.get('desc') or r.get('repo_data_description') or ''
    copies = None
    m = re.search(r"(\d+)\s*(?:times|time)", desc)
    if m:
        copies = int(m.group(1))
    else:
        m2 = re.search(r"appearing\s+(\d+)", desc)
        if m2:
            copies = int(m2.group(1))
        else:
            m3 = re.search(r"copied\s+(\d+)", desc)
            if m3:
                copies = int(m3.group(1))
    if copies is None:
        try:
            copies = int(r.get('copies', 1))
        except:
            copies = 1
    rows.append({
        'id': r.get('id'),
        'copies': copies,
        'one_repo': r.get('one_repo'),
        'one_path': r.get('one_path'),
        'desc': desc
    })

# find max copies
max_copies = max([row['copies'] for row in rows]) if rows else 0
candidates = [row for row in rows if row['copies'] == max_copies]

result = {
    'max_copies': max_copies,
    'candidates': candidates
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DgKBRtyuyT8gBkxfcT5h90d7': [], 'var_call_ukBEzmhZOzEhJBvEFWPeSgmY': [{'id': 'c4d6ced29fbff41f82c1e9ebd9d4e5fe0c4fd795', 'copies': '1', 'one_repo': 'apple/swift', 'one_path': 'test/Driver/Dependencies/bindings-build-record.swift', 'desc': 'It is a non-binary file of 3880 bytes, repeated 31 times in the dataset under mode 33188.'}, {'id': '6a1a4b8c332c4d5fd3fd71b44b5268d5a21e68cd', 'copies': '1', 'one_repo': 'iOSDevLog/iOSDevLog', 'one_path': '211. StackView/211. StackView/ViewController.swift', 'desc': 'This file has a size of 511 bytes, is non-binary, and appears 1 times with sample mode 33188.'}, {'id': '1f63b3ceb821ef39296b65b13366ccb7c8e363b6', 'copies': '1', 'one_repo': 'jmfieldman/Cadmium', 'one_path': 'Examples/CadmiumBasicExample/CadmiumBasicExample/ViewController.swift', 'desc': 'Non-binary content file (8942 bytes) seen 1 times, using sample mode 33188.'}, {'id': '5217202d6d4290af2bebeb1ae7bff0ea62775b4c', 'copies': '1', 'one_repo': 'davedelong/DDMathParser', 'one_path': 'MathParser/IdentifierExtractor.swift', 'desc': 'A 1376-byte non-binary file appearing 5 times, with sample mode code 33188.'}, {'id': 'e103d83f307794fca0e989be5ba6df80da69f842', 'copies': '1', 'one_repo': 'braintree/braintree_ios', 'one_path': 'UnitTests/BTApplePay_Tests.swift', 'desc': 'A 8061-byte non-binary file appearing 5 times, with sample mode code 33188.'}, {'id': 'be6be234f9d404b0251c9a3626d644104cfe359b', 'copies': '1', 'one_repo': 'practicalswift/swift-compiler-crashes', 'one_path': 'crashes-duplicates/15704-no-stacktrace.swift', 'desc': 'It is a non-binary file of 243 bytes, repeated 15 times in the dataset under mode 33188.'}, {'id': '5fb353bfd251866214a3550d1f4bd33f2bc23333', 'copies': '1', 'one_repo': 'practicalswift/swift-compiler-crashes', 'one_path': 'crashes-duplicates/07164-swift-sourcemanager-getmessage.swift', 'desc': 'The dataset includes this non-binary file, 323 bytes in size and copied 15 times (mode: 33188).'}, {'id': '8e81b35a4cbd4c53a339cbc1dd30d7cf8f2f0eec', 'copies': '1', 'one_repo': 'PureSwift/Cacao', 'one_path': 'Sources/Cacao/ScrollView.swift', 'desc': 'It is a non-binary file of 224 bytes, repeated 1 times in the dataset under mode 33188.'}, {'id': 'e13df7e85e2071f29bbf6bef79323269e9e88bc6', 'copies': '1', 'one_repo': 'therealglazou/quaxe-for-swift', 'one_path': 'quaxe/core/protocols/pMutationObserver.swift', 'desc': 'This file has a size of 374 bytes, is non-binary, and appears 1 times with sample mode 33188.'}, {'id': '061e1b677455b609b3725754014caf28d5775d42', 'copies': '1', 'one_repo': 'onmyway133/Scale', 'one_path': 'Example/Scale/AppDelegate.swift', 'desc': 'With a file size of 2140 bytes and sample mode 33188, this non-binary file is duplicated 1 times.'}, {'id': '1c331b4ee6bf6d47575d1ba7be047a2f2a02c394', 'copies': '1', 'one_repo': 'IBM-MIL/IBM-Ready-App-for-Venue', 'one_path': 'iOS/Venue/Controllers/OnboardingContentViewController.swift', 'desc': 'A 1171-byte non-binary file appearing 1 times, with sample mode code 33188.'}, {'id': '0989d91c91a2ae2d15225e64b34ffbebe9b98db0', 'copies': '1', 'one_repo': 'rugheid/Swift-MathEagle', 'one_path': 'MathEagleTests/ComplexTests.swift', 'desc': 'This file has a size of 3924 bytes, is non-binary, and appears 1 times with sample mode 33188.'}, {'id': '1acc0c8e5a1ac7b18e587906b33b73e9d778a406', 'copies': '1', 'one_repo': 'Estimote/iOS-SDK', 'one_path': 'Examples/swift/Blank/Blank/ViewController.swift', 'desc': 'This file has a size of 402 bytes, is non-binary, and appears 2 times with sample mode 33188.'}, {'id': '0fe09241b77bd34943472f6cff76e71eeb03773a', 'copies': '1', 'one_repo': 'tinysun212/swift-windows', 'one_path': 'validation-test/compiler_crashers_fixed/26959-std-function-func-swift-type-subst.swift', 'desc': 'A 457-byte non-binary file appearing 23 times, with sample mode code 33188.'}, {'id': 'f2a35422a5bf04eba40c03e05adb0f15db319cf8', 'copies': '1', 'one_repo': 'gregttn/GTToast', 'one_path': 'Example/Tests/GTToastAnimationTests.swift', 'desc': 'The dataset includes this non-binary file, 7324 bytes in size and copied 1 times (mode: 33188).'}, {'id': 'c236a42435aa5e367f87077c802b0a77e8047faa', 'copies': '1', 'one_repo': 'kitasuke/TwitterClientDemo', 'one_path': 'TwitterClientDemo/Classes/Views/PostingView.swift', 'desc': 'Non-binary content file (2535 bytes) seen 1 times, using sample mode 33188.'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'copies': '1', 'one_repo': 'practicalswift/swift-compiler-crashes', 'one_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'desc': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': '3d42ac2c0fad831225f80a9355a196027e6ccc3e', 'copies': '1', 'one_repo': 'practicalswift/swift-compiler-crashes', 'one_path': 'fixed/00118-swift-dependentgenerictyperesolver-resolvegenerictypeparamtype.swift', 'desc': 'It is a non-binary file of 306 bytes, repeated 15 times in the dataset under mode 33188.'}, {'id': 'cc4de346f66613edef22d12b73c44fc2c8834acd', 'copies': '1', 'one_repo': 'practicalswift/swift-compiler-crashes', 'one_path': 'crashes-duplicates/02484-swift-sourcemanager-getmessage.swift', 'desc': 'With a file size of 226 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': 'c46ff203c0ab2432f4a283cb31c7912fd61467e5', 'copies': '1', 'one_repo': 'slavapestov/swift', 'one_path': 'validation-test/compiler_crashers_fixed/00363-swift-scopeinfo-addtoscope.swift', 'desc': 'It is a non-binary file of 741 bytes, repeated 21 times in the dataset under mode 33188.'}], 'var_call_zyBa8RDtW3ddvCAcDjzNMBIA': 'file_storage/call_zyBa8RDtW3ddvCAcDjzNMBIA.json'}

exec(code, env_args)
