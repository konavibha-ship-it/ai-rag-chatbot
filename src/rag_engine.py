"""Main RAG Engine for the chatbot"""

import logging
from typing import List, Optional

logger = logging.getLogger(__name__)

class RAGChatbot:
    """
    Retrieval-Augmented Generation Chatbot
    
    Combines document retrieval with LLM generation
    to provide accurate, context-aware responses.
    """
    
    def __init__(
        self,
        openai_api_key: Optional[str] = None,
        pinecone_api_key: Optional[str] = None,
        model_name: str = "gpt-3.5-turbo",
        embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
    ):
        """
        Initialize the RAG chatbot.
        
        Args:
            openai_api_key: OpenAI API key
            pinecone_api_key: Pinecone API key
            model_name: LLM model to use
            embedding_model: Embedding model name
        """
        self.openai_api_key = openai_api_key
        self.pinecone_api_key = pinecone_api_key
        self.model_name = model_name
        self.embedding_model = embedding_model
        self.documents = []
        self.embeddings_list = []
        
        logger.info(f"Initialized RAG Chatbot with model: {self.model_name}")
    
    def add_documents(self, file_paths: List[str]) -> None:
        """
        Add documents to the RAG system.
        
        Args:
            file_paths: List of paths to documents (txt, pdf)
        """
        for path in file_paths:
            logger.info(f"Loading document: {path}")
            try:
                # Simple text file loading for MVP
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.documents.append({
                    "path": path,
                    "content": content,
                    "size": len(content)
                })
                logger.info(f"Successfully loaded: {path}")
            except FileNotFoundError:
                logger.error(f"File not found: {path}")
            except Exception as e:
                logger.error(f"Error loading {path}: {str(e)}")
    
    def retrieve_context(self, query: str, top_k: int = 3) -> List[str]:
        """
        Retrieve relevant document chunks for a query.
        
        Args:
            query: User's question
            top_k: Number of chunks to retrieve
            
        Returns:
            List of relevant document chunks
        """
        if not self.documents:
            return ["No documents loaded. Please add documents first."]
        
        logger.info(f"Retrieving context for query: {query}")
        
        # Simple retrieval (in production, use vector DB)
        results = []
        for doc in self.documents:
            # Check if query keywords are in document
            if any(keyword in doc["content"].lower() 
                   for keyword in query.lower().split()):
                results.append(doc["content"][:500])  # First 500 chars
        
        return results if results else ["No matching documents found."]
    
    def generate_response(self, query: str, context: str = "") -> str:
        """
        Generate a response using LLM.
        
        Args:
            query: User's question
            context: Retrieved context (optional for MVP)
            
        Returns:
            Generated response
        """
        logger.info(f"Generating response for: {query}")
        
        # For MVP, return informative message
        # In production, integrate with OpenAI API
        if context:
            return f"Based on the documents: '{context[:200]}...' - Response would be generated here using {self.model_name}"
        else:
            return f"I don't have relevant documents to answer: '{query}'. Please add documents using add_documents()"
    
    def ask(self, query: str) -> str:
        """
        Full pipeline: retrieve + generate.
        
        Args:
            query: User's question
            
        Returns:
            Final response
        """
        context_list = self.retrieve_context(query)
        context = "\n".join(context_list)
        response = self.generate_response(query, context)
        return response
    
    def get_stats(self) -> dict:
        """Get chatbot statistics"""
        return {
            "total_documents": len(self.documents),
            "total_size_chars": sum(d["size"] for d in self.documents),
            "model": self.model_name,
            "embedding_model": self.embedding_model
        }

    def __repr__(self) -> str:
        return f"RAGChatbot(model={self.model_name}, docs={len(self.documents)})"