"""Main entry point for the RAG Chatbot"""

import logging
import sys
from typing import Optional
from src.config import Config
from src.rag_engine import RAGChatbot

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main function to run chatbot"""
    
    print("=" * 60)
    print("🤖 AI RAG Chatbot")
    print("=" * 60)
    
    # Initialize chatbot
    try:
        chatbot = RAGChatbot(
            openai_api_key=Config.OPENAI_API_KEY,
            pinecone_api_key=Config.PINECONE_API_KEY,
            model_name=Config.MODEL_NAME,
            embedding_model=Config.EMBEDDING_MODEL
        )
        print("✓ Chatbot initialized successfully")
        print("\nStats:", chatbot.get_stats())
    except Exception as e:
        logger.error(f"Failed to initialize chatbot: {e}")
        sys.exit(1)
    
    # Interactive loop
    print("\n📝 Interactive Mode")
    print("Type 'quit' to exit")
    print("Type 'add <filepath>' to add documents")
    print("Type your question to ask the chatbot\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == 'quit':
                print("Goodbye! 👋")
                break
            
            if user_input.lower().startswith('add '):
                filepath = user_input[4:].strip()
                chatbot.add_documents([filepath])
                print(f"✓ Added document(s)\n")
                continue
            
            # Ask chatbot
            response = chatbot.ask(user_input)
            print(f"\nBot: {response}\n")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            break
        except Exception as e:
            logger.error(f"Error: {e}")
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()