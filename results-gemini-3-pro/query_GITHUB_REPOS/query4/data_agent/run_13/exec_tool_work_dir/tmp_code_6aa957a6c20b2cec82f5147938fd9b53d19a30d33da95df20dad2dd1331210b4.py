code = """import re
import json

data = [
    {"repo_name": "tensorflow/tensorflow", "language_description": "While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes)."},
    {"repo_name": "twbs/bootstrap", "language_description": "The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes)."},
    {"repo_name": "apple/swift", "language_description": "The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes)."},
    {"repo_name": "facebook/react", "language_description": "While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes)."},
    {"repo_name": "Microsoft/vscode", "language_description": "The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes)."}
]

# Commit counts
commit_counts = {
    "torvalds/linux": 16061,
    "apple/swift": 1051,
    "twbs/bootstrap": 340,
    "Microsoft/vscode": 190,
    "facebook/react": 178,
    "tensorflow/tensorflow": 156
}

def get_main_language(desc):
    # Regex to find Language (bytes)
    matches = re.findall(r'([a-zA-Z0-9\+\-\#\s]+) \((\d{1,3}(?:,\d{3})*) bytes\)', desc)
    if not matches:
        return None, 0
    
    max_lang = None
    max_bytes = -1
    
    for lang, byte_str in matches:
        byte_val = int(byte_str.replace(',', ''))
        lang = lang.strip()
        # Clean up wording like "includes:", "is built in", "written in" if captured
        # The regex captures the language name directly usually, but let's be careful
        # In the examples: "Ruby (22,438 bytes)" -> lang="Ruby"
        # "built in C++ (..." -> "built in C++" is not matched by simple regex if spaces allowed?
        # My regex: ([a-zA-Z0-9\+\-\#\s]+) allows spaces.
        # "built in C++" might be captured.
        # Let's refine the regex or cleaning.
        # The structure is usually "Language (Number bytes)"
        # But preceeding text might be "built in " or "includes: "
        # A better regex might be simply looking for the pattern and taking the last word(s) before the parens?
        # Or relying on the fact that language names are usually capitalized.
        
        # Let's try to match strict "Name (Bytes bytes)"
        pass

    # Let's re-parse carefully.
    # The format seems to be a list of "Language (bytes)" separated by commas, potentially with intro text.
    # Example: "While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes)..."
    # Matches:
    # 1. "built in C++", "126,099,822"
    # 2. "Python", "42,782,002"
    
    # We need to strip "built in ", "includes: ", "written in ", "code is in ", "followed by "
    
    bad_prefixes = ["built in ", "includes: ", "written in ", "code is in ", "followed by ", "most of the project is ", "The majority of the ", "The codebase "]
    
    clean_lang = lang
    for p in bad_prefixes:
        if clean_lang.lower().endswith(p.strip().lower()): # Check if the captured group ends with a prefix? No.
             pass
    
    # Actually, the regex `([a-zA-Z0-9\+\-\#\s]+)` is too greedy.
    # It captures "While most of the project is built in C++".
    # I should try to extract the language name which is usually the last words before (.
    
    # Split by spaces?
    words = lang.split()
    # Usually the language name is 1 or 2 words (e.g. "Emacs Lisp", "Jupyter Notebook").
    # It rarely contains "in" or "by".
    # Heuristic: Take the last 1-3 words that look like a language name.
    # But simpler: The intro text is standard.
    # "While most of the project is built in "
    # "The codebase includes: "
    # "The majority of the code is in "
    # "followed by "
    # "it also incorporates "
    # ", " (separator)
    
    # Let's use a simpler approach: Extract all "Name (N bytes)" and process names.
    # Common languages: C++, Python, JavaScript, TypeScript, HTML, CSS, Shell, Ruby, Java, Go, C, C#, Swift, PHP, etc.
    # I can just clean the name by removing known prefixes.
    
    clean_lang = lang.replace("The codebase includes:", "")
    clean_lang = clean_lang.replace("The majority of the code is in", "")
    clean_lang = clean_lang.replace("While most of the project is built in", "")
    clean_lang = clean_lang.replace("it also incorporates", "")
    clean_lang = clean_lang.replace("followed by", "")
    clean_lang = clean_lang.replace("This repository is mainly written in", "")
    clean_lang = clean_lang.replace("with additional code in", "")
    clean_lang = clean_lang.replace("and", "") # sometimes "and Shell"
    clean_lang = clean_lang.strip()
    
    if byte_val > max_bytes:
        max_bytes = byte_val
        max_lang = clean_lang
        
    return max_lang, max_bytes

parsed_results = []
for entry in data:
    repo = entry['repo_name']
    desc = entry['language_description']
    
    # Parse
    matches = re.findall(r'([a-zA-Z0-9\+\-\#\.\s]+)\s\((\d{1,3}(?:,\d{3})*) bytes\)', desc)
    
    langs = {}
    for l, b in matches:
        b_val = int(b.replace(',', ''))
        # Clean l
        l_clean = l
        for prefix in ["The codebase includes:", "While most of the project is built in", "it also incorporates", "The majority of the code is in", "followed by", "This repository is mainly written in", "with additional code in", ","]:
            if prefix in l_clean:
                l_clean = l_clean.replace(prefix, "")
        l_clean = l_clean.strip()
        langs[l_clean] = b_val
    
    # Determine main
    if not langs:
        main_lang = "Unknown"
    else:
        main_lang = max(langs, key=langs.get)
    
    parsed_results.append({
        "repo_name": repo,
        "main_language": main_lang,
        "commit_count": commit_counts.get(repo, 0)
    })

# Add torvalds/linux manually if needed, but let's stick to the list I have
# parsed_results.append({"repo_name": "torvalds/linux", "main_language": "C", "commit_count": 16061}) 

# Sort
parsed_results.sort(key=lambda x: x['commit_count'], reverse=True)

print("__RESULT__:")
print(json.dumps(parsed_results))"""

