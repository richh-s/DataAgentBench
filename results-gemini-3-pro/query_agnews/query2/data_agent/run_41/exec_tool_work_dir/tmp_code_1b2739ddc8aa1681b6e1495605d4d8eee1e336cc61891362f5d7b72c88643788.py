code = """import json
import re

with open(locals()['var_function-call-6280066398469303272'], 'r') as f:
    articles = json.load(f)

scitech_titles = []

# Keywords
tech_kw = set([
    'technology', 'science', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'digital', 'wireless', 'mobile',
    'robot', 'ai', 'nasa', 'space', 'astronomy', 'biology', 'physics', 'chemistry', 'genetics', 'medical', 'health', 'disease',
    'research', 'scientist', 'gadget', 'device', 'electronics', 'video game', 'console', 'nintendo', 'sony', 'microsoft',
    'google', 'apple', 'ibm', 'intel', 'linux', 'windows', 'browser', 'yahoo', 'amazon', 'facebook', 'email', 'hacker',
    'security', 'chip', 'server', 'network', 'wifi', 'xbox', 'playstation', 'ipod', 'smartphone', 'laptop', 'energy', 'solar',
    'satellite', 'gps', 'biotech', 'nanotech', 'telecom', 'broadband', 'mp3', 'dvd', 'voip', 'skype', 'tech', 'virus', 'spam',
    'malware', 'blog', 'itunes', 'pc', 'mac', 'monitor', 'screen', 'battery', 'cell', 'genome', 'stem cell', 'cloning', 'mars',
    'shuttle', 'station', 'telescope', 'microscope', 'lab', 'laboratory', 'experiment', 'innovation', 'invention', 'engine',
    'cyber', 'pixel', 'resolution', 'format', 'usb', 'bluetooth', 'app', 'application', 'code', 'coding', 'program', 'developer'
])

business_strong = set([
    'stock', 'share', 'market', 'profit', 'revenue', 'earnings', 'invest', 'trade', 'deal', 'merger', 'acquisition', 'buyout',
    'ipo', 'ceo', 'cfo', 'bank', 'fund', 'financial', 'economy', 'business', 'sales', 'retail', 'dow', 'nasdaq', 'wall street',
    'dividend', 'currency', 'dollar', 'euro', 'oil', 'gas', 'price', 'cost', 'expense', 'bid', 'offer', 'acquire', 'sell',
    'billion', 'million', 'quarter', 'fiscal', 'debt', 'loan', 'growth', 'rate', 'inflation', 'fed', 'treasury'
])

sports_strong = set([
    'sport', 'game', 'team', 'player', 'coach', 'manager', 'cup', 'league', 'championship', 'tournament', 'win', 'loss',
    'victory', 'defeat', 'score', 'goal', 'point', 'medal', 'olympic', 'football', 'soccer', 'basketball', 'baseball',
    'tennis', 'golf', 'cricket', 'rugby', 'hockey', 'boxing', 'racing', 'driver', 'match', 'season', 'club', 'stadium',
    'liverpool', 'arsenal', 'manchester', 'red sox', 'yankees', 'broncos', 'cowboys', 'lakers', 'bulls', 'knicks',
    'united', 'real madrid', 'barcelona', 'ac milan', 'juventus', 'chelsea', 'bayern', 'fifa', 'nfl', 'nba', 'mlb', 'nhl'
])

world_strong = set([
    'government', 'president', 'minister', 'leader', 'election', 'vote', 'parliament', 'congress', 'senate', 'law', 'court',
    'trial', 'judge', 'police', 'crime', 'war', 'military', 'soldier', 'bomb', 'attack', 'terror', 'kill', 'die', 'dead',
    'injury', 'wound', 'iraq', 'iran', 'afghanistan', 'israel', 'palestine', 'un', 'united nations', 'bush', 'kerry',
    'blair', 'putin', 'china', 'russia', 'japan', 'france', 'germany', 'uk', 'britain', 'prime minister', 'official',
    'authority', 'strike', 'protest', 'riot', 'disaster', 'crash', 'storm', 'hurricane', 'earthquake'
])

for article in articles:
    title = article.get('title', '')
    desc = article.get('description', '')
    text = (title + " " + desc).lower()
    tokens = re.findall(r'[a-z]+', text)
    
    # Scores
    s_tech = 0
    s_bus = 0
    s_sport = 0
    s_world = 0
    
    for t in tokens:
        if t in tech_kw: s_tech += 1
        if t in business_strong: s_bus += 1
        if t in sports_strong: s_sport += 1
        if t in world_strong: s_world += 1
        
    # Context adjustments
    if 'video game' in text or 'computer game' in text:
        s_tech += 3
        s_sport -= 1 # mitigate "game"
    
    if 'oil' in tokens and ('price' in tokens or 'market' in tokens):
        s_bus += 3
        
    # Tech company + financial term -> Business
    # e.g. "Intel revenue"
    tech_companies = ['intel', 'microsoft', 'google', 'apple', 'ibm', 'cisco', 'oracle', 'hp', 'dell', 'sony', 'nintendo', 'ebay', 'amazon', 'yahoo']
    has_tech_company = any(tc in tokens for tc in tech_companies)
    if has_tech_company and s_bus > 0:
        s_bus += 2 # Boost business if tech company + profit/loss etc.
        
    # NASA -> Tech
    if 'nasa' in tokens: s_tech += 5
    
    # Categorize
    # Check if Tech is dominant
    if s_tech > 0:
        if s_tech >= s_bus and s_tech >= s_sport and s_tech >= s_world:
            # Check for close calls
            # "Liverpool prepares for life" -> s_sport should be high due to "liverpool" (if added), "prepares"?
            # My list has "liverpool".
            if s_sport >= s_tech:
                pass # Sport
            elif s_bus > s_tech: # Strong business
                pass
            elif s_world > s_tech:
                pass
            else:
                scitech_titles.append(title)
        else:
            # Tech is present but not dominant
            pass

print("__RESULT__:")
print(json.dumps({"count": len(scitech_titles), "titles": scitech_titles}))"""

