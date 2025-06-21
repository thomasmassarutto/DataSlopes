# DataSlopes

## Analisi dati per il corso di Fondamenti di Scienza dei Dati e Laboratorio A.A.2024/2025

Questa repository contiene il progetto d’esame per il corso di Fondamenti di Scienza dei Dati e Laboratorio (A.A. 2024/2025), incentrato sull’analisi di una giornata di snowboard nel comprensorio sciistico di Ravascletto/Zoncolan.

```
├── data
│   ├── 20-02-25
│   │   ├── discese.csv
│   │   ├── RawGPS.csv
│   │   └── salite.csv
│   └── 22-12-24            ## Dati utilizzati per l'analisi
│       ├── discese.csv
│       ├── RawGPS.csv
│       └── salite.csv
├── DataSlopes.ipynb        ## Analisi
├── DataSlopes.slides.html  ## Presentazione
└── README.md
```

Comando per la conversione:

`jupyter nbconvert DataSlopes.ipynb  --to slides --SlidesExporter.reveal_number='c/t' --SlidesExporter.reveal_scroll=True --no-input`

