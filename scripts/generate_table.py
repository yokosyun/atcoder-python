import argparse
import glob


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root_path", type=str, default="ABC")
    return parser.parse_args()


def main():
    args = parse_args()
    file_paths = sorted(glob.glob(args.root_path + "/*/*.py"))

    pre_folder = ""
    line = ""
    for file_path in file_paths:
        folder = file_path.split("/")[-2]

        if pre_folder != folder:
            print(line)
            line = "|" + folder + "|"
            pre_folder = folder

        line += "[&check;](" + file_path + ")|"
    print(line)


if __name__ == "__main__":
    main()