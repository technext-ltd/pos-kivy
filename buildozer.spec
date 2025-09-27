[app]

# Name of your app
title = POS System

# Package name (no spaces or special characters)
package.name = posapp

# Unique domain for your app
package.domain = org.yourname

# Main folder where your code is
source.dir = .

# Main entry file
source.main = pos2.py

# Application version
version = 0.1

# List of Python modules your app needs
requirements = python3,kivy

# Orientation of the app: portrait or landscape
orientation = portrait

# Fullscreen mode (1 = fullscreen, 0 = normal window)
fullscreen = 0

# Permissions your app needs (important for reading/writing JSON files)
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Optional: Set a custom app icon
# icon.filename = %(source.dir)s/icon.png

# Minimum Android API level
android.api = 31

# Target Android API level
android.minapi = 21

# Hide the title bar
show_status_bar = 0

# Optimize APK size
android.release_artifact = app-release.apk

[buildozer]

# Log level: 1 (quiet) to 2 (debug)
log_level = 2

# Ignore warnings about running as root
warn_on_root = 1
