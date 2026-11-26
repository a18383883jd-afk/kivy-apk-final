[app]
title = Payment Tester Pro
package.name = paymenttesterpro
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,requests,urllib3,chardet,idna,certifi
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE
android.accept_sdk_license = True
android.api = 33
android.ndk = 25b
android.sdk = 24
android.buildtools = 30.0.3
android.use_aapt2 = True

[buildozer]
log_level = 2
warn_on_root = 1
