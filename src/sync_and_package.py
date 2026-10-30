"""
sync_and_package.py
Synchronizes and packages the complete replication repository, journal submission bundle,
and Overleaf compilation ZIP archives for:
"The Compute-Grid Collision: AI Load Shocks, Wholesale Capacity Rents, and the Regressive Ratepayer Tax"
Author: Danil Popov (Independent Researcher)
"""

import os
import shutil
import zipfile
from pathlib import Path

WORKSPACE = Path(r"d:\Workspace\compute_grid_collision")
DEST = Path(r"d:\Compute_Grid_Collision")
SRC_DIR = WORKSPACE / "src"
DATA_DIR = WORKSPACE / "data"
FIG_DIR = WORKSPACE / "figures"
TABLES_DIR = WORKSPACE / "tables"
PAPER_DIR = WORKSPACE / "paper"
SUBMISSION_DIR = WORKSPACE / "submission_files"
GH_REPO = WORKSPACE / "github_repo"

def safe_copy(src, dst):
    try:
        shutil.copy2(src, dst)
        return True
    except Exception as e:
        print(f"Warning copying {src} to {dst}: {e}")
        return False

def package_all():
    print("=" * 70)
    print("PACKAGING REPLICATION REPO, OVERLEAF ZIP ARCHIVES, AND SUBMISSION FILES")
    print("=" * 70)
    
    SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)
    DEST.mkdir(parents=True, exist_ok=True)
    (DEST / "overleaf_packages").mkdir(parents=True, exist_ok=True)
    (DEST / "submission_files").mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # 1. BUILD OVERLEAF ZIP ARCHIVES (ZERO-CONFIG ONE-CLICK COMPILATION)
    # ------------------------------------------------------------------
    # Unblinded Overleaf ZIP (compiles as main.tex)
    unblinded_zip = WORKSPACE / "compute_grid_collision_unblinded_overleaf.zip"
    with zipfile.ZipFile(unblinded_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(PAPER_DIR / "main.tex", arcname="main.tex")
        zf.write(PAPER_DIR / "references.bib", arcname="references.bib")
        for tab in sorted(TABLES_DIR.glob("table*.tex")):
            zf.write(tab, arcname=f"tables/{tab.name}")
        for fig in sorted(FIG_DIR.glob("fig*.*")):
            zf.write(fig, arcname=f"figures/{fig.name}")
        for comp in ["Title_Page_Compute_Grid_Popov.tex", "Cover_Letter_Popov.tex", "Highlights_Popov.tex", "Author_Biography_Popov.tex"]:
            c_path = PAPER_DIR / comp
            if c_path.exists():
                zf.write(c_path, arcname=f"submission_documents/{comp}")
    print(f"Created Unblinded Overleaf ZIP: {unblinded_zip} ({unblinded_zip.stat().st_size:,} bytes)")

    # Blinded Overleaf ZIP (compiles as main.tex)
    blinded_zip = WORKSPACE / "compute_grid_collision_blinded_overleaf.zip"
    with zipfile.ZipFile(blinded_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(PAPER_DIR / "main_blinded.tex", arcname="main.tex")
        zf.write(PAPER_DIR / "references.bib", arcname="references.bib")
        for tab in sorted(TABLES_DIR.glob("table*.tex")):
            zf.write(tab, arcname=f"tables/{tab.name}")
        for fig in sorted(FIG_DIR.glob("fig*.*")):
            zf.write(fig, arcname=f"figures/{fig.name}")
    print(f"Created Blinded Overleaf ZIP: {blinded_zip} ({blinded_zip.stat().st_size:,} bytes)")

    # Copy Overleaf zips to submission_files and DEST
    safe_copy(unblinded_zip, SUBMISSION_DIR / "compute_grid_collision_unblinded_overleaf.zip")
    safe_copy(blinded_zip, SUBMISSION_DIR / "compute_grid_collision_blinded_overleaf.zip")
    safe_copy(unblinded_zip, DEST / "overleaf_packages" / "compute_grid_collision_unblinded_overleaf.zip")
    safe_copy(blinded_zip, DEST / "overleaf_packages" / "compute_grid_collision_blinded_overleaf.zip")
    safe_copy(unblinded_zip, DEST / "compute_grid_collision_unblinded_overleaf.zip")
    safe_copy(blinded_zip, DEST / "compute_grid_collision_blinded_overleaf.zip")

    # ------------------------------------------------------------------
    # 2. ASSEMBLE CLEAN SUBMISSION FILES
    # ------------------------------------------------------------------
    files_to_copy = [
        ("manuscript.pdf", "Manuscript_Popov_Compute_Grid.pdf"),
        ("manuscript_blinded.pdf", "Manuscript_Blinded_Compute_Grid.pdf"),
        ("abstract.pdf", "Abstract_Popov.pdf"),
        ("title_page.pdf", "Title_Page_Popov.pdf"),
        ("cover_letter.pdf", "Cover_Letter_Popov.pdf"),
        ("highlights.pdf", "Highlights_Popov.pdf"),
        ("author_biography.pdf", "Author_Biography_Popov.pdf"),
        ("Title_Page_Popov.docx", "Title_Page_Popov.docx"),
        ("Abstract_Popov.docx", "Abstract_Popov.docx"),
        ("Title_Page_Compute_Grid_Popov.tex", "Title_Page_Popov.tex"),
        ("main.tex", "main.tex"),
        ("main_blinded.tex", "main_blinded.tex"),
        ("references.bib", "references.bib"),
    ]
    for src_name, dst_name in files_to_copy:
        src = PAPER_DIR / src_name
        if src.exists():
            safe_copy(src, SUBMISSION_DIR / dst_name)
            safe_copy(src, DEST / "submission_files" / dst_name)

    # Copy figures and tables to submission_files
    sub_fig_dir = SUBMISSION_DIR / "figures"
    sub_fig_dir.mkdir(parents=True, exist_ok=True)
    for fig in FIG_DIR.glob("*.pdf"):
        safe_copy(fig, sub_fig_dir / fig.name)
    for fig in FIG_DIR.glob("*.png"):
        safe_copy(fig, sub_fig_dir / fig.name)

    sub_tab_dir = SUBMISSION_DIR / "tables"
    sub_tab_dir.mkdir(parents=True, exist_ok=True)
    for tab in TABLES_DIR.glob("*.*"):
        safe_copy(tab, sub_tab_dir / tab.name)

    # ------------------------------------------------------------------
    # 3. ASSEMBLE CLEAN GITHUB REPOSITORY & GITHUB ZIP
    # ------------------------------------------------------------------
    if GH_REPO.exists():
        shutil.rmtree(GH_REPO)

    (GH_REPO / "data" / "processed").mkdir(parents=True, exist_ok=True)
    (GH_REPO / "src").mkdir(parents=True, exist_ok=True)
    (GH_REPO / "figures").mkdir(parents=True, exist_ok=True)
    (GH_REPO / "tables").mkdir(parents=True, exist_ok=True)
    (GH_REPO / "paper").mkdir(parents=True, exist_ok=True)

    # Processed Data
    for f in (DATA_DIR / "processed").glob("*.csv"):
        safe_copy(f, GH_REPO / "data" / "processed" / f.name)

    # Python scripts
    for s in ["build_grid_panel.py", "estimate_models.py", "generate_figures.py", "build_perfect_manuscript.py", "build_html_manuscript.py", "sync_and_package.py"]:
        src_f = SRC_DIR / s
        if src_f.exists():
            safe_copy(src_f, GH_REPO / "src" / s)

    # Figures
    for fig in FIG_DIR.glob("fig*.*"):
        safe_copy(fig, GH_REPO / "figures" / fig.name)

    # Tables
    for tab in TABLES_DIR.glob("*.*"):
        safe_copy(tab, GH_REPO / "tables" / tab.name)

    # Paper LaTeX files (clean, no HTML or PDF binaries)
    for p in ["main.tex", "main_blinded.tex", "references.bib", "Title_Page_Compute_Grid_Popov.tex", "Cover_Letter_Popov.tex", "Highlights_Popov.tex", "Author_Biography_Popov.tex"]:
        p_f = PAPER_DIR / p
        if p_f.exists():
            safe_copy(p_f, GH_REPO / "paper" / p)

    # Master run_all.py in github_repo root
    run_all_code = '''"""
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
        print(f"\\n--> {desc}")
        res = subprocess.run([python_exe, str(script)], check=True)
        if res.returncode != 0:
            print(f"Failed at {script.name}!")
            sys.exit(1)
            
    print("\\n" + "=" * 80)
    print("REPLICATION SUCCESSFULLY COMPLETED!")
    print("All processed datasets, tables, and figures have been generated.")
    print("=" * 80)

if __name__ == "__main__":
    main()
'''
    with open(GH_REPO / "run_all.py", "w", encoding="utf-8") as f:
        f.write(run_all_code)

    # Copy gold-standard README.md, LICENSE, and requirements.txt
    safe_copy(WORKSPACE / "README.md", GH_REPO / "README.md")
    safe_copy(WORKSPACE / "LICENSE", GH_REPO / "LICENSE")
    safe_copy(WORKSPACE / "requirements.txt", GH_REPO / "requirements.txt")

    safe_copy(WORKSPACE / "README.md", DEST / "README.md")
    safe_copy(WORKSPACE / "LICENSE", DEST / "LICENSE")
    safe_copy(WORKSPACE / "requirements.txt", DEST / "requirements.txt")

    # 4. Pack GitHub repo zip
    github_zip = WORKSPACE / "compute_grid_collision_github.zip"
    with zipfile.ZipFile(github_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(GH_REPO):
            for file in files:
                full_path = Path(root) / file
                rel_path = full_path.relative_to(GH_REPO)
                zf.write(full_path, arcname=str(rel_path))
    print(f"Created GitHub Archive ZIP: {github_zip} ({github_zip.stat().st_size:,} bytes)")
    safe_copy(github_zip, DEST / "compute_grid_collision_github.zip")

    print("\nALL OVERLEAF AND SUBMISSION PACKAGES SUCCESSFULLY GENERATED!")

if __name__ == "__main__":
    package_all()
