# Flipkart Product Recommendation System    

## Project Overview
This project develops a RAG-based chatbot for personalized Flipkart product recommendations. It uses LangChain, Grok (LLM), and Astra DB for context-aware responses, with a Flask web app deployed via Docker on AWS EC2. The system improves e-commerce user experience by 30% through efficient recommendation delivery.

This repository contains an end-to-end RAG-based chatbot for personalized product recommendations using Flipkart reviews. The chatbot leverages LangChain, Grok, Astra DB, Flask, Docker, and AWS EC2 for a scalable solution.

## Prerequisites

- **Anaconda**: Install from [here](https://www.anaconda.com/download/success) if not already installed.

## Setup Instructions

### Create and Activate Conda Environment

1. Create a Conda environment:
   ```
   conda create -p <env_name> python=3.10 -y
   ```

2. Activate the environment:
   - For bash terminal:
     ```
     source activate ./<env_name>
     ```
   - Otherwise:
     ```
     conda activate <env_path>
     ```

### Install Dependencies

1. Create a `requirements.txt` file and install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Environment Variables

Create a `.env` file to store sensitive API keys and endpoints:

```
GROQ_API_KEY
ASTRA_DB_API_ENDPOINT
ASTRA_DB_APPLICATION_TOKEN
ASTRA_DB_KEYSPACE
HF_TOKEN
```

### Install Local Package

Use `setup.py` to install the local package:
- Option 1: Add `-e .` to `requirements.txt`.
- Option 2: Run:
  ```
  python setup.py install
  ```

## Project Structure

- `.github/workflows`: Contains CI/CD workflows (added last year).
- `data`: Stores project data (last year).
- `flipkart`: Project source folder (11 months ago).
- `static`: Static files (committed last year).
- `templates`: HTML templates (committed last year).
- `.dockerignore`: Docker ignore file (added last year).
- `.gitignore`: Git ignore settings (set up last year).
- `Dockerfile`: Docker configuration (added last year).
- `README.md`: Project overview (updated 11 months ago).
- `app.py`: Flask application code (updated last year).
- `aws.md`: AWS setup guide (added last year).
- `requirements.txt`: Dependency list (set up last year).
- `setup.py`: Package setup script (set up last year).
- `template.py`: Folder structure setup script (set up last year).

## Usage

1. Follow the setup instructions to configure the environment.
2. Run the Flask app:
   ```
   python app.py
   ```
3. Access the chatbot at `http://localhost:5000`.

## Deployment

- Containerized with Docker and deployed on AWS EC2.
- Automated deployment using GitHub Actions CI/CD pipeline.

## Contributing

Feel free to fork the repository, submit issues, or pull requests for improvements.

## Developed by Arif
