code = """import json

try:
    # Load languages
    languages_file = locals()['var_function-call-1390691453327523512']
    with open(languages_file, 'r') as f:
        languages_list = json.load(f)
    
    # Build a dict for quick lookup
    # repo -> desc
    languages_map = {entry['repo_name']: entry['language_description'] for entry in languages_list}

    # Load readme data
    readme_data_var = locals()['var_function-call-3098194492094024582']
    readme_list = []
    if isinstance(readme_data_var, str) and readme_data_var.endswith('.json'):
        with open(readme_data_var, 'r') as f:
            readme_list = json.load(f)
    elif isinstance(readme_data_var, list):
        readme_list = readme_data_var
    
    readme_repos = set(item['repo_name'] for item in readme_list)
    
    # Stats
    total_readme_repos = len(readme_repos)
    repos_in_metadata = 0
    repos_using_python = 0
    repos_not_using_python = 0
    
    sample_missing = []
    
    for repo in readme_repos:
        if repo in languages_map:
            repos_in_metadata += 1
            desc = languages_map[repo]
            if "python" in desc.lower():
                repos_using_python += 1
            else:
                repos_not_using_python += 1
        else:
            if len(sample_missing) < 5:
                sample_missing.append(repo)
    
    result = {
        "total_readme_repos": total_readme_repos,
        "repos_in_metadata": repos_in_metadata,
        "repos_using_python": repos_using_python,
        "repos_not_using_python": repos_not_using_python,
        "sample_missing_from_metadata": sample_missing
    }
    
    print("__RESULT__:")
    print(json.dumps(result))

except Exception as e:
    print("__RESULT__:")
    print(json.dumps({"error": str(e)}))"""

