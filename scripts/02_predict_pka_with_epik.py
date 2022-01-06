import os, subprocess
import argparse


def main():
    """
    takes molecules from Schrödinger maestro (mae) file and
    returns new mae file containing Epik pka prediction data
    for each molecule.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="input filename, type: .mae.gz or .mae")
    parser.add_argument("--output", help="output filename, type: .mae.gz or .mae")
    args = parser.parse_args()

    print("inputfile:", args.input)
    print("outputfile:", args.output)

    mae_file_name = args.input
    mae_file_name_with_pka = args.output

    schroedinger_dir = "/data/shared/software/schrodinger2021-1/"
    epik = f"{schroedinger_dir}/epik"

    if not os.path.isfile(mae_file_name):
        raise RuntimeError(f"{mae_file_name} file not found")

    # predict pka of mols in .mae files with epik
    o = subprocess.run(
        [
            f"{epik}",
            "-scan",
            "-imae",
            mae_file_name,
            "-omae",
            mae_file_name_with_pka,
            "-ph",
            "7.4",
            "-p",
            "0.1",
            "-highest_pka",
            "14.0",
            "-lowest_pka",
            "0.0",
            "-SUBHOST",
            "localhost:14",
            "-NJOBS",
            "14",
        ]
    )
    o.check_returncode()


if __name__ == "__main__":
    main()
