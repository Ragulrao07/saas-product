## 1. Setup Project Base and Initial Test
Goal: Initialize the project repository with basic structure and a passing unit test.
Description: Create the standard project directory layout and configuration files required for the development environment. Configure the unit testing framework to ensure a basic dummy test executes and passes successfully.

## 2. Define Core Data Models
Goal: Establish the primary data structures and domain interfaces required for the application.
Description: Draft and export the initial domain models and data contracts needed across the system. Write corresponding unit tests to verify object instantiation and basic model validation logic.

## 3. Implement Centralised Logging Utility
Goal: Create a standard logger module to handle application logging across components.
Description: Build a logging utility wrapper that supports standard log levels such as INFO, WARN, and ERROR. Add tests to ensure log messages are correctly formatted and captured.

## 4. Set Up Automated CI Pipeline
Goal: Configure automated building and testing on repository changes.
Description: Add a continuous integration workflow configuration file to automatically install dependencies and run tests on code pushes. Verify that the pipeline correctly runs the test suite and reports build status.
