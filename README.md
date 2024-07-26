# File I/O in Python: Examples from CS50's Introduction to Programming with Python

Welcome to the repository for my File I/O exploration in Python, inspired by CS50's Introduction to Programming with Python course. This repository contains various scripts demonstrating how to read from and write to files, manipulate CSV data, create GIFs, and more.

## Contents

- `costume.py`: Generates GIF images from a series of input images.
- `names.py`: Reads names from a text file and prints a sorted list.
- `students.py`: Writes user input to a CSV file.
- `shirt.py`: Overlays a shirt image on top of another image.
- `scourgify.py`: Transforms and cleans CSV data.
- `pizza.py`: Displays CSV data as a formatted table.
- `lines.py`: Counts the number of lines of code in a Python file, excluding comments and blank lines.

## Getting Started

### Prerequisites

- Python 3.x
- Pillow library: Install using `pip install pillow`
- Tabulate library: Install using `pip install tabulate`

### Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/bonheurNE07/file_io.git
    cd file_io
    ```

2. Run the scripts with the appropriate input files. Below are some examples:

#### Generating a GIF from Images

```bash
$ python costume.py costume1.gif costume2.gif
```

#### Reading Names from a Text File

Ensure you have a `names.txt` file with names listed line by line.

```bash
python names.py
```

#### Writing User Input to a CSV File

```bash
python students.py
```

#### Overlaying a Shirt Image on Another Image

```bash
$ cd shirt
$ python shirt.py before1.jpg after1.jpg
$ python shirt.py before2.jpg after2.jpg
$ python shirt.py before3.jpg after3.jpg
```

#### Transforming and Cleaning CSV Data

```bash
$ cd scourgify
$ python scourgify.py before.csv after.csv
```

#### Displaying CSV Data as a Formatted Table

```bash
$ cd pizza
$ python pizza.py regular.csv
```

#### Counting Lines of Code

```bash
$ cd lines
$ python lines.py test.py
```

## Contributing

I invite everyone to contribute to this project for improvements and additional functionalities. If you have suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This repository is inspired by CS50's Introduction to Programming with Python course. Special thanks to the CS50 team for their excellent educational content.

## Conclusion

File I/O is a powerful feature in Python that allows us to read from and write to files, manipulate data, and perform various operations. The examples provided here are just a glimpse of what you can achieve with file handling in Python. 

Feel free to check out the complete code, share your thoughts, and contribute to the project. I will continue to update the repository with more examples of file manipulations, including Excel and Word file handling. Happy coding!

---

### Author

NDEZE BONHEUR EMMANUEL

- [Medium](https://medium.com/@bonheurndezenc/exploring-file-i-o-in-python-a-journey-with-cs50-e312568a2473)
- [LinkedIn](https://www.linkedin.com/in/bonheur-ndeze-8b88342b0/)
- [GitHub](https://github.com/bonheurNE07)

---

Thank you for visiting! If you like this project, please give it a star ⭐ on GitHub.