code = """import json
import re

languages_data = locals()['var_function-call-12576396899734812553']
# languages_data is a list of dicts: [{'repo_name': ..., 'language_description': ...}, ...]

# Commits count for ordering
# I'll just hardcode the order or map it, but the question asks for the names.
# repo_commits = {
#     "apple/swift": 1051,
#     "twbs/bootstrap": 340,
#     "Microsoft/vscode": 190,
#     "facebook/react": 178,
#     "tensorflow/tensorflow": 156
# }
# Wait, I should use the data I have.

repo_commits = [
    {"repo_name": "apple/swift", "commit_count": 1051},
    {"repo_name": "twbs/bootstrap", "commit_count": 340},
    {"repo_name": "Microsoft/vscode", "commit_count": 190},
    {"repo_name": "facebook/react", "commit_count": 178},
    {"repo_name": "tensorflow/tensorflow", "commit_count": 156}
]

def get_main_language(description):
    # regex to find Language (bytes)
    # e.g. "Ruby (22,438 bytes)"
    # Pattern: Name followed by (numbers bytes)
    # Be careful with "Objective-C++"
    matches = re.findall(r'([a-zA-Z0-9\+\-\#\s]+)\s\(([\d,]+)\sbytes\)', description)
    
    max_bytes = -1
    main_lang = None
    
    for lang, bytes_str in matches:
        lang = lang.strip()
        # Clean up lang name if it was preceded by "includes:" or similar if regex caught it?
        # My regex `([a-zA-Z0-9\+\-\#\s]+)` might catch "includes: Ruby"
        # Let's clean the lang string
        if "includes:" in lang:
            lang = lang.replace("includes:", "").strip()
        if "in " in lang: # "mainly written in Ruby"
             # This is tricky. Let's look at specific prefixes.
             pass
        
        # A better regex might be needed or split by comma.
        # But looking at the examples:
        # "The codebase includes: Ruby (22,438 bytes), Shell (465 bytes)."
        # "This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes)."
        # "While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python ..."
        
        # The structure seems to be parts separated by comma, each part containing `Lang (bytes)`.
        # So maybe finding `Lang (bytes)` is safer if we ignore the surrounding text.
        # The regex `([a-zA-Z0-9\+\-\#\s]+)` is greedy and might eat words before the language name.
        # However, language names are usually capitalized.
        # Let's try to match the immediate word(s) before `(`.
        
        # Actually, let's just parse the regex group 1 carefully.
        # Example: "written in Ruby" -> lang="written in Ruby"
        # I can just take the last word(s) that look like a language.
        # Or I can simply look at the common languages list or just assume the language name is at the end.
        
        # Let's refine regex to be non-greedy at start? No.
        # Let's try to split by the bytes part.
        
        byte_val = int(bytes_str.replace(',', ''))
        if byte_val > max_bytes:
            max_bytes = byte_val
            main_lang = lang

    return main_lang, max_bytes

# Refined extraction:
# Iterate over the string, find `(N bytes)`. Look backwards to find the language name.
# Language name boundaries: comma, colon, "and", "in".

def extract_main_lang_robust(desc):
    # Find all patterns of "(N bytes)"
    # We will split the string by these patterns to isolate the text before them.
    
    # Actually, simpler:
    # 1. Find all `(N bytes)` matches including positions.
    # 2. For each match, look at the text immediately preceding it.
    # 3. Clean that text to get the language name.
    
    matches = list(re.finditer(r'\(([\d,]+)\sbytes\)', desc))
    
    max_b = -1
    main_l = "Unknown"
    
    prev_end = 0
    for m in matches:
        bytes_str = m.group(1)
        bytes_val = int(bytes_str.replace(',', ''))
        
        start_index = m.start()
        # Look backwards from start_index
        # The text before is like "... includes: Ruby " or ", Shell "
        
        # Get the segment from previous match end to current match start
        segment = desc[prev_end:start_index].strip()
        
        # The language name is at the end of this segment.
        # It might be preceded by:
        # ","
        # ":"
        # "and"
        # "in" (as in "written in")
        # "incorporates"
        
        # Let's split by simple delimiters first
        # delimiters: , :
        
        # Take the last part after splitting
        candidates = re.split(r'[,:]', segment)
        candidate = candidates[-1].strip()
        
        # Now remove common preamble words
        words_to_remove = ["and", "in", "written", "built", "incorporates", "includes", "code", "majority", "of", "the", "is", "project", "most", "While", "followed", "by", "with", "additional", "This", "repository", "mainly"]
        
        # Tokenize and keep taking words from the end until we hit a lowercase word or a stop word?
        # Most languages are Capitalized (C++, Python, Shell).
        # But some might have spaces (Emacs Lisp).
        
        # Let's just remove the known stop words from the candidate string
        # Be careful with "Go" vs "go".
        
        tokens = candidate.split()
        lang_tokens = []
        for token in reversed(tokens):
            if token in words_to_remove:
                break
            lang_tokens.insert(0, token)
        
        lang_name = " ".join(lang_tokens)
        
        if bytes_val > max_b:
            max_b = bytes_val
            main_l = lang_name
            
        prev_end = m.end()
        
    return main_l

results = []
for entry in languages_data:
    rname = entry['repo_name']
    desc = entry['language_description']
    main_lang = extract_main_lang_robust(desc)
    results.append({"repo_name": rname, "main_lang": main_lang})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15169692526087577307': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-15422262497849479724': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-3947306500369176434': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-7039475553940906156': [{'count(DISTINCT repo_name)': '6'}], 'var_function-call-12576396899734812553': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_function-call-8077468883540931106': [], 'var_function-call-9372389408847432712': [{'repo_name': 'dinahosting/dinaip-linux-grafica'}, {'repo_name': 'linuxsimba/packer-libvirt-profiles'}, {'repo_name': 'instantlinux/desviar'}, {'repo_name': 'pexip/os-util-linux'}, {'repo_name': 'ShinySide/Linux-Patches'}, {'repo_name': 'arcivanov/linuxbrew'}, {'repo_name': 'Ginfung/linux-variability-analysis-tools'}, {'repo_name': 'leutheus/linux-variability-analysis-tools.fm-translation'}, {'repo_name': 'ohnosequences/amazon-linux-ami'}, {'repo_name': 'christinloehner/linuxcounter-update-examples'}], 'var_function-call-4727492944734109076': [{'repo_name': 'torvalds/subsurface'}]}

exec(code, env_args)
