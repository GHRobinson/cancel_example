import asyncio
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

task_list = []

async def do_work():
    begin = datetime.now()
    try:
        await asyncio.sleep(30)
    except asyncio.CancelledError:
        pass
    return datetime.now() - begin


@app.get("/start")
async def start():
    t = asyncio.Task(do_work())
    task_list.append(t)
    await t
    return t.result()


@app.get("/cancel_now")
def cancel():      # not async; can't await
    if len(task_list) > 0:
        t = task_list[-1]
        t.cancel()
    return "OK"   # can't be sure of t's final state if we can't await and return the result


@app.get("/delay_cancel")
async def cancel_later(delay_seconds: int):
    if len(task_list) > 0:
        t = task_list[-1]
    await asyncio.sleep(delay_seconds)
    t.cancel()
    await t
    return t.result()
