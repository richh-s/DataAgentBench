code = """import json, re, pandas as pd

# Load Swift non-binary rows (may be file path)
rows_src = var_call_WtVFUlpoI56rKjn2bDubgbDI
if isinstance(rows_src, str):
    with open(rows_src, 'r', encoding='utf-8') as f:
        rows = json.load(f)
else:
    rows = rows_src

df = pd.DataFrame(rows)
if df.empty:
    out = {"error": "No Swift files found in contents table."}
else:
    # Extract copy count from natural language description
    def extract_copies(s):
        if not isinstance(s, str):
            return None
        s_low = s.lower()
        m = re.search(r'(?:duplicat(?:ed|ion)|appear(?:ing|s)|repeated|copied)\s+([0-9]+)\s+times', s_low)
        if not m:
            # also handle 'cop(?:y|ies) ... copied 12 times' pattern: 'copied 12 times'
            m = re.search(r'cop(?:y|ies).*?([0-9]+)\s+times', s_low)
        return int(m.group(1)) if m else None

    df['copies'] = df['repo_data_description'].apply(extract_copies)
    df2 = df.dropna(subset=['copies']).copy()
    if df2.empty:
        out = {"error": "Could not extract copy counts from repo_data_description for Swift files."}
    else:
        # Ensure each file uniquely determined by id: group by id and take max copies; keep a sample repo_name
        agg = df2.groupby('id', as_index=False).agg(
            copies=('copies', 'max'),
            sample_repo_name=('sample_repo_name', 'first'),
            sample_path=('sample_path', 'first')
        )
        top = agg.sort_values(['copies', 'id'], ascending=[False, True]).head(1)
        rec = top.iloc[0].to_dict()
        out = {"repo_name": rec['sample_repo_name'], "file_id": rec['id'], "copies": int(rec['copies']), "sample_path": rec['sample_path']}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_bQcU0xBzFTAzUFhjKkAEttjq': [], 'var_call_R4vjWM3P1TKITMSg8Y0XClry': 'file_storage/call_R4vjWM3P1TKITMSg8Y0XClry.json', 'var_call_Zhv0dqU9UnmxJSfNWzLcivNk': [], 'var_call_WtVFUlpoI56rKjn2bDubgbDI': 'file_storage/call_WtVFUlpoI56rKjn2bDubgbDI.json', 'var_call_Pg7v3R567L5aH4kHg9Lljram': [{'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_repo_name': 'slavapestov/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'sample_repo_name': 'firebase/quickstart-ios', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.'}, {'id': '601d7b08677a1e95fcccea27fb1269c2110dc618', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.'}], 'var_call_nFyXdFS4JGrWTEWYzuup6EqX': [{'id': 'c4d6ced29fbff41f82c1e9ebd9d4e5fe0c4fd795', 'sample_repo_name': 'apple/swift', 'copies': 'None'}], 'var_call_jWUP0bcA2jMSBSrVC743aDg7': [{'id': 'c4d6ced29fbff41f82c1e9ebd9d4e5fe0c4fd795', 'sample_repo_name': 'apple/swift', 'copies_copied': 'None', 'copies_duplicated': 'None', 'copies_appearing': 'None'}], 'var_call_SB8UvJUP5zHl1H0YOuXDLSlC': [{'id': 'c4d6ced29fbff41f82c1e9ebd9d4e5fe0c4fd795', 'sample_repo_name': 'apple/swift', 'sample_path': 'test/Driver/Dependencies/bindings-build-record.swift', 'repo_data_description': 'It is a non-binary file of 3880 bytes, repeated 31 times in the dataset under mode 33188.'}], 'var_call_UUnkIow40X1hkQ8HIIExz5Pe': [{'id': 'b32abcab564f4e4e7d409d97ba8415e9a8e59484', 'sample_repo_name': 'slavapestov/swift', 'copies_repeated': 'None', 'copies_appearing': 'None', 'copies_duplicated': 'None', 'copies_copied': 'None', 'copies': '0'}], 'var_call_8PdhQCkqll5v2rHlH1uTNg1u': [], 'var_call_BY2UcGKwq8V9CPBhv8egf90j': [], 'var_call_AJcP1Wv9LTkiGvUIw2NSobBC': [], 'var_call_uw6MdJomOarpptO4BB0qkmAo': [{'n': '20'}], 'var_call_5wXvna92GHgZio0jw6bjGRgl': [], 'var_call_NlyqyXhsUBXt14KtcXhFyhHZ': [{'id': '3d42ac2c0fad831225f80a9355a196027e6ccc3e', 'repo_data_description': 'It is a non-binary file of 306 bytes, repeated 15 times in the dataset under mode 33188.', 'extracted': ''}, {'id': 'be6be234f9d404b0251c9a3626d644104cfe359b', 'repo_data_description': 'It is a non-binary file of 243 bytes, repeated 15 times in the dataset under mode 33188.', 'extracted': ''}, {'id': '155c8e9cb6a189697b32e35e929e2867aa8fac91', 'repo_data_description': 'It is a non-binary file of 241 bytes, repeated 20 times in the dataset under mode 33188.', 'extracted': ''}, {'id': 'aca574fc3ae413d3357a643241c27e95fb02a9e5', 'repo_data_description': 'It is a non-binary file of 481 bytes, repeated 21 times in the dataset under mode 33188.', 'extracted': ''}, {'id': 'c46ff203c0ab2432f4a283cb31c7912fd61467e5', 'repo_data_description': 'It is a non-binary file of 741 bytes, repeated 21 times in the dataset under mode 33188.', 'extracted': ''}], 'var_call_ajdlYFE8Z9YfLNsHJbNFWE28': [{'id': '3d42ac2c0fad831225f80a9355a196027e6ccc3e', 'repo_data_description': 'It is a non-binary file of 306 bytes, repeated 15 times in the dataset under mode 33188.', 'first_num': '306'}]}

exec(code, env_args)
