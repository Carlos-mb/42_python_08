from importlib import import_module


def c_import_mod(module: str, description: str) -> bool:

    ok: bool = True

    try:
        imported = import_module(module)
        version = getattr(imported, "__version__", "unknown")
        print(f"[OK] {module} ({version}) - {description} Ready")
    except ModuleNotFoundError:
        print(f"[MISSING] {module} - Install required")
        ok = False

    return ok


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:\n")

    modules = {"pandas": "Data manipulation",
               "requests": "Network access",
               "matplotlib": "Visualization"}

    ok: bool = True
    for module, description in modules.items():
        ok = c_import_mod(module, description) and ok

    if not ok:
        print("\nInstall with pip:")
        print("pip install -r requirements.txt")
        print("\nOr with Poetry:")
        print("poetry install")
        return

    import pandas
    import numpy    
    from matplotlib import pyplot

    print("Analyzing Matrix data...\n")

    x = numpy.arange(0, 50)
    y = x ** 2
    df = pandas.DataFrame({
        "cycle": x,
        "energy": y
    })

    print(f"Processing {len(df)} data points...")

    # Basic statistics
    mean_energy: float = float(df["energy"].mean())
    max_energy: float = float(df["energy"].max())

    print(f"Average energy: {mean_energy}")
    print(f"Maximum energy: {max_energy}")

    # Visualization
    pyplot.plot(df["cycle"], df["energy"])
    pyplot.title("Matrix Energy Growth")
    pyplot.xlabel("Cycle")
    pyplot.ylabel("Energy Level")

    output_file = "matrix_analysis.png"
    pyplot.savefig(output_file)

    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    main()
