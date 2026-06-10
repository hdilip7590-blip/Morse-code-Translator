# Morse Code Encoder / Decoder

A simple command-line Python tool to convert plain text to Morse code and back.

## Features

- Encode letters (A–Z) and digits (0–9) to Morse code
- Decode Morse code back to text
- Multi-word support using `/` as a word separator

## Usage

Run the script with Python 3:

```bash
python morse.py
```

You'll be prompted to choose an option:

```
Option 1: Code to Morse
Option 2: Decode to text
Option 3: Exit
Select your option:
```

### Encoding example

```
Select your option: 1
What word would you like to code:
HELLO WORLD
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

### Decoding example

```
Select your option: 2
What word would you like to decode:
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
HELLO WORLD
```

## Morse code format

| Element | Meaning |
|---|---|
| `.` | Dot |
| `-` | Dash |
| ` ` (space) | Letter separator |
| `/` | Word separator |

## Limitations

- Only supports A–Z and 0–9. Unsupported characters (e.g. `!`, `?`) are silently dropped during encoding.

## Requirements

- Python 3.x
- No external dependencies
