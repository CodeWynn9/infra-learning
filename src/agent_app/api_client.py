import httpx

class APIClient:
	def __init__(self,base_url,timeout=10):
		self.client = httpx.Client(
			base_url=base_url,
			timeout=timeout
		)
	def get(self,path):
		response = self.client.get(path)
		response.raise_for_status()
		return response.json()
	def close(self):
		self.client.close()
