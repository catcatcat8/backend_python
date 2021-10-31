#!/bin/bash

ab -kc 10 -t 60 http://localhost:8000/ > dynamic_test.txt
