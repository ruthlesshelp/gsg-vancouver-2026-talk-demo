# Shopping Cart Calculator Kata

This kata teaches how to implement a small, well-specified library while evolving collaboration with AI agents. You will move through three phases:

1. Human red/green/refactor TDD
2. Human + AI pair programming with red/green/refactor
3. Fully agentic engineering with guardrails

Target stack: Python + `pytest` + `flake8`. The implementation name is `checkout` and it must follow the rules in [SPEC.md](SPEC.md) and [TEST_PLAN.md](TEST_PLAN.md).

## Learning objectives

- Learn human-AI collaboration patterns on a small, concrete example
- Practice iterative refinement: human-led TDD -> pair programming -> fully agentic with guardrails
- Build comprehensive test coverage from a language-agnostic spec
- Run validation checks (linting, tests, and optional type checking)

## Prerequisites

- Python 3.8+ recommended
- `pytest` installed
- `flake8` installed

If you do not have these tools installed, install with `pip` in a virtual environment.

See this how-to on [Installation](README.md#installation)

## Inputs

- [SPEC.md](SPEC.md) is the single source of truth for behavior
- [TEST_PLAN.md](TEST_PLAN.md) contains scenarios you must translate into `pytest` tests

## Expected outputs

- `checkout.py` (implementation)
- `test_checkout.py` (tests generated from [TEST_PLAN.md](TEST_PLAN.md))

## Phase 1: Human-led TDD (red/green/refactor)

**Goal:** Build the core behavior by writing tests first and implementing in small steps.

**Timebox:** 10 to 15 minutes

**Constraints and guardrails**

- No AI assistance for tests or implementation
- Implement in tiny steps; one failing test at a time
- Avoid over-design; solve the test in front of you

**Suggested steps**

1. Read [SPEC.md](SPEC.md) and outline the API and error rules.
2. Convert the first 2 to 4 scenarios from [TEST_PLAN.md](TEST_PLAN.md) into `pytest` tests.
3. Implement only enough code to pass those tests.
4. Refactor after green if duplication appears.
5. Repeat until you cover discounts and errors.

**Checkpoint**

- At least 6 scenarios implemented as tests
- Passing tests for **Basic Functionality**: empty cart total, single item totals, and correct combined total
- Implementation does not use floats for money

## Phase 2: Human + AI pair programming (red/green/refactor)

**Goal:** Use an AI agent as a coding partner while you steer the TDD cycle and review changes.

**Timebox:** 10 to 15 minutes

**Constraints and guardrails**

- You decide the next test; the agent may propose a test but you approve it
- The agent can write code, but you run tests and interpret failures
- Red/green/refactor discipline maintained.
- All changes must be justified by a test or a refactor plan

**Suggested steps**

1. Ask the agent to translate a block of scenarios into `pytest` tests.
2. Review the tests for alignment with [SPEC.md](SPEC.md) and adjust as needed.
3. Run `pytest -v`, then ask the agent to implement the minimal fix.
4. Refactor with the agent only after green.

**Checkpoint**

- All scenarios from **Error Handling** and **Discount Boundary Tests** [TEST_PLAN.md](TEST_PLAN.md) are implemented as tests
- All **Error Handling** and **Discount Boundary Tests** tests pass
- Error handling is covered for unknown and invalid SKU input
- Both discount and non-discount cases are handled properly

## Phase 3: Fully agentic engineering (guardrailed)

**Goal:** Let the agent drive the work end-to-end while you set guardrails and review outputs.

**Timebox:** 10 to 30 minutes

**Constraints and guardrails**

- The agent must not skip tests or validation steps
- The agent must keep all changes within this repo
- The agent must stop and ask for clarification on ambiguities
- You review diffs before accepting them

**Suggested steps**

1. Provide the agent with explicit guardrails and completion criteria.
2. Ask for a short plan before changes.
3. Ask for a summary of changes and the test results.
4. Review the diff and confirm it matches the spec.

**Checkpoint**

- Implementation passes `pytest` and `flake8`
- The tests match the scenarios in [TEST_PLAN.md](TEST_PLAN.md)

## Sample prompts (verbatim)

Use these prompts as-is in each phase. You can copy and paste them into your AI tool.

### Phase 1 prompt (human-only reminder)

```
I am doing human-led red/green/refactor. Do not write code or tests. Only answer questions about process or TDD discipline.
```

### Phase 2 prompt (pair programming)

```
You are my pair programmer for the checkout kata in Python.

Rules:
- I will choose the next test to add. You can propose tests, but I approve them.
- Use red/green/refactor. No refactor without a green test.
- Make minimal changes to pass the failing test.
- Align strictly to SPEC.md and Test Plan.
- Ask when unclear.

Tasks:
1. Translate the next 3 scenarios from Test Plan into `pytest` tests in test_checkout.py.
2. Implement only the minimal code in checkout.py to pass those tests.
3. Stop after the tests pass and summarize what changed.
```

### Phase 3 prompt (fully agentic with guardrails)

```
You are a fully agentic engineer implementing the checkout kata in Python.

Guardrails:
- Read SPEC.md and Test Plan and treat them as the single source of truth.
- Create or update checkout.py and test_checkout.py only.
- Use `pytest` for tests and `flake8` for linting.
- Run tests after each meaningful change and report results.
- Stop and ask if any requirement conflicts or seems ambiguous.

Deliverables:
- Passing `pytest` suite based on all scenarios in Test Plan
- Lint clean with `flake8`
- Short summary of diffs and remaining risks

Begin by writing a plan of 5 to 8 steps, then execute it.
```

## Validation workflow

Run these commands locally:

```bash
pytest
`flake8`
```

Optional type checking:

```bash
mypy checkout.py
```

If mypy is not installed, either install it or note that type checking was skipped.

## Completion criteria checklist

- All scenarios from [TEST_PLAN.md](TEST_PLAN.md) are implemented as `pytest` tests
- `scan()` raises errors for unknown and invalid SKU input
- `total()` is idempotent and order independent
- Discounts are applied only for complete sets
- No floating point arithmetic for money
- `pytest` and ``flake8`` pass (and `mypy` if used)

## Reflection

- What did you learn about slowing down to keep red/green/refactor clean?
- Where did AI help the most, and where did it create risk?
- What guardrail kept the agent honest?
- What would you change before using this workflow on a larger system?
