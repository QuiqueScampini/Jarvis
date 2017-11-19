#!/bin/bash

cd ${JARVIS_VIDEO}

actualProcessPid=${1}

kill ${actualProcessPid}

if [ -f FILM_PID ]; then
    pid=`cat FILM_PID`
    kill -9 ${pid}
    wait ${pid}
fi

if [ -f STITCH_PID ]; then
    pid=`cat STITCH_PID`
    kill -9 ${pid}
    wait ${pid}
fi

if [ -f CONVERT_PID ]; then
    pid=`cat CONVERT_PID`
    kill -9 ${pid}
    wait ${pid}
fi

rm -f FILM_PID STITCH_PID CONVERT_PID

exit 0