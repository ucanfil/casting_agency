# Example curl command for DELETE /movies/<int:movie_id> Endpoint
    curl -H "Accept: application/json" -H "Authorization: Bearer $JWT_EXECUTIVE_PRODUCER" http://$HOSTNAME/movies/10 --request DELETE