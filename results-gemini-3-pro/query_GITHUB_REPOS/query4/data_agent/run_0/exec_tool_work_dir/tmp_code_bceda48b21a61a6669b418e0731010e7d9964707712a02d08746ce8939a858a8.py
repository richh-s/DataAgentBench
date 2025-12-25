code = """import json
import re

# Load data from previous steps
# languages_data = var_call_4092120059926940335 (list of dicts)
# commits_data = var_call_10694482225128531242 (list of dicts)

languages_data = locals()['var_function-call-4092120059926940335']
commits_data = locals()['var_function-call-10694482225128531242']

# Helper to parse language description
def get_main_language(desc):
    # Pattern to find "Language (bytes)" or similar
    # Examples: 
    # "The codebase includes: Ruby (22,438 bytes), Shell (465 bytes)."
    # "While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python..."
    
    # We can extract all (Language, Bytes) pairs
    # Regex look for: ([A-Za-z0-9\+\#\s]+) \(([0-9,]+) bytes\)
    matches = re.findall(r'([A-Za-z0-9\+\-\#\s]+)\s\(([0-9,]+)\sbytes\)', desc)
    
    if not matches:
        return None
    
    max_bytes = -1
    main_lang = None
    
    for lang, byte_str in matches:
        # Clean lang name (trim whitespace, remove "and", "most of the project is built in")
        # Actually the regex might capture preceding words if not careful.
        # Let's refine regex or clean up.
        
        # A safer way: Iterate over matches, the language name is usually the last word(s) before the parenthesis?
        # No, "C++ (123 bytes)" -> "C++"
        # "Visual Basic (123 bytes)" -> "Visual Basic"
        # "built in C++ (123 bytes)" -> "built in C++" is captured by first group.
        
        # Heuristic: Take the captured string, split by words, take the last few that look like a language?
        # Or better: The format seems to be ", Language (Bytes)" or "includes: Language (Bytes)".
        # Let's just assume the language name doesn't contain "built in".
        # But "most of the project is built in C++" -> lang="most of the project is built in C++"
        
        lang = lang.strip()
        # Remove common prefixes
        prefixes = ["The codebase includes:", "This repository is mainly written in", "The majority of the code is in", "While most of the project is built in", "it also incorporates", "followed by", "with additional code in", ","]
        for p in prefixes:
            if lang.startswith(p):
                lang = lang[len(p):].strip()
            # Also handle if it's inside the string? No, the regex splits by (...) bytes. 
            # The capturing group is greedy. 
            # Let's try to match from the end of the previous match or start of string?
            # It's complicated.
            
        # Alternative: The language name is usually capitalized.
        # Let's try to just clean up specific known noise words.
        noise = ["The", "codebase", "includes:", "While", "most", "of", "the", "project", "is", "built", "in", "it", "also", "incorporates", "majority", "code", "mainly", "written", "with", "additional", "followed", "by", ","]
        
        # Let's split by space and take the last continuous chunk that looks like a language?
        # Actually, languages like "Objective-C++" are one token. "Visual Basic" are two.
        # Let's clean the string by removing the noise words from the START.
        
        words = lang.split()
        clean_words = []
        for w in words:
            if w.lower() not in [n.lower() for n in noise]:
                clean_words.append(w)
            elif clean_words: # If we hit noise after starting words, maybe stop? No.
                pass 
        
        # This is getting messy.
        # Let's look at the specific structure.
        # "built in C++" -> C++
        # "includes: Ruby" -> Ruby
        
        # Let's look at the end of the string 'lang'.
        # Usually the language is at the end.
        # e.g. "built in C++"
        # "includes: Ruby"
        # "incorporates Python"
        
        # Let's rely on the fact that language names are usually Title Case or Uppercase.
        # But 'built' is not. 'in' is not.
        
        # Let's try to strip known prefixes again carefully.
        lang_clean = lang
        for p in prefixes:
             # Case insensitive check
             if lang_clean.lower().startswith(p.lower()):
                 lang_clean = lang_clean[len(p):].strip()
        
        # Remove leading "and " or ", "
        if lang_clean.lower().startswith("and "):
            lang_clean = lang_clean[4:].strip()
        if lang_clean.startswith(","):
            lang_clean = lang_clean[1:].strip()
            
        byte_val = int(byte_str.replace(',', ''))
        
        if byte_val > max_bytes:
            max_bytes = byte_val
            main_lang = lang_clean
            
    return main_lang

repo_langs = {}
for entry in languages_data:
    repo = entry['repo_name']
    desc = entry['language_description']
    main = get_main_language(desc)
    repo_langs[repo] = main

# Add torvalds/linux manually as 'C' since we verified it via files
repo_langs['torvalds/linux'] = 'C'

# Combine with commits
final_list = []
for entry in commits_data:
    repo = entry['repo_name']
    count = int(entry['commit_count'])
    lang = repo_langs.get(repo, 'Unknown')
    
    final_list.append({
        'repo_name': repo,
        'commit_count': count,
        'main_language': lang
    })

# Filter out Python
# Also filtering out Unknown if we want to be safe, but we know our top list is covered.
filtered_list = [x for x in final_list if x['main_language'] and 'python' not in x['main_language'].lower()]

# Sort
filtered_list.sort(key=lambda x: x['commit_count'], reverse=True)

# Top 5
top_5 = [x['repo_name'] for x in filtered_list[:5]]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-3851700333804338257': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-1400654356691633291': [{'count(DISTINCT repo_name)': '6'}], 'var_function-call-9807336367130074651': [{'repo_name': 'facebook/react'}, {'repo_name': 'tensorflow/tensorflow'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'Microsoft/vscode'}], 'var_function-call-4092120059926940335': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_function-call-17408270997679529244': [], 'var_function-call-1060131580210487567': [{'repo_name': 'dinahosting/dinaip-linux-grafica'}, {'repo_name': 'linuxsimba/packer-libvirt-profiles'}, {'repo_name': 'instantlinux/desviar'}, {'repo_name': 'pexip/os-util-linux'}, {'repo_name': 'ShinySide/Linux-Patches'}, {'repo_name': 'arcivanov/linuxbrew'}, {'repo_name': 'Ginfung/linux-variability-analysis-tools'}, {'repo_name': 'leutheus/linux-variability-analysis-tools.fm-translation'}, {'repo_name': 'ohnosequences/amazon-linux-ami'}, {'repo_name': 'christinloehner/linuxcounter-update-examples'}], 'var_function-call-10694482225128531242': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-4745072053055115910': [{'repo_name': 'torvalds/linux', 'watch_count': '5332'}], 'var_function-call-9774409782511097845': [{'path': 'arch/arm64/boot/dts/arm/vexpress-v2m-rs1.dtsi'}, {'path': 'scripts/coccinelle/api/alloc/kzalloc-simple.cocci'}, {'path': 'arch/powerpc/platforms/86xx/common.c'}, {'path': 'arch/cris/include/asm/eshlibld.h'}, {'path': 'tools/perf/util/color.c'}, {'path': 'arch/mn10300/include/asm/spinlock.h'}, {'path': 'arch/blackfin/include/asm/io.h'}, {'path': 'drivers/usb/serial/belkin_sa.c'}, {'path': 'Documentation/ABI/removed/sysfs-class-rfkill'}, {'path': 'drivers/gpu/drm/gma500/cdv_intel_hdmi.c'}, {'path': 'drivers/virtio/Kconfig'}, {'path': 'arch/arm/boot/dts/ste-ccu9540.dts'}, {'path': 'include/linux/mfd/tps65086.h'}, {'path': 'fs/gfs2/trace_gfs2.h'}, {'path': 'arch/arm/mach-omap2/cm1_44xx.h'}, {'path': 'drivers/media/rc/keymaps/rc-kworld-315u.c'}, {'path': 'drivers/net/ethernet/atheros/atlx/atl2.c'}, {'path': 'sound/soc/codecs/ts3a227e.h'}, {'path': 'arch/powerpc/include/uapi/asm/siginfo.h'}, {'path': 'arch/cris/include/arch-v32/arch/intmem.h'}]}

exec(code, env_args)
