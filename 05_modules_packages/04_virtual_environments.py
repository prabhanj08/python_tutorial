"""
05. Modules and Packages - Virtual Environments
==============================================

Virtual environments are isolated Python environments that allow you to manage
dependencies for different projects separately. This prevents version conflicts
and keeps your global Python installation clean.

Topics covered:
- Why use virtual environments?
- Creating virtual environments with venv
- Activating and deactivating environments
- Managing project dependencies
- Best practices for environment management
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

print("=" * 60)
print("PYTHON VIRTUAL ENVIRONMENTS - ISOLATED DEVELOPMENT")
print("=" * 60)

# =============================================================================
# 1. WHY USE VIRTUAL ENVIRONMENTS?
# =============================================================================

print("\n1. WHY USE VIRTUAL ENVIRONMENTS?")
print("-" * 30)

print("Problems without virtual environments:")
print("- Global package conflicts")
print("- Version incompatibilities between projects")
print("- Difficulty reproducing environments")
print("- Polluted global Python installation")
print("- Hard to manage project-specific dependencies")

print(f"\nBenefits of virtual environments:")
print("- Isolated dependencies per project")
print("- No version conflicts")
print("- Easy environment reproduction")
print("- Clean project setup")
print("- Safe experimentation")
print("- Easy cleanup (just delete the folder)")

# =============================================================================
# 2. CURRENT PYTHON ENVIRONMENT INFO
# =============================================================================

print("\n2. CURRENT PYTHON ENVIRONMENT INFO")
print("-" * 30)

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Platform: {platform.platform()}")
print(f"Architecture: {platform.architecture()}")

# Check if we're in a virtual environment
def in_virtual_env():
    return hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )

if in_virtual_env():
    print("✓ Currently running in a virtual environment")
    print(f"Virtual env path: {sys.prefix}")
else:
    print("✗ Running in global Python environment")

print(f"Python path (first 3 locations):")
for i, path in enumerate(sys.path[:3], 1):
    print(f"  {i}. {path}")

# =============================================================================
# 3. CREATING VIRTUAL ENVIRONMENTS WITH VENV
# =============================================================================

print("\n3. CREATING VIRTUAL ENVIRONMENTS WITH VENV")
print("-" * 30)

print("The venv module is included with Python 3.3+")
print("Basic commands:")
print("python -m venv myenv          # Create virtual environment")
print("python -m venv myenv --prompt myproject  # With custom prompt")
print("python -m venv myenv --system-site-packages  # Access global packages")

def run_command(command, capture_output=True):
    """Run a command and return the result"""
    try:
        if capture_output:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout.strip(), result.stderr.strip(), result.returncode
        else:
            result = subprocess.run(command, shell=True)
            return "", "", result.returncode
    except Exception as e:
        return "", str(e), 1

# Demonstrate creating a virtual environment
demo_env_name = "demo_env"
print(f"\nCreating demonstration virtual environment: {demo_env_name}")

# Remove existing demo environment if it exists
if os.path.exists(demo_env_name):
    import shutil
    shutil.rmtree(demo_env_name)

# Create virtual environment
stdout, stderr, returncode = run_command(f"python -m venv {demo_env_name}")
if returncode == 0:
    print(f"✓ Successfully created {demo_env_name}")
    
    # Show directory structure
    print(f"\nVirtual environment structure:")
    for root, dirs, files in os.walk(demo_env_name):
        level = root.replace(demo_env_name, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 2 * (level + 1)
        for file in files[:3]:  # Show first 3 files only
            print(f"{subindent}{file}")
        if len(files) > 3:
            print(f"{subindent}... and {len(files) - 3} more files")
        if level > 2:  # Limit depth
            break
else:
    print(f"✗ Failed to create virtual environment: {stderr}")

# =============================================================================
# 4. ACTIVATING AND DEACTIVATING ENVIRONMENTS
# =============================================================================

print("\n4. ACTIVATING AND DEACTIVATING ENVIRONMENTS")
print("-" * 30)

print("Activation commands by platform:")
print("Windows:")
print("  myenv\\Scripts\\activate.bat      # Command Prompt")
print("  myenv\\Scripts\\Activate.ps1      # PowerShell")
print("")
print("macOS/Linux:")
print("  source myenv/bin/activate         # bash/zsh")
print("  . myenv/bin/activate              # sh")
print("")
print("Deactivation (all platforms):")
print("  deactivate")

# Show activation script content (first few lines)
if os.path.exists(demo_env_name):
    if platform.system() == "Windows":
        activate_script = f"{demo_env_name}\\Scripts\\activate.bat"
    else:
        activate_script = f"{demo_env_name}/bin/activate"
    
    if os.path.exists(activate_script):
        print(f"\nActivation script preview ({activate_script}):")
        try:
            with open(activate_script, 'r') as f:
                lines = f.readlines()[:10]  # First 10 lines
                for i, line in enumerate(lines, 1):
                    print(f"  {i:2d}: {line.rstrip()}")
                if len(lines) == 10:
                    print("     ... (more lines)")
        except Exception as e:
            print(f"Could not read activation script: {e}")

# =============================================================================
# 5. MANAGING PACKAGES IN VIRTUAL ENVIRONMENTS
# =============================================================================

print("\n5. MANAGING PACKAGES IN VIRTUAL ENVIRONMENTS")
print("-" * 30)

print("Package management workflow:")
print("1. Create virtual environment")
print("2. Activate environment")
print("3. Install packages with pip")
print("4. Work on your project")
print("5. Generate requirements.txt")
print("6. Deactivate when done")

# Demonstrate package installation in virtual environment
if os.path.exists(demo_env_name):
    if platform.system() == "Windows":
        pip_path = f"{demo_env_name}\\Scripts\\pip"
        python_path = f"{demo_env_name}\\Scripts\\python"
    else:
        pip_path = f"{demo_env_name}/bin/pip"
        python_path = f"{demo_env_name}/bin/python"
    
    print(f"\nDemonstrating package installation in virtual environment:")
    
    # Install a simple package
    stdout, stderr, returncode = run_command(f"{pip_path} install requests")
    if returncode == 0:
        print("✓ Successfully installed requests in virtual environment")
        
        # List packages in virtual environment
        stdout, stderr, returncode = run_command(f"{pip_path} list")
        if returncode == 0:
            print(f"\nPackages in virtual environment:")
            lines = stdout.split('\n')
            for line in lines[:10]:  # Show first 10 lines
                print(f"  {line}")
    else:
        print(f"✗ Failed to install package: {stderr}")

# =============================================================================
# 6. REQUIREMENTS.TXT AND ENVIRONMENT REPRODUCTION
# =============================================================================

print("\n6. REQUIREMENTS.TXT AND ENVIRONMENT REPRODUCTION")
print("-" * 30)

print("Creating reproducible environments:")
print("pip freeze > requirements.txt     # Export current packages")
print("pip install -r requirements.txt   # Install from requirements")

# Create a sample requirements.txt
sample_requirements = """# Core dependencies
requests==2.31.0
click==8.1.7
python-dateutil==2.8.2

