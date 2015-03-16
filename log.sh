#! /bin/sh

TIME_LOG_FILE=$1
shift
if [ ! -f $TIME_LOG_FILE ]
then
    echo 0 >> $TIME_LOG_FILE
fi

START=$(date +%s)

$@

LOGGED=$(expr $(date +%s) - $START)
echo "$(expr $(cat $TIME_LOG_FILE) + $LOGGED)" > $TIME_LOG_FILE

echo "Logged: $LOGGED seconds"
echo "Total: $(cat $TIME_LOG_FILE) seconds"
