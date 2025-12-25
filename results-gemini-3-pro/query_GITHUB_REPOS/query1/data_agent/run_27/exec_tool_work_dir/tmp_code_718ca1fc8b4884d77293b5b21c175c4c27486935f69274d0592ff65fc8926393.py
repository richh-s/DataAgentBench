code = """import json

# Load languages
langs_file = locals()['var_function-call-10580302241464987080']
with open(langs_file, 'r') as f:
    langs = json.load(f)

# Identify non-Python repos
non_python_repos = set()
for item in langs:
    # item is {"repo_name": ..., "language_description": ...}
    desc = item.get('language_description', '')
    if 'Python' not in desc:
        non_python_repos.add(item['repo_name'])

# Load contents
contents_file = locals()['var_function-call-7927489025446291411']
with open(contents_file, 'r') as f:
    readme_contents = json.load(f)

# Filter and Count
numerator = 0
denominator = 0

# We iterate through the available README contents.
# We treat each entry as a representative of a repo.
# If multiple entries have the same sample_repo_name, we should probably deduplicate by repo.
# Let's count repos, not files (query says "proportion of their README.md files" but "Among repositories...").
# Usually means proportion of repos.
# Let's deduplicate by repo name to be safe.

processed_repos = set()

for item in readme_contents:
    repo = item.get('sample_repo_name')
    content = item.get('content', '')
    
    if repo in non_python_repos:
        # Check if we already processed this repo (if multiple READMEs exist for one repo in the sample)
        # However, sample_repo_name is just a sample. The content might be used in multiple repos.
        # But we only know of 'repo' using it.
        # If we have multiple entries for the same repo (e.g. README.md and src/README.md), 
        # usually the main README.md is what matters.
        # The query asks "proportion of their README.md files".
        # If a repo has 2 READMEs, do we count it twice? "Among repositories... what proportion..." usually implies Repo is the unit.
        # So I will deduplicate by repo.
        
        if repo not in processed_repos:
            denominator += 1
            processed_repos.add(repo)
            
            # Check for copyright
            if 'copyright' in content.lower():
                numerator += 1

proportion = 0.0
if denominator > 0:
    proportion = numerator / denominator

print(f"Denominator (Non-Python repos with README): {denominator}")
print(f"Numerator (With Copyright): {numerator}")
print(f"Proportion: {proportion}")

result = {
    "denominator": denominator,
    "numerator": numerator,
    "proportion": proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10580302241464987080': 'file_storage/function-call-10580302241464987080.json', 'var_function-call-7473736151300254069': 'file_storage/function-call-7473736151300254069.json', 'var_function-call-18425556115361685171': {'num_repos': 841, 'num_blobs': 841, 'sample_blobs': ['e49e766d879de979b50a15698b1c18932393d7e7', 'ae530ac7b6aa33cdacec27b12e54ce940cef2740', 'ffc7352ed759d3a1db68039d44ca1da0924f3961', 'be73f17a980cba6d230563c70da46325e4591783', 'a76f5c3cc28c484ef4cbd0932c7d123b7fe023fd', '44149cd7dea6c54bd150045636f4fcc716772d66', 'd88b51108f39916a94002b657fb4610dbe7380f6', '12a68b1616a3de4a1a1b881064dd84d3de745f32', '17233b5906d31b40d8d31867a4fdacbc097b1210', '608a03147ecc61c9597634806cfc88a82c60f44a']}, 'var_function-call-13246476975072318056': [{'count(DISTINCT id)': '1059'}], 'var_function-call-16782485148288642015': [], 'var_function-call-1038141842882834763': [], 'var_function-call-15905126436149358890': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'device/nfc/nfc.mojom'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2', 'sample_repo_name': 'nwjs/chromium.src', 'sample_path': 'net/tools/quic/synchronous_host_resolver.cc'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171', 'sample_repo_name': 'pirapira/coq2rust', 'sample_path': 'lib/cUnix.mli'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67', 'sample_repo_name': 'unfiltered/unfiltered', 'sample_path': 'json4s/src/main/ls/0.6.5.json'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75', 'sample_repo_name': 'JosefRypacek/PrimeTV', 'sample_path': 'assets/images/svg/ic_menu_folder_w.svg'}], 'var_function-call-6823852178274930176': [{'count_star()': '195'}], 'var_function-call-3455266268313531227': [{'id': '478202e6f40409f0f588373073108c7eb71f8cbe', 'sample_path': 'rtrouton_scripts/Casper_Scripts/install_company_canon_printer_drivers/README.md'}, {'id': '2392030363d98f198f24348dc242e90370159b18', 'sample_path': 'api/docs/README.md'}, {'id': 'a230555c7a43e56ed55b96d9256ce7097142207f', 'sample_path': 'README.md'}, {'id': 'cb29c159f88b49e8e3b50f5cf15d9b0cba8c78c3', 'sample_path': 'centos7.mongodb24/examples/replica/README.md'}, {'id': '1b7be69e7afd090f96a4ea04475a8254886bca66', 'sample_path': 'README.md'}, {'id': 'eff0054756ffe250ef4b8098d3467ce247d01a7a', 'sample_path': '022. Balanced Binary Tree/README.md'}, {'id': 'f5d19158456d375540b7f118dfc968183a18e256', 'sample_path': 'examples/python/README.md'}, {'id': '30651a5965ffbf37d8931c72687d0c66e52d4f55', 'sample_path': 'lib/ehstorguids/README.md'}, {'id': 'd7f62193ca0b588863bac5d2cb4b4caca5623194', 'sample_path': 'README.md'}, {'id': 'dbe1d698ade54334043e8eb59be7d908e6934ff0', 'sample_path': 'modoboa/bower_components/eonasdan-bootstrap-datetimepicker/README.md'}], 'var_function-call-17703220596568104929': [], 'var_function-call-16273075676224829933': [{'count_star()': '417'}], 'var_function-call-77232157542451469': [{'path': 'lib/django/contrib/sessions/locale/fa/LC_MESSAGES/django.po', 'sample_path': 'django/contrib/sessions/locale/fa/LC_MESSAGES/django.po'}, {'path': 'arch/openrisc/include/asm/byteorder.h', 'sample_path': 'arch/openrisc/include/asm/byteorder.h'}, {'path': 'drivers/net/ethernet/intel/igb/e1000_mac.c', 'sample_path': 'drivers/net/ethernet/intel/igb/e1000_mac.c'}, {'path': 'arch/sh/include/asm/ioctls.h', 'sample_path': 'arch/sh/include/asm/ioctls.h'}, {'path': 'src/main/resources/icons/action/drawable-xhdpi/ic_view_array_black_36dp.png', 'sample_path': 'ajax/libs/material-design-icons/2.2.0/action/drawable-hdpi/ic_view_array_black_48dp.png'}, {'path': 'drivers/net/wireless/ath/reg.h', 'sample_path': 'drivers/net/wireless/ath/reg.h'}, {'path': 'app/assets/images/backend/loaders/circular/029.gif', 'sample_path': 'app/assets/images/backend/loaders/circular/029.gif'}, {'path': 'indexes/NOPOS/II_docs/ilists.imp/4.Repair/5.integradoSkippingBB.Sanders.2015[ver.leeme]/srcREPAIR/rebuildPost', 'sample_path': 'indexes/NOPOS/II_docs/ilists.imp/4.Repair/5.integradoSkippingBB.Sanders.2015[ver.leeme]/srcREPAIR/rebuildPost'}, {'path': 'data/gfx/cards/default_800x480/0.png', 'sample_path': 'data/gfx/cards/default_800x480/0.png'}, {'path': 'Matlab/projects/buildsys/results/parsonAppliance/fridgeInitial/house1_meanOn_varOn/20_80/summary.mat', 'sample_path': 'Matlab/projects/buildsys/results/parsonAppliance/fridgeInitial/house1_meanOn_varOn/20_80/summary.mat'}], 'var_function-call-7927489025446291411': 'file_storage/function-call-7927489025446291411.json'}

exec(code, env_args)
