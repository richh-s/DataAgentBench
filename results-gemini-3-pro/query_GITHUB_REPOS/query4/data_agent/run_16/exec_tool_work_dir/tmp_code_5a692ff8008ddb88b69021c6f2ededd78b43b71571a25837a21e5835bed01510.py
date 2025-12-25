code = """import json

# Languages data from previous tool call
languages_data = [
    {"repo_name": "tensorflow/tensorflow", "language_description": "While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes)."},
    {"repo_name": "twbs/bootstrap", "language_description": "The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes)."},
    {"repo_name": "apple/swift", "language_description": "The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes)."},
    {"repo_name": "facebook/react", "language_description": "While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes)."},
    {"repo_name": "Microsoft/vscode", "language_description": "The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes)."}
]

# Commit counts (manually transcribed from previous step)
commits_data = {
    "torvalds/linux": 16061,
    "apple/swift": 1051,
    "twbs/bootstrap": 340,
    "Microsoft/vscode": 190,
    "facebook/react": 178,
    "tensorflow/tensorflow": 156
}

def get_main_language(desc):
    # This is a heuristic parser based on the observed format
    # Format examples:
    # "The codebase includes: Ruby (22,438 bytes), Shell (465 bytes)."
    # "While most of the project is built in C++ (126,099,822 bytes), it also incorporates..."
    # "The majority of the code is in TypeScript (21,066,876 bytes), followed by..."
    
    # We can try to extract all "Language (Bytes bytes)" patterns and find the max.
    import re
    # Pattern to match: Word or Words (number bytes)
    # Be careful with "Jupyter Notebook" (two words)
    # Regex: ([A-Za-z0-9\+\-\#\s]+)\s\(([0-9,]+)\sbytes\)
    matches = re.findall(r'([A-Za-z0-9\+\-\#\s]+)\s\(([0-9,]+)\sbytes\)', desc)
    
    lang_stats = []
    for lang, bytes_str in matches:
        # Clean up language name (trim spaces, remove "The codebase includes: " prefix if stuck)
        lang = lang.replace("The codebase includes:", "").replace("While most of the project is built in", "").replace("The majority of the code is in", "").replace(", followed by", "").replace("it also incorporates", "").strip()
        # Clean up bytes (remove commas)
        try:
            bytes_val = int(bytes_str.replace(",", ""))
            lang_stats.append((lang, bytes_val))
        except:
            continue
            
    if not lang_stats:
        return None
        
    # Sort by bytes desc
    lang_stats.sort(key=lambda x: x[1], reverse=True)
    return lang_stats[0][0]

results = []
for repo in commits_data:
    commits = commits_data[repo]
    
    # Find language desc
    lang_desc = next((item['language_description'] for item in languages_data if item['repo_name'] == repo), None)
    
    main_lang = "Unknown"
    if lang_desc:
        main_lang = get_main_language(lang_desc)
    elif repo == "torvalds/linux":
        main_lang = "C" # Inferred from file extensions
        
    results.append({
        "repo_name": repo,
        "commits": commits,
        "main_language": main_lang
    })

# Filter out Python
# (Assuming Unknown is not Python if verified manually)
non_python_repos = [r for r in results if r['main_language'] != 'Python']

# Sort by commits
non_python_repos.sort(key=lambda x: x['commits'], reverse=True)

# Top 5
top_5 = non_python_repos[:5]

print("__RESULT__:")
print(json.dumps([r['repo_name'] for r in top_5]))"""

