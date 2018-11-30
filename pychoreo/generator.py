import os

from  grpc.tools import protoc

SRC_PREFIX = "proto"
DEST_PREFIX = "pychoreo"


def generate(file):
    pwd = os.path.dirname(os.path.realpath(__file__))
    cwd = os.getcwd()
    args = ("",
            f"-I{cwd}",
            f"-I/usr/local/include",
            f"-I/usr/include",
            f"--python_out={pwd}/svc",
            f"--grpc_python_out={pwd}/svc",
            f"{file}")
    protoc.main(args)


def compile_files(srcpath):
    """Compile protobuf files into project"""
    cwd = os.getcwd()
    os.chdir(srcpath)
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".proto"):
                # Make sure we're an absolute path
                path = root
                if not os.path.isabs(path):
                    path = os.path.join(os.getcwd(), path)
                generate(os.path.join(path, file))
    os.chdir(cwd)


if __name__ == "__main__":
    compile_files(f"{SRC_PREFIX}/msg")
