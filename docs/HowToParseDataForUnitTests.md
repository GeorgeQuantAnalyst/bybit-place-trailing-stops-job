---
title: How to parse data for unit tests
date: 23.1.2023
description: Guidence how parse data from input and result for unit tests
tags: Testing, Python, UnitTests
---

# How parse positions raw
```python
with open("tests/resources/positions_raw.json", "w") as out_file: out_file.write(json.dumps(positions_raw, indent =4))
```