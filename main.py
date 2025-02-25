import sys
import os
import asyncio

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from src.agent.agent import Agent


async def main():
    agent = Agent()
    print("agent start\n")

    while True:
        try:
            user_input = input("\n你: ").strip()
            if user_input.lower() in ['exit', 'quit']:
                break
            if not user_input:
                continue
            response = await agent.process_input(user_input)

        except Exception as e:
            print(f"\n{str(e)}")
            continue


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    sys.exit(0)
