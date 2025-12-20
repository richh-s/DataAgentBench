code = """import json
import re

# Load the articles from the file path provided in the previous step
file_path = locals()['var_function-call-13227321165050657980']
# The previous result was a direct list if small, or a file path if large.
# The system message said "If a tool result is large, the next message will include a preview... and the storage entry will be the .json file path".
# However, the preview was shown, but it didn't explicitly say "The result is stored in file: ...". 
# Wait, looking at the previous tool output: "The result is stored under key: var_function-call-13227321165050657980".
# And the content displayed was a list `[...]` but it was truncated in my thought simulation? 
# Actually, the user message said "The result is: [...]" and provided a few items. It's likely the full list.
# But wait, the list in the prompt has ~127 items. The preview had 5 items.
# Let's check if the variable is a list or a string (path).
# The system instruction says: "If a tool result is large... the storage entry will be the .json file path (a string)".
# The variable `var_function-call-13227321165050657980` in the `locals()` might be the list itself if it wasn't too large?
# Or it might be a string path.
# I'll check the type.

data = locals()['var_function-call-13227321165050657980']
if isinstance(data, str):
    # It's a file path
    with open(data, 'r') as f:
        articles = json.load(f)
else:
    # It's the data itself
    articles = data

# Categories and keywords
categories = {
    "Science/Technology": [
        "science", "technology", "tech", "computer", "internet", "web", "software", "hardware", "chip", "phone", 
        "mobile", "wireless", "network", "satellite", "space", "nasa", "astronomy", "robot", "gadget", "device", 
        "innovation", "physics", "biology", "chemistry", "genetics", "research", "lab", "scientist", "discovery", 
        "study", "medical", "drug", "cancer", "disease", "health", "microsoft", "google", "apple", "intel", "linux", 
        "windows", "sony", "nintendo", "gameboy", "xbox", "playstation", "wii", "video game", "console", "browser", 
        "server", "data", "digital", "cyber", "virus", "hacker", "security", "online", "email", "spam", "blog", 
        "search engine", "mp3", "ipod", "dvd", "hdtv", "gps", "battery", "engine", "automotive", "ev", "electric vehicle"
    ],
    "Sports": [
        "sport", "football", "soccer", "baseball", "basketball", "cricket", "rugby", "hockey", "tennis", "golf", 
        "boxing", "f1", "racing", "motorsport", "olympics", "athlete", "player", "team", "coach", "manager", 
        "club", "league", "tournament", "championship", "match", "score", "win", "loss", "draw", "cup", "medal", 
        "stadium", "wimbledon", "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "super bowl", "world cup", "grand slam"
    ],
    "Business": [
        "business", "finance", "economy", "market", "stock", "share", "trade", "industry", "company", "corporate", 
        "firm", "profit", "revenue", "loss", "invest", "bank", "imf", "wto", "dollar", "euro", "oil", "gas", 
        "price", "cost", "sale", "deal", "merger", "acquisition", "ceo", "cfo", "chairman", "executive", 
        "employ", "job", "work", "strike", "union", "fed", "rate", "tax", "budget", "debt", "deficit", 
        "inflation", "recession", "growth", "nasdaq", "dow jones", "wall street"
    ],
    "World": [
        "world", "international", "politics", "government", "president", "minister", "premier", "senate", "congress", 
        "parliament", "election", "vote", "party", "democrat", "republican", "war", "peace", "military", "army", 
        "navy", "air force", "police", "crime", "court", "judge", "law", "legal", "prison", "jail", "attack", 
        "bomb", "blast", "terrorism", "terrorist", "rebel", "protest", "riot", "disaster", "earthquake", "tsunami", 
        "flood", "hurricane", "typhoon", "storm", "fire", "accident", "crash", "kill", "die", "dead", "injure", 
        "victim", "hostage", "kidnap", "nuclear", "weapon", "treaty", "agreement", "un", "united nations", "eu", 
        "european union", "nato", "country", "nation", "state", "region", "city", "town", "village", "border", "iraq", "afghanistan", "iran", "korea"
    ]
}

sci_tech_count = 0
total_articles = len(articles)

for article in articles:
    text = (article.get('title', '') + " " + article.get('description', '')).lower()
    
    scores = {cat: 0 for cat in categories}
    
    for cat, keywords in categories.items():
        for keyword in keywords:
            # Use regex to find whole words to avoid partial matches like 'win' in 'winter'
            if re.search(r'\b' + re.escape(keyword) + r'\b', text):
                scores[cat] += 1
    
    # Heuristic adjustments
    # If "game" appears, check context. But we have "video game", "gameboy" in SciTech and "match" in Sports.
    
    # Determine category with max score
    if sum(scores.values()) == 0:
        predicted_category = "Unknown"
    else:
        predicted_category = max(scores, key=scores.get)
    
    if predicted_category == "Science/Technology":
        sci_tech_count += 1

result = {
    "sci_tech_count": sci_tech_count,
    "total_articles": total_articles,
    "fraction": sci_tech_count / total_articles if total_articles > 0 else 0
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1250528354804147004': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-10631316298380501498': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-13227321165050657980': [{'_id': '6944a8bc539490c90ae0e94f', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944a8bc539490c90ae0f100', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944a8bc539490c90ae0f3ab', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944a8bc539490c90ae0f43a', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944a8bc539490c90ae0f60a', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
