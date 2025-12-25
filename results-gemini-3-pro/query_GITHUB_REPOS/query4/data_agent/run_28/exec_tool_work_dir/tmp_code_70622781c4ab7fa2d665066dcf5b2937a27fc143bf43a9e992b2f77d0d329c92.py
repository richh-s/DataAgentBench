code = """import re
import json

# Data from previous steps
# Commit counts
commits_data = [
    {"repo_name": "facebook/react", "commit_count": 178},
    {"repo_name": "tensorflow/tensorflow", "commit_count": 156},
    {"repo_name": "twbs/bootstrap", "commit_count": 340},
    {"repo_name": "Microsoft/vscode", "commit_count": 190},
    {"repo_name": "torvalds/linux", "commit_count": 16061},
    {"repo_name": "apple/swift", "commit_count": 1051}
]

# Language descriptions
languages_data = [
    {"repo_name": "tensorflow/tensorflow", "language_description": "While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes)."},
    {"repo_name": "twbs/bootstrap", "language_description": "The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes)."},
    {"repo_name": "apple/swift", "language_description": "The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes)."},
    {"repo_name": "facebook/react", "language_description": "While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes)."},
    {"repo_name": "Microsoft/vscode", "language_description": "The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes)."}
]

lang_map = {item['repo_name']: item['language_description'] for item in languages_data}

def get_main_language(desc):
    # Pattern to find "Language (Bytes bytes)"
    # We strip commas from bytes
    pattern = re.compile(r"([A-Za-z0-9\+\-\#\s]+)\s\((\d[\d,]*)\sbytes\)")
    matches = pattern.findall(desc)
    
    max_bytes = -1
    main_lang = None
    
    for lang, byte_str in matches:
        byte_val = int(byte_str.replace(',', ''))
        lang = lang.strip()
        # Clean up lang name if it has leading words like "built in " or "includes: " 
        # But based on regex, the first group might catch preceding words if not careful.
        # Let's adjust regex or clean up.
        # The strings are like: " Ruby (22,438 bytes), Shell (465 bytes)."
        # Or "built in Ruby (10,174 bytes)"
        
        # Actually, looking at the regex `([A-Za-z0-9\+\-\#\s]+)`, it is greedy.
        # "built in Ruby" will be captured.
        # We need to be careful.
        # The languages seem to be Capitalized usually. 
        # But simpler: the list is usually comma separated.
        # Let's try to extract just the last word(s) before the parenthesis?
        # Many languages are single words, but some are "Jupyter Notebook", "Emacs Lisp".
        
        # Let's rely on the structure.
        # It seems the language name is immediately before the parenthesis.
        # But determining where it starts is hard if we capture "built in Ruby".
        # However, the bytes comparison is what matters. 
        # If I get "built in Ruby", it is not "Python".
        # If I get "includes: Python", it contains "Python".
        
        # Let's refine the logic.
        # If the captured string ends with "Python", we treat it as Python.
        # If it ends with "C++", it's C++.
        
        if byte_val > max_bytes:
            max_bytes = byte_val
            main_lang = lang.strip()
            
    return main_lang

qualified_repos = []

for repo in commits_data:
    name = repo['repo_name']
    count = repo['commit_count']
    
    if name == 'torvalds/linux':
        # Special case: verified as C/Non-Python manually
        qualified_repos.append((name, count))
        continue
        
    if name in lang_map:
        desc = lang_map[name]
        main_lang = get_main_language(desc)
        
        # Check if main_lang is Python
        # Use simple string check
        if main_lang:
            # Clean the main_lang string to get the actual language name
            # e.g. "built in C++" -> "C++"
            # e.g. "includes: JavaScript" -> "JavaScript"
            # We can split by space and take the last part, 
            # but "Jupyter Notebook" has 2 parts.
            # "Emacs Lisp" has 2.
            # "Objective-C++" has 1.
            
            # If "Python" is in the string, is it the language or "built in Python"?
            # If the string is "built in Python", it is Python.
            # If "includes: Python", it is Python.
            # If "includes: C++", it is C++.
            
            # So if "Python" appears in the main_lang string, we treat it as Python?
            # Wait, "IPython Notebook" might be tricky?
            # But the list shows "Python" explicitly.
            
            if "Python" in main_lang and "Jupyter" not in main_lang:
                 # It is likely Python.
                 # Let's be strict. "Python" alone or "built in Python".
                 pass 
            else:
                # Not Python
                qualified_repos.append((name, count))
        else:
            # Could not parse, maybe safe to skip or inspect? 
            # In this case all 5 matched regex.
            pass

# Sort by count desc
qualified_repos.sort(key=lambda x: x[1], reverse=True)

# Top 5
top_5 = [r[0] for r in qualified_repos[:5]]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-17224946105187292561': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-9014716004781249598': 'file_storage/function-call-9014716004781249598.json', 'var_function-call-8976438063855130854': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}], 'var_function-call-371796768190273776': [{'count(DISTINCT repo_name)': '6'}], 'var_function-call-11374255790452465108': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_function-call-7782925397343972086': [], 'var_function-call-5663300052942526752': [{'path': 'arch/arm64/boot/dts/arm/vexpress-v2m-rs1.dtsi'}, {'path': 'scripts/coccinelle/api/alloc/kzalloc-simple.cocci'}, {'path': 'arch/powerpc/platforms/86xx/common.c'}, {'path': 'arch/cris/include/asm/eshlibld.h'}, {'path': 'tools/perf/util/color.c'}, {'path': 'arch/mn10300/include/asm/spinlock.h'}, {'path': 'arch/blackfin/include/asm/io.h'}, {'path': 'drivers/usb/serial/belkin_sa.c'}, {'path': 'Documentation/ABI/removed/sysfs-class-rfkill'}, {'path': 'drivers/gpu/drm/gma500/cdv_intel_hdmi.c'}, {'path': 'drivers/virtio/Kconfig'}, {'path': 'arch/arm/boot/dts/ste-ccu9540.dts'}, {'path': 'include/linux/mfd/tps65086.h'}, {'path': 'fs/gfs2/trace_gfs2.h'}, {'path': 'arch/arm/mach-omap2/cm1_44xx.h'}, {'path': 'drivers/media/rc/keymaps/rc-kworld-315u.c'}, {'path': 'drivers/net/ethernet/atheros/atlx/atl2.c'}, {'path': 'sound/soc/codecs/ts3a227e.h'}, {'path': 'arch/powerpc/include/uapi/asm/siginfo.h'}, {'path': 'arch/cris/include/arch-v32/arch/intmem.h'}]}

exec(code, env_args)
