from django.shortcuts import render
from datetime import date
from .models import Post

# Create your views here.

all_posts = [
    {
        "slug": "Rajasthan-tour",
        "image": "rajasthan.jpg",
        "author": "Om Deshmukh",
        "date": date(2023, 12, 12),
        "title": "Rajasthan Tour",
        "excerpt": "These cities of Rajasthan are not just places on a map; they are living embodiments of India's rich cultural heritage, offering a tapestry of forts, temples, and landscapes that weave together the story of a land steeped in tradition and history.",
        "content": """
Jaipur, the Pink City of Rajasthan, captivates with its grandeur and history. Adorned with palaces, including the iconic Hawa Mahal, and the majestic Amber Fort, it is a testament to the region's royal legacy. Jodhpur, the Blue City, boasts the towering Mehrangarh Fort, offering panoramic views of the city's azure hues. Its narrow streets and vibrant markets pulse with life, showcasing the essence of Rajasthan's cultural richness.

Ajmer, a city revered by both Hindus and Muslims, is home to the Ajmer Sharif Dargah, a Sufi shrine dedicated to Khwaja Moinuddin Chishti. Jaisalmer, the Golden City, rises from the Thar Desert like a mirage, with its golden-hued sandstone architecture and the formidable Jaisalmer Fort, known as the Sonar Quila.

Pushkar, nestled beside a tranquil lake, holds spiritual significance with its Brahma Temple, one of the few in the world dedicated to Lord Brahma. Its annual camel fair attracts travelers from far and wide, adding to the city's vibrant charm.

These cities of Rajasthan are not just places on a map; they are living embodiments of India's rich cultural heritage, offering a tapestry of forts, temples, and landscapes that weave together the story of a land steeped in tradition and history.
""",
    },
    {
        "slug": "MP_tour",
        "image": "mahakal.jpg",
        "author": "Maximilian",
        "date": date(2023, 12, 12),
        "title": "MP tour",
        "excerpt": "Indore, the bustling commercial hub of Madhya Pradesh, seamlessly blends tradition with modernity. Its bustling markets, iconic Rajwada Palace, and delectable cuisine reflect the city's rich cultural heritage.",
        "content": """
Ujjain, situated on the banks of the Shipra River, is a city of spiritual significance in Madhya Pradesh, India. Its crowning jewel is the revered Mahakaleshwar Temple, dedicated to Lord Shiva, drawing pilgrims worldwide for its sacred aura and the renowned Bhasma Aarti ceremony. Omkareshwar, nestled in the Narmada River, hosts another esteemed Jyotirlinga shrine of Lord Shiva, offering seekers a tranquil retreat amidst natural beauty.

Indore, the bustling commercial hub of Madhya Pradesh, seamlessly blends tradition with modernity. Its bustling markets, iconic Rajwada Palace, and delectable cuisine reflect the city's rich cultural heritage.

Madhya Pradesh's temples, including those in Ujjain and Omkareshwar, are not just religious landmarks but also cultural treasures, symbolizing centuries of devotion and architectural brilliance. Each site tells a story, inviting visitors to explore the depths of spirituality and history.

Together, these destinations form a tapestry of spirituality, culture, and heritage, inviting travelers to immerse themselves in the essence of Madhya Pradesh's soul.
""",
    },
    {
        "slug": "Kerala_tour",
        "image": "kerala.jpeg",
        "author": "Om Deshmukh",
        "date": date(2023, 12, 12),
        "title": "Kerala tour",
        "excerpt": "Kerala's temple festivals, known as 'Utsavams,' are vibrant celebrations of music, dance, and rituals, reflecting the state's cultural vibrancy. The temples themselves often serve as centers of community life, fostering traditions and rituals that have been passed down through generations",
        "content": """
Kerala, often referred to as "God's Own Country," is a land of enchanting beauty and spiritual fervor. Its geography is characterized by lush greenery, tranquil backwaters, and pristine beaches that fringe the Arabian Sea. Amidst this natural splendor, Kerala is home to a myriad of temples that add to its cultural richness.

The state is dotted with temples of architectural magnificence and spiritual significance. The Padmanabhaswamy Temple in Thiruvananthapuram, dedicated to Lord Vishnu, stands out for its Dravidian architecture and treasures. The Guruvayur Temple in Thrissur, dedicated to Lord Krishna, is another revered site visited by devotees from across the globe. The Sabarimala Temple, nestled in the Western Ghats, is famed for its annual pilgrimage, drawing millions of devotees.

Kerala's temple festivals, known as "Utsavams," are vibrant celebrations of music, dance, and rituals, reflecting the state's cultural vibrancy. The temples themselves often serve as centers of community life, fostering traditions and rituals that have been passed down through generations.

From the misty hills of Munnar to the tranquil backwaters of Alleppey, Kerala's temples and geography weave together a tapestry of spirituality and natural beauty, making it a destination that truly resonates with the soul.
""",
    },
]


def get_date(post):
    return post["date"]


def startingpage(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})
