import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

MODEL = 'gpt-4o-mini'

openai = OpenAI()

system_message = """You are a helpful airline chatbot assistant. Give short courteous answers,
no more than 1 sentence. Always be accurate, if you don't know the answer, say so."""

ticket_prices = {"london": "$700", "mumbai": "$900", "paris": "$800", "dubai": "$1000"}

def get_ticket_prices(destination_city):
    print(f"Tool get_ticket_price is called for {destination_city}")
    city = destination_city.lower()
    return ticket_prices.get(city, "Unknown")

price_function = {
    "name" : "get_ticket_prices",
    "description" : """"Get the return ticket price of the destination city. Call this function
    when the user asks for the ticket price of a city. For example when the user asks "What is the
    price of a ticket to this city?""",
    "parameters" : {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description" : "the city the customer wants to fly to."
            },
        },
        "required": ["destination_city"],
        "additionalProperties": False
    }
}

tools = [{"type": "function", "function": price_function}]

def chat(message, history):
    messages = ([{"role": "system", "content": system_message}] + 
                history + 
                [{"role": "user", "content": message}])
    response = openai.chat.completions.create(model = MODEL, messages = messages, tools = tools)

    if response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        response, city = handle_tool_call(message)
        messages.append(message)  
        messages.append(response) 
        response = openai.chat.completions.create(model = MODEL, messages = messages)

    return response.choices[0].message.content

def handle_tool_call(message):
    tool_call = message.tool_calls[0]
    arguments = json.loads(tool_call.function.arguments)
    city = arguments.get("destination_city")
    price = get_ticket_prices(city)
    response = {
        "role": "tool",
        "content": json.dumps({"destination_city": city, "price": price}),
        "tool_call_id": tool_call.id
        }
    return response, city


