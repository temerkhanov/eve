# This mkimage-raw-efi produces the raw EFI partition for EVE,
# including the files in efi-files in the image.  This includes:
#
#   /EFI/BOOT/grub.cfg - Chainloads main bootloader
#   /UsbInvocationScript.txt - Enables USB boot on Dell 3000 series
#
ARG BUILDER=lfedge/eve-alpine:fc754568b1fa784544ff306e465c634811d1d6d9
FROM ${BUILDER} as initrd
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]

COPY nlplug-findfs.c initramfs-init /tmp/
RUN apk add --no-cache         \
      mkinitfs=3.4.5-r3        \
      gcc=9.3.0-r2             \
      musl-dev=1.1.24-r9       \
      linux-headers=5.4.5-r1   \
      kmod-dev=27-r0           \
      util-linux-dev=2.35.2-r0 \
      cryptsetup-dev=2.3.2-r1
RUN cc -Wall -Werror -g -D_GNU_SOURCE -DDEBUG -I/usr/include/blkid -I/usr/include/uuid /tmp/nlplug-findfs.c -lblkid  -lkmod  -L/lib -lcryptsetup -o /sbin/nlplug-findfs
RUN mkinitfs -n -i /tmp/initramfs-init -o /initrd.gz

FROM ${BUILDER} as build
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]

WORKDIR /out

RUN mkdir -p /out/etc/apk /out/boot && cp -r /etc/apk/* /out/etc/apk/
RUN apk add --no-cache --initdb -p /out \
  busybox=1.31.1-r19        \
  mtools=4.0.24-r0          \
  dosfstools=4.1-r1         \
  libarchive-tools=3.4.3-r1 \
  sgdisk=1.0.5-r0           \
  e2fsprogs=1.45.6-r0       \
  util-linux=2.35.2-r0      \
  squashfs-tools=4.4-r0     \
  coreutils=8.32-r0         \
  tar=1.32-r1

COPY make-raw install trampoline.grub.cfg grub.cfg.in UsbInvocationScript.txt /out/

RUN echo "mtools_skip_check=1" >> etc/mtools.conf

FROM scratch
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]

COPY --from=build /out/ /
COPY --from=initrd /initrd.gz /
COPY grub.stage1 /usr/lib/grub/i386-pc/boot.img
RUN gzip -d < /initrd.gz | cpio -id && \
    find . -xdev | grep -v initrd.gz | sort | cpio --quiet -o -H newc | gzip > /initrd.gz && \
    mv /initrd.gz /initrd.img

COPY grub.cfg /EFI/BOOT/

ENTRYPOINT [ "/make-raw" ]
