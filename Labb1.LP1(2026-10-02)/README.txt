Word Frequency Analyzer (Python)

Ett skript som analyserar text och räknar ut de vanligaste orden i en dokumentfil eller direkt från en URL (t.ex. Project Gutenberg). Projektet fokuserar på grundläggande stränghantering, datastrukturer och fil-I/O i Python.

Funktionalitet:
- Tokenisering som hanterar skiljetecken, siffror och bokstäver separat.
- Filtrering av stoppord (vanliga ord som "and", "the", etc.).
- Stöd för både lokala textfiler och hämtning via HTTP/HTTPS.

Filer i repot:
- wordfreq.py: Logik för tokenisering, räkning och utskrift.
- topmost.py: CLI-program som binder ihop logiken.

Användning:
python3 topmost.py eng_stopwords.txt examples/article1.txt 20