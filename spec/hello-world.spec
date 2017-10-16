Summary: Hello World demo RPM
Name: hello-world
Version: 1.0.0
Release: 1
Vendor: %{_vendor}
Group: Demo/Demo
License: GPL
Source: %{name}-%{version}-%{release}.tgz
Packager: %{_packager}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
%description
Let's say a friendly hello to everybody

%prep
#%setup -q -n %{name}-%{version}-%{release}
%setup -c

%clean
rm -rf $RPM_BUILD_ROOT

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
cp -pr . $RPM_BUILD_ROOT/

%files
%defattr(-,root,root)
%attr(755, root, root) /usr/local/bin/hw.sh

%changelog
* Thu Oct 12 2017 Achmea DevOps (devopsunix@achmea.nl)
- First installment
