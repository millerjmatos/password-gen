# Password Generator & Entropy Calculator
> Python toolkit for generating secure passwords and calculating entropy strength.

## :: Features

- Multiple length options from 8 to 128 characters
- Entropy calculation based on information theory
- Control over digit and special character distribution
- Ambiguous character exclusion and sequential repetition blocking
- Interactive CLI with strength indicators

## :: Usage

1. Generate a password:
```bash
python web16.py
```
```
Password: aB3@xK9!mP2$qR7%
```

2. Analyze password strength:
```bash
python entropy.py
```
```
=== Password Entropy Calculator ===
Enter the password to analyze (or 'exit' to quit): MyP@ssw0rd123
Password analysis:
- Length: 13 characters
- Character set size: 88
- Entropy: 84.0 bits
- Strength: Strong
Characteristics:
- Contains lowercase letters: yes
- Contains uppercase letters: yes
- Contains numbers: yes
- Number of digits: 4
- Contains special characters: yes
- Number of special characters: 1
```

3. Customize generation parameters:
```python
pwd = generate_password(
    length=16,         # Password length
    num_digits=3,      # Minimum digits
    num_special=3      # Minimum special chars
)
```

## :: Prerequisites

1. Python 3.6+
2. Standard library only - no external dependencies required

## :: Available Generators

| File | Length | Use Case |
|------|--------|----------|
| `web8.py` | 8 chars | Basic accounts |
| `web16.py` | 16 chars | Standard security |
| `web24.py` | 24 chars | Enhanced protection |
| `web32.py` | 32 chars | High security |
| `web48.py` | 48 chars | Critical systems |
| `web64.py` | 64 chars | Maximum security |
| `web96.py` | 96 chars | Cryptographic keys |
| `web128.py` | 128 chars | Enterprise-grade |
| `entropy.py` | - | Strength analysis |

## :: Entropy Reference

| Entropy (bits) | Strength | Recommendation |
|----------------|----------|----------------|
| < 28 | Very Weak | Avoid |
| 28-36 | Weak | Upgrade |
| 36-60 | Reasonable | Use with 2FA |
| 60-128 | Strong | Recommended |
| > 128 | Very Strong | Excellent |

___
Created by [Muller Matos](https://linktr.ee/millerjmatos)
