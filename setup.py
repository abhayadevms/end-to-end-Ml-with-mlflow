from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of the README file
current_dir = Path(__file__).parent
readme_file = current_dir / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Write the dependencies to a requirements.txt file
requirements_file = current_dir / "requirements.txt"
if requirements_file.exists():
    requirements = requirements_file.read_text(encoding="utf-8").splitlines()
else:
    requirements = [
        "mlflow>=1.0.0",
        "pandas>=1.0.0",
        "numpy>=1.18.0",
        "scikit-learn>=0.22.0",
        "matplotlib>=3.0.0",
        "seaborn>=0.10.0",
    ]
# Filter out invalid dependency specifiers like '-e .'
filtered_requirements = [req for req in requirements if not req.startswith("-e ")]
# Do not overwrite the requirements.txt file with filtered requirements

setup(
    name="end_to_end_ml_with_mlflow",
    version="0.1.0",  # Semantic versioning: MAJOR.MINOR.PATCH
    author="Abhayadev M S",
    author_email="email.abhayadev@gmail.com",
    description="An end-to-end machine learning project with MLflow integration.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhayadevms/end-to-end-ml-with-mlflow",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    keywords="machine learning mlflow data-science",
    project_urls={
        "Bug Tracker": "https://github.com/abhayadevms/end-to-end-ml-with-mlflow/issues",
        "Documentation": "https://github.com/abhayadevms/end-to-end-ml-with-mlflow#readme",
        "Source Code": "https://github.com/abhayadevms/end-to-end-ml-with-mlflow",
    },
)