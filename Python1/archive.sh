#!/bin/bash

PROJECTS="Operators Variables Output Conditions Loops Functions Strings Lists Dictionaries Classes WordGuess"

git archive --format=zip --output=Python1_projects_answers.zip --prefix=Python1_projects_answers/ master $PROJECTS
git archive --format=zip --output=Python1_projects.zip --prefix=Python1_projects/ student $PROJECTS
