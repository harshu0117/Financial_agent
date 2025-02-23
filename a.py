from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.googlesearch import GoogleSearch
import os
import yfinance as yf
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set Groq API Key
os.environ["GROQ_API_KEY"] = "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"  

# Web Search Agent (For Latest News)
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="mixtral-8x7b-32768"),
    tools=[GoogleSearch()],  
    instructions=["Always include sources."],
    show_tool_calls=True,
    markdown=True,
)

# Finance AI Agent (For Stock Analysis)
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="mixtral-8x7b-32768"),
    tools=[YFinanceTools(
        stock_price=True, 
        analyst_recommendations=True, 
        stock_fundamentals=True,
        company_info=True, 
        company_news=True
    )],
    instructions=["Use tables to display the data."],
    show_tool_calls=True,
    markdown=True,
)

# Manually Assign Tasks to Agents
try:
    print("\n✅ Fetching Latest NVDA News...")
    news_response = web_search_agent.run("Find the latest news for NVDA")

    print("\n✅ Fetching Analyst Recommendations for NVDA...")
    finance_response = finance_agent.run("Summarize analyst recommendations for NVDA")

    # Display Outputs
    print("\n📰 **Latest NVDA News:**\n", news_response)
    print("\n📊 **Analyst Recommendations:**\n", finance_response)

except Exception as e:
    print("❌ Error:", e)
