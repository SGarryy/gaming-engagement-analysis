import sys

required_packages = {
    'pandas': '2.1.0',
    'numpy': '1.26.0',
    'matplotlib': '3.8.0',
    'seaborn': '0.13.0',
    'sklearn': '1.3.0'
}

missing = []
for package, required_version in required_packages.items():
    try:
        module = __import__(package)
        actual_version = module.__version__
        print(f"✓ {package}: {actual_version}")
    except ImportError:
        missing.append(package)

if missing:
    print(f"\n✗ Missing packages: {', '.join(missing)}")
    sys.exit(1)
else:
    print("\n✓ All dependencies installed successfully.")