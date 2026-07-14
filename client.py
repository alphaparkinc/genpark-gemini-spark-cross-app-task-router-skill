class GeminiSparkCrossAppRouterClient:
    def get_route(self, source_app: str, task_type: str) -> dict:
        return {"target_app": "Google Sheets" if task_type == "data_entry" else "Gmail"}