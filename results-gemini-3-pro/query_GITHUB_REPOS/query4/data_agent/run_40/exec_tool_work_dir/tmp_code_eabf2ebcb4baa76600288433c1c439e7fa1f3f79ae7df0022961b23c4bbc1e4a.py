code = """import re
import json

# Data from previous steps
repos_commits = [
    {"repo_name": "torvalds/linux", "commit_count": 16061},
    {"repo_name": "apple/swift", "commit_count": 1051},
    {"repo_name": "twbs/bootstrap", "commit_count": 340},
    {"repo_name": "Microsoft/vscode", "commit_count": 190},
    {"repo_name": "facebook/react", "commit_count": 178},
    {"repo_name": "tensorflow/tensorflow", "commit_count": 156}
]

languages_data = [
    {"repo_name": "tensorflow/tensorflow", "language_description": "While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes)."},
    {"repo_name": "twbs/bootstrap", "language_description": "The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes)."},
    {"repo_name": "apple/swift", "language_description": "The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes)."},
    {"repo_name": "facebook/react", "language_description": "While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes)."},
    {"repo_name": "Microsoft/vscode", "language_description": "The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes)."}
]

lang_map = {item['repo_name']: item['language_description'] for item in languages_data}

def get_main_language(desc):
    # Pattern to match "Language (bytes)"
    # Examples: "Ruby (22,438 bytes)", "C++ (126,099,822 bytes)"
    # Need to be careful about languages with spaces or symbols, e.g. "Objective-C++"
    # The bytes part is at the end of the match.
    
    # We can split by ',' or 'and' or 'followed by' etc to isolate chunks, 
    # but finding all occurrences of "Name (Bytes bytes)" is easier.
    
    matches = re.findall(r'([A-Za-z0-9\+\-\#\s]+)\s\((\d+(?:,\d+)*)\sbytes\)', desc)
    
    stats = []
    for lang, bytes_str in matches:
        lang = lang.strip().replace("incorporates ", "").replace("built in ", "").replace("includes: ", "") # cleanup prefix noise if captured
        # actually regex above captures the name directly if strictly followed by " (numbers bytes)"
        # However, the first group might include leading text if I use .+
        # Using [A-Za-z0-9\+\-\#\s]+ is safer but might capture "built in C++"
        
        # Let's refine:
        # The structure is usually "Language (X bytes)".
        # Let's iterate over matches and clean up the language name.
        
        # Clean up: remove common prefix words if they got caught? 
        # With the regex `([A-Za-z0-9\+\-\#\s]+)` it will capture spaces.
        # e.g. "built in C++"
        
        # A better approach: split the string by commas or known separators, then parse.
        # But regex is fine if we look at the end of the string before the parens.
        pass

    # New Regex approach:
    # Look for the pattern `(digits) bytes` and capture the preceding word(s).
    # But names are variable length.
    
    # Let's just use the finding all pattern and clean up.
    data = []
    for m in matches:
        name_raw = m[0].strip()
        # Remove potential prefix words from natural language
        for prefix in ["includes:", "built in", "code is in", "incorporates", "majority of the", "followed by", "project is", "codebase", "The", "This", "repository", "mainly", "written", "additional", "code", "with", ",", "and"]:
             if name_raw.lower().startswith(prefix.lower() + " "):
                 name_raw = name_raw[len(prefix)+1:].strip()
             # Repeat to peel off multiple words
             if name_raw.lower().startswith(prefix.lower() + " "):
                 name_raw = name_raw[len(prefix)+1:].strip()

        # Last cleanup, take the last words? No, "Jupyter Notebook" has 2 words.
        # "Objective-C++"
        
        bytes_val = int(m[1].replace(',', ''))
        data.append((name_raw, bytes_val))
    
    if not data:
        return None
        
    # Sort by bytes desc
    data.sort(key=lambda x: x[1], reverse=True)
    return data[0][0]

results = []
for repo in repos_commits:
    name = repo['repo_name']
    desc = lang_map.get(name)
    
    if name == 'torvalds/linux':
        main_lang = 'C' # Verified manually
    elif desc:
        main_lang = get_main_language(desc)
    else:
        main_lang = "Unknown"
        
    if main_lang != 'Python':
        results.append(name)

print("__RESULT__:")
print(json.dumps(results[:5]))"""

env_args = {'var_function-call-7179692331047649389': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-5813911523085245114': [{'count(*)': '3325634'}], 'var_function-call-8534464942752221286': [{'count_star()': '17976'}], 'var_function-call-13674762478554316985': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-2068936035393879919': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_function-call-16403999775822601663': [], 'var_function-call-12065534056767185982': [{'path': 'arch/arm64/boot/dts/arm/vexpress-v2m-rs1.dtsi'}, {'path': 'scripts/coccinelle/api/alloc/kzalloc-simple.cocci'}, {'path': 'arch/powerpc/platforms/86xx/common.c'}, {'path': 'arch/cris/include/asm/eshlibld.h'}, {'path': 'tools/perf/util/color.c'}, {'path': 'arch/mn10300/include/asm/spinlock.h'}, {'path': 'arch/blackfin/include/asm/io.h'}, {'path': 'drivers/usb/serial/belkin_sa.c'}, {'path': 'Documentation/ABI/removed/sysfs-class-rfkill'}, {'path': 'drivers/gpu/drm/gma500/cdv_intel_hdmi.c'}]}

exec(code, env_args)
