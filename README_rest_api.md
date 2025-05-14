
# 🛒 REST API – Διαχείριση Προϊόντων

Αυτό το έργο υλοποιεί ένα πλήρες REST API με χρήση Flask & MySQL για CRUD λειτουργίες σε προϊόντα.

---

## 📌 Τι κάνει το API

- ✅ Εισαγωγή προϊόντων
- 📥 Ανάκτηση προϊόντων (όλα ή ανά ID)
- ✏️ Ενημέρωση στοιχείων
- ❌ Διαγραφή προϊόντων

---

## 📦 Τεχνολογίες

- Python 3.9+
- Flask
- MySQL
- Flask-MySQLdb
- Postman (για δοκιμές)

---

## ⚙️ Οδηγίες Εγκατάστασης

1. Κλωνοποίησε το repo:
```bash
git clone https://github.com/yourusername/rest-api-project.git
cd rest-api-project
```

2. Εγκατάσταση dependencies:
```bash
pip install -r requirements.txt
```

3. Δημιούργησε βάση δεδομένων:
- Εκτέλεσε το `schema.sql` στη MySQL.

4. Ενημέρωσε το αρχείο `db_config.py` με τα στοιχεία σύνδεσης.

5. Τρέξε το app:
```bash
python app.py
```

---

## 🔌 Endpoints

| Μέθοδος | Endpoint           | Περιγραφή                      |
|--------|--------------------|--------------------------------|
| GET    | `/products`        | Επιστρέφει όλα τα προϊόντα     |
| GET    | `/products/<id>`   | Προϊόν με συγκεκριμένο ID      |
| POST   | `/products`        | Δημιουργία νέου προϊόντος      |
| PUT    | `/products/<id>`   | Ενημέρωση στοιχείων προϊόντος  |
| DELETE | `/products/<id>`   | Διαγραφή προϊόντος             |
| DELETE | `/products/all`    | Διαγραφή όλων των προϊόντων    |

---

## 🧾 Παράδειγμα POST JSON

```json
{
  "name": "Laptop",
  "price": 899.99,
  "stock": 20
}
```

---

## 📁 Δομή Αρχείων

```
rest-api-project/
├── app.py
├── db_config.py
├── schema.sql
├── requirements.txt
├── postman-tests/
│   └── tests.json
└── README.md
```

---

## ✍️ Συντάκτης

[Το Ονοματεπώνυμό σου]  
[Τμήμα / Μάθημα / Εξάμηνο (αν χρειάζεται)]
