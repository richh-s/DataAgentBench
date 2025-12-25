code = """import re
import json

# Data from previous steps
commits_data = [
    {"repo_name": "facebook/react", "commit_count": 178},
    {"repo_name": "tensorflow/tensorflow", "commit_count": 156},
    {"repo_name": "twbs/bootstrap", "commit_count": 340},
    {"repo_name": "apple/swift", "commit_count": 1051},
    {"repo_name": "Microsoft/vscode", "commit_count": 190},
    {"repo_name": "torvalds/linux", "commit_count": 16061}
]

languages_data = [
    {"repo_name": "tensorflow/tensorflow", "language_description": "While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes)."},
    {"repo_name": "twbs/bootstrap", "language_description": "The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes)."},
    {"repo_name": "apple/swift", "language_description": "The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes)."},
    {"repo_name": "facebook/react", "language_description": "While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes)."},
    {"repo_name": "Microsoft/vscode", "language_description": "The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes)."}
]

# Helper to parse language description
def get_main_language(desc):
    if not desc:
        return "Unknown"
    # Pattern: LanguageName (Bytes bytes)
    # Note: Language names can contain spaces, +, #.
    # We look for the pattern "... (X bytes)" and take the preceding words.
    # A cleaner regex might be simpler.
    # The strings are like: "JavaScript (865,640 bytes), HTML (679,522 bytes)..."
    # Let's use finding all matches.
    matches = re.findall(r'([a-zA-Z0-9\+\-\#\s\.]+)\s\((\d[\d,]*)\sbytes\)', desc)
    
    lang_stats = []
    for m in matches:
        lang_name = m[0].strip()
        # Clean up leading words if any (like "built in ", "includes: ", ", ")
        # This is tricky because the text is natural language.
        # But looking at the examples:
        # "built in C++" -> lang "C++"
        # "includes: JavaScript" -> lang "JavaScript"
        # ", HTML" -> lang "HTML"
        # We can try to clean known prefixes or just take the last word?
        # No, "Jupyter Notebook" is two words.
        # Let's iterate and clean.
        
        # Common prefixes to remove from the captured group 1:
        # "The codebase includes: "
        # "While most of the project is built in "
        # "it also incorporates "
        # "The majority of the code is in "
        # "followed by "
        # ", "
        # "with additional code in "
        
        raw_name = lang_name
        # Remove common phrases
        for phrase in ["The codebase includes:", "While most of the project is built in", "it also incorporates", "The majority of the code is in", "followed by", "with additional code in", ","]:
            raw_name = raw_name.replace(phrase, "")
        
        clean_name = raw_name.strip()
        bytes_count = int(m[1].replace(",", ""))
        lang_stats.append((clean_name, bytes_count))
    
    if not lang_stats:
        return "Unknown"
    
    # Sort by bytes desc
    lang_stats.sort(key=lambda x: x[1], reverse=True)
    return lang_stats[0][0]

# Join and process
result_list = []
lang_map = {item['repo_name']: item['language_description'] for item in languages_data}

for repo in commits_data:
    r_name = repo['repo_name']
    c_count = repo['commit_count']
    desc = lang_map.get(r_name)
    
    if r_name == "torvalds/linux":
        main_lang = "C" # Inferred
    else:
        main_lang = get_main_language(desc)
        
    result_list.append({
        "repo_name": r_name,
        "commit_count": c_count,
        "main_language": main_lang
    })

# Filter out Python main
final_list = [r for r in result_list if r['main_language'] != "Python"]

# Sort by commits desc
final_list.sort(key=lambda x: x['commit_count'], reverse=True)

# Top 5
top_5 = final_list[:5]
top_5_names = [r['repo_name'] for r in top_5]

print("__RESULT__:")
print(json.dumps(top_5_names))"""

env_args = {'var_function-call-16471197811849354120': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-8166592957097970495': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_function-call-13684901240068363440': [{'COUNT(*)': '3325634'}], 'var_function-call-13756113528975911609': [{'count_star()': '17976'}], 'var_function-call-15148297051725668016': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_function-call-7112589545204160389': [], 'var_function-call-6267246946622457647': [{'repo_name': 'dinahosting/dinaip-linux-grafica'}, {'repo_name': 'linuxsimba/packer-libvirt-profiles'}, {'repo_name': 'instantlinux/desviar'}, {'repo_name': 'pexip/os-util-linux'}, {'repo_name': 'ShinySide/Linux-Patches'}, {'repo_name': 'arcivanov/linuxbrew'}, {'repo_name': 'Ginfung/linux-variability-analysis-tools'}, {'repo_name': 'leutheus/linux-variability-analysis-tools.fm-translation'}, {'repo_name': 'ohnosequences/amazon-linux-ami'}, {'repo_name': 'christinloehner/linuxcounter-update-examples'}], 'var_function-call-10849808157294005650': [{'repo_name': 'torvalds/linux', 'watch_count': '5332'}], 'var_function-call-17398397908963596168': [{'path': 'arch/arm64/boot/dts/arm/vexpress-v2m-rs1.dtsi'}, {'path': 'scripts/coccinelle/api/alloc/kzalloc-simple.cocci'}, {'path': 'arch/powerpc/platforms/86xx/common.c'}, {'path': 'arch/cris/include/asm/eshlibld.h'}, {'path': 'tools/perf/util/color.c'}, {'path': 'arch/mn10300/include/asm/spinlock.h'}, {'path': 'arch/blackfin/include/asm/io.h'}, {'path': 'drivers/usb/serial/belkin_sa.c'}, {'path': 'Documentation/ABI/removed/sysfs-class-rfkill'}, {'path': 'drivers/gpu/drm/gma500/cdv_intel_hdmi.c'}, {'path': 'drivers/virtio/Kconfig'}, {'path': 'arch/arm/boot/dts/ste-ccu9540.dts'}, {'path': 'include/linux/mfd/tps65086.h'}, {'path': 'fs/gfs2/trace_gfs2.h'}, {'path': 'arch/arm/mach-omap2/cm1_44xx.h'}, {'path': 'drivers/media/rc/keymaps/rc-kworld-315u.c'}, {'path': 'drivers/net/ethernet/atheros/atlx/atl2.c'}, {'path': 'sound/soc/codecs/ts3a227e.h'}, {'path': 'arch/powerpc/include/uapi/asm/siginfo.h'}, {'path': 'arch/cris/include/arch-v32/arch/intmem.h'}], 'var_function-call-15991030464052608285': [{'ext': 'c', 'cnt': '160'}, {'ext': 'h', 'cnt': '136'}, {'ext': '', 'cnt': '36'}, {'ext': 'txt', 'cnt': '21'}, {'ext': 'S', 'cnt': '12'}]}

exec(code, env_args)
