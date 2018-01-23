#!/bin/bash

cut -f 1 -d ":" jenkPlug.fail | sed 's/^/https:\/\/plugins.jenkins.io\//' > URLsList.txt