env_args = {'var_function-call-12696708420631098980': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-12696708420631097987': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-16313240652779871748': [{'COUNT(*)': '3325634'}], 'var_function-call-9839929009655525160': [{'repo_name': 'tensorflow/tensorflow', 'language_description': 'While most of the project is built in C++ (126,099,822 bytes), it also incorporates Python (42,782,002 bytes), MLIR (11,447,433 bytes), Starlark (7,738,020 bytes), HTML (4,686,483 bytes), Go (2,129,888 bytes), C (1,400,913 bytes), Java (1,074,438 bytes), Jupyter Notebook (792,906 bytes), Shell (621,854 bytes), Dockerfile (416,133 bytes), Objective-C++ (300,213 bytes), CMake (182,430 bytes), Objective-C (172,666 bytes), Smarty (89,538 bytes), Swift (78,435 bytes), Batchfile (36,962 bytes), SourcePawn (14,625 bytes), C# (13,584 bytes), Ruby (9,199 bytes), Perl (7,536 bytes), LLVM (6,536 bytes), Pawn (5,552 bytes), Roff (5,034 bytes), Cython (5,003 bytes), Makefile (2,760 bytes), Vim Snippet (58 bytes).'}, {'repo_name': 'twbs/bootstrap', 'language_description': 'The codebase includes: JavaScript (865,640 bytes), HTML (679,522 bytes), SCSS (322,086 bytes), CSS (263,808 bytes), PowerShell (932 bytes).'}, {'repo_name': 'apple/swift', 'language_description': 'The codebase includes: C++ (49,043,456 bytes), Swift (41,439,628 bytes), C (5,467,361 bytes), Python (1,831,390 bytes), CMake (730,234 bytes), Objective-C (486,889 bytes), Shell (217,313 bytes), Objective-C++ (166,236 bytes), LLVM (74,481 bytes), Emacs Lisp (57,637 bytes), Batchfile (47,838 bytes), Vim Script (20,025 bytes), Roff (3,683 bytes), DTrace (2,593 bytes), Makefile (2,361 bytes), Ruby (2,132 bytes), D (1,107 bytes).'}, {'repo_name': 'facebook/react', 'language_description': 'While most of the project is built in JavaScript (6,256,474 bytes), it also incorporates HTML (120,058 bytes), CSS (64,972 bytes), C++ (44,290 bytes), TypeScript (21,454 bytes), CoffeeScript (17,390 bytes), C (5,227 bytes), Shell (2,306 bytes), Python (259 bytes), Makefile (189 bytes).'}, {'repo_name': 'Microsoft/vscode', 'language_description': 'The majority of the code is in TypeScript (21,066,876 bytes), followed by JavaScript (872,486 bytes), CSS (492,430 bytes), Inno Setup (165,483 bytes), HTML (47,005 bytes), Shell (25,657 bytes), PowerShell (6,430 bytes), Batchfile (5,369 bytes), Groovy (3,928 bytes), Python (2,405 bytes), Makefile (2,127 bytes), Ruby (1,703 bytes), Objective-C (1,387 bytes), Clojure (1,206 bytes), C++ (1,072 bytes), Perl 6 (1,065 bytes), PHP (998 bytes), Visual Basic (893 bytes), Perl (857 bytes), C (818 bytes), Go (652 bytes), F# (634 bytes), Java (599 bytes), CoffeeScript (590 bytes), Rust (532 bytes), C# (488 bytes), Dockerfile (425 bytes), R (362 bytes), Roff (351 bytes), ShaderLab (330 bytes), Swift (284 bytes), Lua (252 bytes), HLSL (184 bytes).'}], 'var_function-call-17573399889133660242': [], 'var_function-call-10478411352979745654': [{'repo_name': 'torvalds/linux', 'watch_count': '5332'}], 'var_function-call-17979381866051681959': [{'path': 'arch/arm64/boot/dts/arm/vexpress-v2m-rs1.dtsi'}, {'path': 'scripts/coccinelle/api/alloc/kzalloc-simple.cocci'}, {'path': 'arch/powerpc/platforms/86xx/common.c'}, {'path': 'arch/cris/include/asm/eshlibld.h'}, {'path': 'tools/perf/util/color.c'}, {'path': 'arch/mn10300/include/asm/spinlock.h'}, {'path': 'arch/blackfin/include/asm/io.h'}, {'path': 'drivers/usb/serial/belkin_sa.c'}, {'path': 'Documentation/ABI/removed/sysfs-class-rfkill'}, {'path': 'drivers/gpu/drm/gma500/cdv_intel_hdmi.c'}, {'path': 'drivers/virtio/Kconfig'}, {'path': 'arch/arm/boot/dts/ste-ccu9540.dts'}, {'path': 'include/linux/mfd/tps65086.h'}, {'path': 'fs/gfs2/trace_gfs2.h'}, {'path': 'arch/arm/mach-omap2/cm1_44xx.h'}, {'path': 'drivers/media/rc/keymaps/rc-kworld-315u.c'}, {'path': 'drivers/net/ethernet/atheros/atlx/atl2.c'}, {'path': 'sound/soc/codecs/ts3a227e.h'}, {'path': 'arch/powerpc/include/uapi/asm/siginfo.h'}, {'path': 'arch/cris/include/arch-v32/arch/intmem.h'}, {'path': 'fs/btrfs/backref.h'}, {'path': 'arch/arm/mach-bcm/bcm63xx_pmb.c'}, {'path': 'drivers/hwmon/pmbus/max20751.c'}, {'path': 'arch/powerpc/platforms/86xx/gef_sbc610.c'}, {'path': 'drivers/gpu/drm/nouveau/nvkm/subdev/bios/perf.c'}, {'path': 'drivers/net/ethernet/sun/sunqe.c'}, {'path': 'Documentation/ia64/.gitignore'}, {'path': 'crypto/asymmetric_keys/x509_akid.asn1'}, {'path': 'drivers/staging/rtl8192e/rtl8192e/r8192E_dev.c'}, {'path': 'drivers/media/dvb-core/dvb_math.h'}, {'path': 'drivers/tty/serial/8250/8250_uniphier.c'}, {'path': 'drivers/crypto/rockchip/rk3288_crypto.c'}, {'path': 'drivers/pnp/pnpacpi/Kconfig'}, {'path': 'arch/nios2/kernel/signal.c'}, {'path': 'tools/perf/util/xyarray.h'}, {'path': 'drivers/net/wireless/intel/ipw2x00/Makefile'}, {'path': 'arch/x86/include/asm/hpet.h'}, {'path': 'tools/iio/Makefile'}, {'path': 'drivers/isdn/hardware/eicon/debuglib.h'}, {'path': 'drivers/net/wireless/broadcom/b43/phy_ht.c'}, {'path': 'include/linux/mtd/spi-nor.h'}, {'path': 'drivers/usb/host/ehci-orion.c'}, {'path': 'drivers/net/ethernet/mellanox/mlx4/mr.c'}, {'path': 'arch/arm/mach-footbridge/common.h'}, {'path': 'arch/sparc/lib/GENcopy_to_user.S'}, {'path': 'arch/powerpc/platforms/44x/iss4xx.c'}, {'path': 'include/linux/mfd/da9055/reg.h'}, {'path': 'drivers/scsi/53c700.c'}, {'path': 'drivers/net/ethernet/atheros/atl1c/atl1c_hw.h'}, {'path': 'arch/arm/mach-zynq/headsmp.S'}], 'var_function-call-5239983196856624322': [{'count(DISTINCT repo_name)': '6'}]}

exec(code, env_args)
