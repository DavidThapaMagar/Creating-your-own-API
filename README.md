# My FastAPI Project

## Prerequisites
- Python 3 installed on your machine

## Installation

Install the required packages:
```bash
pip3 install fastapi uvicorn
```

## Running the Server
```bash
cd "/path/to/your/project"
uvicorn myapi:app --reload
```

The server will start at `http://127.0.0.1:8000`

## Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/` | Returns a hello world message |
| GET | `/csv` | Returns CSV data as plain text |
| GET | `/greet/{name}` | Returns a greeting for the given name |

## Example

Visit `http://127.0.0.1:8000/greet/David` and you'll get:
```json
{"message": "Hello David!"}
```
