<br />
<p align="center">
  <h2 align="center">YOUR_TITLE</h2>

  <p align="center">
    An expert system that helps to diagnose the diseases of a patient.
    <br />
    <br />
    <a href="https://github.com/nagasaibharath/Medical-Expert-System">View Demo</a>
  </p>
</p>


## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Dependencies](#dependencies)
  - [Installation](#installation)
- [Project Layout](#project-layout)
- [License](#license)
- [Project Contributors](#project-contributors)


## About The Project

An expert system that helps to diagnose the diseases of a patient by asking questions
about any symptoms. Will Also display full diagnosis and cure for common diseases.

Cure and Diagnosis is written down in `Treatment/markdown` files and converted to 
html with pandoc conversion tool.

## Getting Started

To get a local copy up and running follow these simple steps.

### Dependencies

This following list of dependencies are present/used in the project

- experta

### Installation
 
1. Clone the Medical-Expert-System
```sh
git clone https://github.com/nagasaibharath/Medical-Expert-System.git
cd Medical-Expert-System
```
2. Install the experta package with pip (if not installed)
```sh
pip install experta
```
3. Run the program
```sh
python expert.py
```

## Project Layout

```sh
Root directory
├── ExpertSystemDesign # files with design of expert system
├── Treatment # files containing details of all diseases
│   ├── html
│   │   ├── Anemia.html
│   │   ├── ...
│   │   └── Tuberculosis.html
│   └── markdown
│       ├── Anemia.md
│       ├── ...
│       └── Tuberculosis.md
├── expert.py # main application
├── LICENSE
├── README.md
└── symptoms.ods # spreadsheet with diseases and symptoms
```

## License

Distributed under the MIT License. See `LICENSE` for more information.


## Project Contributors

- [Rikil Gajarla](https://github.com/RikilG)
- [Naga Sai Bharath](https://github.com/nagasaibharath)
- [Bonagiri Akash](https://github.com/akashalien)

Project Link: [https://github.com/nagasaibharath/Medical-Expert-System](https://github.com/nagasaibharath/Medical-Expert-System)
