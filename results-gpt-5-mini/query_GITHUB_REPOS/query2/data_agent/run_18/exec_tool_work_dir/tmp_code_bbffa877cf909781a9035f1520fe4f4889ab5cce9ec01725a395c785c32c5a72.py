code = """import json
import pandas as pd
# load the previous query result stored in var_call_sZenICO4E4IHGObLvFFxOpHW (list of records)
var = var_call_sZenICO4E4IHGObLvFFxOpHW
# var is a file path since it's large; check type
if isinstance(var, str):
    # it's a path to json
    data = pd.read_json(var)
else:
    data = pd.DataFrame(var)

# Extract numeric copies from repo_data_description using regex
import re

def extract_copies(text):
    if not isinstance(text, str):
        return None
    # search for patterns like 'copied 12 times', 'appearing 15 times', 'repeated 15 times', 'copied 12 times (mode: 33188)'
    m = re.search(r'(?:copied|appearing|appears|repeated|duplicated|seen)\s+(\d+)\s+times', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    m2 = re.search(r'\b(\d+)\s+times\b', text, flags=re.IGNORECASE)
    if m2:
        return int(m2.group(1))
    m3 = re.search(r'copied\s+(\d+)', text, flags=re.IGNORECASE)
    if m3:
        return int(m3.group(1))
    m4 = re.search(r'appearing\s+(\d+)', text, flags=re.IGNORECASE)
    if m4:
        return int(m4.group(1))
    m5 = re.search(r'repeated\s+(\d+)', text, flags=re.IGNORECASE)
    if m5:
        return int(m5.group(1))
    m6 = re.search(r'\b(\d+)\b', text)
    if m6:
        # fallback: first number
        return int(m6.group(1))
    return None

if 'repo_data_description' not in data.columns:
    # try to load from another key
    print('__RESULT__:')
    print(json.dumps([]))
else:
    data['copies'] = data['repo_data_description'].apply(extract_copies)
    # filter only swift paths
    df = data[data['sample_path'].str.lower().str.endswith('.swift')]
    # drop duplicates by id to ensure unique files by id
    df_unique = df.drop_duplicates(subset=['id'])
    # find max copies
    max_copies = df_unique['copies'].max()
    top = df_unique[df_unique['copies']==max_copies]
    # prepare result records
    result = top[['id','copies','sample_repo_name','sample_path','repo_data_description']].to_dict(orient='records')
    print('__RESULT__:')
    print(json.dumps(result))"""

env_args = {'var_call_NAF0Q4P3l0oFzW5uJ4mufyQO': ['commits', 'contents', 'files'], 'var_call_lkN8Jb97B8Rku4AGOnhBo4ka': 'file_storage/call_lkN8Jb97B8Rku4AGOnhBo4ka.json', 'var_call_0oJl2RYQu6T7m9Sn1GZVHLPW': [], 'var_call_KSzc74CklU5PR2GBkF00KSvh': 'file_storage/call_KSzc74CklU5PR2GBkF00KSvh.json', 'var_call_QMZvl54ZAtBnLq9odjtpaaWA': [], 'var_call_tBO13K4tq278CjT5J9K1wjrY': 'file_storage/call_tBO13K4tq278CjT5J9K1wjrY.json', 'var_call_HtyutJnySFAXylAec3N0j2SU': [{'id': 'c4d6ced29fbff41f82c1e9ebd9d4e5fe0c4fd795', 'copies': '1', 'example_repo': 'apple/swift', 'example_path': 'test/Driver/Dependencies/bindings-build-record.swift'}], 'var_call_AhWHlxbrikJMVF6ViWt0jdJX': [{'id': 'b32abcab564f4e4e7d409d97ba8415e9a8e59484', 'occurrences': '1', 'example_repo': 'slavapestov/swift', 'example_path': 'validation-test/compiler_crashers_fixed/00602-swift-modulefile-gettype.swift'}, {'id': '1ff86af65537e2973b533c27044763ffefd0347d', 'occurrences': '1', 'example_repo': 'slavapestov/swift', 'example_path': 'stdlib/public/SDK/Darwin/MachError.swift'}, {'id': 'ec6d2f9ee3d4ad887abe7e7d488c5287388c9f8b', 'occurrences': '1', 'example_repo': 'lucasmpaim/EasyRest', 'example_path': 'Pod/Classes/API/APIBuilder.swift'}, {'id': '729e22ed109bea5edb4bfb6cef1fe4cf5204e564', 'occurrences': '1', 'example_repo': 'alex-alex/ASAttributedLabelNode', 'example_path': 'ASAttributedLabelNode-Demo/ASAttributedLabelNode-Demo/GameScene.swift'}, {'id': '839b819b98b2b6a934d91229bf9d8d2f565b7855', 'occurrences': '1', 'example_repo': 'RayTao/CoreAnimation_Collection', 'example_path': 'CoreAnimation_Collection/Animations/SwitcherCollection/SwitchersCollectionViewController.swift'}, {'id': '2e2fe40cd35ab655dbb492b20fb7ae8aaea3e7df', 'occurrences': '1', 'example_repo': 'boundsj/ObjectiveDDP', 'example_path': 'Example/swiftExample/swiftddp/AddViewController.swift'}, {'id': '88a9c3190ebcf15a4343642aa4767359c4517a10', 'occurrences': '1', 'example_repo': 'tristanhimmelman/HidingNavigationBar', 'example_path': 'HidingNavigationBar/HidingViewController.swift'}, {'id': 'a452f93131f16c5ea7978582b8253046d6a36f63', 'occurrences': '1', 'example_repo': 'apple/swift-corelibs-foundation', 'example_path': 'TestFoundation/TestNSByteCountFormatter.swift'}, {'id': '6488a8d4c15e8c5af390dc4ae272a9bb6e55a1e8', 'occurrences': '1', 'example_repo': 'czechboy0/Redbird', 'example_path': 'Tests/Redbird/StringTests.swift'}, {'id': 'c4d6ced29fbff41f82c1e9ebd9d4e5fe0c4fd795', 'occurrences': '1', 'example_repo': 'apple/swift', 'example_path': 'test/Driver/Dependencies/bindings-build-record.swift'}], 'var_call_sZenICO4E4IHGObLvFFxOpHW': 'file_storage/call_sZenICO4E4IHGObLvFFxOpHW.json'}

exec(code, env_args)
