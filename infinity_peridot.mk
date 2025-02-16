#
# Copyright (C) 2024 The infinityOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common RisingOs stuff.
$(call inherit-product, vendor/infinity/config/common_full_phone.mk)

# Inherit from peridot device
$(call inherit-product, device/xiaomi/peridot/device.mk)

PRODUCT_NAME := infinity_peridot
PRODUCT_DEVICE := peridot
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_BRAND := POCO
PRODUCT_MODEL := 24069PC21G

# Build prop overides

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="peridot_global-user 14 UKQ1.240116.001 V816.0.10.0.UNPMIXM release-keys" \
    BuildFingerprint=POCO/peridot_global/peridot:14/UKQ1.240116.001/V816.0.10.0.UNPMIXM:user/release-keys \
    DeviceName=peridot
    DeviceProduct=peridot_global \
    SystemName=peridot_global \
    SystemDevice=peridot

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

# Infinity-X Flags
TARGET_BOOT_ANIMATION_RES := 1080
INFINITY_BUILD_TYPE := OFFICIAL
INFINITY_MAINTAINER := AtharvaSwamy
TARGET_SUPPORTS_BLUR := true
TARGET_HAS_UDFPS := true
WITH_GAPPS := true
