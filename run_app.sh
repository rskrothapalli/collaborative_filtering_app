#!/bin/bash

/opt/conda/bin/uvicorn main:app --reload --host=0.0.0.0 --port=8001 --log-level=debug