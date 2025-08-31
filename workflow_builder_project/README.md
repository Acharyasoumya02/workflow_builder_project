# Workflow Builder - No-Code/Low-Code Intelligence Platform

A comprehensive full-stack application that enables users to visually create and interact with intelligent workflows using drag-and-drop components.

## 🚀 Features

### Core Components
- **User Query Component**: Entry point for user interactions
- **Knowledge Base Component**: Document processing with vector embeddings
- **LLM Engine Component**: AI-powered responses using OpenAI GPT or Google Gemini
- **Output Component**: Formatted responses with optional source citations

### Frontend Features
- **Visual Workflow Builder**: Drag-and-drop interface using React Flow
- **Component Configuration**: Dynamic configuration panels for each component
- **Real-time Chat Interface**: Execute workflows through conversational interface
- **Responsive Design**: Modern Material-UI components with dark/light theme support

### Backend Features
- **Document Processing**: PDF text extraction with PyMuPDF
- **Vector Storage**: ChromaDB for semantic search capabilities
- **Multi-LLM Support**: OpenAI GPT and Google Gemini integration
- **Web Search Integration**: SerpAPI for real-time web information
- **Workflow Orchestration**: Intelligent component execution engine

## 🏗️ Architecture

```
┌─────────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
│     Frontend        │    │      Backend        │    │     Database        │
│   (React.js)        │◄──►│    (FastAPI)        │◄──►│   (PostgreSQL)      │
│                     │    │                     │    │                     │
│ • React Flow        │    │ • Document APIs     │    │ • Workflows         │
│ • Material-UI       │    │ • Workflow Engine   │    │ • Documents         │
│ • Component Config  │    │ • Vector Store      │    │ • Chat Sessions     │
│ • Chat Interface    │    │ • LLM Integration   │    │ • Messages          │
└─────────────────────┘    └─────────────────────┘    └─────────────────────┘
                                      │
                           ┌─────────────────────┐
                           │   Vector Store      │
                           │   (ChromaDB)        │
                           │                     │
                           │ • Document Chunks   │
                           │ • Embeddings        │
                           │ • Similarity Search │
                           └─────────────────────┘
```

## 🛠️ Tech Stack

### Frontend
- **React.js 18** - Modern React with hooks
- **TypeScript** - Type safety and better development experience
- **Material-UI (MUI)** - Component library and theming
- **React Flow** - Visual workflow builder
- **Axios** - API communication
- **React Hot Toast** - User notifications

### Backend
- **FastAPI** - High-performance Python web framework
- **SQLAlchemy** - Database ORM with PostgreSQL
- **ChromaDB** - Vector database for embeddings
- **OpenAI API** - GPT models for text generation
- **Google Gemini API** - Alternative LLM provider
- **PyMuPDF** - PDF text extraction
- **SerpAPI** - Web search capabilities

### Database & Storage
- **PostgreSQL** - Primary relational database
- **ChromaDB** - Vector storage for document embeddings
- **File System** - Document storage with organized structure

## 🚀 Quick Start

### Prerequisites
- **Node.js 16+** and **npm**
- **Python 3.8+** and **pip**
- **PostgreSQL 12+**
- **API Keys**: OpenAI, Google Gemini (optional), SerpAPI (optional)

### 1. Clone and Setup
```bash
git clone <repository-url>
cd workflow-builder-app
```

### 2. Backend Setup
```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your configuration

# Initialize database
python -c "from app.database.config import create_tables; create_tables()"

# Run backend server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Frontend Setup
```bash
cd ../frontend

# Install dependencies
npm install

# Start development server
npm start
```

### 4. Environment Configuration

Create `.env` file in the backend directory:

```env
# Database Configuration
DATABASE_URL=postgresql://postgres:password@localhost:5432/workflow_builder
DATABASE_ECHO=false

# ChromaDB Configuration
CHROMA_DB_PATH=./chroma_db

# API Keys
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
SERP_API_KEY=your_serpapi_key_here

# File Upload Configuration
UPLOAD_DIR=./uploads
MAX_FILE_SIZE=52428800  # 50MB
```

## 📊 Database Schema

### Core Tables
```sql
-- Workflows table
CREATE TABLE workflows (
    id VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL,
    description TEXT,
    components JSON NOT NULL,
    connections JSON NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);

-- Documents table
CREATE TABLE documents (
    id VARCHAR PRIMARY KEY,
    filename VARCHAR NOT NULL,
    original_filename VARCHAR NOT NULL,
    file_path VARCHAR NOT NULL,
    file_size INTEGER NOT NULL,
    content_type VARCHAR NOT NULL,
    extracted_text TEXT,
    is_processed BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);

