from openai import OpenAI
from openai.types.beta import Assistant
from openai.types.beta.thread import Thread
from openai.types.beta.threads.thread_message import ThreadMessage
from openai.types.beta.threads.run import Run
import json
from dotenv import load_dotenv, find_dotenv
import os
import time
import requests
from typing import Any


"""
#Imporrting the keys
"""
_: bool = load_dotenv(find_dotenv())
FMP_API_KEY = os.environ["API_KEY"]
API_KEY = os.environ["OPENAI_API_KEY"]
"""
#Functions to be used defined
"""
def get_financial_statements(symbol: str) -> str | dict | None:
    url: str = f"https://financialmodelingprep.com/api/v3/cik-search/{symbol}?&apikey={FMP_API_KEY}"
    try:
        response = requests.get(url)
        return json.dumps(response.json())
    except:
        return json.dumps({"response": "Apologies,I could not access the requested information"})

# Function Number : 2


def get_financial_ratios(symbol: str) -> str | dict | None:

    url: str = f"https://financialmodelingprep.com/api/v3/ratios/{symbol}?&apikey={FMP_API_KEY}"
    try:
        response = requests.get(url)
        return json.dumps(response.json())
    except:
        return json.dumps({"response": "Apologies,I could not access the requested information"})

# Function Number : 3


def get_key_metrics(symbol: str) -> str | dict | None:
    url: str = f"https://financialmodelingprep.com/api/v3/key-metrics/{symbol}?&apikey={FMP_API_KEY}"
    try:
        response = requests.get(url)
        return json.dumps(response.json())
    except:
        return json.dumps({"response": "Apologies,I could not access the requested information"})

# Function Number : 4


def get_financial_growth(symbol: str) -> str | dict | None:
    url: str = f"https://financialmodelingprep.com/api/v3/search?query={symbol}&apikey={FMP_API_KEY}"
    try:
        response = requests.get(url)
        return json.dumps(response.json())
    except:
        return json.dumps({"response": "Apologies,I could not access the requested information"})

# Function Number : 5


def get_company_profile(symbol: str) -> str | dict | None:
    url: str = f"https://financialmodelingprep.com/api/v3/profile/{symbol}?&apikey={FMP_API_KEY}"
    try:
        response = requests.get(url)
        return json.dumps(response.json())
    except:
        return json.dumps({"response": "Apologies,I could not access the requested information"})
# Function Number : 6


def get_income_statements(symbol: str) -> str | dict | None:
    url: str = f"https://financialmodelingprep.com/api/v3/income-statement/{symbol}?period=annual&apikey={FMP_API_KEY}"
    try:
        response = requests.get(url)
        return json.dumps(response.json())
    except:
        return json.dumps({"response": "Apologies,I could not access the requested information"})
# Function Number : 7


def get_balance_sheet(symbol: str) -> str | dict | None:
    url: str = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{symbol}?period=annual&apikey={FMP_API_KEY}"
    try:
        response = requests.get(url)
        return json.dumps(response.json())
    except:
        return json.dumps({"response": "Apologies,I could not access the requested information"})
# Function Number : 8


def get_cash_flow(symbol: str) -> str | dict | None:
    url: str = f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{symbol}?period=annual&apikey={FMP_API_KEY}"
    try:
        response = requests.get(url)
        return json.dumps(response.json())
    except:
        return json.dumps({"response": "Apologies,I could not access the requested information"})


# Step 2 : Map your functions
available_functions = {
    "get_financial_statements": get_financial_statements,
    "get_financial_ratios": get_financial_ratios,
    "get_key_metrics": get_key_metrics,
    "get_financial_growth": get_financial_growth,
    "get_company_profile": get_company_profile,
    "get_income_statements": get_income_statements,
    "get_balance_sheet": get_balance_sheet,
    "get_cash_flow": get_cash_flow

}

"""
#The class for message 
"""
class MessageItem:
      def __init__(self, role: str, content: str | Any):
        self.role: str = role
        self.content: str | Any = content

