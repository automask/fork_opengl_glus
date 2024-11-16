import os, sys, shutil, glob, subprocess

config = "Debug"
src_root = os.path.dirname(__file__)
bin_root = os.path.abspath(f"{src_root}/build/{config}")


def copy_shaders():
    dirs = glob.glob(f"{src_root}/Example*/**/*.glsl", recursive=True)
    for file in dirs:
        rel = os.path.relpath(file, src_root)
        dst = os.path.join(src_root, "build", rel)
        dst_dir = os.path.dirname(dst)

        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        if not os.path.exists(dst):
            shutil.copyfile(file, dst)
            print(f"copy shader {rel} => {dst}")
        else:
            print(f"has exist {dst}")


def copy_assets():
    dirs = glob.glob(f"{src_root}/Binaries/**/*", recursive=True)
    for file in dirs:
        if os.path.isfile(file):
            rel = os.path.relpath(file, os.path.join(src_root, "Binaries"))
            dst = os.path.join(src_root, "build", config, rel)
            dst_dir = os.path.dirname(dst)

            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)

            if not os.path.exists(dst):
                shutil.copyfile(file, dst)
                print(f"copy asset {rel} => {dst}")
            else:
                print(f"has exist {dst}")


def cmake_config():
    cmd = 'cmake -S . -B build -G "Visual Studio 17 2022" -T host=x86 -A win32'
    subprocess.run(cmd, shell=True, cwd=src_root)


copy_assets()
copy_shaders()
cmake_config()


__doc__ = r"""
- glew|win32 only
    - External/x86/Windows/MSVC/lib/glew32s.lib
- cmake -S . -B build -G "Visual Studio 17 2022" -T host=x86 -A win32
"""
