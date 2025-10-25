# DeepAgentt - AI Research Assistant

A powerful AI research agent built using DeepSeek and Tavily, capable of conducting thorough internet research and generating comprehensive reports.

## 🌟 Features

- Automated web research using Tavily's search API
- Advanced language processing using DeepSeek's chat model
- Customizable search parameters (max results, topics, content depth)
- Memory system for storing user preferences
- Support for different research topics (general, news, finance)

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- DeepSeek API key
- Tavily API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/[your-username]/deepagentt.git
cd deepagentt
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your API keys:
```env
DEEPSEEK_API_KEY=your_deepseek_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## 🔧 Configuration

The agent can be configured with different parameters:

- `max_results`: Number of search results to return (default: 5)
- `topic`: Research topic type ("general", "news", "finance")
- `include_raw_content`: Option to include detailed content in search results

## 💻 Usage

The agent can be used to conduct research on any topic. Here's a basic example:

```python
from app import agent

# Create a research query
result = agent.invoke({
    "messages": [{
        "role": "user", 
        "content": "Research query here"
    }]
})

# Print the research results
print(result["messages"][-1].content)
```

## 🛠️ Project Structure

```
deepagentt/
├── .env                    # Environment variables (not in git)
├── .gitignore             # Git ignore file
├── app.py                 # Main application file
├── README.md              # Project documentation
└── requirements.txt       # Project dependencies
```

## 📝 Dependencies

- `deepagents`: For creating and managing the AI research agent
- `tavily`: For web search capabilities
- `python-dotenv`: For environment variable management
- `langchain`: For chat model initialization and memory management

## ⚠️ Environment Variables

Make sure to set up the following environment variables in your `.env` file:

- `DEEPSEEK_API_KEY`: Your DeepSeek API key
- `TAVILY_API_KEY`: Your Tavily API key

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📮 Contact

[Your Name] - [your.email@example.com]

Project Link: https://github.com/[your-username]/deepagentt