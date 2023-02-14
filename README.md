# vacancy-section-generator

Generate vacancy sections (Freimeldeabschnitte) for yaramo topologies

## Process

This generator works on the assumption that one edge can be part of zero or one vacancy sections.
It will create one vacancy section for each edge and also add them to the topology as a whole as
well as the relevant routes.

## Installation
```shell
$ poetry add git+https://github.com/simulate-digital-rail/yaramo
$ poetry install
```

## Usage

```python
VacancySectionGenerator(topology).generate()
print(topology.vacancy_sections)
```