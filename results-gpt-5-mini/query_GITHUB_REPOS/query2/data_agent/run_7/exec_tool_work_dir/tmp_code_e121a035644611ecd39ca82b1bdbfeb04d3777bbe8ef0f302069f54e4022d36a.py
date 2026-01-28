code = """import json
# prepare final answer: repository containing the most frequently copied non-binary Swift file
res = {
  'repo': 'uacaps/PageMenu',
  'file_id': '6f4cdb70f044b0486a24a07403600cb964a02672',
  'sample_path': 'Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift',
  'copies': 38,
  'language_description': 'Swift (56,461 bytes), Objective-C (51,756 bytes), Ruby (5,999 bytes)'
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_DUErrSokKG3PRG7zSrtA4aZx': ['commits', 'contents', 'files'], 'var_call_wgsnNNA88jyFHDqGdEdot5YK': 'file_storage/call_wgsnNNA88jyFHDqGdEdot5YK.json', 'var_call_wfzn5aaNjjl6eYUGYmiAm2Dv': [{'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift', 'repo_data_description': 'This file has a size of 273 bytes, is non-binary, and appears 15 times with sample mode 33188.', 'copies': '1'}, {'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'sample_repo_name': 'SwiftAndroid/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27485-swift-bracestmt-create.swift', 'repo_data_description': 'It is a non-binary file of 470 bytes, repeated 23 times in the dataset under mode 33188.', 'copies': '1'}], 'var_call_P2oQ09PSYSmlUSWnq7Nus4oZ': [{'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copies': '1'}, {'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'copies': '1'}], 'var_call_8EFg3SPTsa3djfRUFd7pBspe': ['languages', 'repos', 'licenses'], 'var_call_84LWxVyzvxtL3YOdDNOTrJPF': [{'repo_name': 'SwiftAndroid/swift', 'language_description': 'The majority of the code is in C++ (18,941,219 bytes), followed by Swift (12,538,936 bytes), Python (382,672 bytes), CMake (245,437 bytes), Objective-C (183,862 bytes), Objective-C++ (154,889 bytes), Shell (130,393 bytes), LLVM (49,912 bytes), C (47,409 bytes), Emacs Lisp (34,021 bytes), VimL (11,829 bytes), Perl (2,219 bytes), Ruby (2,087 bytes), Assembly (2,024 bytes), DTrace (1,857 bytes), Makefile (1,841 bytes), D (1,686 bytes).'}], 'var_call_10Xn3FmZVi7BrKaCOoW3w2tz': [{'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copies': '1'}], 'var_call_eo2SizTwkH9xYiDCDygww0Rg': 'file_storage/call_eo2SizTwkH9xYiDCDygww0Rg.json', 'var_call_P8GPMDpQKBKDuBGKC5cv21ir': 'file_storage/call_P8GPMDpQKBKDuBGKC5cv21ir.json', 'var_call_ej0qnGa8zVsbr7pPchj3DNlx': {'max_count': 38, 'top_files': [{'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'sample_repo_name': 'uacaps/PageMenu', 'sample_path': 'Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift', 'count': 38}]}, 'var_call_Ju2wogWKSV2Tzv9qCJyKgKOf': [{'repo_name': 'uacaps/PageMenu', 'language_description': 'The codebase includes: Swift (56,461 bytes), Objective-C (51,756 bytes), Ruby (5,999 bytes).'}]}

exec(code, env_args)
