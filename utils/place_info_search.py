from langchain_tavily import TavilySearch


class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str):
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke(
            {"query": f"Top tourist attractions in {place}"}
        )

        if isinstance(result, dict):
            return result.get("answer", str(result))

        return str(result)

    def tavily_search_restaurants(self, place: str):
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke(
            {"query": f"Best restaurants in {place}"}
        )

        if isinstance(result, dict):
            return result.get("answer", str(result))

        return str(result)

    def tavily_search_activity(self, place: str):
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke(
            {"query": f"Best activities in {place}"}
        )

        if isinstance(result, dict):
            return result.get("answer", str(result))

        return str(result)

    def tavily_search_transportation(self, place: str):
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke(
            {"query": f"Transportation options in {place}"}
        )

        if isinstance(result, dict):
            return result.get("answer", str(result))

        return str(result)