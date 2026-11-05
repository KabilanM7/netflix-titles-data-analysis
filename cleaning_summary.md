# Netflix Data Cleaning Report

Original Rows: 8807

Original Columns: 12

Duplicates Removed: 0

## Missing Values Before Cleaning

show_id            0
type               0
title              0
director        2634
cast             825
country          831
date_added        10
release_year       0
rating             4
duration           3
listed_in          0
description        0

## Missing Values After Cleaning

show_id          0
type             0
title            0
director         0
cast             0
country          0
date_added      10
release_year     0
rating           0
duration         0
listed_in        0
description      0

## Final Dataset Shape

(8807, 12)

## Final Data Types

show_id         string[python]
type            string[python]
title           string[python]
director        string[python]
cast            string[python]
country         string[python]
date_added              object
release_year             int64
rating          string[python]
duration        string[python]
listed_in       string[python]
description     string[python]