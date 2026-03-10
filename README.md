# GSG Vancouver 2026 AI and Agile Engineering Demo

Python test-driven development (TDD) exercises for the Global Scrum Gathering Vancouver 2026 "AI and Agile Engineering" talk's live coding demonstration. See https://www.gsgvan26.com/agenda/session/1820794

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

Install dependencies:
```bash
pip install pytest pytest-cov
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
├── KATA.md             # Description of the kata
├── SPEC.md             # Functional specification
├── src/                # Python source code
├── tests/              # Python test code
└── TEST_PLAN.md        # Examples of testing scenarios
```

## Learning Objectives

This coding dojo focuses on:

- **Test-Driven Development**: Write tests first, implement to make them pass

## License

This project is licensed under the MIT License. See LICENSE file for details.

---

**Note**: This project is designed as a learning exercise for understanding test-driven development, pair programming, collective code ownership, and AI-assisted development.