env_args = {'var_function-call-13856584322929331039': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_function-call-6193642506899711196': [{'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/fun1_to_proc_par2.ll', 'mode': '40960', 'id': '316ad972693d0355c3504729fff14287419e004d', 'symlink_target': '../all/fun1_to_proc_par2.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'tests/failure/wrong_order_par_seq_middle.t/wrong_order_par_seq_middle.ll', 'mode': '40960', 'id': 'daa40d563068ee94f01b1e87952d607a6588a589', 'symlink_target': '../../../fixtures/all/wrong_order_par_seq_middle.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/layout_case.ll', 'mode': '40960', 'id': '6bd679ec4ff94d8149986d49b8e789d1b4d6a44a', 'symlink_target': '../all/layout_case.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/merger_loli_Sort.ll', 'mode': '40960', 'id': '0cfcfb70b14958a8ba30cb83808c9bcc25516969', 'symlink_target': '../all/merger_loli_Sort.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/failure/infer_recv.ll', 'mode': '40960', 'id': 'de516c994d6cc8b7bcc1fb6bf986699fced404f6', 'symlink_target': '../all/infer_recv.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/parallel_assoc_tensor3_flat.ll', 'mode': '40960', 'id': '248004ff4dd7722e31b548a776a3463ab8b52a78', 'symlink_target': '../all/parallel_assoc_tensor3_flat.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-failure/ten_loli_par.ll', 'mode': '40960', 'id': '23bb40fccf644811f011fb80b8f484a825d66543', 'symlink_target': '../all/ten_loli_par.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/compile/my_loli.ll', 'mode': '40960', 'id': '561e0c258b57a3dec9da2a2b6143003ede425013', 'symlink_target': '../all/my_loli.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/failure/dead_lock_tensor2_tensor2.ll', 'mode': '40960', 'id': '053669348398e5f7a34966fb62f93cc6f694e888', 'symlink_target': '../all/dead_lock_tensor2_tensor2.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/sequence/par_ten_ten_v1.ll', 'mode': '40960', 'id': '4d284e73f44321e6291601728fd1a6d15e26d2f2', 'symlink_target': '../all/par_ten_ten_v1.ll'}], 'var_function-call-16945481037319419184': [{'COUNT(*)': '3325634'}], 'var_function-call-15908428891108684607': [{'count_star()': '524077'}], 'var_function-call-3098194492094024582': [{'repo_name': 'waydelyle/openfund', 'content': "CKEditor 4\n==========\n\nCopyright (c) 2003-2015, CKSource - Frederico Knabben. All rights reserved.\nhttp://ckeditor.com - See LICENSE.md for license information.\n\nCKEditor is a text editor to be used inside web pages. It's not a replacement\nfor desktop text editors like Word or OpenOffice, but a component to be used as\npart of web applications and websites.\n\n## Documentation\n\nThe full editor documentation is available online at the following address:\nhttp://docs.ckeditor.com\n\n## Installation\n\nInstalling CKEditor is an easy task. Just follow these simple steps:\n\n 1. **Download** the latest version from the CKEditor website:\n    http://ckeditor.com. You should have already completed this step, but be\n    sure you have the very latest version.\n 2. **Extract** (decompress) the downloaded file into the root of your website.\n\n**Note:** CKEditor is by default installed in the `ckeditor` folder. You can\nplace the files in whichever you want though.\n\n## Checking Your Installation\n\nThe editor comes with a few sample pages that can be used to verify that\ninstallation proceeded properly. Take a look at the `samples` directory.\n\nTo test your installation, just call the following page at your website:\n\n\thttp://<your site>/<CKEditor installation path>/samples/index.html\n\nFor example:\n\n\thttp://www.example.com/ckeditor/samples/index.html\n"}, {'repo_name': 'DaMSL/K3', 'content': 'K3 Dockerfiles\n==========\n\nDockerfiles are updated for three images:\n\n1. **k3-app** -- (~250MB) light-weight image to run a K3 program. Based on debian:jessie. It contains only the necessary dependency libraries.\n2. **k3-compiler** -- (~2 GB) Image containing the GHC and GCC tool chains to compile a K3 program to binary. Based on debian:jessie\n3. **k3-dev** (~2.5 GB)  -- Larger container with additional library and application support (e.g. clang, ruby, vim, and others). It is based on debian:sid\n\nTo build an image use the following command:\n\n```\ndocker build -f k3-dev -t damsl/k3-dev:<your_tag> .\n```\n\n(Note: Docker build now has the -f option, so you don\'t have to call all docker files, "Dockerfile")\n\nThe image ```damsl/k3-dev:vanilla``` which is pushed to the repo contains the K3 source built with no options. Feel free to pull, use, & re-build K3 with whatever options necessary (and re-push with a new tag if needed).\n\nThe other scripts in here are left for legacy purposes.\n\nBuild Dependency Versions:\n<pre>\n  - GHC: 7.10.1\n  - GCC: 4.9.2\n  - Boost: 1.57\n  - Mesos: 0.22.1</pre>\n'}, {'repo_name': 'rgardler/azure-quickstart-templates', 'content': '# Emercoin Instance\n\nThis Microsoft Azure template deploys a single Emercoin client which will connect to the public Emercoin network.\n\n[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Femercoin-ubuntu%2Fazuredeploy.json)\n<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Femercoin-ubuntu%2Fazuredeploy.json" target="_blank">\n    <img src="http://armviz.io/visualizebutton.png"/>\n</a>\n\nOnce your deployment is complete you will be able to connect to the Emercoin public network.\n\n![Emercoin-Azure](https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/emercoin-ubuntu/images/emercoin.png)\n\n# Template Parameters\nWhen you launch the installation of the VM, you need to specify the following parameters:\n* `vmDnsPrefix`: this is the public DNS name for the VM that you will use interact with your console. You just need to specify an unique name.\n* `adminUsername`: self-explanatory. This is the account you will use for connecting to the node\n* `adminPassword`: self-explanatory. Be aware that Azure requires passwords to have One upper case, one lower case, a special character, and a number\n* `vmSize`: The type of VM that you want to use for the node. The default size is D1_v2 but you can change that if you expect to run workloads that require more RAM or CPU resources.\n\n# Emercoin Deployment Walkthrough\n1. Get your node\'s IP\n 1. browse to https://portal.azure.com\n\n 2. then click browse all, followed by "resource groups", and choose your resource group\n\n 3. then expand your resources, and public ip address of your node.\n\n2. Connect to your node\n 1. SSH to the public ip of your node as the user you specified for `adminUsername`, enter your `adminPassword`\n 2. Try to use the cli-client by `emc help` or `emc getinfo`\n 3. Point your browser to the public ip of your node, sign in with `adminUsername` and `adminPassword` specified before (note that browser may show you a warning of bad certificate - it\'s OK, you may replace the self-signed certificates by yours at /etc/ssl/emc/emcweb*)\n'}, {'repo_name': 'briancavalier/todomvc-fab', 'content': "curl.js loader plugins\n===\n\nPlease see the wiki for information about using plugins.  If you're interested\nin creating your own plugins, please check out the Plugin Author's Guide\non the wiki (TBD).\n\nAll of these plugins conform to the AMD specification.  However, that\ndoesn't necessarily mean that they'll work with other AMD loaders or\nbuilders.  Until the build-time API of AMD is finalized, there will be\nincompatibilities.\n\nModules that should work with any loader/builder:\n\nasync!\ndomReady!\njs!\nlink!\n\nTODO:\n\njson! (auto-detects xdomain and uses JSON-P)\n"}], 'var_function-call-1390691453327523512': 'file_storage/function-call-1390691453327523512.json', 'var_function-call-12395121544471155189': [{'count_star()': '2743'}], 'var_function-call-13726056270869898853': 0.3333333333333333, 'var_function-call-11765115713429978939': {'target_readmes_count': 3, 'copyright_found_count': 1, 'proportion': 0.3333333333333333}}

exec(code, env_args)