env_args = {'var_function-call-272766112025871937': [{'author_id': '218'}], 'var_function-call-1129033257989242514': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-2517229971613781264': {'count': 111, 'ids': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}, 'var_function-call-5205776640490666422': [{'_id': '6944b5055d1fedd5e55e6c80', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944b5055d1fedd5e55e7431', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944b5055d1fedd5e55e76dc', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944b5055d1fedd5e55e776b', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944b5055d1fedd5e55e793b', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-15430713433211264809': {'count': 4, 'total': 5, 'titles': ['GameBoy mini-games win prize', 'Bailey Tries WR', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award']}, 'var_function-call-13974877051957634948': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966'], 'var_function-call-2361739143471268052': [], 'var_function-call-6280066398469303272': 'file_storage/function-call-6280066398469303272.json', 'var_function-call-242255182868878882': {'count': 26, 'total': 111, 'titles': ['GameBoy mini-games win prize', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'In Iraq, a Quest to Rebuild One More Broken Edifice: Science', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Shuttle repair price tag soars', 'Microsoft settles with UK phone maker', 'EMC Unveils E-mail Storage For Microsoft Exchange', 'Liverpool prepares for life without Gerrard', 'Ex-Astronaut Casts Doubt on Space Tourism', 'Diabetes delay adds to AstraZeneca #39;s ills', 'Texas Instruments Posts Higher 3Q Profits (AP)', 'FCC Approves Merger, Wireless Giant Created', 'Satellite write-downs widen DirecTV #39;s loss', 'Backs off drastic fare  amp; service plans', 'Why I had to leave Australia', 'Revealed: why the fear factor runs with the pack', 'Ontario to dedicate  #36;12.5 million to water studies and watershed protection (Canadian Press)', 'HP to launch  #39;virus-throttling #39; software', 'XM CEO Sees Satellite Radio on Cell Phones', "EBay Adds 'Want It Now' Feature (Reuters)", 'Chinese Firm To Buy IBM #39;s PC Business For \\$1.75 Billion', 'Paypal and Apple iTunes link-up', 'US mobile groups confirm merger', 'Bush Ordering Better Ocean Oversight (AP)', 'Log on to be a satellite spy']}}

exec(code, env_args)
