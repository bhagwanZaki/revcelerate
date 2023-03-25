# Contact-book

## Installation

Clone the repository

```bash
    git clone https://github.com/bhagwanZaki/revcelerate.git
```

Install the dependencies

```bash
    pip install -r requirements.text
```

Migrating db

```bash
   python manage.py makemigrations
   python manage.py migrate
```

Run the server

```bash
    python manage.py runserver
```

## API Documentation

### 1. To store contact detail

<b>
Request : POST
</b>
```bash
    http://127.0.0.1:8000/
```
<b>
Data</b>

```json
{
  "name": "Rahul",
  "mobile_number": "7894563245",
  "address": "Mumbai",
  "email": "rahul@gmail.com",
  "instagram_handle": "tre1222",
  "companies": [
    {
      "name": "Swiggy"
    },
    {
      "name": "Zomato"
    }
  ]
}
```

### 2. To retrieve all contact

<b>
Request : GET
</b>
```bash
    http://127.0.0.1:8000/
```

### 3. Retrieve a contact using phone, email, or Instagram handle

<b>
Request : GET
</b>

```bash
    http://127.0.0.1:8000/?email=rahul@gmail.com
```

### 4. Search all contacts by subscribed companies

<b>
Request : GET
</b>

```bash
    http://127.0.0.1:8000/companyContact/<str: company_name>
```

### 5. Update a fixed for a contact with given mobile, email, or Instagram

<b>
Request : PUT
</b>
```bash
    http://127.0.0.1:8000/contact/<int : contactId>/
```
<b>
data
</b>
```json
{
  "name": "Rahul",
  "email": "tahul1234.tarveen@gmail.com",
  "instagram_handle": "tre1222"
}
```
