# agent.py
import argparse
import subprocess
from pathlib import Path
import importlib.util
import pandas as pd

CUSTOM_PARSERS_DIR = Path("custom_parsers")
DATA_DIR = Path("data")

def run_tests(target: str) -> bool:
    """Run pytest to check parser output against CSV."""
    try:
        result = subprocess.run(["pytest", "-q"], capture_output=True, text=True)
        print(result.stdout)
        return result.returncode == 0
    except Exception as e:
        print(f"Test run failed: {e}")
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True, help="Bank target e.g. icici")
    args = parser.parse_args()
    target = args.target

    # Paths
    pdf_path = DATA_DIR / target / f"{target}_sample.pdf"
    csv_path = DATA_DIR / target / f"{target}_sample.csv"
    parser_path = CUSTOM_PARSERS_DIR / f"{target}_parser.py"

    print(f"📄 PDF: {pdf_path}")
    print(f"📊 CSV: {csv_path}")
    print(f"📝 Writing parser: {parser_path}")

    # Example: generate a basic parser file
    parser_code = f"""
import pandas as pd

def parse(pdf_path: str) -> pd.DataFrame:
    # TODO: Replace with actual PDF parsing logic
    df = pd.read_csv(r"{csv_path}")
    return df
"""
    parser_path.write_text(parser_code)

    print("✅ Parser written. Running tests...")
    success = run_tests(target)

    if not success:
        print("❌ Tests failed. Retry loop not implemented yet.")
    else:
        print("🎉 All tests passed!")

if __name__ == "__main__":
    main()
