# PicnicChallenge - Ticket analyser

Simple command-line application designed to read, validate, and analyze a collection of support tickets from a JSON file. It provides an interactive shell, allowing users to identify trends, view tickets by category, find recent/oldest issues, and see which users are most active.

-----

## Features

  * **Data Validation**: Uses Pydantic to ensure the input JSON data conforms to a predefined structure.
  * **Automatic Categorization**: Automatically categorizes each ticket into predefined groups based on keywords in the ticket subject.
  * **Data Summary**: Displays a summary of the total number of tickets in each category on startup.
  * **Interactive Shell**: Command-line interface to explore the data with the following options:
      * View all tickets by a specific category.
      * Show the top users with the most submitted tickets.
      * List the oldest tickets.
      * List the most recent tickets.

-----

## Stack/Prerequisites

  * **Language**: Python 3.10
  * **Libraries**: `pydantic`, `json`, `collections`, `enum`, `typing`

-----

## How to Run the Application

If not installed, run:
```shell
pip install pydantic
```
then

```shell
python main.py
```

## Future improvements
* Add unit tests (pytest) to ensure the reliability and correctness of the data models and analysis functions.
* Add a virtual environment to keep project dependencies isolated.
* Evolve the application from a command-line tool to dashboard, providing a graphical interfaces/charts/tables for better visualization.