# Simple Calculator

```python
simple_calculator_controller = client.simple_calculator
```

## Class Name

`SimpleCalculatorController`


# Calculate

Calculates the expression using the specified operation.

```python
def calculate(self,
             x,
             y,
             operation)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x` | `float` | Query, Required | The LHS value. |
| `y` | `float` | Query, Required | The RHS value. |
| `operation` | [`OperationTypeEnum`](../../doc/models/operation-type-enum.md) | Template, Required | The operator to apply on the variables. |

## Response Type

`float`

## Example Usage

```python
x = 222.14
y = 165.14
operation = OperationTypeEnum.ADD

result = simple_calculator_controller.calculate(x, y, operation)
```

