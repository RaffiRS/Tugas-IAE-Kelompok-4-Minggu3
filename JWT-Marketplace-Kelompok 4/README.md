# JWT Marketplace API (Flask Modular)

# Kelompok 4 - IAE
# Anggota:
# 1. Casta Garneta
# 2. Putvi Indrisa Emylia Syahputri
# 3. Salsabil Salwa Putri Maharani
# 4. Raffi Raditya Sofwan

## 🚀 Cara Menjalankan
```bash
# 1. Aktifkan virtualenv
python -m venv venv
venv\Scripts\activate

# 2. Install dependensi
pip install -r requirements.txt

# 3. Jalankan server
python app.py

# 4. Get Token Login
curl -X POST http://localhost:3000/auth/login -H "Content-Type: application/json" -d "{\"email\": \"eko@example.com\", \"password\": \"12345\"}"

# 5. Get Items
curl -X GET http://localhost:3000/items 

# 6. EndPoint
curl -X GET http://localhost:3000/ 

#7. Update Profile
curl -X PUT http://localhost:3000/profile -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_TOKEN" -d "{\"name\": \"Bagus Updated\"}" 
# atau curl -X PUT http://localhost:3000/profile -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_TOKEN" -d "{^\"name^\": ^\"Eko Updated^\"}"