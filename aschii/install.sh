#!/bin/bash

set -e

INSTALL_DIR="$HOME/.local/bin"
BIN_NAME="aschii"
FILE_NAME="aschii.py"

REPO_URL="${ASCHII_REPO_URL:-}"

echo "Installing ASCHII..."

mkdir -p "$INSTALL_DIR"

curl -sL "$REPO_URL/$FILE_NAME" -o "$INSTALL_DIR/$FILE_NAME"

chmod +x "$INSTALL_DIR/$FILE_NAME"

if [ -L "$INSTALL_DIR/$BIN_NAME" ]; then
    rm "$INSTALL_DIR/$BIN_NAME"
fi
ln -s "$INSTALL_DIR/$FILE_NAME" "$INSTALL_DIR/$BIN_NAME"

if ! echo "$PATH" | grep -q "$INSTALL_DIR"; then
    SHELL_RC=""
    if [ -n "$ZSH_VERSION" ]; then
        SHELL_RC="$HOME/.zshrc"
    elif [ -n "$BASH_VERSION" ]; then
        SHELL_RC="$HOME/.bashrc"
    fi
    if [ -n "$SHELL_RC" ] && [ -f "$SHELL_RC" ]; then
        if ! grep -q "$INSTALL_DIR" "$SHELL_RC" 2>/dev/null; then
            echo "" >> "$SHELL_RC"
            echo "# ASCHII" >> "$SHELL_RC"
            echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" >> "$SHELL_RC"
            echo "Added $INSTALL_DIR to PATH in $SHELL_RC"
            echo "Run: source $SHELL_RC to update PATH"
        fi
    else
        echo "NOTE: Add '$INSTALL_DIR' to your PATH if not already present"
    fi
fi

echo ""
echo "ASCHII installed successfully!"
echo "Run 'aschii' to start the interactive mode."
echo "Run 'aschii -m \"hello\"' for CLI mode."