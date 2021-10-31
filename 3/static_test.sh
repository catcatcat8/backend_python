#!/bin/bash

ab -kc 10 -t 60 http://localhost/ > static_test.txt
