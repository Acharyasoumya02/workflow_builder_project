"""
Main FastAPI application for the workflow builder.
"""

from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import os
from contextlib import asynccontextmanager

from app.database.config import get_database_session, create_tables
from app.routers import documents, workflows, chat, components
from app.services.vector_store import vector_store

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    # Startup
    print("Starting up workflow builder application...")
    create_tables()
    print("Database tables created successfully")

    yield

    # Shutdown
    print("Shutting down workflow builder application...")

# Create FastAPI app with lifespan
app = FastAPI(
    title="Workflow Builder API",
    description="No-Code/Low-Code workflow builder with intelligent components",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(documents.router, prefix="/api/documents", tags=["documents"])
app.include_router(workflows.router, prefix="/api/workflows", tags=["workflows"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(components.router, prefix="/api/components", tags=["components"])

# Health check endpoint
@app.get("/")
async def root():
    return {
        "message": "Workflow Builder API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    try:
        # Check vector store
        stats = vector_store.get_collection_stats()

        return {
            "status": "healthy",
            "database": "connected",
            "vector_store": "connected",
            "vector_store_stats": stats
        }
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Service unhealthy: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