class OpenAIAssistant:
    def __init__(self,name:str,instructions:str,model:str="gpt-3.5-turbo-1106"):
        self.name:str= name;
        self.instructions:str = instructions;
        self.model :str = model;
        load_dotenv(find_dotenv());
        self.client :OpenAI = OpenAI();
        self.assistant : Assistant = self.client.beta.assistants.create(
            name=self.name,
            instructions= self.instructions,
            tools = [
                {"type":"code_interpreter"},
                {

            "type": "function",
            "function": {
                "name": "get_financial_statements",
                "description": "Get the financial statement of a company",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string", "description": "The name or abbreviation of the company,one wants to know about"}

                    },
                    "required": ["symbol"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_financial_ratios",
                "description": "Get the financial ratios of a company",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string", "description": "The name or abbreviation of the company,one wants to know about"}

                    },
                    "required": ["symbol"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_key_metrics",
                "description": "Get the key metrics of a company",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string", "description": "The name or abbreviation of the company,one wants to know about"}

                    },
                    "required": ["symbol"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_financial_growth",
                "description": "Get information about the financial growth of a company",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string", "description": "The name or abbreviation of the company,one wants to know about"}

                    },
                    "required": ["symbol"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_company_profile",
                "description": "Get information about the overall financial status of a company across different areas",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string", "description": "The name or abbreviation of the company,one wants to know about"}

                    },
                    "required": ["symbol"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_income_statements",
                "description": "provides access to real-time income statement data for a wide range of companies, including public companies",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string", "description": "The name or abbreviation of the company,one wants to know about"}

                    },
                    "required": ["symbol"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_balance_sheet",
                "description": "a financial statement that displays a company’s total assets, liabilities, and shareholder equity over a specific timeframe (quarterly or yearly).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string", "description": "The name or abbreviation of the company,one wants to know about"}

                    },
                    "required": ["symbol"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_cash_flow",
                "description": "a financial statement that highlights how cash moves through the company, including both cash inflows and outflows",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string", "description": "The name or abbreviation of the company,one wants to know about"}

                    },
                    "required": ["symbol"]
                }
            }
        }
            ],
            model = self.model
            )
        """
        #1Thread being initialized 
        """
        self.thread :Thread = self.client.beta.threads.create()
        """
        #2.Creating a list of messages to keep track of the conversation between the user and the assistant
        """
        self.messages :list[MessageItem] = [];

        """
        #This will return the name of the assistant
        """
    def get_name(self):
        return self.name
        """
        #This will return the instrctions
        """
    def get_instructions(self):
        return self.instructions
        
    def ask_question(self,message:str):
        current_thread : ThreadMessage = self.client.beta.threads.messages.create(
            thread_id = self.thread.id,
            role = "user",
            content = message
            )

        self.latest_run :Run = self.client.beta.threads.runs.create(
                thread_id = self.thread.id,
                assistant_id = self.assistant.id,
                instructions = self.instructions
            )

        self.addMessage(MessageItem(role="user", content=message))

        """
        #This function will check the status of the run 
        """
    def is_complete(self)->bool:
            print("Status",self.latest_run.status)
            while True:
                # print("Going to sleep")
                # time.sleep(1)
                self.latest_run : Run = self.client.beta.threads.runs.retrieve(
                    thread_id = self.thread.id,
                    run_id = self.latest_run.id
                )
                print("Latest Status: ", self.latest_run.status)
                if self.latest_run.status == "requires_action":
                    print("Latest Status: ", self.latest_run.status)
                    if self.latest_run.required_action.submit_tool_outputs and self.latest_run.required_action.submit_tool_outputs.tool_calls:
                        print("tool calls present")
                        toolCalls = self.latest_run.required_action.submit_tool_outputs.tool_calls
                        tool_outputs = [];
                        for toolcall in toolCalls:
                             function_name = toolcall.function.name
                             function_args = json.loads(toolcall.function.arguments)
                             
                             if function_name in available_functions:
                                 function_to_call = available_functions[function_name]
                                 output = function_to_call(**function_args)
                                 tool_outputs.append({
                                                "tool_call_id": toolcall.id,
                                                "output": output,
                                            })
                                 # Submit tool outputs and update the run
                        self.client.beta.threads.runs.submit_tool_outputs(
                            thread_id = self.thread.id,
                            run_id=self.latest_run.id,
                            tool_outputs=tool_outputs
                                     )
                                 
                           
                           
                elif self.latest_run.status == "completed": 
                    messages = self.client.beta.threads.messages.list(
                        thread_id = self.thread.id
                    )

                    break

                elif self.latest_run.status == "failed":
                    print("Run Failed")
                    break
                
                elif self.latest_run.status in ["in_progress","queued"]:
                      print(f"Run is {self.latest_run.status}. Waiting...")
                      time.sleep(5)

            return True
        
    def get_response(self)->MessageItem:
            messages = self.client.beta.threads.messages.list(thread_id = self.thread.id)
            print("Answer",messages.data[0])

            answer = MessageItem(messages.data[0].role, messages.data[0].content[0].text.value)
            self.addMessage(answer)
            return answer
        
    def getMessages(self)->list[MessageItem]:
            return self.messages

    def addMessage(self, message: MessageItem)->None: 
            self.messages.append(message)








