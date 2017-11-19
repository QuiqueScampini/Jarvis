#!/bin/bash

cd ${JARVIS_VIDEO}

if [ -f FILM_PID ]; then
    pid=`cat FILM_PID`
    kill ${pid}
fi

exit 0