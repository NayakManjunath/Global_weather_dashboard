# Global Weather Dashboard

A simple Python tool to view and compare weather conditions for cities using a public weather API.

## Features
- Get current weather for any city
- Compare weather across multiple cities
- Simple command-line menu

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Global-Weather-Dashboard.git
Install requirements:

bash
Copy code
pip install -r requirements.txt
API Key
Create a config.py file:

python
Copy code
API_KEY = "your_openweathermap_api_key"
Run the App
bash
Copy code
python global_weather_dashboard.py
yaml
Copy code

---
### Recommended Project Structure
Global-Weather-Dashboard/
│
├── global_weather_dashboard.py
├── requirements.txt
├── README.md
├── .gitignore
└── config_example.py   (optional)

✅ 1. global_weather_dashboard.py

This is your main script.
You already have it, but fix this line:

weather_data = fetch_weather_data(city)


If you want, paste your full script and I’ll clean it up before you upload.

✅ 2. requirements.txt

Create this file so users can install the necessary packages.

requests
python-dotenv

✅ **3. config_example.py**
This helps users know what config file they must create.

```python
API_KEY = "YOUR_API_KEY_HERE"
Your real config.py will not be committed.
```

✅ 4. .gitignore
This keeps sensitive files out of GitHub.

bash
Copy code
# Ignore python cache
__pycache__/
*.pyc

# Ignore API keys
config.py

# OS files
.DS_Store
