

from phi.agent import Agent # type: ignore
from phi.model.groq import groq # type: ignore
from phi.tools.yfinance import YFinanceTools # type: ignore
from phi.tools.duckduckgo import DuckDuckGo #type: ignore


web_search_agent=Agent(
    name="Web Search Agent",
    role="Searchg the Web for the information",
    model=groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tools_calls=True,
    markdown=True,

)
