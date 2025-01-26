import wikipediaapi
import re
from collections import Counter

def fetch_german_wikipedia_articles(keywords, num_articles=5):
    user_agent = "YourCustomUserAgent/1.0 (xyz@domain.com)"  # Kendi User-Agent'ini buraya yaz
    wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language='de')

    all_text = ""

    for keyword in keywords:
        page = wiki.page(keyword)
        if page.exists():
            print(f"Makale bulundu: {keyword}")
            all_text += page.text + "\n\n"
        else:
            print(f"Makale bulunamadı: {keyword}")

    return all_text

def clean_text(text):
    """
    Metindeki gereksiz karakterleri temizler ve sadece Almanca kelimeleri bırakır.
    """
    text = text.lower()
    words = re.findall(r'\b[a-zäöüß]+\b', text)
    return words

def analyze_word_frequency(text, output_path, top_n=10000):
    """
    Metni analiz edip en sık kullanılan kelimeleri sıralayarak bir dosyaya kaydeder.
    """
    words = clean_text(text)
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(top_n)

    with open(output_path, 'w', encoding='utf-8') as file:
        for word, freq in most_common_words:
            file.write(f"{word}: {freq}\n")

    print(f"En sık kullanılan {top_n} kelime '{output_path}' dosyasına kaydedildi.")

keywords = ["Deutschland", "Technologie", "Geschichte", "Kultur", "Wissenschaft"]

german_text = fetch_german_wikipedia_articles(keywords)

with open("german_text.txt", "w", encoding="utf-8") as file:
    file.write(german_text)

analyze_word_frequency(german_text, "top_10000_words.txt")
