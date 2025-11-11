#  MeteoAPI

REST API za meteorološke podatke - merenja, lokacije, varijable i izvori. Flask + PostgreSQL + Swagger.



##  Pokretanje

### Docker (preporučeno)
```bash
docker compose up --build
```

### Lokalno
```bash
pip install -r requirements.txt
cd src
python app.py
```

---

##  URL-ovi

| Servis | URL |
|--------|-----|
| API | `http://localhost:5001` |
| PostgreSQL | `localhost:5432` |

**DB kredencijali:** `meteoapi` / `meteoapi123`

---

##  API Endpoints

- `GET /api/measurements` - Sve meritve
- `GET /api/variable` - Sve varijable
- `GET /api/location` - Sve lokacije
- `GET /api/source` - Svi izvori

Kompletan opis na Swagger UI: `http://localhost:5001/api/ui/`

---

##  Zavisnosti

```
flask, connexion, flask-sqlalchemy, sqlalchemy, openalchemy, psycopg2-binary, flask-cors
```

Vidi `requirements.txt` za sve zavisnosti.

---

##  Struktura projekta

```
src/
├── app.py           # Glavna aplikacija
├── api.py           # API operacije
├── database.py      # DB konfiguracija
├── models.py        # Modeli (auto-generisano)
├── meteoapi.yaml    # OpenAPI specifikacija
└── swagger.py       # Swagger UI
```

