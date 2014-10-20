Summary: aufs3 user space utilities
Name: aufs3-util
Version: 3.9
Release: 1
Source0: %{name}-%{version}.tar.gz
Group: Applications/System
License: GPL
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc
BuildRequires: make
BuildRequires: glibc-static
BuildRequires: coreutils
BuildRequires: sed
BuildRequires: binutils
BuildRequires: /usr/include/linux/aufs_type.h

%description
User space utilities for aufs3 kernel module (union file system).
Mount helpers etc.
See aufs.sorceforge.net

%prep
%setup -q

%build
# TODO: better as patches, even better: submit upstream
sed -i -e 's/^Install = .*/Install = ${INSTALL} -p/' Makefile
sed -i -e 's/^install: .*/install: /' fhsm/Makefile
make BuildFHSM=no

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sysconfdir}/default/aufs
/sbin/auibusy
/sbin/auplink
/sbin/aumvdown
/sbin/mount.aufs
/sbin/umount.aufs
/usr/bin/aubrsync
/usr/bin/aubusy
/usr/bin/auchk
/usr/lib/libau.so
/usr/lib/libau.so.2
/usr/lib/libau.so.2.7
/usr/share/man/man5/aufs.5.gz
/usr/share/man/man8/aumvdown.8.gz

%changelog
* Mon Oct 20 2014 Jakob Blomer <jblomer@cern.ch> - 3.9
- Initial package