env_args = {'var_function-call-8876726468203478653': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-7606346406738300137': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-15049861181369331278': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-15793171899676888522': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_function-call-17917522121960587970': [], 'var_function-call-13284469100739712436': 'file_storage/function-call-13284469100739712436.json', 'var_function-call-17900297610301207470': [{'repo_name': 'torvalds/linux', 'watch_count': '5332'}], 'var_function-call-4561435959719821443': [{'path': 'arch/arm64/boot/dts/arm/vexpress-v2m-rs1.dtsi'}, {'path': 'scripts/coccinelle/api/alloc/kzalloc-simple.cocci'}, {'path': 'arch/powerpc/platforms/86xx/common.c'}, {'path': 'arch/cris/include/asm/eshlibld.h'}, {'path': 'tools/perf/util/color.c'}, {'path': 'arch/mn10300/include/asm/spinlock.h'}, {'path': 'arch/blackfin/include/asm/io.h'}, {'path': 'drivers/usb/serial/belkin_sa.c'}, {'path': 'Documentation/ABI/removed/sysfs-class-rfkill'}, {'path': 'drivers/gpu/drm/gma500/cdv_intel_hdmi.c'}, {'path': 'drivers/virtio/Kconfig'}, {'path': 'arch/arm/boot/dts/ste-ccu9540.dts'}, {'path': 'include/linux/mfd/tps65086.h'}, {'path': 'fs/gfs2/trace_gfs2.h'}, {'path': 'arch/arm/mach-omap2/cm1_44xx.h'}, {'path': 'drivers/media/rc/keymaps/rc-kworld-315u.c'}, {'path': 'drivers/net/ethernet/atheros/atlx/atl2.c'}, {'path': 'sound/soc/codecs/ts3a227e.h'}, {'path': 'arch/powerpc/include/uapi/asm/siginfo.h'}, {'path': 'arch/cris/include/arch-v32/arch/intmem.h'}], 'var_function-call-1783511665804092331': [{'repo_name': 'torvalds/subsurface', 'language_description': 'This repository is mainly written in C++ (1,499,813 bytes), with additional code in C (925,754 bytes), XSLT (241,013 bytes), Shell (72,247 bytes), QML (64,225 bytes), CMake (43,823 bytes), JavaScript (40,793 bytes), HTML (33,129 bytes), CSS (12,885 bytes), Perl (9,298 bytes), QMake (9,165 bytes), R (4,070 bytes), Makefile (3,446 bytes), TeX (1,671 bytes), Objective-C (301 bytes).'}]}

exec(code, env_args)
