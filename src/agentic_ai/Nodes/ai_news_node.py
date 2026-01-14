from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate
from src.agentic_ai.State.state import AgentState

from pathlib import Path
from datetime import datetime


class AINewsNode:
    def __init__(self, llm) -> None:
        """
        Initializes the AI News Node with API Keys for Tavily and Groq.
        """

        self.tavily = TavilyClient()
        self.llm = llm


    def fetch_news(self, state : AgentState):
        """
        Fetch AI News based on specified frequency.

        Args:
            state (dict) : The state dictionary containing 'frequency'.

        Returns:
            dict: Updated state with 'news_data' key containing fetched news.

        """

        frequency = state["messages"][0].content.strip().lower()
        state['frequency'] = frequency
        time_range_map = {'day' : 'd', 'week' : 'w', 'month' : 'm', 'year' : 'y'}
        days_map = {'day' : 1, 'week' : 7, 'month' : 30, 'year' : 366}

        if frequency not in time_range_map:
            raise ValueError(f"Invalid frequency: {frequency}")

        response = self.tavily.search(
            query= "Top Artificial Intelligence (AI) news in India and globally." ,
            topic= "news",
            time_range= frequency , 
            include_answer= "advanced",
            max_results= 20,
            days= days_map[frequency],
        )

        state['news_data'] = response.get('results', [])

        return state

       
    def summarize_news(self, state : AgentState):
        """
        Summarize the Fetched News using an LLM.

        Args:
            state (dict) : The state dictionary containing 'news_data' .

        Returns:
            dict: Updated state with 'summary'key containing summarized news.

        """

        news_items= state['news_data']

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", """Summarize AI news articles into markdown format. For each item include:
            - Date in **YYYY-MM-DD** format in IST timezone
            - Concise sentences summary from latest news
            - Sort news by date wise (latest first)
            - Source URL as link
            Use format:
            ### [Date]
            - [Summary](URL)"""),
            ("user", "Articles:\n{articles}")
        ])

        articles_str = "\n\n".join([
            f"Content: {item.get('content', '')}\nURL: {item.get('url', '')}\nDate: {item.get('published_date', '')}"
            for item in news_items
        ])

        response = self.llm.invoke(prompt_template.format(articles=articles_str))
        state['summary'] = response.content
        #self.state['summary'] = state['summary']

        return state
    

    def save_result(self,state : AgentState):

        output_dir = Path("AINews")
        output_dir.mkdir(exist_ok=True)

        frequency = state['frequency']
        summary = state['summary']

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")      
        filename = output_dir / f"{frequency}_summary_{timestamp}.md"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            f.write(summary)

        state['filename'] = filename

        return state
    


      






    



