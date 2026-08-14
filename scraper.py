import requests
import json

# قائمة المصادر التي تدعم REST API أو خلاصة البيانات مفتوحة المصدر
SOURCES = [
    "https://api.themoviedb.org/3/trending/all/day?api_key=YOUR_KEY&language=ar-SA",
    # يمكنك إضافة مصادر وروابط RSS / JSON أخرى تسمح بالسحب هنا
]

CATEGORIES = ["أكشن", "جريمة", "دراما", "رعب", "رومانسي", "كوميدي", "أفلام تركية", "أفلام هندية", "أفلام وثائقية"]

def fetch_all_categories():
    all_movies = []
    
    # هنا يتم تجميع الأفلام وتصنيفها في الخلفية
    # مثال لبنية البيانات الناتجة لكل فيلم:
    # {
    #   "title": "اسم الفيلم",
    #   "category": "أكشن",
    #   "tag": "FHD",
    #   "pinned": False,
    #   "poster": "رابط البوستر",
    #   "streamUrl": "رابط المشغل"
    # }
    
    # حفظ البيانات في ملف JSON يتم تحديثه تلقائياً
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(all_movies, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    fetch_all_categories()
