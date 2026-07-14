from client import GeminiSparkCrossAppRouterClient
client = GeminiSparkCrossAppRouterClient()
print(client.get_route("Slack", "data_entry"))