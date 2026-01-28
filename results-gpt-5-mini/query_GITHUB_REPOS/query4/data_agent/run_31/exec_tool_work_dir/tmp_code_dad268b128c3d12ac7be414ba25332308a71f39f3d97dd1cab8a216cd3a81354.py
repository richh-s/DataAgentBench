code = """import json
import re
import pandas as pd

# Load stored variables
commits = var_call_BK37beVeM4iMPHYzaMzMbFfv
langs_subset = var_call_QgY1WH3lSqM8AAs2nTHqs638
# var_call_eb1y... may be a file path for the full languages table
full_langs_data = None
if isinstance(var_call_eb1yBxdjbwGkIIqPSWkPvEEC, str):
    # It's a file path to a JSON file
    with open(var_call_eb1yBxdjbwGkIIqPSWkPvEEC, 'r', encoding='utf-8') as f:
        full_langs_data = json.load(f)
else:
    full_langs_data = var_call_eb1yBxdjbwGkIIqPSWkPvEEC

# Build mapping from repo_name to language_description using full data, fallback to subset
lang_map = {}
if full_langs_data:
    for r in full_langs_data:
        repo = r.get('repo_name')
        desc = r.get('language_description')
        if repo and desc:
            lang_map[repo] = desc
# Add/override with subset
for r in langs_subset:
    repo = r.get('repo_name')
    desc = r.get('language_description')
    if repo and desc:
        lang_map[repo] = desc

# Helper to extract main language
pattern = re.compile(r"([A-Za-z0-9\+\#\._\- ]+?) \(([\d,]+) bytes\)")

def get_main_language(desc):
    if not desc or not isinstance(desc, str):
        return None
    matches = pattern.findall(desc)
    if not matches:
        # try alternative 'The majority of the code is in LANGUAGE (X bytes)'
        m = re.search(r"in ([A-Za-z0-9\+\#\._\- ]+?) \(([\d,]+) bytes\)", desc)
        if m:
            return m.group(1).strip()
        return None
    # matches is list of (lang, bytes)
    best = None
    best_bytes = -1
    for lang, b in matches:
        try:
            val = int(b.replace(',', ''))
        except:
            val = 0
        if val > best_bytes:
            best_bytes = val
            best = lang.strip()
    return best

# Prepare commits dataframe
df_commits = pd.DataFrame(commits)
if 'commit_count' in df_commits.columns:
    df_commits['commit_count'] = df_commits['commit_count'].astype(int)

# Add main language
df_commits['language_description'] = df_commits['repo_name'].map(lang_map)

df_commits['main_language'] = df_commits['language_description'].apply(get_main_language)

# Filter out where main_language is Python or unknown (None)
filtered = df_commits[df_commits['main_language'].notnull() & (df_commits['main_language'].str.lower() != 'python')]
# Sort by commit_count desc
filtered_sorted = filtered.sort_values(by='commit_count', ascending=False)
# Take top 5
top5 = filtered_sorted.head(5)['repo_name'].tolist()

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_rcyyxG8Tiud56rmWOi4S9Q3R': ['languages', 'repos', 'licenses'], 'var_call_i7OhYBeYICckvmGe0xgrUsaL': ['commits', 'contents', 'files'], 'var_call_eb1yBxdjbwGkIIqPSWkPvEEC': 'file_storage/call_eb1yBxdjbwGkIIqPSWkPvEEC.json', 'var_call_CnjSiZhP4VKYc1Uvnt7lsVOg': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}], 'var_call_QgY1WH3lSqM8AAs2nTHqs638': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_call_i6jZkoYwzd01PXuEQNCmjx0F': [], 'var_call_BK37beVeM4iMPHYzaMzMbFfv': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
