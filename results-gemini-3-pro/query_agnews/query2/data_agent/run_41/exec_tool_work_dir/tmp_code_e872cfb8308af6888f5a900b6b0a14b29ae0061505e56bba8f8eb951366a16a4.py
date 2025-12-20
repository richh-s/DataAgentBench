code = """import json
import re

# Load the articles
with open(locals()['var_function-call-5205776640490666422'], 'r') as f:
    articles = json.load(f)

# Keywords for Science/Technology
scitech_keywords = [
    'technology', 'science', 'computer', 'internet', 'software', 'hardware', 'web', 'online', 'net', 'digital', 
    'cyber', 'wireless', 'mobile', 'phone', 'cellphone', 'telecom', 'broadband', 'satellite', 'gps', 'robot', 
    'artificial intelligence', 'ai', 'nasa', 'space', 'astronomy', 'planet', 'mars', 'moon', 'universe', 'galaxy', 
    'solar', 'biology', 'physics', 'chemistry', 'genetics', 'dna', 'genome', 'stem cell', 'clone', 'medical', 
    'medicine', 'health', 'disease', 'virus', 'flu', 'vaccine', 'drug', 'cancer', 'aids', 'hiv', 'doctor', 
    'hospital', 'patient', 'treatment', 'therapy', 'research', 'study', 'scientist', 'researcher', 'laboratory', 
    'lab', 'experiment', 'innovation', 'invention', 'gadget', 'device', 'electronics', 'ipod', 'mp3', 'dvd', 
    'hdtv', 'video game', 'gaming', 'console', 'nintendo', 'sony', 'microsoft', 'google', 'apple', 'ibm', 'intel', 
    'linux', 'windows', 'mac', 'browser', 'firefox', 'explorer', 'search engine', 'yahoo', 'amazon', 'ebay', 
    'facebook', 'twitter', 'myspace', 'youtube', 'blog', 'email', 'spam', 'hacker', 'security', 'piracy', 
    'copyright', 'patent', 'chip', 'semiconductor', 'processor', 'server', 'database', 'network', 'router', 
    'wifi', 'bluetooth', 'gameboy', 'playstation', 'xbox', 'wii', 'ipod', 'itunes', 'napster', 'p2p', 'file sharing',
    'tech', 'biotech', 'nanotech', 'telecoms', 'telephony', 'broadband', 'isp', 'voip', 'skype', 'msn', 'aim', 
    'icq', 'chat', 'message', 'messaging', 'texting', 'sms', 'mms', 'cameraphone', 'smartphone', 'pda', 'palm', 
    'blackberry', 'laptop', 'notebook', 'desktop', 'pc', 'monitor', 'screen', 'display', 'lcd', 'plasma', 'led', 
    'oled', 'crt', 'pixel', 'resolution', 'definition', 'hd', 'high def', 'high definition', 'dvd', 'blu-ray', 
    'hd-dvd', 'vhs', 'beta', 'cassette', 'tape', 'disc', 'disk', 'drive', 'storage', 'memory', 'flash', 'usb', 
    'firewire', 'port', 'interface', 'peripheral', 'mouse', 'keyboard', 'printer', 'scanner', 'camera', 'camcorder', 
    'photography', 'lens', 'zoom', 'megapixel', 'shutter', 'focus', 'flash', 'battery', 'charge', 'power', 'energy',
    'fuel cell', 'hydrogen', 'solar power', 'wind power', 'nuclear', 'atomic', 'proton', 'electron', 'neutron', 
    'quark', 'quantum', 'relativity', 'gravity', 'evolution', 'species', 'organism', 'cell', 'bacteria', 'microbe', 
    'germ', 'fungus', 'mold', 'yeast', 'enzyme', 'protein', 'amino acid', 'vitamin', 'mineral', 'nutrient', 
    'calorie', 'diet', 'nutrition', 'obesity', 'diabetes', 'heart disease', 'stroke', 'alzheimer', 'parkinson', 
    'autism', 'asthma', 'allergy', 'depression', 'anxiety', 'stress', 'mental health', 'psychology', 'psychiatry', 
    'neurology', 'brain', 'nerve', 'neuron', 'synapse', 'hormone', 'gland', 'organ', 'liver', 'kidney', 'lung', 
    'heart', 'stomach', 'intestine', 'colon', 'blood', 'vein', 'artery', 'capillary', 'bone', 'muscle', 'skin', 
    'hair', 'eye', 'ear', 'nose', 'mouth', 'tooth', 'teeth', 'gum', 'tongue', 'throat', 'neck', 'shoulder', 
    'arm', 'hand', 'finger', 'thumb', 'chest', 'breast', 'back', 'spine', 'hip', 'leg', 'knee', 'foot', 'toe', 
    'ankle', 'wrist', 'elbow', 'joint', 'skeleton', 'skull', 'rib', 'pelvis', 'fossil', 'dinosaur', 'extinct', 
    'endangered', 'habitat', 'ecosystem', 'environment', 'climate', 'warming', 'greenhouse', 'carbon', 'emission', 
    'pollution', 'waste', 'recycle', 'conservation', 'wildlife', 'nature', 'animal', 'plant', 'tree', 'flower', 
    'forest', 'ocean', 'sea', 'river', 'lake', 'mountain', 'volcano', 'earthquake', 'tsunami', 'storm', 'hurricane',
    'typhoon', 'tornado', 'cyclone', 'flood', 'drought', 'weather', 'meteorology', 'geology', 'geography', 'map', 
    'atlas', 'globe', 'earth', 'world', 'land', 'water', 'air', 'atmosphere', 'sky', 'cloud', 'rain', 'snow', 
    'ice', 'hail', 'fog', 'mist', 'wind', 'breeze', 'gale', 'gust', 'storm', 'thunder', 'lightning', 'forecast', 
    'temperature', 'heat', 'cold', 'freeze', 'melt', 'boil', 'evaporate', 'condense', 'precipitate', 'sublime', 
    'solid', 'liquid', 'gas', 'plasma', 'state', 'phase', 'matter', 'mass', 'weight', 'density', 'volume', 
    'area', 'length', 'width', 'height', 'depth', 'distance', 'time', 'speed', 'velocity', 'acceleration', 
    'force', 'momentum', 'energy', 'work', 'power', 'pressure', 'stress', 'strain', 'elasticity', 'viscosity', 
    'friction', 'gravity', 'magnetism', 'electricity', 'charge', 'current', 'voltage', 'resistance', 'capacitance', 
    'inductance', 'impedance', 'frequency', 'wavelength', 'amplitude', 'period', 'cycle', 'hertz', 'wave', 
    'sound', 'light', 'color', 'spectrum', 'optics', 'laser', 'photon', 'electron', 'neutron', 'proton', 'atom', 
    'molecule', 'compound', 'element', 'periodic table', 'metal', 'nonmetal', 'metalloid', 'alloy', 'mixture', 
    'solution', 'suspension', 'colloid', 'acid', 'base', 'salt', 'ph', 'reaction', 'reactant', 'product', 
    'catalyst', 'enzyme', 'kinetics', 'thermodynamics', 'entropy', 'enthalpy', 'gibbs free energy', 'equilibrium', 
    'redox', 'oxidation', 'reduction', 'electrolysis', 'battery', 'cell', 'corrosion', 'rust', 'galvanize', 
    'plate', 'electroplate', 'anode', 'cathode', 'electrolyte', 'ion', 'isotope', 'radioactivity', 'radiation', 
    'fission', 'fusion', 'nuclear', 'atomic', 'bomb', 'weapon', 'warhead', 'missile', 'rocket', 'torpedo', 
    'bullet', 'gun', 'rifle', 'pistol', 'revolver', 'shotgun', 'cannon', 'artillery', 'mortar', 'grenade', 
    'mine', 'bomb', 'explosive', 'dynamite', 'tnt', 'c4', 'semtex', 'nitroglycerin', 'gunpowder', 'cordite', 
    'primer', 'fuse', 'detonator', 'timer', 'trigger', 'switch', 'sensor', 'detector', 'radar', 'sonar', 'lidar', 
    'laser', 'infrared', 'ultraviolet', 'x-ray', 'gamma ray', 'microwave', 'radio wave', 'broadcast', 
    'transmission', 'reception', 'antenna', 'dish', 'cable', 'wire', 'fiber', 'optic', 'network', 'router', 
    'switch', 'hub', 'modem', 'gateway', 'firewall', 'server', 'client', 'peer', 'host', 'node', 'link', 
    'connection', 'bandwidth', 'throughput', 'latency', 'lag', 'ping', 'packet', 'frame', 'datagram', 'segment', 
    'bit', 'byte', 'kilobyte', 'megabyte', 'gigabyte', 'terabyte', 'petabyte', 'exabyte', 'zettabyte', 'yottabyte', 
    'binary', 'hexadecimal', 'octal', 'decimal', 'number', 'digit', 'integer', 'float', 'double', 'char', 
    'string', 'boolean', 'true', 'false', 'null', 'void', 'undefined', 'nan', 'infinity', 'class', 'object', 
    'method', 'function', 'procedure', 'subroutine', 'library', 'module', 'package', 'namespace', 'interface', 
    'api', 'sdk', 'ide', 'compiler', 'interpreter', 'debugger', 'profiler', 'linker', 'loader', 'assembler', 
    'disassembler', 'editor', 'viewer', 'player', 'browser', 'client', 'server', 'engine', 'framework', 'platform', 
    'system', 'application', 'app', 'program', 'software', 'hardware', 'firmware', 'middleware', 'driver', 
    'kernel', 'shell', 'gui', 'cli', 'user', 'admin', 'root', 'guest', 'account', 'profile', 'settings', 
    'preferences', 'options', 'config', 'configuration', 'setup', 'install', 'uninstall', 'update', 'upgrade', 
    'patch', 'fix', 'bug', 'error', 'fault', 'failure', 'crash', 'hang', 'freeze', 'lock', 'deadlock', 'race', 
    'condition', 'exception', 'throw', 'catch', 'try', 'finally', 'block', 'scope', 'variable', 'constant', 
    'literal', 'expression', 'statement', 'declaration', 'definition', 'assignment', 'operator', 'operand', 
    'precedence', 'associativity', 'evaluation', 'execution', 'runtime', 'compile', 'time', 'build', 'make', 
    'deploy', 'release', 'version', 'revision', 'branch', 'trunk', 'tag', 'commit', 'checkout', 'update', 
    'merge', 'conflict', 'resolve', 'revert', 'rollback', 'log', 'history', 'diff', 'patch', 'issue', 'ticket', 
    'bug', 'report', 'feature', 'request', 'enhancement', 'task', 'todo', 'plan', 'schedule', 'timeline', 
    'deadline', 'milestone', 'deliverable', 'status', 'progress', 'report', 'meeting', 'agenda', 'minutes', 
    'action', 'item', 'decision', 'conclusion', 'summary', 'abstract', 'introduction', 'background', 'methodology', 
    'result', 'discussion', 'conclusion', 'reference', 'bibliography', 'citation', 'appendix', 'index', 'glossary', 
    'table', 'figure', 'chart', 'graph', 'diagram', 'image', 'picture', 'photo', 'drawing', 'sketch', 'map', 
    'plan', 'blueprint', 'layout', 'design', 'draft', 'mockup', 'prototype', 'model', 'simulation', 'test', 
    'experiment', 'trial', 'pilot', 'demo', 'sample', 'example', 'case', 'study', 'scenario', 'use', 'case', 
    'story', 'requirement', 'specification', 'standard', 'protocol', 'format', 'encoding', 'encryption', 
    'decryption', 'compression', 'decompression', 'archive', 'backup', 'restore', 'recovery', 'disaster', 
    'risk', 'threat', 'vulnerability', 'exploit', 'attack', 'defense', 'protection', 'security', 'privacy', 
    'anonymity', 'identity', 'authentication', 'authorization', 'access', 'control', 'permission', 'privilege', 
    'role', 'group', 'user', 'policy', 'rule', 'regulation', 'law', 'compliance', 'audit', 'monitor', 'log', 
    'alert', 'notification', 'alarm', 'warning', 'error', 'critical', 'fatal', 'debug', 'info', 'trace', 
    'verbose', 'silent', 'quiet', 'noise', 'signal', 'ratio', 'quality', 'integrity', 'availability', 
    'reliability', 'maintainability', 'portability', 'usability', 'accessibility', 'scalability', 'performance', 
    'efficiency', 'effectiveness', 'productivity', 'profitability', 'cost', 'benefit', 'value', 'price', 
    'expense', 'budget', 'finance', 'money', 'currency', 'exchange', 'market', 'trade', 'commerce', 'business', 
    'industry', 'economy', 'finance', 'banking', 'investment', 'stock', 'share', 'bond', 'option', 'future', 
    'derivative', 'asset', 'liability', 'equity', 'capital', 'revenue', 'income', 'profit', 'loss', 'margin', 
    'return', 'yield', 'interest', 'dividend', 'tax', 'levy', 'duty', 'tariff', 'fee', 'charge', 'fine', 
    'penalty', 'subsidy', 'grant', 'loan', 'credit', 'debit', 'balance', 'account', 'statement', 'invoice', 
    'bill', 'receipt', 'payment', 'transaction', 'transfer', 'withdrawal', 'deposit', 'check', 'cheque', 
    'cash', 'coin', 'note', 'bill', 'currency', 'exchange', 'rate', 'conversion', 'inflation', 'deflation', 
    'recession', 'depression', 'growth', 'development', 'expansion', 'contraction', 'boom', 'bust', 'cycle', 
    'trend', 'forecast', 'prediction', 'projection', 'estimate', 'guess', 'speculation', 'hypothesis', 'theory', 
    'model', 'law', 'principle', 'axiom', 'theorem', 'lemma', 'corollary', 'proof', 'evidence', 'fact', 
    'data', 'information', 'knowledge', 'wisdom', 'insight', 'understanding', 'meaning', 'context', 'semantics', 
    'syntax', 'grammar', 'language', 'speech', 'text', 'writing', 'script', 'code', 'cipher', 'cryptography', 
    'steganography', 'watermark', 'signature', 'fingerprint', 'biometrics', 'retina', 'iris', 'face', 'voice', 
    'palm', 'hand', 'geometry', 'vein', 'dna', 'typing', 'gait', 'odor', 'behavior', 'psychology', 'sociology', 
    'anthropology', 'archaeology', 'history', 'politics', 'government', 'democracy', 'republic', 'monarchy', 
    'dictatorship', 'communism', 'socialism', 'capitalism', 'liberalism', 'conservatism', 'libertarianism', 
    'anarchism', 'fascism', 'nationalism', 'patriotism', 'terrorism', 'war', 'peace', 'conflict', 'violence', 
    'aggression', 'defense', 'security', 'intelligence', 'espionage', 'spying', 'surveillance', 'reconnaissance', 
    'patrol', 'guard', 'police', 'crime', 'justice', 'law', 'order', 'court', 'trial', 'jury', 'judge', 
    'lawyer', 'attorney', 'prosecutor', 'defendant', 'plaintiff', 'witness', 'evidence', 'testimony', 'verdict', 
    'sentence', 'punishment', 'prison', 'jail', 'correction', 'rehabilitation', 'probation', 'parole', 'pardon', 
    'amnesty', 'asylum', 'refugee', 'immigration', 'emigration', 'migration', 'border', 'customs', 'visa', 
    'passport', 'citizenship', 'nationality', 'residence', 'domicile', 'address', 'location', 'position', 
    'coordinates', 'latitude', 'longitude', 'altitude', 'elevation', 'depth', 'height', 'width', 'length', 
    'area', 'volume', 'mass', 'weight', 'density', 'temperature', 'pressure', 'speed', 'velocity', 'acceleration', 
    'force', 'energy', 'power', 'work', 'heat', 'light', 'sound', 'electricity', 'magnetism', 'gravity', 
    'radiation', 'matter', 'antimatter', 'dark matter', 'dark energy', 'black hole', 'wormhole', 'big bang', 
    'inflation', 'expansion', 'contraction', 'collapse', 'singularity', 'event horizon', 'hawking radiation', 
    'string theory', 'quantum mechanics', 'relativity', 'standard model', 'grand unified theory', 'theory of everything'
]
# Filtering specifically for Science/Technology context as commonly found in news datasets (like AG News).
# This list is too broad (includes "law", "government", etc.). I should stick to the core ones I identified earlier.

core_scitech = [
    'technology', 'science', 'computer', 'internet', 'software', 'hardware', 'web', 'online', 'digital', 'cyber', 
    'wireless', 'mobile', 'robot', 'ai', 'nasa', 'space', 'astronomy', 'biology', 'physics', 'chemistry', 
    'genetics', 'dna', 'medical', 'medicine', 'health', 'disease', 'virus', 'vaccine', 'research', 'scientist', 
    'laboratory', 'gadget', 'device', 'electronics', 'video game', 'console', 'nintendo', 'sony', 'microsoft', 
    'google', 'apple', 'ibm', 'intel', 'linux', 'windows', 'mac', 'browser', 'search engine', 'yahoo', 'amazon', 
    'facebook', 'twitter', 'email', 'hacker', 'security', 'chip', 'server', 'database', 'network', 'wifi', 
    'gameboy', 'xbox', 'playstation', 'ipod', 'smartphone', 'laptop', 'desktop', 'screen', 'battery', 'energy', 
    'solar', 'nuclear', 'cell', 'telescope', 'microscope', 'nanotech', 'biotech', 'broadband', 'satellite', 'gps',
    'firefox', 'explorer', 'spam', 'spyware', 'malware', 'blog', 'blogger', 'myspace', 'youtube', 'itunes', 'mp3',
    'dvd', 'hdtv', 'lcd', 'plasma', 'voip', 'skype', 'telecom', 'phone', 'tech', 'supercomputer', 'mainframe'
]

# Adding some business terms to exclude or be careful with, but we just want to count Sci/Tech.
# If a title has "Apple" it's likely Sci/Tech unless it's "Apple posts profits" -> Business. 
# But in AG News, "Apple posts profits" might still be under Business.
# However, "Apple releases new iPod" -> Sci/Tech.
# The hint says "understand the meaning".
# I'll try to score them.

scitech_articles = []
for article in articles:
    text = (article['title'] + " " + article['description']).lower()
    
    # Check for core keywords
    is_scitech = False
    for kw in core_scitech:
        # strict matching might be better? e.g. "space" in "space for lease" (Business) vs "outer space" (Sci/Tech).
        # But "space" is strong signal.
        if kw in text:
            # refine "apple"
            if kw == 'apple' and ('profit' in text or 'stock' in text or 'share' in text or 'market' in text):
                continue # likely Business
            if kw == 'google' and ('profit' in text or 'stock' in text):
                continue
            
            is_scitech = True
            break
            
    if is_scitech:
        scitech_articles.append(article['title'])

print("__RESULT__:")
print(json.dumps({"count": len(scitech_articles), "total": len(articles), "titles": scitech_articles}))"""

env_args = {'var_function-call-272766112025871937': [{'author_id': '218'}], 'var_function-call-1129033257989242514': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-2517229971613781264': {'count': 111, 'ids': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}, 'var_function-call-5205776640490666422': [{'_id': '6944b5055d1fedd5e55e6c80', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944b5055d1fedd5e55e7431', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944b5055d1fedd5e55e76dc', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944b5055d1fedd5e55e776b', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944b5055d1fedd5e55e793b', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
