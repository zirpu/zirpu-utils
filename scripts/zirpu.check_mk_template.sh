#!/bin/bash
# check_mk local check template script.
prog=$(basename $0 .sh)

port=NNNN

# check_mk output format:
# return-code name-of-check perf-data(k-v,...) (OK|WARNING|CRITICAL|UNKNOWN) msg
# perf is:  key=val[;warn;crit;min;max][|key2=val2...]

nc=$(which nc)
if [ -z "$nc" ]; then
    echo "2 $prog - CRIT missing nc command for checking."
    exit 0
fi

# 
if ! nc -z localhost ${port}
then
    echo "2 $prog - CRIT ${prog} refusing connections on localhost:${port}"
    exit 0
fi

# TODO: add more thorough checking.

# default. everything is OK.
echo "0 $prog - OK"

exit 0
