# WarmteAtlas SVG Hosting

Deze repository host WarmteAtlas SVG-afbeeldingen voor gebruik in Power BI.

De SVG-bestanden worden via GitHub Pages gepubliceerd vanaf de `main` branch en de root van de repository.

## Publieke Basis-URL

```text
https://n-guy-en.github.io/WarmteAtlas-SVG/
```

Voorbeeld van een afbeeldings-URL:

```text
https://n-guy-en.github.io/WarmteAtlas-SVG/images/Achtkarspelen/Achtkarspelen-2-1.svg
```

## Repositorystructuur

```text
.
├── index.html
├── powerbi-image-urls.csv
├── .nojekyll
└── images/
    ├── Achtkarspelen/
    ├── Ameland/
    ├── Dantumadiel/
    ├── De-Fryske-Marren/
    ├── Harlingen/
    ├── Heerenveen/
    ├── Leeuwarden/
    └── ...
```

`images/` bevat de SVG-bestanden die Power BI via een URL moet laden.

`powerbi-image-urls.csv` bevat de volledige lijst met beschikbare afbeeldings-URL's met deze kolommen:

```text
Municipality,Image,FileName,URL
```

## GitHub Pages Instellen

Configureer GitHub Pages voor deze repository in GitHub:

```text
Settings > Pages > Build and deployment
Source: Deploy from a branch
Branch: main
Folder: / (root)
```

Nadat GitHub Pages klaar is met publiceren, moet de hoofdpagina bereikbaar zijn via:

```text
https://n-guy-en.github.io/WarmteAtlas-SVG/
```

## Gebruik in Power BI

Gebruik de kolom `URL` uit `powerbi-image-urls.csv` als bron voor de afbeeldings-URL in Power BI.

Gebruik alleen GitHub Pages-URL's. Gebruik geen GitHub repository-interface-URL's zoals:

```text
https://github.com/n-guy-en/WarmteAtlas-SVG/blob/main/...
```

Dat zijn HTML-pagina's, geen directe SVG-bestanden.

## Afbeeldingen Bijwerken

Bij het toevoegen of vervangen van SVG-bestanden:

1. Plaats SVG-bestanden onder `images/<Gemeente>/`.
2. Gebruik URL-veilige map- en bestandsnamen.
3. Vermijd spaties, komma's, haakjes, speciale tekens en `%20`.
4. Gebruik deze naamgeving:

```text
Achtkarspelen-2-1.svg
Achtkarspelen-2-2.svg
Achtkarspelen-2-3.svg
```

Optimaliseer, verklein, comprimeer, converteer of wijzig SVG-bestanden visueel niet, tenzij dat later expliciet wordt gevraagd.

## CSV Opnieuw Genereren

Als er SVG-bestanden zijn toegevoegd, verwijderd of hernoemd, genereer dan de CSV opnieuw met:

```bash
python svg-url.py
```

Het script leest alle `.svg`-bestanden onder `images/` en schrijft `powerbi-image-urls.csv` opnieuw met deze kolommen:

```text
Naam,Image,FileName,URL
```

Controleer daarna de wijziging met:

```bash
git diff -- powerbi-image-urls.csv
```

## Validatie

Test na publicatie enkele representatieve SVG-URL's direct in een browser of met `curl`.

Een geldige URL moet:

- HTTP 200 teruggeven
- de SVG direct tonen
- werken zonder GitHub-login
- geen GitHub repository-pagina tonen
- geen HTML-foutpagina teruggeven
