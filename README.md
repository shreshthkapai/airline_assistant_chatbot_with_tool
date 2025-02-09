# ✈️ Airline Chatbot Assistant  

A simple chatbot using **OpenAI's function calling** to fetch airline ticket prices.  

## 🚀 Features  
- Retrieves **return ticket prices** for selected cities.  
- Uses **OpenAI tools (function calling)** for accurate responses.  

## 🛠️ Setup  
```bash
git clone https://github.com/your-username/Airline-Chatbot.git
cd Airline-Chatbot
pip install -r requirements.txt
```

Create a `.env` file with your OpenAI API key:  
```ini
OPENAI_API_KEY=your_openai_api_key
```

Run the chatbot:  
```bash
python main.py
```

## 🏗️ How It Works  
The chatbot calls `get_ticket_prices(destination_city)` using OpenAI’s **tools feature** and returns the **return ticket price**.

## ✉️ Contributions  
PRs & issues welcome! 🚀  