# Data processing
pandas==2.0.3
numpy==1.24.3

# Web framework
flask==2.3.3
jinja2==3.1.2

# Development tools
pytest==7.4.0
black==23.7.0
flake8==6.0.0

# Optional dependencies
matplotlib==3.7.2  # For plotting
beautifulsoup4==4.12.2  # For web scraping
"""

with open("sample_requirements.txt", "w") as f:
    f.write(sample_requirements)

print("Created sample_requirements.txt")

# Generate requirements from demo environment
if os.path.exists(demo_env_name):
    stdout, stderr, returncode = run_command(f"{pip_path} freeze")
    if returncode == 0 and stdout:
        print(f"\nCurrent virtual environment packages:")
        print(stdout)
        
        # Save to file
        with open("demo_requirements.txt", "w") as f:
            f.write(stdout)
        print("Saved to demo_requirements.txt")

# =============================================================================
# 7. VIRTUAL ENVIRONMENT BEST PRACTICES
# =============================================================================

print("\n7. VIRTUAL ENVIRONMENT BEST PRACTICES")
print("-" * 30)

print("Best practices:")
print("1. One virtual environment per project")
print("2. Use descriptive names for environments")
print("3. Keep environments outside project directory")
print("4. Use requirements.txt for dependency management")
print("5. Regularly update packages")
print("6. Document Python version requirements")
print("7. Use .gitignore to exclude virtual environments")
print("8. Consider using environment management tools")

# Create a sample .gitignore
gitignore_content = """# Virtual environments
venv/
env/
ENV/
env.bak/
venv.bak/
.venv/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
"""

with open("sample_gitignore.txt", "w") as f:
    f.write(gitignore_content)

print("Created sample .gitignore file")

# =============================================================================
# 8. ALTERNATIVE VIRTUAL ENVIRONMENT TOOLS
# =============================================================================

print("\n8. ALTERNATIVE VIRTUAL ENVIRONMENT TOOLS")
print("-" * 30)

print("Other virtual environment tools:")
print("1. virtualenv - Original virtual environment tool")
print("2. pipenv - Combines pip and virtualenv")
print("3. conda - Cross-platform package and environment manager")
print("4. poetry - Modern dependency management")
print("5. pyenv - Python version management")

# Check for alternative tools
tools_to_check = [
    ("virtualenv", "virtualenv --version"),
    ("pipenv", "pipenv --version"),
    ("conda", "conda --version"),
    ("poetry", "poetry --version"),
    ("pyenv", "pyenv --version")
]

print(f"\nChecking for alternative tools:")
for tool_name, command in tools_to_check:
    stdout, stderr, returncode = run_command(command)
    if returncode == 0:
        print(f"✓ {tool_name}: {stdout}")
    else:
        print(f"✗ {tool_name}: Not installed")

# =============================================================================
# 9. PIPENV EXAMPLE
# =============================================================================

print("\n9. PIPENV EXAMPLE")
print("-" * 30)

print("Pipenv combines pip and virtualenv:")
print("pipenv install requests        # Install package and create Pipfile")
print("pipenv install pytest --dev   # Install development dependency")
print("pipenv shell                  # Activate virtual environment")
print("pipenv run python script.py   # Run command in environment")
print("pipenv lock                   # Generate Pipfile.lock")

# Create sample Pipfile
pipfile_content = """[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
requests = "*"
flask = ">=2.0"
pandas = "~=1.5.0"

[dev-packages]
pytest = "*"
black = "*"
flake8 = "*"
mypy = "*"

[requires]
python_version = "3.9"

[scripts]
test = "pytest"
format = "black ."
lint = "flake8 ."
"""

with open("sample_Pipfile", "w") as f:
    f.write(pipfile_content)

print("Created sample Pipfile")

# =============================================================================
# 10. PROJECT SETUP AUTOMATION
# =============================================================================

print("\n10. PROJECT SETUP AUTOMATION")
print("-" * 30)

# Create a project setup script
setup_script = '''#!/usr/bin/env python3
"""
Project setup automation script
"""

import os
import subprocess
import sys
from pathlib import Path

def create_project_structure(project_name):
    """Create a standard Python project structure"""
    
    # Create directories
    directories = [
        f"{project_name}",
        f"{project_name}/{project_name}",
        f"{project_name}/tests",
        f"{project_name}/docs",
        f"{project_name}/scripts"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {directory}")
    
    # Create files
    files = {
        f"{project_name}/README.md": f"# {project_name}\\n\\nProject description here.",
        f"{project_name}/requirements.txt": "# Add your dependencies here\\n",
        f"{project_name}/requirements-dev.txt": "pytest>=6.0\\nblack>=21.0\\nflake8>=3.9\\n",
        f"{project_name}/.gitignore": "venv/\\n__pycache__/\\n*.pyc\\n.env\\n",
        f"{project_name}/{project_name}/__init__.py": f'"""\\n{project_name} package\\n"""\\n\\n__version__ = "0.1.0"\\n',
        f"{project_name}/tests/__init__.py": "",
        f"{project_name}/setup.py": f"""from setuptools import setup, find_packages

setup(
    name="{project_name}",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
)"""
    }
    
    for file_path, content in files.items():
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Created file: {file_path}")

def setup_virtual_environment(project_name):
    """Set up virtual environment for the project"""
    venv_path = f"{project_name}/venv"
    
    # Create virtual environment
    result = subprocess.run([sys.executable, "-m", "venv", venv_path])
    if result.returncode == 0:
        print(f"Created virtual environment: {venv_path}")
        return True
    else:
        print(f"Failed to create virtual environment")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python setup_project.py <project_name>")
        sys.exit(1)
    
    project_name = sys.argv[1]
    print(f"Setting up project: {project_name}")
    
    create_project_structure(project_name)
    setup_virtual_environment(project_name)
    
    print(f"\\nProject {project_name} setup complete!")
    print(f"Next steps:")
    print(f"1. cd {project_name}")
    print(f"2. source venv/bin/activate  # On Windows: venv\\\\Scripts\\\\activate")
    print(f"3. pip install -r requirements-dev.txt")
    print(f"4. Start coding!")
'''

with open("setup_project.py", "w") as f:
    f.write(setup_script)

print("Created setup_project.py automation script")
print("Usage: python setup_project.py my_new_project")

# =============================================================================
# EXERCISES
# =============================================================================

print("\n" + "=" * 60)
print("EXERCISES")
print("=" * 60)

print("""
Exercise 1: Basic Virtual Environment
- Create a virtual environment named 'test_env'
- Activate it and install 'requests' and 'beautifulsoup4'
- Generate a requirements.txt file
- Deactivate and delete the environment

Exercise 2: Project Environment Setup
- Create a new project directory
- Set up a virtual environment for the project
- Install development dependencies (pytest, black, flake8)
- Create a simple Python module and test file
- Run tests in the virtual environment

Exercise 3: Environment Reproduction
- Create a virtual environment with specific package versions
- Generate requirements.txt with exact versions
- Create a new environment and install from requirements.txt
- Verify both environments have identical packages

Exercise 4: Multiple Environment Management
- Create 3 different virtual environments for different projects
- Install different package versions in each
- Practice switching between environments
- Compare package lists between environments

Exercise 5: Automation Script
- Write a script that automates project setup
- Include virtual environment creation
- Add standard project structure creation
- Test the script with a new project
""")

# =============================================================================
# SOLUTIONS (Uncomment to see solutions)
# =============================================================================

print("\n" + "=" * 60)
print("EXERCISE SOLUTIONS")
print("=" * 60)

# Solution 1: Basic Virtual Environment
print("\nSolution 1: Basic Virtual Environment Commands")
print("# Create environment")
print("python -m venv test_env")
print("")
print("# Activate (Linux/Mac)")
print("source test_env/bin/activate")
print("# Activate (Windows)")
print("test_env\\Scripts\\activate")
print("")
print("# Install packages")
print("pip install requests beautifulsoup4")
print("")
print("# Generate requirements")
print("pip freeze > requirements.txt")
print("")
print("# Deactivate")
print("deactivate")
print("")
print("# Remove environment")
print("rm -rf test_env  # Linux/Mac")
print("rmdir /s test_env  # Windows")

# Solution 2: Project Environment Setup
print("\nSolution 2: Project Environment Setup")

project_name = "sample_project"
if not os.path.exists(project_name):
    os.makedirs(project_name)
    
    # Create project files
    project_files = {
        f"{project_name}/main.py": '''"""
Sample project main module
"""

def greet(name):
    """Greet a person"""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    print(greet("World"))
    print(f"2 + 3 = {add_numbers(2, 3)}")
''',
        f"{project_name}/test_main.py": '''"""
Tests for main module
"""

import pytest
from main import greet, add_numbers

def test_greet():
    assert greet("Alice") == "Hello, Alice!"

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

def test_add_numbers_floats():
    assert add_numbers(1.5, 2.5) == 4.0
''',
        f"{project_name}/requirements-dev.txt": '''pytest>=6.0.0
black>=21.0.0
flake8>=3.9.0
''',
        f"{project_name}/README.md": f'''# {project_name}

A sample Python project demonstrating virtual environment usage.

## Setup

1. Create virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate virtual environment:
   ```bash
   source venv/bin/activate  # Linux/Mac
   venv\\Scripts\\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

4. Run tests:
   ```bash
   pytest
   ```

5. Run the main script:
   ```bash
   python main.py
   ```
'''
    }
    
    for file_path, content in project_files.items():
        with open(file_path, 'w') as f:
            f.write(content)
    
    print(f"Created sample project: {project_name}")
    print("Files created:")
    for file_path in project_files.keys():
        print(f"  - {file_path}")

# Clean up demonstration files
cleanup_files = [
    "sample_requirements.txt",
    "demo_requirements.txt", 
    "sample_gitignore.txt",
    "sample_Pipfile",
    "setup_project.py"
]

cleanup_dirs = [demo_env_name]

print(f"\nCleaning up demonstration files...")
for file in cleanup_files:
    try:
        if os.path.exists(file):
            os.remove(file)
    except:
        pass

for dir_name in cleanup_dirs:
    try:
        if os.path.exists(dir_name):
            import shutil
            shutil.rmtree(dir_name)
    except:
        pass

print("\n" + "=" * 60)
print("VIRTUAL ENVIRONMENTS MODULE COMPLETE!")
print("=" * 60)
print("Key takeaways:")
print("1. Virtual environments isolate project dependencies")
print("2. Use 'python -m venv' to create environments")
print("3. Always activate before installing packages")
print("4. Use requirements.txt for reproducible environments")
print("5. One environment per project is best practice")
print("6. Consider automation tools for project setup")