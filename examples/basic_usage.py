"""
Basic usage example of the RAG Chatbot
Run with: python examples/basic_usage.py
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.rag_engine import RAGChatbot
from src.config import Config

def main():
    print("=" * 60)
    print("📚 RAG Chatbot - Basic Usage Example")
    print("=" * 60)
    
    # Initialize chatbot
    chatbot = RAGChatbot(
        openai_api_key=Config.OPENAI_API_KEY,
        pinecone_api_key=Config.PINECONE_API_KEY,
        model_name=Config.MODEL_NAME
    )
    print("\n✓ Chatbot initialized")
    
    # Add sample document
    print("\n📂 Loading sample document...")
    chatbot.add_documents(["tests/sample_document.txt"])
    
    # Print stats
    print("\n📊 Chatbot Stats:")
    stats = chatbot.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Example questions
    questions = [
        "What is artificial intelligence?",
        "Tell me about machine learning",
        "What are the applications of AI?",
        "Explain deep learning"
    ]
    
    print("\n" + "=" * 60)
    print("🤖 Asking Questions:")
    print("=" * 60)
    
    for question in questions:
        print(f"\n❓ Q: {question}")
        response = chatbot.ask(question)
        print(f"💬 A: {response}")
        print("-" * 60)
    
    print("\n✓ Example completed successfully!")

if __name__ == "__main__":
    main()