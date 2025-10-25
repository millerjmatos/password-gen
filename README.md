# Password Generator & Entropy Calculator

> Python toolkit for generating secure passwords and calculating entropy strength.

## ✨ Features

- **Multiple Length Options**: Generate passwords from 8 to 128 characters
- **Entropy Analysis**: Calculate password strength using information theory
- **Character Diversity**: Control digits and special characters distribution
- **Security Filters**: Avoid ambiguous characters and sequential repetitions
- **Visual Feedback**: Interactive CLI with strength indicators

## 🚀 Usage

### Generate Password 🔒
```bash
python web16.py
```

**Output:**
```
Password: aB3@xK9!mP2$qR7%
```

### Analyze Password Strength
```bash
python entropy.py
```

**Interactive Session:**
```
=== Password Entropy Calculator ===
Enter the password to analyze (or 'exit' to quit): MyP@ssw0rd123

Password analysis:
- Length: 13 characters
- Character set size: 88
- Entropy: 84.0 bits
- Strength: Strong

Characteristics:
- Contains lowercase letters: ✓
- Contains uppercase letters: ✓
- Contains numbers: ✓
- Number of digits: 4
- Contains special characters: ✓
- Number of special characters: 1
```

## 🔧 Prerequisites

1. **Python 3.6+**
2. **Standard Library Only** (no external dependencies)

## 📋 Available Generators

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

## ⚙️ Customization

Modify generation parameters in any generator file:
```python
pwd = generate_password(
    length=16,         # Password length
    num_digits=3,      # Minimum digits
    num_special=3      # Minimum special chars
)
```

## 🛡️ Security Features

- ⚠ **Ambiguous Characters Excluded**: `0OoLlIi1` removed
- ✗ **No Sequential Repetition**: `aa`, `11` patterns blocked
- ✓ **Cryptographic Randomness**: Uses `random.choices()` for distribution
- ✓ **Character Set Validation**: Ensures minimum complexity requirements

## 📊 Entropy Scale

| Entropy (bits) | Strength | Recommendation |
|----------------|----------|----------------|
| < 28 | Very Weak | ✗ Avoid |
| 28-36 | Weak | ⚠ Upgrade |
| 36-60 | Reasonable | Use with 2FA |
| 60-128 | Strong | ✓ Recommended |
| > 128 | Very Strong | 😀 Excellent |

___

**Created by [Muller Matos](https://linktr.ee/millerjmatos)**
