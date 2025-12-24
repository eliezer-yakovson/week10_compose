# Contacts Management API
## my name 
eliezer yakovson
negev 
id: 206568107
## Description
REST API for managing contacts using FastAPI with CRUD operations and manual SQL queries. Containerized with Docker and Docker Compose.

### API Endpoints
- **GET /contacts** - Get all contacts
- **POST /contacts** - Create new contact
- **PUT /contacts/{id}** - Update contact
- **PUT /contacts/{id}/field** - Update specific field of a contact
- **DELETE /contacts/{id}** - Delete contact

## Setup

Create `.env` file:
```env
DB_HOST=db
DB_USER=root
MYSQL_ROOT_PASSWORD=1234
MYSQL_DATABASE=contacts_db
DB_PORT=3306
```

Run:
```bash
docker-compose up -d
```

## Testing

**GET all contacts:**
```bash
curl http://localhost:8000/contacts
```

**POST new contact:**
```bash
curl.exe -X POST http://localhost:8000/contacts -H "Content-Type: application/json" -d "{\""first_name\"":\""Alice\"",\""last_name\"":\""Williams\"",\""phone_number\"":\""053-1111111\""}"
```

**PUT update contact:**
```bash
curl.exe -X PUT http://localhost:8000/contacts/1 -H "Content-Type: application/json" -d "{\""first_name\"":\""John\"",\""last_name\"":\""Updated\"",\""phone_number\"":\""050-9999999\""}"
```

**DELETE contact:**
```bash
curl.exe -X DELETE http://localhost:8000/contacts/1
```

**PUT update specific field of a contact:**
```bash
curl.exe -X PUT "http://localhost:8000/contacts/5/field?field_name=first_name&new_value=UpdatedName"
```

**Interactive docs:** http://localhost:8000/docs



