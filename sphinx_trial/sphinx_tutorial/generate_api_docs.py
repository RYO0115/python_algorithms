import os
from pathlib import Path

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent # sphinx_trial
CPP_PROJECT_ROOT = PROJECT_ROOT / "cpp_trial_project"
INCLUDE_DIR = CPP_PROJECT_ROOT / "include"
SRC_DIR = CPP_PROJECT_ROOT / "src"
DOCS_DIR = Path(__file__).parent / "docs"
API_OUTPUT_DIR = DOCS_DIR / "api"

def main():
    # Ensure output directory exists
    if not API_OUTPUT_DIR.exists():
        API_OUTPUT_DIR.mkdir(parents=True)

    generated_files = []

    # Walk through the include directory
    for header_path in INCLUDE_DIR.rglob("*.h"):
        relative_path = header_path.relative_to(INCLUDE_DIR)
        class_name = header_path.stem
        
        # Determine paths for literalinclude (relative to docs/api/)
        # docs/api/ -> docs/ -> sphinx_tutorial/ -> sphinx_trial/ -> cpp_trial_project/
        # So we need ../../../cpp_trial_project/
        
        # Construct the path to the header file relative to the build root (for display/linking)
        # But literalinclude takes a path relative to the rst file.
        
        rel_header_path = Path("../../../cpp_trial_project/include") / relative_path
        
        # Try to find the corresponding source file
        # Assuming src structure mirrors include structure
        src_file_name = class_name + ".cpp"
        src_path = SRC_DIR / relative_path.parent / src_file_name
        
        rel_src_path = None
        if src_path.exists():
            rel_src_path = Path("../../../cpp_trial_project/src") / relative_path.parent / src_file_name
        else:
            # Fallback: search in src directory if not found in mirrored path
            try:
                found_src = next(SRC_DIR.rglob(src_file_name))
                rel_src_path = Path("../../../cpp_trial_project/src") / found_src.relative_to(SRC_DIR)
            except StopIteration:
                print(f"Warning: Source file for {class_name} not found.")

        # Generate RST content
        rst_content = f"""{class_name}
{'=' * len(class_name)}

.. doxygenclass:: {class_name}
   :project: RPG Battle Simulator
   :members:
   :private-members:
   :undoc-members:

**Source Code**

Header (``include/{relative_path}``):

.. literalinclude:: {rel_header_path}
   :language: cpp
   :linenos:
"""

        if rel_src_path:
            # Determine relative path for display
            src_display_path = rel_src_path.as_posix().replace("../../../cpp_trial_project/", "")
            rst_content += f"""
Implementation (``{src_display_path}``):

.. literalinclude:: {rel_src_path}
   :language: cpp
   :linenos:
"""

        # Write RST file
        rst_file_path = API_OUTPUT_DIR / f"{class_name}.rst"
        with open(rst_file_path, "w") as f:
            f.write(rst_content)
        
        generated_files.append(class_name)
        print(f"Generated {rst_file_path}")

    # Update api_reference.rst
    update_api_reference_index(generated_files)

def update_api_reference_index(classes):
    index_file = DOCS_DIR / "api_reference.rst"
    
    content = """API Reference
=============

This section provides the API documentation for the RPG Battle Simulator.

.. toctree::
   :maxdepth: 1
   :caption: Classes
   :glob:

   api/*
"""

    with open(index_file, "w") as f:
        f.write(content)
    print(f"Updated {index_file}")

if __name__ == "__main__":
    main()
