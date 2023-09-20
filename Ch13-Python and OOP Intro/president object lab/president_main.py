#!/usr/bin/env python
from president_codealong import President

for term in 1, 26, 39, 44:
    p = President(term)  # George Washington

    print("{} {} was born at {}, {} on {}".format(
        p.first_name, p.last_name, p.birth_place, p.birth_state, p.birth_date
    ))
    print()
