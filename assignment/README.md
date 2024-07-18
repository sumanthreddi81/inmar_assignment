1) To populate data:   python manage.py shell < populate.py

2) create a superuser: python manage.py createsuperuser
3)  create a normal user from admin UI

Obtain JWT Token
curl -X POST http://127.0.0.1:8000/api/v1/token/ -d '{"username": "inmar", "password": "Passw0rd1!"}' -H "Content-Type: application/json"

Replace jwt_token in the commands below with the generated token:
GET Locations
curl -H "Authorization: Bearer jwt_token" http://127.0.0.1:8000/api/v1/location/

POST a New Location
curl -X POST http://127.0.0.1:8000/api/v1/location/ -H "Authorization: Bearer jwt_token" -H "Content-Type: application/json" -d '{
  "description": "New Location",
  "departments": [
    {
      "description": "New Department 1",
      "categories": [
        {
          "description": "New Category 1",
          "subcategories": [
            {"description": "New SubCategory 1"},
            {"description": "New SubCategory 2"}
          ]
        }
      ]
    }
  ]
}'

GET Departments for a Location
curl -H "Authorization: Bearer jwt_token" http://127.0.0.1:8000/api/v1/location/1/department/

POST a New Department for a Location
curl -X POST http://127.0.0.1:8000/api/v1/location/1/department/ -H "Authorization: Bearer jwt_token" -H "Content-Type: application/json" -d '{
  "description": "New Department",
  "categories": [
    {
      "description": "New Category",
      "subcategories": [
        {"description": "New SubCategory 1"},
        {"description": "New SubCategory 2"}
      ]
    }
  ]
}'

GET Categories for a Department
curl -H "Authorization: Bearer jwt_token" http://127.0.0.1:8000/api/v1/location/1/department/1/category/

POST a New Category for a Department
curl -X POST http://127.0.0.1:8000/api/v1/location/1/department/1/category/ -H "Authorization: Bearer jwt_token" -H "Content-Type: application/json" -d '{
  "description": "New Category",
  "subcategories": [
    {"description": "New SubCategory 1"},
    {"description": "New SubCategory 2"}
  ]
}'

GET SubCategories for a Category
curl -H "Authorization: Bearer jwt_token" http://127.0.0.1:8000/api/v1/location/1/department/1/category/1/subcategory/

POST a New SubCategory for a Category
curl -X POST http://127.0.0.1:8000/api/v1/location/1/department/1/category/1/subcategory/ -H "Authorization: Bearer jwt_token" -H "Content-Type: application/json" -d '{
  "description": "New SubCategory"
}'

PATCH a Location
curl -X PATCH http://127.0.0.1:8000/api/v1/location/1/ -H "Authorization: Bearer jwt_token" -H "Content-Type: application/json" -d '{
  "description": "Updated Location Description"
}'

PUT a Location
curl -X PUT http://127.0.0.1:8000/api/v1/location/1/ -H "Authorization: Bearer jwt_token" -H "Content-Type: application/json" -d '{
  "description": "Updated Location",
  "departments": [
    {
      "description": "Updated Department",
      "categories": [
        {
          "description": "Updated Category",
          "subcategories": [
            {"description": "Updated SubCategory 1"},
            {"description": "Updated SubCategory 2"}
          ]
        }
      ]
    }
  ]
}'

DELETE a Location
curl -X DELETE http://127.0.0.1:8000/api/v1/location/1/ -H "Authorization: Bearer jwt_token"

PATCH a Department
curl -X PATCH http://127.0.0.1:8000/api/v1/location/1/department/1/ -H "Authorization: Bearer jwt_token" -H "Content-Type: application/json" -d '{
  "description": "Updated Department Description"
}'

PUT a Department
curl -X PUT http://127.0.0.1:8000/api/v1/location/1/department/1/ -H "Authorization: Bearer jwt_token" -H "Content-Type: application/json" -d '{
  "description": "Updated Department",
  "categories": [
    {
      "description": "Updated Category",
      "subcategories": [
        {"description": "Updated SubCategory 1"},
        {"description": "Updated SubCategory 2"}
      ]
    }
  ]
}'

DELETE a Department
curl -X DELETE http://127.0.0.1:8000/api/v1/location/1/department/1/ -H "Authorization: Bearer jwt_token"

PATCH a Category
curl -X PATCH http://127.0.0.1:8000/api/v1/location/1/department/1/category/1/ -H "Authorization: Bearer jwt_token" -H "Content-Type: application/json" -d '{
  "description": "Updated Category Description"
}'

PUT a Category
curl -X PUT http://127.0.0.1:8000/api/v1/location/1/department/1/category/1/ -H "Authorization: Bearer jwt_token" -H "Content-Type: application/json" -d '{
  "description": "Updated Category",
  "subcategories": [
    {"description": "Updated SubCategory 1"},
    {"description": "Updated SubCategory 2"}
  ]
}'

DELETE a Category
curl -X DELETE http://127.0.0.1:8000/api/v1/location/1/department/1/category/1/ -H "Authorization: Bearer jwt_token"

PATCH a SubCategory
curl -X PATCH http://127.0.0.1:8000/api/v1/location/1/department/1/category/1/subcategory/1/ -H "Authorization: Bearer jwt_token" -H "Content-Type: application/json" -d '{
  "description": "Updated SubCategory Description"
}'

PUT a SubCategory
curl -X PUT http://127.0.0.1:8000/api/v1/location/1/department/1/category/1/subcategory/1/ -H "Authorization: Bearer jwt_token" -H "Content-Type: application/json" -d '{
  "description": "Updated SubCategory"
}'

DELETE a SubCategory
curl -X DELETE http://127.0.0.1:8000/api/v1/location/1/department/1/category/1/subcategory/1/ -H "Authorization: Bearer jwt_token"

