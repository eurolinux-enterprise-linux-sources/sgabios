%define tardir %{name}-0

Name:           sgabios
Epoch:          1
Version:        0.20110622svn
Release:        4%{?dist}
Summary:        Open-source serial graphics BIOS option rom

Group:          Applications/Emulators
License:        ASL 2.0
URL:            http://code.google.com/p/sgabios/
# Tarball created from SVN archive using the following commands:
# svn export -r 8 http://sgabios.googlecode.com/svn/trunk sgabios-0
# tar -czvf sgabios-0-svnr8.tar.gz sgabios-0
Source0:        sgabios-0-svnr8.tar.gz

ExclusiveArch:  x86_64

Requires: %{name}-bin = %{epoch}:%{version}-%{release}

# Sgabios is noarch, but required on architectures which cannot build it.
# Disable debuginfo because it is of no use to us.
%global debug_package %{nil}

%description
SGABIOS is designed to be inserted into a BIOS as an option rom to provide over
a serial port the display and input capabilities normally handled by a VGA
adapter and a keyboard, and additionally provide hooks for logging displayed
characters for later collection after an operating system boots.

%ifarch %{ix86} x86_64
%package bin
Summary: Sgabios for x86
Buildarch: noarch

%description bin
SGABIOS is designed to be inserted into a BIOS as an option rom to provide over
a serial port the display and input capabilities normally handled by a VGA
adapter and a keyboard, and additionally provide hooks for logging displayed
characters for later collection after an operating system boots.
%endif

%prep
%setup -q -n %{tardir}

%build
unset MAKEFLAGS
%ifarch %{ix86} x86_64
export CFLAGS="$RPM_OPT_FLAGS"
make
%endif


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/sgabios
%ifarch %{ix86} x86_64
install -m 0644 sgabios.bin $RPM_BUILD_ROOT%{_datadir}/sgabios
%endif


%files
%doc COPYING design.txt

%ifarch %{ix86} x86_64
%files bin
%dir %{_datadir}/sgabios/
%{_datadir}/sgabios/sgabios.bin
%endif


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:0.20110622svn-4
- Mass rebuild 2013-12-27

* Wed Oct 17 2012 Cole Robinson <crobinso@redhat.com> - 1:0.20110622svn-2
- Fix deps with epoch bump

* Tue Oct 15 2012 Paolo Bonzini <pbonzini@redhat.com> - 1:0.20110622svn-1
- Move date from release to version (requires epoch bump).

* Sun Aug 12 2012 Richard W.M. Jones <rjones@redhat.com> - 0-1.1.20110622svn
- Fix date in release string.
  NB: To make this version > than the previous, I had to use 1.1.20110622
  instead of 0.1.20110622, since the old second field was 20110623.
- Unset MAKEFLAGS, since parallel make breaks the build.
- Bring the spec file up to modern standards.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.20110623SVN
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.20110622SVN
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Justin M. Forbes <jforbes@redhat.com> 0.0-0.20110621SVN
- Updates per review.

* Tue Jun 21 2011 Justin M. Forbes <jforbes@redhat.com> 0.1-0.20110621SVN
- Created initial package
