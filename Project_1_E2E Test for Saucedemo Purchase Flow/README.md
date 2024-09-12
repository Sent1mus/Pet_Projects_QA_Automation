# E2E Test for Saucedemo Purchase Flow

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Test](#running-the-test)
- [Test Description](#test-description)
- [Notes](#notes)

## Requirements

- Python 3.x
- Selenium WebDriver
- ChromeDriver (automatically installed via webdriver-manager)

## Installation

pip install selenium webdriver-manager

## Running the Test

To run the test, execute the following command:
python test_saucedemo.py

## Test Description

This End-to-End (E2E) test automates the purchase flow on saucedemo.com:
1. Logs in with provided credentials
2. Adds a product to cart
3. Proceeds to checkout
4. Fills out required information
5. Completes the order
6. Verifies successful completion of the purchase

## Notes

- The test uses Selenium WebDriver with ChromeDriver.
- Webdriver-manager is used to automatically install and manage ChromeDriver.
- Explicit waits are implemented to handle potential delays in page loading.
- The test runs headlessly by default but can be easily modified to run with a visible browser window.
- This test assumes you're using Chrome as your browser. If you want to use a different browser, you'll need to adjust the WebDriver configuration accordingly.
