from csv import writer
from pathlib import Path
from urllib.parse import quote


BASE_URL = "https://n-guy-en.github.io/WarmteAtlas-SVG"
IMAGES_DIR = Path("images")
OUTPUT_FILE = Path("powerbi-image-urls.csv")

DISPLAY_NAMES = {
    "De-Fryske-Marren": "De Fryske Marren",
    "Noardeast-Fryslan": "Noardeast-Fryslan",
    "Provinciale-overzicht": "Provinciale overzicht",
}


def image_value(file_name: str) -> str:
    stem = Path(file_name).stem
    parts = stem.rsplit("-", 2)

    if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit():
        return f"{parts[1]}.{parts[2]}"

    return stem


def url_for(folder: str, file_name: str) -> str:
    return f"{BASE_URL}/{quote('images')}/{quote(folder)}/{quote(file_name)}"


def main() -> None:
    rows = [["Naam", "Image", "FileName", "URL"]]

    for folder in sorted(path for path in IMAGES_DIR.iterdir() if path.is_dir()):
        svg_files = sorted(path for path in folder.iterdir() if path.is_file() and path.suffix.lower() == ".svg")

        for svg_file in svg_files:
            rows.append([
                DISPLAY_NAMES.get(folder.name, folder.name),
                image_value(svg_file.name),
                svg_file.name,
                url_for(folder.name, svg_file.name),
            ])

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as csv_file:
        writer(csv_file).writerows(rows)

    print(f"Wrote {len(rows) - 1} rows to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
