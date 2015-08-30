#!/bin/bash
set -e  # exit on any error, or uncaught error?

# assumptions:
## ubuntu 12.04 at least. -allan

prog=$(basename $0)
pidfile=/var/tmp/$prog.pid
logdir=/var/tmp/${prog}.logs
mkdir -p $logdir
logfile=$logdir/$prog.$(date +%FT%T)

# handle cli options.

# save all output to the logfile
exec > $logfile
exec 2>&1


# clean up on exit.  purge log files > 30 days.
_cleanup() {
    rm -f $pidfile ${pidfile}.lock
    find $logdir -type f -ctime +30|xargs --no-run-if-empty /bin/rm
}

_sendlog() {
    #TODO: put log somewhere like in a mongodb cluster instead of email.
    #      or generate an alert for someone to look at the log.
    echo caught ERR, sending logfile.
    mail root -s"$prog log file from error run." < $logfile
    exit 1
}

trap "_sendlog" ERR
trap "_cleanup" EXIT

if [ ! -x /usr/bin/lockfile-create ]; then
    echo lockfile-create not found or not executable. install lockfile-progs
    exit 1
fi

# get lock on pidfile, else bail.
## TODO: add some monitoring here if this cron job should not run too long.
##       if someone needs to be warned or alerted, we'll need to monitor for
##       lock failures, or old running processes.
lockfile-create --retry 2 --use-pid $pidfile 2> /dev/null || exit 1

echo $$ > $pidfile

# run lockfile-touch in background to keep lock fresh.
lockfile-touch $pidfile &
BADGER="$!"

# do your thing here.
# example of an error, which causes script abort and email of the log file.
ls /tmp/bogus.$$.file

# normal non-error functioning.
echo sleeping 60 secs.
sleep 60


# we're done here.
kill $BADGER
lockfile-remove $pidfile

# neatness counts.
exit 0

