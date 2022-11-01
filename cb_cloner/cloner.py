import logging
from pathlib import Path
import shutil


def ru_to_en(dir_path):
    p = normalize_path(dir_path)
    logging.info(f'Directory is {p}')
    for path in list(p.rglob('description.ru.yml')):
        shutil.copy(path, path.with_name('description.en.yml'))
        logging.info(f'Successfully copied in directory {path.parts[-2]}')


def normalize_path(dir_path):
    p = Path(dir_path)
    if p.is_absolute():
        return p
    return p.joinpath(Path.home(), dir_path)
