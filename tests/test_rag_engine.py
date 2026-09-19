"""Tests for RAG Engine"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.rag_engine import RAGChatbot
from src.config import Config

class TestRAGChatbot:
    """Test cases for RAGChatbot"""
    
    @pytest.fixture
    def chatbot(self):
        """Create a chatbot instance for testing"""
        return RAGChatbot(
            openai_api_key="test-key",
            pinecone_api_key="test-key",
            model_name="gpt-3.5-turbo"
        )
    
    def test_initialization(self, chatbot):
        """Test chatbot initializes correctly"""
        assert chatbot is not None
        assert chatbot.model_name == "gpt-3.5-turbo"
        assert len(chatbot.documents) == 0
    
    def test_add_documents_no_file(self, chatbot):
        """Test adding non-existent document handles gracefully"""
        chatbot.add_documents(["nonexistent.txt"])
        assert len(chatbot.documents) == 0
    
    def test_retrieve_context_empty(self, chatbot):
        """Test retrieval with no documents"""
        results = chatbot.retrieve_context("test query")
        assert isinstance(results, list)
        assert len(results) > 0
    
    def test_generate_response(self, chatbot):
        """Test response generation"""
        response = chatbot.generate_response("What is AI?")
        assert isinstance(response, str)
        assert len(response) > 0
    
    def test_ask(self, chatbot):
        """Test full pipeline"""
        response = chatbot.ask("What is machine learning?")
        assert isinstance(response, str)
    
    def test_get_stats(self, chatbot):
        """Test statistics retrieval"""
        stats = chatbot.get_stats()
        assert isinstance(stats, dict)
        assert "total_documents" in stats
        assert "model" in stats
    
    def test_repr(self, chatbot):
        """Test string representation"""
        repr_str = repr(chatbot)
        assert "RAGChatbot" in repr_str
        assert "gpt-3.5-turbo" in repr_str

class TestConfig:
    """Test configuration"""
    
    def test_config_exists(self):
        """Test config loads"""
        assert Config.MODEL_NAME is not None
        assert Config.EMBEDDING_MODEL is not None