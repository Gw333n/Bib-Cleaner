import re
import shutil

def regex_bibtex(fields: list) -> re.Pattern:
  patterns = [rf'^\s*{fld}\s*=\s*[{{"].*?[}}"],?\s*' for fld in fields]
  regex = re.compile("|".join(patterns), flags=re.IGNORECASE)
  return regex

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
        regex = regex_bibtex(["url", "issn", "isbn", "doi", "notes", "pages"])
    else:
        raise ValueError(f"Format '{format}' not supported for cleaning.")
    with open(file_path, "r", encoding="utf-8") as f:
        cleaned_lines = []
        for line in f:
            match = regex.search(line)
            if match:
                line = line.replace(match.group(0), "")
            cleaned_lines.append(line)
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(cleaned_lines)

    print(f"'{file_path}' cleaned (removed url, issn, isbn, doi, notes, pages).")
