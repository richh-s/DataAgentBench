code = """import json
import os

# Get all repository names that meet our criteria
check_file = rl3  # This contains the file path from the previous query
print(f"Repository file info: {check_file}")

# Read the repository list
if isinstance(check_file, str):
    # It's a file path
    path = check_file.replace('file://', '')
    if os.path.exists(path):
        with open(path, 'r') as f:
            metadata_repos = json.load(f)
    else:
        print(f"File not found at {path}")
        metadata_repos = []
else:
    # It's already the data
    metadata_repos = check_file

print(f"Total Shell + Apache-2.0 repos in metadata: {len(metadata_repos)}")
print(f"First 5 repos: {[r['repo_name'] for r in metadata_repos[:5]]}")

# Since we can't load all 114k repos at once in DuckDB efficiently,
# let's try a different approach - query commits table for a sample
# and see what repositories actually have commits data

print('__RESULT__:')
print(json.dumps({
    'metadata_repo_count': len(metadata_repos),
    'sample_repos': [r['repo_name'] for r in metadata_repos[:10]]
}))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'status': 'check complete'}, 'var_functions.query_db:14': [{'repo_name': '0--key/lib'}, {'repo_name': '0-complexity/G8VDC'}, {'repo_name': '0-complexity/whmcs-oauth2-addon'}, {'repo_name': '001szymon/phonegap-app-desktop'}, {'repo_name': '007slm/nutz'}, {'repo_name': '00christian00/unity3d-levelup'}, {'repo_name': '00pauln00/yapio'}, {'repo_name': '00wendi00/MyProject'}, {'repo_name': '01000101/cloudify-cli'}, {'repo_name': '01022499/end-to-end'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': [{'count': '0'}], 'var_functions.query_db:24': [{'total_commits': '17976'}], 'var_functions.query_db:26': [{'repo_name': 'facebook/react'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'Microsoft/vscode'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'twbs/bootstrap'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': [{'repo_name': 'facebook/react'}, {'repo_name': 'tensorflow/tensorflow'}], 'var_functions.query_db:34': [{'commit_count': '219'}], 'var_functions.query_db:36': [{'repo_name': 'facebook/react'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'Microsoft/vscode'}], 'var_functions.query_db:40': [{'commit_count': '0'}], 'var_functions.query_db:42': [], 'var_functions.query_db:44': [{'commit_count': '15016'}], 'var_functions.query_db:46': [{'repo_name': 'torvalds/linux', 'commit_count': '13413'}, {'repo_name': 'facebook/react', 'commit_count': '104'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '171'}, {'repo_name': 'apple/swift', 'commit_count': '965'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '115'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '251'}], 'var_functions.query_db:48': [{'repo_name': 'twbs/bootstrap', 'license': 'mit'}, {'repo_name': 'Microsoft/vscode', 'license': 'mit'}, {'repo_name': 'tensorflow/tensorflow', 'license': 'apache-2.0'}, {'repo_name': 'facebook/react', 'license': 'mit'}, {'repo_name': 'apple/swift', 'license': 'apache-2.0'}], 'var_functions.query_db:50': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}], 'var_functions.query_db:52': [{'total_filtered_commits': '15019'}], 'var_functions.query_db:54': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '115'}, {'repo_name': 'apple/swift', 'commit_count': '965'}], 'var_functions.query_db:56': [{'repo_name': 'tensorflow/tensorflow', 'commit_count': '115'}, {'repo_name': 'apple/swift', 'commit_count': '965'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:60': [{'COUNT(*)': '114972'}]}

exec(code, env_args)
