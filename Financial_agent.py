
import os
from dotenv import load_dotenv # type: ignore

from phi.agent import Agent # type: ignore
from phi.model.groq import Groq # type: ignore
from phi.tools.yfinance import YFinanceTools # type: ignore
from phi.tools.duckduckgo import DuckDuckGo #type: ignore
load_dotenv()




web_search_agent=Agent(
    name="Web Search Agent",
    role="Searchg the Web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview",api_key="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"),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tools_calls=True,
    markdown=True,

)

finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview",api_key="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"),
    tools=[YFinanceTools(
        stock_price=True,company_info=True,stock_fundamentals=True,key_financial_ratios=True,
        company_news=True,historical_prices=True,income_statements=True,technical_indicators=True,

    )],
    instructions=["use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)
multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for Lockhead martin", stream=True)
