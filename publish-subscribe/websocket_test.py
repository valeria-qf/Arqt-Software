import asyncio
import websockets
import json

async def test_websocket():
    # url do websocket com o token incluído na query string
    token = "ccccde1ff3e703bc5794607c35c0ea8dfeb67877"
    ws_url = f"ws://127.0.0.1:8000/ws/notifications/?token={token}"
    
    async with websockets.connect(ws_url) as websocket:
        print("WebSocket conectado.")

        # envia uma mensagem de inscrição para o tópico
        subscribe_message = json.dumps({
            "type": "subscribe",
            "topic": "music"

        })
        await websocket.send(subscribe_message)
        print(f"Enviado: {subscribe_message}")

        # Recebe e imprime mensagens do websocket
        while True:
            response = await websocket.recv()
            print(f"Recebido: {response}")

if __name__ == "__main__":
    asyncio.run(test_websocket())
