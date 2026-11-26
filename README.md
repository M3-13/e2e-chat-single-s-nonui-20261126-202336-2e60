# e2e-chat-single-s-nonui-20261126-202336-2e60
office-crew-sprint-runner e2e case chat-single-s-nonui

## Beschreibung

`textutils` ist eine kleine, eigenständige Python-Bibliothek mit fünf voneinander unabhängigen String-Hilfsfunktionen: `slugify`, `truncate`, `word_count`, `is_palindrome` und `reverse_words`. Sie hat keine Oberfläche, speichert keine Daten und benötigt zur Laufzeit ausschließlich die Standardbibliothek.

## Tech-Stack

- Python 3.10 oder neuer
- Paketierung mit `pyproject.toml` (src-Layout)
- Tests mit `pytest`
- Linting mit `ruff`
- Keine Laufzeit-Abhängigkeiten

## Installation

```bash
pip install .
```

Für die Entwicklung (inklusive `pytest` und `ruff`):

```bash
pip install -e ".[dev]"
```

## Verwendung

Alle Funktionen werden direkt aus dem Paket importiert:

```python
from textutils import slugify, truncate, word_count, is_palindrome, reverse_words
```

### `slugify(text: str) -> str`

Wandelt Text in einen URL-freundlichen Slug um: Kleinbuchstaben, Akzente werden entfernt, alles außer `a-z`, `0-9` wird zu einzelnen Bindestrichen, ohne führende oder abschließende Bindestriche.

```python
slugify("Hello, World!")  # 'hello-world'
slugify("  Crème   brûlée  ")  # 'creme-brulee'
slugify("!!!")  # ''
```

### `truncate(text: str, max_len: int, suffix: str = "...") -> str`

Kürzt Text auf höchstens `max_len` Zeichen; das Ergebnis endet dann auf `suffix`. Kürzere Texte bleiben unverändert. Ein negatives `max_len` löst `ValueError` aus, ein Nicht-`int` (auch `bool`) `TypeError`.

```python
truncate("abcdefghij", 8)  # 'abcde...'
truncate("abc", 8)  # 'abc'
truncate("abcdefghij", 8, suffix="~")  # 'abcdefg~'
truncate("abcdefghij", 2)  # '..'
truncate("abc", -1)  # ValueError
```

### `word_count(text: str) -> int`

Zählt die Wörter; Leerzeichen, Tabulatoren und Zeilenumbrüche gelten als Trenner.

```python
word_count("one two  three")  # 3
word_count("")  # 0
word_count("   ")  # 0
word_count("one\ttwo\nthree")  # 3
```

### `is_palindrome(text: str) -> bool`

Prüft, ob ein Text vorwärts und rückwärts gleich gelesen wird; Groß-/Kleinschreibung und Satzzeichen werden ignoriert.

```python
is_palindrome("A man, a plan, a canal: Panama")  # True
is_palindrome("hello")  # False
is_palindrome("")  # True
```

### `reverse_words(text: str) -> str`

Kehrt die Reihenfolge der Wörter um; mehrfache Leerzeichen werden zu einem einzigen.

```python
reverse_words("one two  three")  # 'three two one'
reverse_words("  solo ")  # 'solo'
reverse_words("")  # ''
```

### Fehlerverhalten

Wird einer Funktion ein Nicht-`str` übergeben (z. B. `None` oder `42`), löst sie `TypeError` aus.

## Tests und Linting

```bash
pytest
ruff check .
```

## Funktionen

- `slugify`, `truncate`, `word_count`, `is_palindrome`, `reverse_words`
- Nur Standardbibliothek, keine Ein-/Ausgabe, keine dynamische Codeausführung
- Verarbeitung beliebig langer Eingaben in linearer Zeit
