[app]
title = Mi Regalo
package.name = appregalo
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 1

# ESTA ES LA PARTE CLAVE PARA EVITAR EL ERROR 100
android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 23b
android.accept_sdk_license = True
android.archs = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1

