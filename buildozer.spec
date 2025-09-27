[app]
title = POS System
package.name = posapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 0.1
requirements = python3,kivy,openssl

presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.3.0

fullscreen = 0
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 34
android.ndk_path = 
android.sdk_path = 

[buildozer]
log_level = 2
warn_on_root = 1

[app]
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Add this section for Android
android.arch = arm64-v8a,armeabi-v7a
