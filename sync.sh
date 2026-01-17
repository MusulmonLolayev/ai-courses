#!/bin/bash

# --- Configuration Variables ---
# Local directory to sync (must have a trailing slash to sync contents)
LOCAL_DIR="${PWD}/build/"

# Remote server details
# Remote directory destination
REMOTE_DIR="/var/www/ai.cs.tqqt.uz/"

# Rsync options
# -a: archive mode (preserves permissions, ownership, timestamps, recursive, etc)
# -v: verbose (optional, shows files being transferred)
# -z: compress file data during transfer (optional, saves bandwidth)
# --delete: deletes files in the destination that are not in the source (for true sync)
OPTIONS="-avzh --delete"

# --- Rsync Command ---
echo "Starting synchronization of $LOCAL_DIR to contabo:$REMOTE_DIR"

rsync $OPTIONS "$LOCAL_DIR" "contabo:$REMOTE_DIR"

if [ $? -eq 0 ]; then
    echo "Synchronization completed successfully."
else
    echo "Synchronization failed."
fi
