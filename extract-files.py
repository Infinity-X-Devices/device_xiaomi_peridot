#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2025 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools
extract_utils.tools.DEFAULT_PATCHELF_VERSION = '0_18'

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/peridot',
    'hardware/qcom-caf/sm8650',
    'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/commonsys/display',
]

blob_fixups: blob_fixups_user_type = {
    ('odm/etc/camera/enhance_motiontuning.xml',
     'odm/etc/camera/motiontuning.xml',
     'odm/etc/camera/night_motiontuning.xml'): blob_fixup()
        .regex_replace('xml=version', 'xml version'),

    ('odm/lib64/hw/camera.qcom.so',
     'odm/lib64/hw/com.qti.chi.override.so',
     'odm/lib64/hw/camera.xiaomi.so',
     'odm/lib64/libcamxcommonutils.so',
     'odm/lib64/libmialgoengine.so',
     'odm/lib64/libchifeature2.so'): blob_fixup()
        .add_needed('libprocessgroup_shim.so'),

    'odm/lib64/libwrapper_dlengine.so': blob_fixup()
        .add_needed('libwrapper_dlengine_shim.so'),

    'system_ext/bin/wfdservice64': blob_fixup()
        .add_needed('libwfdservice_shim.so'),

    'system_ext/lib64/libwfdmmsrc_system.so': blob_fixup()
        .add_needed('libgui_shim.so'),

    'system_ext/lib64/libwfdnative.so': blob_fixup()
        .remove_needed('android.hidl.base@1.0.so')
        .add_needed('libbinder_shim.so')
        .add_needed('libinput_shim.so'),

    'vendor/bin/init.qcom.usb.sh': blob_fixup()
        .regex_replace('ro.product.marketname', 'ro.product.odm.marketname'),

    'vendor/lib64/libqcodec2_core.so': blob_fixup()
        .add_needed('libcodec2_shim.so'),

    ('vendor/lib64/libqcrilNr.so', 
     'vendor/lib64/libril-db.so'): blob_fixup()
         .binary_regex_replace(rb'persist\.vendor\.radio\.poweron_opt', rb'persist.vendor.radio.poweron_ign'),   

    ('vendor/bin/hw/vendor.dolby.media.c2@1.0-service',
     'vendor/bin/hw/vendor.qti.media.c2@1.0-service',
     'vendor/bin/hw/vendor.qti.media.c2audio@1.0-service'): blob_fixup()
        .add_needed('libcodec2_hidl_shim.so'),

    'vendor/lib64/vendor.libdpmframework.so': blob_fixup()
        .add_needed('libhidlbase_shim.so'),

    ('vendor/etc/media_codecs.xml',
     'vendor/etc/media_codecs_cliffs_v0.xml',
     'vendor/etc/media_codecs_performance_cliffs_v0.xml'): blob_fixup()
        .regex_replace(
            '.+media_codecs_(google_audio|google_c2|google_telephony|vendor_audio).+\n',
            ''
        ),

    'vendor/etc/seccomp_policy/c2audio.vendor.ext-arm64.policy': blob_fixup()
        .add_line_if_missing('setsockopt: 1'),

    'vendor/etc/sensors/hals.conf': blob_fixup()
        .add_line_if_missing('sensors.xiaomi.v2.so'),
}

module = ExtractUtilsModule(
    'peridot',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=False,
    add_firmware_proprietary_file=True
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
