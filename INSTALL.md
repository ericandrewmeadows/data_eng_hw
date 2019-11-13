# Setup (running)
1.  In the root directory, run `docker-compose up --build`
2.  Open a web-browser
    1.  Navigate to `localhost:8191`
        * Do not enter a password, and hit `return`
    2.  Navigate in Jupyter to the notebook below
        * `notebooks` --> `TakeHomeAssignment - Eric Meadows.ipynb`
    3.  Select, in the Jupyter Navbar:  `Kernel` --> `Restart & Run All`

# Setup (developers)
Configure development environment
1.  Install Python3
    1.  Install Homebrew
        * Run `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
    2.  Install Python3
        * Run `brew install python`
2.  Install pre-commit hooks (this ensures code quality and formatting)
    1.  Install developer Python3 requirements
        * Run `pip3 install -r requirements-dev.txt`
    2.  Install pre-commit hooks
        * Run `pre-commit install`
