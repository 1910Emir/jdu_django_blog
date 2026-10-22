Mavzu: Blog boshqaruv tizimi (Blog Application).

Modellar:

Post (title, content, category, image, created_at, updated_at).

Category (name, slug).

Sahifalar:

Bosh sahifa va postlar ro'yxati (/posts/).

Postning batafsil sahifasi (/posts/<id>/).

Yangi post yaratish formasi (/posts/new/).

Postni tahrirlash formasi (/posts/<id>/edit/).

Autentifikatsiya sahifalari (/login/, /logout/, /register/).

Foydalanuvchi rollari:

Oddiy mehmon (Anonim): Postlar ro'yxati va batafsil sahifasini o'qiy oladi.

Tizim foydalanuvchisi (Muallif): Yangi post yaratishi va tahrirlashi mumkin.

Admin (Superuser): Django admin paneli orqali barcha postlar va kategoriyalarni to'liq boshqaradi.