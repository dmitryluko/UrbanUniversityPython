import os
import stat
import pwd
import grp
import time

from typing import List


def list_directory_entries(path: str) -> List[str]:
    """
    Lists the entries in the given directory path.

    Args:
        path (str): The directory path to list entries from.

    Returns:
        List[str]: A list of directory entries, sorted, with the current
                   and parent directory entries added at the beginning.

    Handles:
        PermissionError: Prints a message when there are permission issues.
        FileNotFoundError: Prints a message when the directory is not found.
    """
    try:
        entries = os.listdir(path)
        entries = sorted(entries)  # Sort entries
        entries.insert(0, '.')  # Add current directory
        entries.insert(1, '..')  # Add parent directory
        return entries
    except PermissionError as e:
        print(f'Permission denied: {e}')
    except FileNotFoundError as e:
        print(f'File not found: {e}')

    return []


def get_file_info(path: str, entry: str) -> str:
    """
    Retrieves detailed information about a file or directory specified by the path and entry name.

    Args:
        path (str): The directory path where the file or directory is located.
        entry (str): The name of the file or directory for which information is to be retrieved.

    Returns:
        str: A formatted string containing the file or directory's permissions, number of links, owner name, group name, size, last modification time, and name.
    """
    full_path = os.path.join(path, entry)
    stats = os.lstat(full_path)
    permission = stat.filemode(stats.st_mode)
    n_links = stats.st_nlink
    owner = pwd.getpwuid(stats.st_uid).pw_name
    group = grp.getgrgid(stats.st_gid).gr_name
    size = stats.st_size
    mtime = time.strftime('%b %d %H:%M', time.localtime(stats.st_mtime))

    return f'{permission} {n_links:3} {owner:<8} {group:<8} {size:8} {mtime} {entry}'


def custom_ls(path: str = '.') -> None:
    """
    Lists the contents of a directory with detailed information.

    Args:
        path (str): The directory path to list. Defaults to the current directory ('.').

    Returns:
        None
    """
    entries = list_directory_entries(path)

    for entry in entries:
        print(get_file_info(path, entry))


def main():
    custom_ls()


if __name__ == '__main__':
    main()
