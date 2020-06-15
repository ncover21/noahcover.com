#!/bin/bash

grep -r --exclude-dir={node_modules,_site} "$1" *
