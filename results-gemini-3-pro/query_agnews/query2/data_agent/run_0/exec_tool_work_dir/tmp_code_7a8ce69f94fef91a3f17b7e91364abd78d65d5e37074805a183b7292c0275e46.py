code = """import json
import re

# Load the articles
# results from the second tool call (MongoDB query)
# The variable name is var_function-call-16257297644781231984
data_source = locals()['var_function-call-16257297644781231984']

if isinstance(data_source, str) and data_source.endswith('.json'):
    with open(data_source, 'r') as f:
        articles = json.load(f)
else:
    articles = data_source

# Keywords for Science/Technology
st_keywords = [
    'science', 'technology', 'tech', 'computer', 'software', 'hardware', 
    'internet', 'web', 'online', 'digital', 'mobile', 'phone', 'wireless', 
    'broadband', 'network', 'satellite', 'space', 'nasa', 'astronomy', 
    'galaxy', 'planet', 'mars', 'orbit', 'robot', 'ai', 'artificial intelligence', 
    'gadget', 'device', 'chip', 'processor', 'microsoft', 'google', 'apple', 
    'ibm', 'intel', 'linux', 'windows', 'mac', 'ios', 'android', 'video game', 
    'gaming', 'nintendo', 'sony', 'playstation', 'xbox', 'gameboy', 'hacker', 
    'virus', 'security', 'cyber', 'data', 'server', 'cloud', 'program', 'code', 
    'app', 'browser', 'search engine', 'email', 'spam', 'blog', 'social media', 
    'facebook', 'twitter', 'amazon', 'ebay', 'yahoo', 'telecom', 'physics', 
    'biology', 'chemistry', 'genetics', 'genome', 'medical', 'research', 'lab', 
    'scientist', 'engineer', 'innovation', 'ipod', 'itunes', 'firefox', 'explorer',
    'semiconductor', 'lcd', 'plasma', 'dvd', 'mp3', 'gps', 'biotech', 'cloning',
    'stem cell', 'supercomputer', 'nanotech'
]

# Keywords for other categories to disambiguate if needed (simple check first)
# Actually, let's score each category and pick the max, or just check if S/T score > threshold?
# Given the prompt implies binary "belong to S/T", I will count S/T keywords.
# However, "Apple" could be a fruit (unlikely in news) or company (Business vs Tech). 
# "Amazon" (Business vs Tech). 
# Usually, tech companies are classified under S/T in these datasets, or Business.
# Let's look at the sample:
# "GameBoy mini-games win prize" -> S/T
# "Students Win ... Science Competition" -> S/T
# "Energy from waves ... science award" -> S/T
# "China's appetite boosts BHP" -> Business (BHP is mining)

# Let's try to classify based on "Science" or "Technology" presence, and strong tech terms.

def is_science_tech(text):
    text = text.lower()
    # Check for strong indicators
    count = 0
    for kw in st_keywords:
        if kw in text:
            count += 1
    
    # Negative keywords to avoid false positives (e.g. "Space" in "Office Space" business news? Unlikely)
    # "Game" is tricky. "Game" in sports vs "Video Game".
    if "game" in text:
        if any(x in text for x in ["video", "console", "nintendo", "sony", "xbox", "computer", "mobile", "online", "software"]):
            count += 1 # Boost for video games
        elif any(x in text for x in ["football", "soccer", "baseball", "basketball", "sport", "coach", "team", "cup", "league"]):
            count -= 1 # Likely sports
    
    return count > 0

# Let's refine the classification. A better way is to see which category has the MOST keywords.
# I will define keywords for all 4 categories.

categories = {
    "Science/Technology": st_keywords,
    "Sports": ['sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'olympic', 'championship', 'tournament', 'league', 'cup', 'medal', 'player', 'coach', 'team', 'athlete', 'stadium', 'match', 'score', 'win', 'loss', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'wimbledon', 'nascar', 'f1', 'racing', 'cricket', 'rugby'],
    "Business": ['business', 'economy', 'market', 'stock', 'trade', 'company', 'profit', 'loss', 'bank', 'finance', 'dollar', 'euro', 'yen', 'currency', 'oil', 'gas', 'energy', 'price', 'corp', 'inc', 'ltd', 'investment', 'investor', 'share', 'revenue', 'sales', 'deal', 'merger', 'acquisition', 'ceo', 'cfo', 'manager', 'executive', 'industry', 'manufacturing', 'retail', 'inflation', 'fed', 'rates', 'wall street', 'dow jones', 'nasdaq'],
    "World": ['world', 'war', 'peace', 'politics', 'president', 'minister', 'government', 'country', 'nation', 'iraq', 'iran', 'china', 'usa', 'america', 'uk', 'britain', 'eu', 'europe', 'un', 'united nations', 'treaty', 'election', 'vote', 'poll', 'military', 'army', 'police', 'attack', 'bomb', 'blast', 'terrorism', 'terrorist', 'disaster', 'quake', 'tsunami', 'storm', 'hurricane', 'flood', 'kill', 'die', 'death', 'hostage', 'baghdad', 'kabul', 'gaza', 'israel', 'palestine', 'nuclear']
}

def categorize(title, desc):
    text = (title + " " + desc).lower()
    scores = {cat: 0 for cat in categories}
    
    for cat, kws in categories.items():
        for kw in kws:
            # simple substring check? Or word boundary?
            # substring is easier but riskier. "manager" in "file manager" (tech).
            # "oil" in "soil" (irrelevant).
            # Let's use regex for word boundaries for short words.
            if len(kw) <= 4:
                if re.search(r'\b' + re.escape(kw) + r'\b', text):
                    scores[cat] += 1
            else:
                if kw in text:
                    scores[cat] += 1
    
    # Specific adjustments
    if "game" in text:
        if any(x in text for x in ["video", "console", "nintendo", "sony", "xbox", "computer", "software", "tech", "gaming"]):
            scores["Science/Technology"] += 2
        if any(x in text for x in ["sport", "football", "soccer", "team", "league", "cup"]):
            scores["Sports"] += 2
            
    if "oil" in text or "gas" in text:
         scores["Business"] += 1
         
    if "microsoft" in text or "google" in text or "internet" in text:
        scores["Science/Technology"] += 2

    # Determine max score
    if sum(scores.values()) == 0:
        return "Unknown"
    
    return max(scores, key=scores.get)

st_count = 0
total = 0
results_list = []

for article in articles:
    total += 1
    cat = categorize(article.get('title', ''), article.get('description', ''))
    if cat == "Science/Technology":
        st_count += 1
        results_list.append((article.get('title'), "ST"))
    else:
        results_list.append((article.get('title'), cat))

fraction = st_count / total if total > 0 else 0

print("__RESULT__:")
print(json.dumps({"st_count": st_count, "total": total, "fraction": fraction, "sample_classifications": results_list[:10]}))"""

env_args = {'var_function-call-15392532606870454627': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-13831368158755182800': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'projection': {'_id': 0, 'title': 1, 'description': 1}}, 'var_function-call-16257297644781231984': [{'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
