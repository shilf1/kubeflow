import pandas as pd
import argparse
import sys

if __name__ == "__main__":
    print("[sheum] start python code 1.0\n")
    print(sys.version)
    
    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument(
        '--data_path', type=str,
        help="Input data path"
    )

    args = argument_parser.parse_args()
    data = pd.read_csv(args.data_path)
    print("[sheum] print data.shape\n")
    print("[sheum] data.shape: {}\n".format(data.shape))
    print("[sheum] data.head: {}\n".format(data.head))

    print("\n[sheum] data.to_csv m_iris.csv\n")

    data.to_csv('/m_iris.csv', index=False)

