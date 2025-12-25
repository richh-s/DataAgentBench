code = """import json
import re

file_path = locals()['var_function-call-7977597934112122912']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Keywords
keywords = {
    'Sci/Tech': {
        'science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 
        'digital', 'mobile', 'phone', 'wireless', 'broadband', 'network', 'server', 'data', 'chip', 'processor',
        'intel', 'microsoft', 'apple', 'google', 'ibm', 'oracle', 'linux', 'windows', 'virus', 'hacker', 'cyber',
        'security', 'nasa', 'space', 'orbit', 'planet', 'moon', 'mars', 'galaxy', 'telescope', 'astronomy', 
        'physicist', 'scientist', 'research', 'study', 'lab', 'experiment', 'biology', 'genetics', 'genome',
        'robot', 'ai', 'video', 'game', 'gameboy', 'nintendo', 'sony', 'xbox', 'console',
        'gadget', 'device', 'innovation', 'physics', 'medical', 'medicine', 'treatment', 'disease', 'drug',
        'engine', 'satellite', 'launch', 'astronaut', 'browser', 'email', 'spam', 'semiconductor', 'storage', 'solution',
        'probe', 'shuttle', 'mission', 'capsule', 'sun', 'solar'
    },
    'Sports': {
        'sport', 'sports', 'game', 'team', 'match', 'win', 'loss', 'score', 'player', 'coach', 'athlete', 'champion',
        'league', 'tournament', 'cup', 'olympic', 'medal', 'gold', 'silver', 'bronze', 'athens',
        'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'hockey', 'racing', 'cycling',
        'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'wta', 'atp', 'quarterback', 'pitcher', 'goalkeeper', 'stadium',
        'season', 'playoff', 'final', 'semi-final', 'record', 'sox', 'yankees', 'broncos', 'red' # 'red sox' split
    },
    'Business': {
        'business', 'market', 'stock', 'share', 'price', 'trade', 'economy', 'economic', 'finance', 'financial',
        'bank', 'investor', 'profit', 'revenue', 'earning', 'loss', 'sales', 'deal', 'merger', 'acquisition',
        'company', 'corp', 'inc', 'firm', 'industry', 'ceo', 'cfo', 'executive', 'manager', 'management',
        'dow', 'nasdaq', 'wall', 'street', 'dollar', 'euro', 'currency', 'inflation', 'rate', 'fed', 'treasury',
        'oil', 'gas', 'energy', 'barrel', 'bonds', 'audit', 'budget', 'forecast', 'growth', 'quarter'
    },
    'World': {
        'world', 'international', 'government', 'president', 'minister', 'leader', 'official', 'parliament',
        'congress', 'senate', 'law', 'court', 'judge', 'legal', 'police', 'crime', 'prison', 'war', 'peace',
        'military', 'army', 'troop', 'soldier', 'weapon', 'nuclear', 'bomb', 'blast', 'explosion', 'attack',
        'kill', 'dead', 'injured', 'disaster', 'storm', 'hurricane', 'flood', 'earthquake', 'tsunami',
        'election', 'vote', 'poll', 'campaign', 'candidate', 'party', 'iraq', 'iran', 'israel', 'palestinian',
        'china', 'russia', 'usa', 'un', 'united', 'nations', 'treaty', 'accord', 'foreign', 'security'
    }
}

# Note: "game" is in both Sci/Tech (video game) and Sports.
# Context is key. "video game" -> Sci/Tech. "football game" -> Sports.
# Set intersection won't handle phrases.
# I'll stick to single words for the set method, but handle phrases separately if needed.
# Actually, let's keep it simple. If "game" appears, it adds to both.
# But "video" adds to Sci/Tech. "football" adds to Sports.
# The one with more matches wins.

scitech_count = 0
total_count = len(articles)

for article in articles:
    text = (article.get('title', '') + " " + article.get('description', '')).lower()
    # Replace non-alphanumeric with space
    clean_text = re.sub(r'[^a-z0-9]', ' ', text)
    words = set(clean_text.split())
    
    scores = {cat: 0 for cat in keywords}
    
    for cat, kw_set in keywords.items():
        # intersection count
        common = words.intersection(kw_set)
        scores[cat] += len(common)
        
    # Heuristic adjustments based on specific strong phrases
    if 'video game' in text or 'gameboy' in text or 'nintendo' in text or 'sony' in text:
        scores['Sci/Tech'] += 2
    if 'olympic' in text or 'cup' in text or 'league' in text:
        scores['Sports'] += 2
    if 'wall street' in text or 'dow jones' in text:
        scores['Business'] += 2
    if 'prime minister' in text:
        scores['World'] += 2
        
    # Determine category
    max_score = -1
    best_cat = 'World' # Default
    
    # Priority: Sci/Tech > Business > Sports > World (Arbitrary, but helps tie-break)
    # Actually, let's just find the max.
    for cat in ['World', 'Sports', 'Business', 'Sci/Tech']:
        if scores[cat] > max_score:
            max_score = scores[cat]
            best_cat = cat
        elif scores[cat] == max_score:
            # Tie logic
            if cat == 'Sci/Tech' and best_cat == 'Business':
                # If tied between Sci/Tech and Business (e.g. tech company revenue)
                # If "revenue" or "profit" in words, prefer Business.
                if 'revenue' in words or 'profit' in words or 'stock' in words:
                    best_cat = 'Business'
                else:
                    best_cat = 'Sci/Tech'
    
    # If all 0, maybe check for 'computer' or 'science' substring?
    # Assuming the keyword sets are comprehensive enough.
    
    if best_cat == 'Sci/Tech':
        scitech_count += 1

fraction = scitech_count / total_count if total_count > 0 else 0

print("__RESULT__:")
print(json.dumps({
    "scitech_count": scitech_count,
    "total_count": total_count,
    "fraction": fraction
}))"""

