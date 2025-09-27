[app]
# App title shown on the phone
title = POS System

# Package name (no spaces or special characters)
package.name = pos_system

# Your app domain (can be anything, usually reversed domain style)
package.domain = org.example

# REQUIRED: App version
version = 1.0.0

# Your source code location
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Permissions your app needs
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Android SDK target version
android.api = 34
android.minapi = 21

# ✅ Force Buildozer to use the manually installed SDK
android.sdk_path = /home/runner/android-sdk

# ✅ Use the build-tools we installed in GitHub Actions
android.build_tools_version = 34.0.0

# Optional: Orientation (uncomment if you want to lock orientation)
# orientation = portrait

# Optional: Icon
# icon.filename = %(source.dir)s/data/icon.png

# Keep this to speed up builds by not cleaning every time
# (If you have build errors, set to 1 to force a clean build)
# buildozer clean
