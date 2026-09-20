import asyncio

from flowforge import Workflow


async def main():
    workflow = Workflow()

    workflow.add(lambda value: value + 1)
    workflow.add(lambda value: value * 2)

    result = await workflow.run(10)

    print(result.value)
    # 22


asyncio.run(main())

