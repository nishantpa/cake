#!/bin/bash

# << Swami Shreeji >>
# @nishantpatel ; 10 Oct 2017
# Create properly formed URL from jenkins plugin IDs
# Command to execute on json output: sed 's/^.\{15\}//' dependents.json | cut -f 1 -f 3 -d ","

cut -f 1 -d ":" jenkPlug.fail | sed 's/^/https:\/\/plugins.jenkins.io\//' > URLsList.txt
