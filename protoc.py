import os

from  grpc.tools import protoc

SRC_PREFIX = "proto/"
DEST_PREFIX = "pychoreo/"

def generate(files):
    for file in files:
        protoc.main((f"--python_out=../../{DEST_PREFIX}/msg",
                    f"--grpc_python_out=../../{DEST_PREFIX}/svc",
                    f"-I../../{SRC_PREFIX}",
                    file))

def find_files(path):
    os.chdir(path)
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".proto"):
                yield os.path.join(root, file)
    os.chdir("../../")

generate(find_files(f"{SRC_PREFIX}/msg"))

generate(find_files(f"{SRC_PREFIX}/svc"))
