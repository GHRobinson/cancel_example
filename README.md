# How to install and run

1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `uvicorn async_cancel_test:app --reload`
5. Visit http://localhost:8000/start (notice that the browser will spin)
6. Within 30 seconds, visit http://localhost:8000/cancel_now or http://localhost:8000/delay_cancel?delay_seconds=4
7. Notice that the time elapsed in each result is the same (or just "OK" with cancel_now)
