Name:             hello-world
Version:          1.0.0
Release:          1
Summary:          Introduces the system to the world
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Packager:         %{_packager}
Vendor:           The Experts, Inc.
Source:           %{name}-%{version}-%{release}.tgz
Group:            Other/Other
License:          Other

%description
Let's say a friendly hello to everybody

%prep
%setup -q -n %{name}-%{version}-%{release}

%build

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
install -m 755 /usr/local/bin/hw.sh $RPM_BUILD_ROOT/usr/local/bin/hw.sh

%files
%defattr(-,root,root)
%attr(755, root, root) /usr/local/bin/hw.sh

%changelog
* Wed Oct 12 2017 Achmea DevOps (devopsunix@achmea.nl)
- First installment
