# Budgeted Purchase Problem: Search Algorithms

## Overview
This project implements two distinct search algorithms to address the Budgeted Purchase Problem: Iterative Deepening and Hill Climbing. These algorithms are encapsulated within two Python scripts located in the `/source` directory. The script `Budget-ID.py` utilizes the Iterative Deepening approach, while `Budget-HC.py` employs the Hill Climbing method with optional random restarts for enhanced solution accuracy.

## Input Format
Input for both programs is provided through plain text files. The structure of these input files is as follows:

- **Iterative Deepening (`Budget-ID.py`):** The first line specifies the target value and budget as integers, followed by a character indicating the desired output verbosity: 'V' for verbose or 'C' for compact output. Each subsequent line describes an object with its name (a string), value, and cost as integers.

- **Hill Climbing (`Budget-HC.py`):** The input format is similar to Iterative Deepening, with an additional integer on the first line representing the number of random restarts for the algorithm.

This project includes six test datasets under the `/data/` directory. Files `1.txt` through `4.txt` are designed for the Iterative Deepening algorithm, while `5.txt` and `6.txt` are intended for Hill Climbing.

## Usage Instructions

### Running Iterative Deepening
To run the Iterative Deepening script with the default input (`1.txt`):

```bash
cd source  # Navigate to the source directory if not already there
python Budget-ID.py
```

To run the script with custom input, for example, `4.txt`:
```bash
python Budget-ID.py --file_path ../data/4.txt
```

### Running Iterative Deepening
To run the Hill Climbing script with the default input (`5.txt`):
```bash
cd source  # Navigate to the source directory if not already there
python Budget-HC.py
```

To run the script with custom input, for example, `6.txt`:
```bash
python Budget-HC.py --file_path ../data/6.txt
```