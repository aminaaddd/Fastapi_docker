# Fastapi_docker

Run the code:
docker-compose build #To build containers
docker-compose up

and then: 
curl -X POST "http://localhost:8000/products/" -H "Content-Type: application/json" -d '{"name": "apple", "price": 1.5, "quantity": 10}' #For POST 

curl -X GET "http://localhost:8000/products/apple" #For GET
