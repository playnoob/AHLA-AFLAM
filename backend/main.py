from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Ahla Aflam API")

# تفعيل CORS لتمكين صفحة index.html من الاتصال بالخادم بدون قيود متصفح
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# بيانات تجريبية تحتوي على التصنيفات والبلد والتقييم العمري
movies_db = [
    {
        "id": 1,
        "title": "مغامرات الغابة",
        "category": "أفلام كرتون",
        "genre": "أنيميشن",
        "country": "أمريكي",
        "age_rating": "عائلي",
        "year": 2026,
        "quality": "WEB-DL",
        "poster": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=500"
    },
    {
        "id": 2,
        "title": "الهروب الكبير",
        "category": "أفلام أجنبي",
        "genre": "إثارة وغموض",
        "country": "كوري",
        "age_rating": "+18",
        "year": 2026,
        "quality": "BluRay",
        "poster": "https://images.unsplash.com/photo-1509347528160-9a9e33742cdb?w=500"
    },
    {
        "id": 3,
        "title": "حرب الفضاء",
        "category": "مسلسلات أجنبي",
        "genre": "خيال علمي",
        "country": "أمريكي",
        "age_rating": "+13",
        "year": 2026,
        "quality": "HD",
        "poster": "https://images.unsplash.com/photo-1535016120720-40c746a6580c?w=500"
    }
]

@app.get("/")
def home():
    return {"status": "online", "message": "خادم أحلى أفلام يعمل بنجاح!"}

@app.get("/api/movies")
def get_movies():
    return movies_db