#!/usr/bin/env bash
# Fails the build if debug markers appear in the production output.
# Usage: scripts/check-debug-bundle.sh [dist_dir] [marker ...]
set -euo pipefail

DIST="${1:-dist}"
shift || true

if [ "$#" -eq 0 ]; then
  set -- "stability-debug" "initDebug" "__DEBUG__"
fi

if [ ! -d "$DIST" ]; then
  echo "ERROR: build output '$DIST' not found" >&2
  exit 2
fi

found=0
for marker in "$@"; do
  if grep -rIl --fixed-strings "$marker" "$DIST" >/dev/null 2>&1; then
    echo "ERROR: debug marker '$marker' found in $DIST:"
    grep -rIl --fixed-strings "$marker" "$DIST"
    found=1
  fi
done

if [ "$found" -eq 1 ]; then
  exit 1
fi

echo "OK: no debug markers found in $DIST"
