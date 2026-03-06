#!/bin/bash

# Configuration
BASE_DIR="/Users/lordwilson/.gemini/antigravity/scratch/sovereign_daemon_env"
INTAKE_DIR="$BASE_DIR/intake"
PROCESSED_DIR="$BASE_DIR/processed"
QUARANTINE_DIR="$BASE_DIR/quarantine"

DAEMON_SCRIPT="/Users/lordwilson/.gemini/antigravity/scratch/sovereign_daemon.py"
FORAGER_SCRIPT="/Users/lordwilson/.gemini/antigravity/scratch/sovereign_forager.py"

# Clean up environment
rm -rf "$PROCESSED_DIR"/* "$QUARANTINE_DIR"/* "$INTAKE_DIR"/*
mkdir -p "$INTAKE_DIR" "$PROCESSED_DIR" "$QUARANTINE_DIR"

echo "Initializing Sovereign Stack Ecosystem..."

# Launch the Daemon in the background
python3 -u "$DAEMON_SCRIPT" &
DAEMON_PID=$!
echo "Sovereign Daemon launched (PID: $DAEMON_PID)."

sleep 2

# Launch the Forager in the foreground to simulate the live feed
python3 -u "$FORAGER_SCRIPT"

echo ""
echo "Forager feed completed. Waiting 5 seconds for final Daemon processing..."
sleep 5

echo "Stopping Daemon (PID: $DAEMON_PID)..."
kill $DAEMON_PID
echo "Sovereign Stack simulation offline."
