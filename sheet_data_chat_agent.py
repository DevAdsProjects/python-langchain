# Importing necessary libraries for the project
!pip install pandas
!pip install langchain-experimental
!pip install openai

# Importing authentication utilities from google.colab for Google Colab notebook
from google.colab import auth
auth.authenticate_user()

# Importing gspread to interact with Google Sheets and google.auth for authentication
import gspread
from google.auth import default
creds, _ = default()

# Importing necessary components from langchain to work with agents
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# Importing pandas for data manipulation
import pandas as pd

# Authorizing gspread with credentials and opening a specific Google Sheet
gc = gspread.authorize(creds)
sh = gc.open('')  # Note: Add the name of your Google Sheet inside the quotes
worksheet = sh.get_worksheet(0)  # Accessing the first worksheet of the Google Sheet

# Retrieving all values from the worksheet and converting it to a pandas DataFrame
data = worksheet.get_all_values()
campaigns_data = pd.DataFrame(data)
campaigns_data.columns = campaigns_data.iloc[0]  # Setting the first row as column headers
campaigns_data = campaigns_data[1:]  # Removing the first row as it's now the header

# Setting up the OpenAI API key for GPT-4 usage
openai_api_key = ""  # Note: Insert your OpenAI API key here

# Creating a ChatOpenAI agent with the specified OpenAI API key and setting its parameters
from langchain_experimental.agents import ChatOpenAI
chat = ChatOpenAI(openai_api_key=openai_api_key, model_name="gpt-4", temperature=0.0)

# Creating an agent that combines the ChatOpenAI agent with the campaigns_data DataFrame
agent = create_pandas_dataframe_agent(chat, campaigns_data)

# Running the agent with an input string (replace "" with your input string)
agent.run("")  # Note: Insert your input string inside the quotes