env_args = {'var_function-call-8694871716275581722': [{'author_id': '218'}], 'var_function-call-18198061042153095051': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-16713519121916546610': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'limit': 10000}, 'var_function-call-7977597934112122912': 'file_storage/function-call-7977597934112122912.json', 'var_function-call-16897453581264574646': {'scitech_count': 0, 'total_count': 111, 'fraction': 0.0, 'debug_sample': []}, 'var_function-call-17672489239389811111': [{'id': '192', 'title': 'GameBoy mini-games win prize', 'scores': {'Sci/Tech': 0, 'Sports': 0, 'Business': 0, 'World': 0}, 'matches': {'Sci/Tech': [], 'Sports': [], 'Business': [], 'World': []}}, {'id': '2161', 'title': 'Bailey Tries WR', 'scores': {'Sci/Tech': 0, 'Sports': 0, 'Business': 0, 'World': 0}, 'matches': {'Sci/Tech': [], 'Sports': [], 'Business': [], 'World': []}}, {'id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'scores': {'Sci/Tech': 0, 'Sports': 0, 'Business': 0, 'World': 0}, 'matches': {'Sci/Tech': [], 'Sports': [], 'Business': [], 'World': []}}, {'id': '2987', 'title': 'Energy from waves  teenager wins science award', 'scores': {'Sci/Tech': 0, 'Sports': 0, 'Business': 0, 'World': 0}, 'matches': {'Sci/Tech': [], 'Sports': [], 'Business': [], 'World': []}}, {'id': '3451', 'title': 'China #39;s appetite boosts BHP', 'scores': {'Sci/Tech': 0, 'Sports': 0, 'Business': 0, 'World': 0}, 'matches': {'Sci/Tech': [], 'Sports': [], 'Business': [], 'World': []}}, {'id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'scores': {'Sci/Tech': 0, 'Sports': 0, 'Business': 0, 'World': 0}, 'matches': {'Sci/Tech': [], 'Sports': [], 'Business': [], 'World': []}}, {'id': '4447', 'title': 'Even in win, nasty vibes', 'scores': {'Sci/Tech': 0, 'Sports': 0, 'Business': 0, 'World': 0}, 'matches': {'Sci/Tech': [], 'Sports': [], 'Business': [], 'World': []}}, {'id': '5354', 'title': 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'scores': {'Sci/Tech': 0, 'Sports': 0, 'Business': 0, 'World': 0}, 'matches': {'Sci/Tech': [], 'Sports': [], 'Business': [], 'World': []}}, {'id': '6705', 'title': 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'scores': {'Sci/Tech': 0, 'Sports': 0, 'Business': 0, 'World': 0}, 'matches': {'Sci/Tech': [], 'Sports': [], 'Business': [], 'World': []}}, {'id': '6869', 'title': 'Somalians sworn in', 'scores': {'Sci/Tech': 0, 'Sports': 0, 'Business': 0, 'World': 0}, 'matches': {'Sci/Tech': [], 'Sports': [], 'Business': [], 'World': []}}], 'var_function-call-3331323504029839669': {'text_preview': 'gameboy mini-games win prize a set of gameboy micro-games is named as the most innovative game of the year at a festival in scotland.', 'has_gameboy': True, 'has_win': True}}

exec(code, env_args)
