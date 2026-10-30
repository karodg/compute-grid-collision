"""
Master Replication Script:
The Compute-Grid Collision: AI Load Shocks, Wholesale Capacity Rents, and the Regressive Ratepayer Tax
Author: Danil Popov (Independent Researcher)
"""

import sys
import subprocess
from pathlib import Path

def main():
    print("=" * 80)
    print("STARTING FULL REPLICATION PIPELINE: The Compute-Grid Collision")
    print("=" * 80)
    
    python_exe = sys.executable
    base_dir = Path(__file__).resolve().parent
    src_dir = base_dir / "src"
    
    steps = [
        ("Step 1: Constructing Microdata Panel (EIA, PJM, FERC, BLS)...", src_dir / "build_grid_panel.py"),
        ("Step 2: Estimating Econometric Models & Tables...", src_dir / "estimate_models.py"),
        ("Step 3: Generating Publication Figures (QJE/AER style)...", src_dir / "generate_figures.py"),
    ]
    
    for desc, script in steps:
        print(f"\n--> {desc}")
        res = subprocess.run([python_exe, str(script)], check=True)
        if res.returncode != 0:
            print(f"Failed at {script.name}!")
            sys.exit(1)
            
    print("\n" + "=" * 80)
    print("REPLICATION SUCCESSFULLY COMPLETED!")
    print("All processed datasets, tables, and figures have been generated.")
    print("=" * 80)

if __name__ == "__main__":
    main()
