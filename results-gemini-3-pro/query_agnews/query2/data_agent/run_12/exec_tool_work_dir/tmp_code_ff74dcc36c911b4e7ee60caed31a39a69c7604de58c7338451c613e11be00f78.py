code = """import json
import re

file_path = locals()['var_function-call-4886813562768488833']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Keywords (include plurals and variations manually or handle via stemming)
scitech_keywords_base = [
    "science", "technology", "tech", "computer", "software", "hardware", 
    "internet", "web", "online", "digital", "mobile", "phone", "wireless", 
    "broadband", "network", "satellite", "space", "nasa", "astronomy", 
    "galaxy", "mars", "moon", "solar", "planet", "biology", "physics", 
    "chemistry", "research", "study", "lab", "scientist", "researcher", 
    "robot", "robotics", "ai", "artificial intelligence", "gadget", "device", 
    "innovation", "invent", "patent", "cyber", "hacker", "virus", "security", 
    "malware", "spyware", "linux", "windows", "mac", "os", "browser", 
    "firefox", "explorer", "chrome", "safari", "email", "spam", 
    "search engine", "google", "yahoo", "microsoft", "apple", "ibm", "intel", 
    "amd", "nvidia", "sony", "nintendo", "game", "gaming", "console", 
    "playstation", "xbox", "wii", "ipod", "iphone", "ipad", 
    "smartphone", "tablet", "laptop", "pc", "server", "cloud", "data", 
    "database", "programming", "code", "developer", "engineer", "biotech", 
    "genetics", "genome", "cloning", "stem cell", "dna", "medical", "medicine", 
    "drug", "treatment", "disease", "cancer", "aids", "hiv", "vaccine",
    "telecom", "telecommunication", "chip", "semiconductor", "electron", 
    "laser", "nano", "nuclear", "power", "energy", "engine", "motor", "battery",
    "gameboy", "star wars", "trek", "supernova", "asteroid", "shuttle", "mission",
    "probe", "orbit", "launch", "telescope", "hubble", "laboratory"
]

# Add plurals
scitech_keywords = set(scitech_keywords_base)
for k in scitech_keywords_base:
    scitech_keywords.add(k + "s")

business_keywords_base = [
    "stock", "market", "revenue", "profit", "earnings", "quarter", "fiscal", 
    "share", "dividend", "dow", "nasdaq", "economy", "trade", "business", 
    "company", "corporation", "merger", "acquisition", "buyout", "bank", 
    "finance", "financial", "investor", "investment", "sales", "retail", 
    "price", "rate", "inflation", "jobless", "unemployment", "fed", "deal", 
    "contract", "ceo", "cfo", "executive", "manager", "management"
]
business_keywords = set(business_keywords_base)
for k in business_keywords_base:
    business_keywords.add(k + "s")

sports_keywords_base = [
    "sport", "football", "baseball", "basketball", "hockey", "soccer",
    "tennis", "golf", "cricket", "rugby", "olympic", "match", "tournament", 
    "league", "cup", "championship", "champion", "win", "winner", "defeat", 
    "loss", "score", "team", "player", "coach", "athlete", "medal", "gold", 
    "silver", "bronze", "record", "season", "playoff", "super bowl", "nba", 
    "nfl", "mlb", "nhl", "fifa", "uefa", "wimbledon", "open", "race", 
    "racing", "driver", "f1", "nascar"
]
sports_keywords = set(sports_keywords_base)
for k in sports_keywords_base:
    sports_keywords.add(k + "s")

def classify(title, description):
    text = (title + " " + description).lower()
    # Replace non-alphanumeric with space
    clean_text = re.sub(r'[^a-z0-9]', ' ', text)
    words = set(clean_text.split())
    
    # Intersection
    common_scitech = words.intersection(scitech_keywords)
    common_business = words.intersection(business_keywords)
    common_sports = words.intersection(sports_keywords)
    
    # Scores (simple count)
    score_scitech = len(common_scitech)
    score_business = len(common_business)
    score_sports = len(common_sports)
    
    # Priority Logic
    # 1. Sports usually distinct. Exception: "game" in video games.
    # Note: "game" is in both lists? No, I didn't put "game" in scitech_base in this script?
    # I put "game" in scitech_base. "game" is also in sports logic usually.
    # Let's handle "game" specifically.
    
    # If "game" is in words, checks for video game clues.
    if "game" in words or "games" in words:
        if any(w in words for w in ["video", "console", "nintendo", "xbox", "playstation", "gameboy", "wii", "arcade", "computer", "software"]):
            score_scitech += 5 # Boost scitech
        else:
            score_sports += 1
            
    # NASA / Space -> Strong SciTech
    if any(w in words for w in ["nasa", "space", "orbit", "shuttle", "mission", "planet", "mars", "moon"]):
        score_scitech += 5

    # Tech companies -> Strong SciTech
    if any(w in words for w in ["microsoft", "google", "apple", "ibm", "intel", "sony", "nintendo"]):
        score_scitech += 3
        
    # Financial terms -> Strong Business
    if any(w in words for w in ["stock", "stocks", "market", "dow", "nasdaq", "revenue", "profit", "earnings", "dividend"]):
        score_business += 5

    # Compare scores
    # If SciTech > others
    if score_scitech > 0 and score_scitech >= score_business and score_scitech >= score_sports:
        # Tie breaking? 
        if score_scitech == score_business:
             # Business usually trumps if keywords are financial
             if any(w in words for w in ["stock", "revenue", "profit"]):
                 return "Business"
        return "Science/Technology"
    
    return "Other"

scitech_count = 0
total = len(articles)
log = []

for article in articles:
    cat = classify(article['title'], article['description'])
    if cat == "Science/Technology":
        scitech_count += 1
        log.append(article['title'])

print("__RESULT__:")
print(json.dumps({
    "count": scitech_count,
    "total": total,
    "fraction": scitech_count / total,
    "log": log
}))"""

