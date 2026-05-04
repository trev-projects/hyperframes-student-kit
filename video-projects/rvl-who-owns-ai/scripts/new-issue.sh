#!/usr/bin/env bash
# Clone the RVL editorial weekly template into a new issue folder.
# Usage:
#   ./scripts/new-issue.sh <issue_num> <slug> "<Issue Title>"
# Example:
#   ./scripts/new-issue.sh 18 stablecoins "Stablecoin Commerce"
#
# Run from the workspace root (where video-projects/ lives) OR from inside the
# template folder — the script resolves paths either way.
set -euo pipefail

if [ "$#" -lt 3 ]; then
  echo "Usage: $0 <issue_num> <slug> \"<Issue Title>\""
  echo "Example: $0 18 stablecoins \"Stablecoin Commerce\""
  exit 1
fi

ISSUE_NUM="$1"
SLUG="$2"
TITLE="$3"

# Derive repo root (script may run from either workspace root or template dir)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TEMPLATE_DIR="$( cd "$SCRIPT_DIR/.." && pwd )"
WORKSPACE_ROOT="$( cd "$TEMPLATE_DIR/../.." && pwd )"
TARGET_SLUG="rvl-week-${ISSUE_NUM}-${SLUG}"
TARGET_DIR="${WORKSPACE_ROOT}/video-projects/${TARGET_SLUG}"

if [ -e "$TARGET_DIR" ]; then
  echo "ERROR: $TARGET_DIR already exists. Aborting." >&2
  exit 1
fi

echo "→ Cloning template → video-projects/${TARGET_SLUG}"
cp -r "$TEMPLATE_DIR" "$TARGET_DIR"

# Clean inherited outputs
rm -rf "$TARGET_DIR/renders" "$TARGET_DIR/preview.mp4" "$TARGET_DIR/preview-small.mp4" \
       "$TARGET_DIR/preview.gif" "$TARGET_DIR/contact-sheet.png" 2>/dev/null || true
mkdir -p "$TARGET_DIR/renders"

# Update meta.json
echo "→ Updating meta.json"
sed -i.bak \
  -e "s/\"id\": \"rvl-weekly-template-editorial\"/\"id\": \"${TARGET_SLUG}\"/" \
  -e "s/\"name\": \"RVL — Weekly Issue Template (Editorial)\"/\"name\": \"RVL — W${ISSUE_NUM} ${TITLE}\"/" \
  "$TARGET_DIR/meta.json"
rm "$TARGET_DIR/meta.json.bak"

# Update hardcoded ISSUE_NO in masthead + all footers + attribution
echo "→ Updating ISSUE 17 → ISSUE ${ISSUE_NUM} in compositions"
find "$TARGET_DIR/compositions" -name "*.html" -exec sed -i.bak \
  -e "s/ISSUE 17/ISSUE ${ISSUE_NUM}/g" \
  -e "s/&bull; W17/\\&bull; W${ISSUE_NUM}/g" \
  {} \;
find "$TARGET_DIR/compositions" -name "*.bak" -delete

# Update data-composition-id on root div
sed -i.bak "s/data-composition-id=\"rvl-weekly-template-editorial\"/data-composition-id=\"${TARGET_SLUG}\"/" \
  "$TARGET_DIR/index.html"
sed -i.bak "s/window.__timelines\[\"rvl-weekly-template-editorial\"\]/window.__timelines[\"${TARGET_SLUG}\"]/" \
  "$TARGET_DIR/index.html"
rm "$TARGET_DIR/index.html.bak"

cat <<DONE

✓ Created video-projects/${TARGET_SLUG}

Next steps:
  1. cd video-projects/${TARGET_SLUG}
  2. Edit remaining swap tokens in compositions/ — search for "<!-- SWAP:"
     (Cover title, chapter labels, chapter quotes, stat rows, summary, attribution)
  3. Update SCRIPT.md → regenerate narration-main.wav
  4. Also check: masthead-date in compositions/00-cover.html
  5. npx hyperframes lint
  6. npx hyperframes render --quality draft --output renders/${TARGET_SLUG}-draft.mp4
  7. Apply loudnorm + generate share assets (see HANDOFF.md)
  8. Commit + push

DONE
