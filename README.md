# Example curl command for DELETE /movies/<int:movie_id> Endpoint
    curl -H "Accept: application/json" -H "Authorization: Bearer $TOKEN" http://$HOSTNAME/movies/10 --request DELETE