-- Chat sessions table
CREATE TABLE chat_sessions (
    id VARCHAR PRIMARY KEY,
    workflow_id VARCHAR REFERENCES workflows(id),
    session_name VARCHAR,
    created_at TIMESTAMP WITH TIME ZONE
);

-- Chat messages table
CREATE TABLE chat_messages (
    id VARCHAR PRIMARY KEY,
    session_id VARCHAR REFERENCES chat_sessions(id),
    role VARCHAR NOT NULL,
    content TEXT NOT NULL,
    metadata JSON,
    created_at TIMESTAMP WITH TIME ZONE
);
```

## 🔧 API Documentation

### Key Endpoints

#### Documents
- `POST /api/documents/upload` - Upload and process documents
- `GET /api/documents` - List all documents
- `GET /api/documents/{id}` - Get specific document
- `DELETE /api/documents/{id}` - Delete document

#### Workflows
- `POST /api/workflows` - Create new workflow
- `GET /api/workflows` - List workflows
- `GET /api/workflows/{id}` - Get specific workflow
- `PUT /api/workflows/{id}` - Update workflow
- `DELETE /api/workflows/{id}` - Delete workflow

#### Chat
- `POST /api/chat/execute` - Execute workflow with query
- `GET /api/chat/sessions/{workflow_id}` - Get chat sessions
- `GET /api/chat/messages/{session_id}` - Get chat messages

#### Health Check
- `GET /health` - Application health status

## 🎯 Component Configuration

### User Query Component
```json
{
  "placeholder_text": "Enter your question...",
  "max_length": 1000
}
```

### Knowledge Base Component
```json
{
  "document_ids": ["doc1", "doc2"],
  "chunk_size": 1000,
  "chunk_overlap": 200,
  "similarity_threshold": 0.7,
  "max_results": 5
}
```

### LLM Engine Component
```json
{
  "provider": "openai",
  "model": "gpt-3.5-turbo",
  "temperature": 0.7,
  "max_tokens": 1000,
  "system_prompt": "You are a helpful assistant.",
  "use_web_search": false,
  "web_search_queries": 3
}
```

### Output Component
```json
{
  "format": "text",
  "show_sources": true,
  "show_confidence": false
}
```

## 🐳 Docker Deployment

### Build and Run with Docker Compose
```bash
# Build and start all services
docker-compose up --build

# Run in detached mode
docker-compose up -d

# Stop services
docker-compose down
```

### Docker Configuration Files

**docker-compose.yml**
```yaml
version: '3.8'

services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    depends_on:
      - postgres
    environment:
      - DATABASE_URL=postgresql://postgres:password@postgres:5432/workflow_builder

  postgres:
    image: postgres:13
    environment:
      - POSTGRES_DB=workflow_builder
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
python -m pytest tests/ -v
```

### Frontend Tests
```bash
cd frontend
npm test
```

### API Testing with curl
```bash
# Health check
curl http://localhost:8000/health

# Upload document
curl -X POST -F "file=@document.pdf" http://localhost:8000/api/documents/upload

# Create workflow
curl -X POST -H "Content-Type: application/json" \
     -d '{"name": "Test Workflow", "components": [], "connections": []}' \
     http://localhost:8000/api/workflows
```

## 🔍 Troubleshooting

### Common Issues

1. **Database Connection Failed**
   - Check PostgreSQL is running
   - Verify DATABASE_URL in .env
   - Ensure database exists

2. **ChromaDB Issues**
   - Check CHROMA_DB_PATH permissions
   - Clear ChromaDB data: `rm -rf ./chroma_db`

3. **API Key Errors**
   - Verify OpenAI/Gemini API keys
   - Check API quota and billing

4. **Frontend Build Errors**
   - Clear node_modules: `rm -rf node_modules && npm install`
   - Check Node.js version compatibility

5. **File Upload Issues**
   - Check UPLOAD_DIR permissions
   - Verify MAX_FILE_SIZE settings

### Performance Optimization

1. **Database Optimization**
   - Add indexes for frequently queried fields
   - Use connection pooling
   - Regular database maintenance

2. **Vector Store Optimization**
   - Batch embedding operations
   - Optimize similarity search parameters
   - Consider chunking strategies

3. **Frontend Optimization**
   - Implement component lazy loading
   - Use React.memo for expensive components
   - Optimize bundle size

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **React Flow** - For the excellent workflow visualization library
- **FastAPI** - For the high-performance web framework
- **ChromaDB** - For the vector database capabilities
- **Material-UI** - For the beautiful component library
- **OpenAI & Google** - For the powerful language models

## 📞 Support

For support, please open an issue in the GitHub repository or contact the development team.

---

**Built with ❤️ for the No-Code/Low-Code community**
