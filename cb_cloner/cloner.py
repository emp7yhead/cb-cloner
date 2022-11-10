import fnmatch
import logging
from pathlib import Path
from os.path import isdir, join
import shutil
import sys


def normalize_path(dir_path):
    p = Path(dir_path)
    if p.is_absolute():
        return p
    return p.joinpath(Path.home(), dir_path)


def include_patterns(*patterns):
    def _ignore_patterns(path, all_names):
        keep = (
            name
            for pattern in patterns
            for name in fnmatch.filter(
                all_names, pattern
                )
            )
        dir_names = (
            name
            for name in all_names
            if isdir(join(path, name))
        )
        return set(all_names) - set(keep) - set(dir_names)
    return _ignore_patterns


def copy_descriptions(dir_path):
    p = normalize_path(dir_path)
    src_path = p.joinpath('modules')
    logging.info(f'Directory is {p}')
    dest_dir = p.joinpath('drafts')
    dest_dir.mkdir(exist_ok=True, parents=True)
    logging.info(f'Successfully created dir {dest_dir}')
    shutil.copy2(
        p.joinpath('description.ru.yml'),
        dest_dir
    )
    try:
        draft_dir = shutil.copytree(
            src_path,
            dest_dir,
            ignore=include_patterns('description.ru.yml'),
            dirs_exist_ok=True
        )
        logging.info(f'Successfully copied to {dir}')
        return draft_dir
    except IOError as e:
        logging.info(f'Can\'t copy {dir}\n{e}')
        sys.exit(1)


def rename_descriptions(result_dir):
    for path in list(result_dir.rglob('description.ru.yml')):
        path.rename(path.with_name('description.en.yml'))


def copy_and_rename(dir_path):
    draft_dir = copy_descriptions(dir_path)
    rename_descriptions(draft_dir)
