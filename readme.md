# Healthcare Assistant RAG Model

## Overview
This project is a Healthcare Assistant built using a Retrieval-Augmented Generation (RAG) model. The system provides accurate and relevant healthcare advice based on user queries by retrieving information from the [NHS A-Z website](https://www.nhs.uk/health-a-z) and augmenting it with a Large Language Model (LLM). 

The project is developed as part of the MLH ["Hack for Hackers"](https://events.mlh.io/events/11516) hackathon.

## Features
- **Comprehensive Healthcare Information**: The system leverages the NHS A-Z data, which covers a wide range of medical conditions, treatments, self-care advice, and medicines.
- **Retrieval-Augmented Generation (RAG)**: Combines a vector similarity search with an LLM to deliver personalized and accurate responses.
- **Efficient Query Handling**: For each query, the system retrieves the most relevant documents from the database to enhance the LLM's output.
- **Scalable Backend**: Powered by MongoDB Atlas for efficient storage and retrieval of embeddings and documents.

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
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd nhs-rag
   ```

2. Install dependencies for the backend:
   ```bash
   cd rest
   npm pip install -r requirements.txt
   ```

3. Install dependencies for the web scraper:
   ```bash
   cd scraper
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the `rest` directory with the following details:
   ```env
   MONGODB_ATLAS_CLUSTER_URI=<your-mongodb-atlas-uri>
   OPENAI_API_KEY=<your-openai-api-key>
   NHS_URL=https://www.nhs.uk/conditions/
   ```

5. Run the web scraper to populate the database:
   ```bash
   python scraper/scraper.py
   ```

6. Start the backend server:
   ```bash
   fastapi dev main.py
   ```

7. Run the frontend (optional):
   ```bash
   cd frontend
   npm install
   npm start
   ```

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
