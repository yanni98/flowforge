from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Any, Awaitable, Callable


Step = Callable[[Any], Any | Awaitable[Any]]


@dataclass
class WorkflowResult:
    """Result returned after a workflow completes."""

    value: Any
    steps_completed: int


class Workflow:
    """Execute a sequence of synchronous or asynchronous steps."""

    def __init__(self) -> None:
        self._steps: list[Step] = []

    def add(self, step: Step) -> "Workflow":
        """Add a step to the workflow."""
        if not callable(step):
            raise TypeError("step must be callable")

        self._steps.append(step)
        return self

    async def run(self, value: Any = None) -> WorkflowResult:
        """Run all workflow steps in order."""
        current = value
        completed = 0

        for step in self._steps:
            result = step(current)

            if asyncio.iscoroutine(result):
                current = await result
            else:
                current = result

            completed += 1

        return WorkflowResult(
            value=current,
            steps_completed=completed,
        )
