import trio

async def main():
    async with httpx.AsyncClient() as client:
        r = await client.get("https://randomuser.me/api")
        print(r.content.decode("utf-8"))

# call_async_context
trio.run(main)
