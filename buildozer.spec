[app]
title = POS System
package.name = posapp
package.domain = org.yourname

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0
requirements = python3,kivy,openssl

orientation = portrait
osx.python_version = 3

fullscreen = 0
android.api = 33
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1

# Android specific
android.accept_sdk_license = True
android.arch = arm64-v8a

# Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
