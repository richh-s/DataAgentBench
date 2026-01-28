code = """import json

# Load the full repository list
file_path = 'file_storage/functions.query_db:0.json'
with open(file_path, 'r') as f:
    repo_data = json.load(f)

repo_names = [repo['repo_name'] for repo in repo_data]

# Process in batches of 500 to avoid query size limits
batch_size = 500
total_commits = 0
batch_queries = []

for i in range(0, len(repo_names), batch_size):
    batch = repo_names[i:i+batch_size]
    # Create a properly formatted list for SQL IN clause
    escaped = [f"'{name.replace("'", "''")}'" for name in batch]
    repo_list_str = ','.join(escaped)
    
    batch_queries.append({
        'start_index': i,
        'end_index': min(i + batch_size, len(repo_names)),
        'repo_list': repo_list_str,
        'query': f"""
            SELECT COUNT(*) as count 
            FROM commits 
            WHERE repo_name IN ({repo_list_str})
              AND message IS NOT NULL 
              AND LENGTH(message) < 1000
              AND LOWER(message) NOT LIKE 'merge%'
              AND LOWER(message) NOT LIKE 'update%'
              AND LOWER(message) NOT LIKE 'test%'
        """
    })

print('__RESULT__:')
print(json.dumps({
    'total_repos': len(repo_names),
    'num_batches': len(batch_queries),
    'batch_size': batch_size,
    'first_query_preview': batch_queries[0]['query'][:200] if batch_queries else '',
    'batch_queries': batch_queries[:3]  # First 3 batches
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': [{'repo_name': 'facebook/react'}, {'repo_name': 'twbs/bootstrap'}, {'repo_name': 'apple/swift'}, {'repo_name': 'torvalds/linux'}, {'repo_name': 'tensorflow/tensorflow'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:20': {'count': 114972, 'first_five': [{'repo_name': 'jitsi/jipopro'}, {'repo_name': 'NuGet/json-ld.net'}, {'repo_name': 'virtualcoinclub/common'}, {'repo_name': 'pydev/jmx_exporter'}, {'repo_name': 'eskatos/qi4j-dev-scripts'}]}, 'var_functions.execute_python:22': {'total_repos': 114972, 'first_10': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts', 'doximity/docker-redis', 'raghavkarol/dotfiles', 'Microsoft/TypeScript', 'romelperez/conky-command', 'NorthernMan54/homebridge-wssensor'], 'sample_batch': ['disqus/python-phabricator', 'shenguoquan/netty', 'abutcher/kubernetes', 'coderanger/brix', 'pnikosis/jHTML2Md', 'opuk/puppet-devel-workshop', 'HazemKhaled/Suds', 'bineanzhou/google-guice', 'bazelbuild/rules_kotlin', 'fbladilo/testing']}, 'var_functions.execute_python:24': {'total_repos': 114972, 'num_batches': 115, 'batch_size': 1000, 'first_batch_sample': ['jitsi/jipopro', 'NuGet/json-ld.net', 'virtualcoinclub/common', 'pydev/jmx_exporter', 'eskatos/qi4j-dev-scripts']}, 'var_functions.query_db:26': [{'total_count': '15016'}], 'var_functions.query_db:28': [{'repo_name': 'torvalds/linux', 'message': 'checkpatch: remove reference to feature-removal-schedule.txt\n\nIn commit 9c0ece069b32 ("Get rid of Documentation/feature-removal.txt"),\nLinus removes feature-removal-schedule.txt from Documentation, but there\nis still some reference to this file.  So remove them.\n\nSigned-off-by: Tao Ma <85dcca6eaef7f88f8513274f73363a9b5feab3ec@taobao.com>\nAcked-by: Andy Whitcroft <b4658fdd7fbd645c2859b0e39d71018f32058d12@canonical.com>\nCc: Joe Perches <16a9a54ddf4259952e3c118c763138e83693d7fd@perches.com>\nSigned-off-by: Andrew Morton <5c1e68b099950c134891f0b6e179498a8ebe9cf9@linux-foundation.org>\nSigned-off-by: Linus Torvalds <69652caca27c8b940640ad396ab71f93cacec34f@linux-foundation.org>\n', 'msg_length': '680'}, {'repo_name': 'torvalds/linux', 'message': "ocfs2: call o2quo_exit() if malloc failed in o2net_init()\n\nIn o2net_init, if malloc failed, it directly returns -ENOMEM.  Then\no2quo_exit won't be called in init_o2nm.\n\nSigned-off-by: Joseph Qi <88260f35dd98758635dbbf2145383e817a86f01c@huawei.com>\nReviewed-by: joyce.xue <e513a8cfffdd1761b5c8047b6b6cbe23f11326f2@huawei.com>\nCc: Mark Fasheh <8f0bc92cac940f3e83deb53ced7a1f201bce5732@suse.com>\nCc: Joel Becker <9d3d88cacb47f143c6cf36b9a61c09b528b2c49a@evilplan.org>\nSigned-off-by: Andrew Morton <5c1e68b099950c134891f0b6e179498a8ebe9cf9@linux-foundation.org>\nSigned-off-by: Linus Torvalds <69652caca27c8b940640ad396ab71f93cacec34f@linux-foundation.org>\n", 'msg_length': '652'}, {'repo_name': 'torvalds/linux', 'message': 'ocfs2: cleanup unused paramters in ocfs2_calc_new_backup_super\n\nParameters new_clusters and first_new_cluster are not used in\nocfs2_update_last_group_and_inode, so remove them.\n\nSigned-off-by: Joseph Qi <88260f35dd98758635dbbf2145383e817a86f01c@huawei.com>\nReviewed-by: joyce.xue <e513a8cfffdd1761b5c8047b6b6cbe23f11326f2@huawei.com>\nCc: Mark Fasheh <8f0bc92cac940f3e83deb53ced7a1f201bce5732@suse.com>\nCc: Joel Becker <9d3d88cacb47f143c6cf36b9a61c09b528b2c49a@evilplan.org>\nSigned-off-by: Andrew Morton <5c1e68b099950c134891f0b6e179498a8ebe9cf9@linux-foundation.org>\nSigned-off-by: Linus Torvalds <69652caca27c8b940640ad396ab71f93cacec34f@linux-foundation.org>\n', 'msg_length': '661'}, {'repo_name': 'torvalds/linux', 'message': 'eCryptfs: Clean up ecryptfs_decode_from_filename()\n\nFlesh out the comments for ecryptfs_decode_from_filename(). Remove the\nreturn condition, since it is always 0.\n\nSigned-off-by: Michael Halcrow <8c1011c9d06fc72acd93645d683782ab9543044d@us.ibm.com>\nCc: Dustin Kirkland <81003606aeb58a7381e4bb211f38072b7ea4a537@gmail.com>\nCc: Eric Sandeen <d55521028c14e0f378be5444e4ea388161c0d7e7@redhat.com>\nCc: Tyler Hicks <f69c264f60e3b997c7d27eb236d1230c0fc7e0a2@us.ibm.com>\nCc: David Kleikamp <9bc4ae2e83dabb4524fc335d7c1dac408a99dbe5@us.ibm.com>\nSigned-off-by: Andrew Morton <5c1e68b099950c134891f0b6e179498a8ebe9cf9@linux-foundation.org>\nSigned-off-by: Linus Torvalds <69652caca27c8b940640ad396ab71f93cacec34f@linux-foundation.org>\n', 'msg_length': '723'}, {'repo_name': 'torvalds/linux', 'message': 'mm,x86,um: move CMPXCHG_DOUBLE config option\n\nMove CMPXCHG_DOUBLE and rename it to HAVE_CMPXCHG_DOUBLE so architectures\ncan simply select the option if it is supported.\n\nSigned-off-by: Heiko Carstens <8dcf0f69152f32f23184f83357a3731522e56b9c@de.ibm.com>\nAcked-by: Christoph Lameter <ef3ecccf258fa062c5c6521a4887d40541963af7@linux.com>\nCc: Pekka Enberg <add4fcd06328a394f0ad91feda7ee057316dc5ed@kernel.org>\nCc: Ingo Molnar <9dbbbf0688fedc85ad4da37637f1a64b8c718ee2@elte.hu>\nCc: Thomas Gleixner <00e4cf8f46a57000a44449bf9dd8cbbcc209fd2a@linutronix.de>\nCc: "H. Peter Anvin" <8a453bad9912ffe59bc0f0b8abe03df9be19379e@zytor.com>\nSigned-off-by: Andrew Morton <5c1e68b099950c134891f0b6e179498a8ebe9cf9@linux-foundation.org>\nSigned-off-by: Linus Torvalds <69652caca27c8b940640ad396ab71f93cacec34f@linux-foundation.org>\n', 'msg_length': '811'}]}

exec(code, env_args)
