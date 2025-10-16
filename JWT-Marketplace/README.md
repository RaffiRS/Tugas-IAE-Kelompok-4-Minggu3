# JWT Marketplace API (Flask Modular)

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
curl -X POST http://localhost:3000/auth/login -H "Content-Type: application/json" -d "{\"email\": \"eko@example.com\", \"password\": \"12345\"}" bisa

# 5. Get Items
curl -X GET http://localhost:3000/items bisa

# 6. Get Token Login
curl -X GET http://localhost:3000/ bisa

#7. Update Profile
curl -X PUT http://localhost:3000/profile -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_TOKEN" -d "{\"name\": \"Bagus Updated\"}" 
# atau curl -X PUT http://localhost:3000/profile -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_TOKEN" -d "{^\"name^\": ^\"Eko Updated^\"}"