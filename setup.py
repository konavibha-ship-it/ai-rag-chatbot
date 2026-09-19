from setuptools import setup, find_packages

setup(
    name="ai-rag-chatbot",
    version="0.1.0",
    description="AI-powered RAG chatbot for intelligent document retrieval",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/YOUR_USERNAME/ai-rag-chatbot",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "openai>=1.0.0",
        "langchain>=0.0.300",
        "pinecone-client>=2.2.0",
        "sentence-transformers>=2.2.0",
        "python-dotenv>=1.0.0",
        "fastapi>=0.104.0",
    ],
)