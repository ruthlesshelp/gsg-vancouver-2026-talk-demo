# TEST_PLAN.md

## Overview
This test plan covers the validation of a supermarket checkout system as specified in [SPEC.md](SPEC.md). The system must correctly scan items, raise errors for invalid SKUs, calculate totals, apply quantity-based discounts, and handle order independence.

## Test Categories
1. **Basic Functionality**
    - No items: total is 0
    - Single item of each product: correct total per SKU
        - APP => 31¢
        - BAN => 13¢
        - CORN => 47¢
        - DIP => 29¢
    - Two different items: correct combined total
        - APP + BAN => 44¢
        - APP + CORN => 78¢
        - BAN + CORN => 60¢
        - BAN + DIP => 42¢

2. **Error Handling**
    - Unknown SKU: raises error
    - Empty SKU: raises error

3. **Discount Boundary Tests**
    - APP (Apple): 3 for 81¢
        - 1, 2, 3, 4, 6 items (discount and non-discount cases)
    - BAN (Banana): 2 for 20¢
        - 1, 2, 3, 4 items (discount and non-discount cases)

4. **Order Independence**
    - Scanning items in different orders yields the same total

5. **Mixed Items**
    - Partial discounts: mix of discounted and non-discounted items
    - Complex cart: multiple discounts and regular items

6. **Items Without Discounts**
    - Multiple items (CORN, DIP) with no discounts applied

## Test Scenarios

### 1. Basic Functionality
- Calculate total for no items
- Calculate total for single item of each product (APP, BAN, CORN, DIP)
- Calculate total for two different items (APP + BAN)

### 2. Error Handling
- Scan UNKNOWN SKU (error)
- Scan empty SKU (error)

### 3. Discount Boundary Tests
- APP: 1, 2, 3, 4, 6 items (check discount application)
- BAN: 1, 2, 3, 4 items (check discount application)

### 4. Order Independence
- Scan APP, BAN, APP, APP (check total is correct regardless of order)

### 5. Mixed Items
- APP, APP, BAN, CORN (partial discount)
- APP, APP, APP, BAN, BAN, CORN, DIP (multiple discounts)

### 6. Items Without Discounts
- Multiple CORN and DIP (no discounts)

## Acceptance Criteria
- All scenarios must pass as described in tests.feature
- Totals must match expected values
- Discounts must be applied correctly
- Errors must be raised for invalid SKUs
- Order of scanning must not affect totals

## Traceability
Each scenario in [TEST_PLAN.md](TEST_PLAN.md) is mapped to a corresponding requirement in [SPEC.md](SPEC.md) and all are covered.
