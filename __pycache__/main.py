import numpy as np  # Numpy-Bibliothek importieren, normalerweise als "np" abgekürzt
import pandas as pd  # Pandas-Bibliothek importieren, normalerweise als "pd" abgekürzt
# Pandas steht für Python und Datenwissenschaft

# Definition des DataFrames mit verschiedenen Spalten
df = pd.DataFrame(
    {
        "id": [0, 1, 2, 3],  # Spalte für IDs
        "name": ["Nura", "Dana", "Mark", "Diana"],  # Spalte für Namen
        "age": [12, 13, 15, 33]  # Spalte für Alter
    }
)

print(df)  # Ausgabe des gesamten DataFrames

print(df["age"].describe)  # Zeigt statistische Informationen über die "age"-Spalte an
print(df["age"])  # Zeigt die Werte in der "age"-Spalte an

# print(df["name"])  # Das Drucken der "name"-Spalte ist auskommentiert
# Auskommentierte Zeilen werden nicht ausgeführt, aber können als Referenz dienen oder später aktiviert werden
