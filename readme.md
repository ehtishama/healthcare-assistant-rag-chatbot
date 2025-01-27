# Healthcare Assistant RAG Chatbot

## Overview
This project is a Healthcare Assistant built using a Retrieval-Augmented Generation (RAG) model. The system provides accurate and relevant healthcare advice based on user queries by retrieving information from the [NHS A-Z website](https://www.nhs.uk/health-a-z) and augmenting it with a Large Language Model (LLM). 

The project is developed as part of the MLH ["Hack for Hackers"](https://events.mlh.io/events/11516) hackathon.

## System Architecture
![System Architecture](https://i.imgur.com/IhmQZIN.jpeg)

### Components:
1. **Frontend**:
   - Accepts user queries and displays responses.
   - Communicates with the backend via REST API.

2. **REST API**:
   - Acts as a bridge between the frontend and the RAG engine.
   - Sends user queries to the RAG engine and returns the response to the frontend.

3. **RAG Engine**:
   - **MongoDB Atlas**:
     - Stores document embeddings and a vector search index.
     - Performs similarity searches to retrieve the top 5 relevant documents for each query.
   - **Web Scraper**:
     - Extracts data from the NHS A-Z website and stores it in the database.
   - **LLM**:
     - Processes the user query along with the retrieved documents to generate a biased, contextually enriched response.

## Data Source
The primary data source is the [NHS A-Z website](https://www.nhs.uk/conditions/), which provides comprehensive healthcare information. The data is scraped and stored in MongoDB Atlas as embedded documents to facilitate efficient similarity search.

## Technologies Used
- **Frontend**: React, HTML, CSS
- **Backend**: Python, FastAPI, Langchain
- **Database**: MongoDB Atlas
- **LLM**: OpenAI GPT
- **Web Scraper**: Python (BeautifulSoup, Requests)
- **Embedding Generation**: OpenAI embeddings API

## Installation and Setup

### Prerequisites
1. **Docker**: Ensure Docker is installed on your machine.
2. **MongoDB**: A MongoDB instance is required for data storage.
3. **OpenAI API Key**: Obtain an API key from OpenAI.

---

### Initial Setup (Required for both options)

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd healthcare-assistant-rag-chatbot
   ```

2. **Scrape and populate data**:
   * Navigate to the `notebooks` folder and run `scrapper_mongodb.ipynb` to populate MongoDB with required data.

### Option 1: Running Locally

1. **Set up the backend**:
   ```bash
   cd backend
   ```
   
   Create a `.env` file with the following environment variables:
   ```env
   MONGODB_ATLAS_CLUSTER_URI=<your-mongodb-atlas-uri>
   OPENAI_API_KEY=<your-openai-api-key>
   ```

   Start the backend server:
   ```bash
   fastapi dev main.py
   ```

2. **Set up the frontend**:
   ```bash
   cd ../frontend
   ```
   
   Create a `.env` file with the following environment variable:
   ```env
   API_BASE_URL=<backend-server-url>  # e.g., http://localhost:8000
   ```

   Install dependencies and start the frontend:
   ```bash
   npm install
   npm run dev
   ```

### Option 2: Running with Docker

1. **Update Docker Compose file**:
   * Open the `compose.yaml` file and update the following environment variables:
     ```yaml
     environment:
       OPENAI_API_KEY: <your-openai-api-key>
       MONGODB_ATLAS_CLUSTER_URI: <your-mongodb-atlas-uri>
     ```

2. **Run Docker Compose**:
   ```bash
   docker compose up
   ```

3. **Access the application**:
   * Once the containers are running, go to `http://localhost:8080` in your browser to access the application.


## How It Works
1. **User Query**: The user submits a query through the frontend.
2. **Document Retrieval**: The REST API sends the query to the RAG engine, which performs a similarity search on the MongoDB database to fetch the top 5 relevant documents.
3. **Augmented Response**: The query and retrieved documents are sent to the LLM to generate a contextually enriched response.
4. **Response Delivery**: The response is sent back to the frontend and displayed to the user.

## Future Improvements
- Enhance the web scraper to update data periodically from the NHS website.
- Add multi-language support for a wider audience.
- Incorporate additional healthcare datasets to improve the breadth of information.
- Optimize the embedding generation and similarity search processes for faster responses.
- 
## Project Members
- [Ehtisham UL Hasan](https://linkedin.com/in/ehtishamhassan9)
- [Muhammad Junaid](https://github.com/jukha)
- [Shamsher](https://github.com/shamshertamang)

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License
This project is licensed under the MIT License.

## Acknowledgments
- [NHS A-Z Website](https://www.nhs.uk/conditions/) for providing the data.
- MLH for organizing the "Hack for Hackers" hackathon.
- OpenAI for the LLM and embeddings API.

---
We hope this Healthcare Assistant helps users make informed healthcare decisions efficiently!