env_args = {'var_function-call-8784467999572360964': [{'author_id': '218'}], 'var_function-call-3853221493662786704': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-14083081770532266708': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-6734003448664079557': [{'_id': '6944982956ccdb3becb80a54', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944982956ccdb3becb81205', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944982956ccdb3becb814b0', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944982956ccdb3becb8153f', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944982956ccdb3becb8170f', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-13071510309338053328': {'total_articles': 5, 'scitech_count': 0, 'fraction': 0.0, 'scitech_titles_preview': []}, 'var_function-call-7819209378570293198': [{'_id': '6944982956ccdb3becb80a54', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944982956ccdb3becb81205', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944982956ccdb3becb814b0', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944982956ccdb3becb8153f', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944982956ccdb3becb8170f', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-4886813562768488833': 'file_storage/function-call-4886813562768488833.json', 'var_function-call-5166366614870757283': {'total_articles': 111, 'scitech_count': 0, 'fraction': 0.0, 'scitech_titles_preview': []}, 'var_function-call-14196602069786120922': [{'title': 'GameBoy mini-games win prize', 'has_scitech': False, 'matched_scitech': [], 'has_business': False, 'matched_business': [], 'has_sports': False, 'matched_sports': []}, {'title': 'Bailey Tries WR', 'has_scitech': False, 'matched_scitech': [], 'has_business': False, 'matched_business': [], 'has_sports': False, 'matched_sports': []}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'has_scitech': False, 'matched_scitech': [], 'has_business': False, 'matched_business': [], 'has_sports': False, 'matched_sports': []}, {'title': 'Energy from waves  teenager wins science award', 'has_scitech': False, 'matched_scitech': [], 'has_business': False, 'matched_business': [], 'has_sports': False, 'matched_sports': []}, {'title': 'China #39;s appetite boosts BHP', 'has_scitech': False, 'matched_scitech': [], 'has_business': False, 'matched_business': [], 'has_sports': False, 'matched_sports': []}, {'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'has_scitech': False, 'matched_scitech': [], 'has_business': False, 'matched_business': [], 'has_sports': False, 'matched_sports': []}, {'title': 'Even in win, nasty vibes', 'has_scitech': False, 'matched_scitech': [], 'has_business': False, 'matched_business': [], 'has_sports': False, 'matched_sports': []}, {'title': 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'has_scitech': False, 'matched_scitech': [], 'has_business': False, 'matched_business': [], 'has_sports': False, 'matched_sports': []}, {'title': 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'has_scitech': False, 'matched_scitech': [], 'has_business': False, 'matched_business': [], 'has_sports': False, 'matched_sports': []}, {'title': 'Somalians sworn in', 'has_scitech': False, 'matched_scitech': [], 'has_business': False, 'matched_business': [], 'has_sports': False, 'matched_sports': []}], 'var_function-call-6668697395197668810': {'text': 'students win \\$100,000 in national team science competition lucie guo, motivated by the death of her grandfather in china before she was born, spent two summers doing research in a duke university laboratory.', 'has_science': True, 'regex_science': False}}

exec(code, env_args)
