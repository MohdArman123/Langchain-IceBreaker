# Ice Breaker

Ice-Breaker Project Setup and Execution
Overview
The Ice-Breaker project integrates LinkedIn and Twitter data with LangChain to create an advanced data extraction and processing application. Follow these steps to set up and run the project on your local machine.

Prerequisites
Python 3.8 or higher
Node.js and npm (for frontend dependencies, if applicable)
Git
Setup
Clone the Repository

Open your terminal and clone the repository:

bash
Copy code
git clone https://github.com/MohdArman123/Langchain-IceBreaker.git
cd ice-breaker
Install Python Dependencies

Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Install Node.js Dependencies (If applicable)

If your project has a frontend or additional Node.js dependencies, navigate to the frontend directory (or similar) and install them:

bash
Copy code
cd frontend
npm install
Set Up Environment Variables

Create a .env file in the root directory and add your environment variables:

dotenv
Copy code
PROXYCURL_API_KEY=your_proxycurl_api_key
TWITTER_BEARER_TOKEN=your_twitter_bearer_token
Make sure to replace your_proxycurl_api_key and your_twitter_bearer_token with your actual API keys.

Run Migrations (If applicable)

If your project uses a database and requires migrations, run them using:

bash
Copy code
python manage.py migrate
Start the Application

Run the backend server:

bash
Copy code
python app.py
If you have a frontend, you can start it with:

bash
Copy code
cd frontend
npm start
How It Works
Data Extraction

LinkedIn Scraping: Uses the Proxycurl API to pull structured profile data from LinkedIn.
Twitter Data: Uses Tweepy with the Twitter API to fetch real-time tweets and user profiles.
Integrating LangChain

Prompt Templates: Custom prompts guide Large Language Models (LLMs) for generating tailored responses.
Chains: Automated workflows process the extracted data.
Agents: Manage the workflow, making decisions on task execution.
Data Transformation

Output Parsing: Converts raw LLM outputs into structured formats like JSON or CSV.
Pydantic Validation: Ensures data accuracy and consistency with schema validation.
Running the Code
Start the Backend Server

Ensure your virtual environment is activated and run:

bash
Copy code
python app.py
Access the Application

Open your browser and navigate to http://localhost:5000 (or the port specified in your configuration) to view the application.

Frontend Interaction

If your project includes a frontend, it will be accessible at http://localhost:3000 (or the port specified in the frontend configuration).

Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements!
