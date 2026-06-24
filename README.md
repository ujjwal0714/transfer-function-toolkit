# Polynomial and Transfer Function Toolkit

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?logo=pydantic)
![License](https://img.shields.io/badge/License-MIT-green)

Lightweight Pydantic models for polynomial algebra and transfer function manipulation, with support for common arithmetic and system operations used in control systems and signal processing.

## Features

### Polynomial

* Addition
* Subtraction
* Polynomial Multiplication (Convolution)
* Scalar Multiplication
* Operator Overloading

### Transfer Function

* Series Combination (`*`)
* Parallel Combination (`+`)
* Subtraction (`-`)
* Inversion (`~`)
* Division (`/`)

## Project Structure

```text
.
├── polynomial.py
├── tf.py
└── usage.py
```

## Example

```python
from polynomial import Polynomial

p = Polynomial(coffs=[4, 5, 6])
q = Polynomial(coffs=[0, 1, 2, 3])

print(p + q)
print(p - q)
print(p * q)

print(2 * q)
print(q * 2)
```

```python
from polynomial import Polynomial
from tf import TF

g1 = TF(
    nr=Polynomial(coffs=[1]),
    dr=Polynomial(coffs=[1, 0])
)

g2 = TF(
    nr=Polynomial(coffs=[1]),
    dr=Polynomial(coffs=[1, 1])
)

series = g1 * g2
parallel = g1 + g2
inverse = ~g1
division = g1 / g2
```

## Motivation

Created as a foundation for higher-level control systems tooling such as transfer function analysis, block diagram reduction, signal flow graphs, and related computational workflows.

## License

MIT
