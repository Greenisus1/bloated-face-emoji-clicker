# bloated face emoji clicker1.0.0

The exact requested click target is 🫪. Space/Enter earns points,1 buys more click power,2 buys automatic points per second. Original offline session-only incremental game; no account, network, ads, payments or saved progress. Quitting clears the session. R resets immediately. This is not Cookie Clicker or a port.

Fullscreen Python3 curses terminal UI. F switches to the explicit text fallback if your terminal/font cannot display the requested emoji. Default keeps the exact character; no silent substitution. The test environment font has no glyph for it, so emoji artwork visibility is unverified on your terminal.

    bash app-store.sh install
    bash app-store.sh run
    python3 game.py --version
    python3 -m unittest -v

Python3/curses and an interactive Unicode terminal required; install only checks source, no sudo/dependency additions. Linux unit/PTY/terminal-restoration tests checked, physical Pi and non-Linux untested. MIT license. Games marker in root app-store.sh.
