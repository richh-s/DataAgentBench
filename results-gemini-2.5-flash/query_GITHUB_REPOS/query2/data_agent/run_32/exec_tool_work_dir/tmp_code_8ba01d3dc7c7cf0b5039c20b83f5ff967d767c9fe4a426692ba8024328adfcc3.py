code = """import pandas as pd
import re
import json

data = json.loads(open(locals()['var_function-call-14209067173377455140'], 'r').read())
df = pd.DataFrame(data)

def extract_copy_count(description):
    match = re.search(r'(?:repeated|copied|appearing) (\d+) times', description)
    if match:
        return int(match.group(1))
    return 0

df['copy_count'] = df['repo_data_description'].apply(extract_copy_count)

# Group by id to ensure unique files and get the maximum copy_count
df_unique_files = df.groupby('id').agg(
    copy_count=('copy_count', 'first'),
    sample_repo_name=('sample_repo_name', lambda x: x.mode()[0] if not x.empty else None)
).reset_index()

# Find the file with the maximum copy_count
most_copied_file = df_unique_files.loc[df_unique_files['copy_count'].idxmax()]

__RESULT__:
print(json.dumps({
    "most_copied_file_id": most_copied_file['id'],
    "most_copied_file_repo": most_copied_file['sample_repo_name'],
    "max_copy_count": most_copied_file['copy_count']
}))"""

env_args = {'var_function-call-6495011211737141236': [], 'var_function-call-6710146837806799287': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_repo_name': 'slavapestov/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'sample_repo_name': 'firebase/quickstart-ios', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift'}, {'id': '679da520fd8ee30c041d816b15d74b14ec42ba75', 'sample_repo_name': 'MakeZL/MLSwiftBasic', 'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift'}, {'id': '601d7b08677a1e95fcccea27fb1269c2110dc618', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift'}, {'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift'}], 'var_function-call-12955612545154498966': [{'repo_data_description': 'It is a non-binary file of 243 bytes, repeated 15 times in the dataset under mode 33188.'}, {'repo_data_description': 'Non-binary content file (398 bytes) seen 21 times, using sample mode 33188.'}, {'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'repo_data_description': 'A 221-byte non-binary file appearing 15 times, with sample mode code 33188.'}, {'repo_data_description': 'It is a non-binary file of 246 bytes, repeated 21 times in the dataset under mode 33188.'}, {'repo_data_description': 'It is a non-binary file of 708 bytes, repeated 38 times in the dataset under mode 33188.'}, {'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}, {'repo_data_description': 'It is a non-binary file of 306 bytes, repeated 15 times in the dataset under mode 33188.'}, {'repo_data_description': 'This file has a size of 241 bytes, is non-binary, and appears 15 times with sample mode 33188.'}, {'repo_data_description': 'It is a non-binary file of 241 bytes, repeated 20 times in the dataset under mode 33188.'}], 'var_function-call-13387491273367047128': [], 'var_function-call-13515316879534029874': [], 'var_function-call-4772778579266837054': [], 'var_function-call-14209067173377455140': 'file_storage/function-call-14209067173377455140.json'}

exec(code, env_args)
