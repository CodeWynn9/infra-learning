from agent_app.api_client import APIClient

client = APIClient(
	base_url="https://api.github.com"
)

data = client.get("/users/octocat")

print(data["login"])

client.close()
