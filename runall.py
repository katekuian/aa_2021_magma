import os
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--kernel", help="jupyter kernel name")
parser.add_argument(
    "--only-preperation", help="only run the preperation notebooks", action="store_true"
)
args = parser.parse_args()

kernel_name = args.kernel if args.kernel else "python3"


def run_notebook(filepath):
    subprocess.call(
        [
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            f"--NotebookClient.kernel_name={kernel_name}",
            filepath,
        ]
    )

    # delete the newly created file
    newfile = filepath.replace(".ipynb", ".nbconvert.ipynb")
    os.remove(newfile)


path = os.getcwd()
for root, dirs, files in os.walk(path):
    files.sort(key=lambda x: x[:2])

    if args.only_preperation and not root.endswith(
        "01_data_collection_and_preparation"
    ):
        continue

    for file in files:
        if file.endswith(".ipynb"):
            filepath = os.path.join(root, file)
            print(f"Running {file}")
            run_notebook(filepath)
