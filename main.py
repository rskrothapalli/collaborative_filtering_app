# Entry point for REST APIs - Main Application

from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(title='FastAPIApplication', debug=False)
    return app

# Initialize FastAPI application
app = create_app()




