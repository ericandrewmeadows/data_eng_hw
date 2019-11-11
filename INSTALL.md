# Setup (running)

# Setup (developers)
1.  Configure development environment
  a.  Install Python3
    i.  Install Homebrew
      - Run `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
    ii.  Install Python3
      - Run `brew install python`
  b.  Install pre-commit hooks (this ensures code quality and formatting)
    i.  Install developer Python3 requirements
      - Run `pip3 install -r requirements-dev.txt`
    ii.  Install pre-commit hooks
      - Run `pre-commit install`
