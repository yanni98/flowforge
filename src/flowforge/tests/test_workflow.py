import asyncio

from flowforge import Workflow


def test_workflow():
    workflow = Workflow()

    workflow.add(lambda value: value + 1)
    workflow.add(lambda value: value * 2)

    result = asyncio.run(workflow.run(10))

    assert result.value == 22
    assert result.steps_completed == 2
