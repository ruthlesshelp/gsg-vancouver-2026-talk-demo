# GSG Vancouver 2026 AI and Agile Engineering Demo

Python test-driven development (TDD) exercises for the Global Scrum Gathering Vancouver 2026 "AI and Agile Engineering" talk's live coding demonstration. See https://www.gsgvan26.com/agenda/session/1820794

This is a **kata** (a small, focused exercise designed to teach and practice skills) and not a production library. Its pedagogical goal is to illustrate three phases of human–AI collaboration during test-driven development.

This project is a shopping cart price calculator that computes the total cost of items scanned at a supermarket checkout, applying quantity-based discounts where applicable.

The kata is described in the [KATA.md](KATA.md) file.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Using virtual environment venv

Python virtual environments enable you to set up a Python sandbox with its own set of packages separate from the system site-packages in which to work.

#### Create

```bash
python -m venv .venv
```

#### Activate

To activate on macOS and Linux.
```bash
source .venv/bin/activate
```

To activate on Windows.
```bash
.venv\Scripts\activate.bat
```

To activate on Windows with PowerShell.
```bash
.venv\Scripts\Activate.ps
```

#### Deactivate

When done with the virtual environment, run:
```bash
deactivate
```

### Setup Instructions

Python modules are packages, which can be imported into a project to use.

Upgrade `pip` before installing dependencies:
```bash
pip install --upgrade pip
```

Install dependencies:
```bash
pip install pytest pytest-cov flake8
```

## Tests

### Running Tests

**Run all unit tests:**
```bash
pytest tests/ -v
```

**Run tests with coverage:**
```bash
python -m pytest tests/ -v --cov=src --cov-report=html --cov-report=term-missing
```

## Linting

**Run flake8 to check for style and syntax issues:**
```bash
flake8 src/ tests/
```

## Problem Statement

Implement a supermarket checkout system that scans items by SKU, looks up unit prices from a product catalog, and computes the total cost. Some products have quantity-based discounts (e.g., "3 apples for 81¢") that must be applied automatically when the required quantity is reached. The system must handle unknown or invalid SKUs by raising errors, and the scanning order must not affect the final total.

### Features

- **Scan items** — add products to the cart by SKU (e.g., `APP`, `BAN`, `CORN`, `DIP`)
- **Calculate totals** — compute the total price in cents, avoiding floating-point issues
- **Quantity discounts** — automatically apply discounts (APP: 3 for 81¢, BAN: 2 for 20¢)
- **Error handling** — raise errors for unknown, empty, or invalid SKUs
- **Order independence** — scanning items in any order produces the same total
- **Idempotent total** — calling `total()` multiple times without new scans returns the same value

### Documentation

- **[Kata](KATA.md)** - a small, focused exercise designed to hone skills
- **[Specification](SPEC.md)** - Business requirements and functional specifications
- **[Test Plan](TEST_PLAN.md)** - Description of the test plan

## Usage

### As a Library

```python
from checkout import Checkout

co = Checkout()
co.scan("APP")
co.scan("BAN")
co.scan("APP")
co.scan("APP")
print(co.total())  # 94 (3 APP for 81 + 1 BAN for 13)
```

## Project Structure

```
checkout_dojo/
├── KATA.md               # Exercise instructions (3 phases)
├── SPEC.md               # Business requirements (source of truth)
├── TEST_PLAN.md          # Scenarios to translate into pytest tests
├── README.md             # Installation, usage, problem statement
├── LICENSE               # MIT
├── pyproject.toml        # pytest config only (pythonpath = ["src"])
├── src/
│   ├── __init__.py       # Module marker (comment: "Makes src a Python module")
│   └── checkout.py       # Checkout class — STUB ONLY
└── tests/
    ├── __init__.py       # Empty
    └── test_checkout.py  # 1 test — currently FAILING
```

## Learning Objectives

This coding dojo focuses on:

- **Test-Driven Development**: Write tests first, implement to make them pass
- **Pair Programming**: Stay closely involved in the lowest levels of the implementation loop
- **Collective Code Ownership**: Encourage developers to feel responsible for the quality of the code

## Global Scrum Gathering Demos

For this GSG Vancouver 2026 [The Impact of AI and Vibe Coding on Agile Engineering Practices - What Every Manager Should Know](https://www.gsgvan26.com/agenda/session/1820794) talk, the demo followed three parts:
1. **TDD with Human Pairing**: using a classic red/green TDD with ping-pong pairing
2. **TDD with AI Pairing**: using the AI model for GitHub Copilot inline suggestions in Visual Studio Code, also known as [Ghost text suggestions](https://docs.github.com/en/copilot/concepts/completions/code-suggestions)
3. **Agentic Engineering**: using the AI model by prompting GitHub Copilot in the IDE while in [Agent mode](https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide#agent-mode)

### Demo 1: TDD with Human Pairing

### Demo 2: TDD with AI Pairing

### Demo 3: Agentic Engineering

#### First Prompt

```
Explore this workspace
```

#### First Response

> Read [src/checkout.py](./gsg-demo-03-2/src/checkout.py)
> 
> Read [tests/test_checkout.py](./gsg-demo-03-2/tests/test_checkout.py)
> 
> Read [TEST_PLAN.md](./gsg-demo-03-2/TEST_PLAN.md)
> 
> Read [SPEC.md](./gsg-demo-03-2/SPEC.md#1-1), lines 1 to 80
> 
> Read [KATA.md](./gsg-demo-03-2/KATA.md#1-1), lines 1 to 80
> 
> Read [pyproject.toml](./gsg-demo-03-2/pyproject.toml)
> 
> This is a **Shopping Cart Calculator Kata** — a TDD exercise for building a supermarket checkout system in Python.
> 
> **Current state:** The project is at the very beginning of implementation.
> 
> - checkout.py — `Checkout` class with `scan()` and `total()` stubs that both raise `NotImplementedError`
> - test_checkout.py — A single test: `test_total_is_0_when_no_items_scanned`, which will currently **fail** since `total()` raises `NotImplementedError`
> 
> **Spec summary** (SPEC.md):
> - Product catalog: `APP` (31¢, 3-for-81¢), `BAN` (13¢, 2-for-20¢), `CORN` (47¢), `DIP` (29¢)
> - `scan(sku)` adds an item; errors on unknown/empty SKU
> - `total()` returns the price in cents with quantity discounts applied
> - Order of scanning doesn't affect the total
> 
> **Kata phases** (KATA.md):
> 1. Human-led TDD (red/green/refactor)
> 2. Human + AI pair programming
> 3. Fully agentic with guardrails
> 
> **Test plan** (TEST_PLAN.md) covers 6 categories: basic functionality, error handling, discount boundaries, order independence, mixed items, and items without discounts.
> 
> The project is configured with `pytest` (pythonpath set to src in pyproject.toml). Ready for the first red/green/refactor cycle.
> 

#### Second Prompt

```
Use the existing virtual environment .venv
Write tests first (TDD)
Write test code that follows the 3A pattern (Arrange, Act, Assert)

This agent drives a TDD loop by invoking each subagent in strict order:
1. tdd-red: Implement next failing test following the 3A pattern
2. tdd-green: Implement minimal code to pass failing test.
3. tdd-refactor: Improve passing tests with no behavior change.

Continue the TDD loops until the TEST_PLAN.md is done
```

#### Second Response

A long-running TDD session.

## License

This project is licensed under the MIT License. See LICENSE file for details.

---

**Note**: This project is designed as a learning exercise for understanding test-driven development, pair programming, collective code ownership, and AI-assisted development.
