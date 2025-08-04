BASE_URL=$(minikube service flask-orders-service --url)

echo "\n🔍 Testing root endpoint: /"
curl -s "$BASE_URL/" | jq

echo "\n📋 Testing GET /orders"
curl -s "$BASE_URL/orders" | jq

echo "\n➕ Testing POST /orders"
curl -s -X POST "$BASE_URL/orders" \
  -H "Content-Type: application/json" \
  -d '{"destination":"London", "start_date":"2025-10-20", "end_date":"2025-10-27"}' | jq

echo "\n📋 Testing GET /orders after POST"
curl -s "$BASE_URL/orders" | jq