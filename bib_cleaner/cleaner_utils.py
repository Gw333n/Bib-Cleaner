import re
import shutil


def clean_bibtex(file_path="bib.bib"):
    """
    Cleans a BibTeX file by removing specific fields (url, issn, isbn, doi) from each entry.

    Args:
        file_path (str):
          Path to the original BibTeX file.
    """
    fields = ["url", "issn", "isbn", "doi"]
    patterns = [rf'^\s*{fld}\s*=\s*[{{"].*?[}}"],?\s*$' for fld in fields]
    regex = re.compile("|".join(patterns), flags=re.IGNORECASE)

    cleaned_lines = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if regex.match(line.strip()):
                continue
            cleaned_lines.append(line)

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(cleaned_lines)

    print(f"'{file_path}' cleaned (removed url, issn, isbn, doi).")


def clean_bibliography(file_path, backup=False):
    """
    Cleans a bibliographic file by removing specific fields (url, issn, isbn, doi) from each entry.

    Args:
        file_path (str):
          Path to the original bibliographic file.
        backup (bool): default = False
          Whether to create a backup of the original file.
    """
    name, format = file_path.rsplit(".", 1)
    if backup:
        shutil.copy(file_path, name + ".bak")
        print(f"Backup created: {name}.bak")
    if format.lower() == "bib":
        clean_bibtex(file_path)
    else:
        print(f"Format '{format}' not supported for cleaning.")

