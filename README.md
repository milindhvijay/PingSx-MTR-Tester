# PingSx-MTR-Tester

PingSx-MTR-Tester is a Python script that uses Selenium to perform MTR (My TraceRoute) tests on multiple servers simultaneously and captures screenshots of the results for easy visualization.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites:

    Python 3.x
    Google Chrome
    Chromedriver

## Installation

* Clone the repository to your local machine.

* Install the required packages with pip:

        pip install -r requirements.txt

Download and install the [latest version of Chromedriver](https://chromedriver.chromium.org/downloads) and add it to your system path or place it in the project directory.

## Usage

* Run the script with **'python mtr.py'**.

* Enter the target IP address to run the MTR tests on.

* Enter the number of threads to use for the tests.

* Enter the path to save the screenshots.

* The script will run MTR tests on the target IP address for each server in batches of the specified number of threads, and save screenshots of the results in a folder named with today's date.

* The script will open Chrome windows and run MTR tests on each server. Screenshots of the MTR results will be saved in a new folder with today's date in the format "DD-MM-YYYY".

* After all MTR tests are complete, the script will terminate.

Note: It is recommended to run this script on a computer with a fast and stable internet connection for best results.
## Contributing

Contributions are welcome! If you would like to contribute to this project, please submit a pull request.
## License

This project is licensed under the MIT License - see the [LICENSE](PingSx-MTR-Tester/LICENSE) for details.
## Acknowledgements

This project was inspired by Ping.Sx, an online tool for performing MTR tests.

 - [Ping.sx](https://ping.sx/mtr)
