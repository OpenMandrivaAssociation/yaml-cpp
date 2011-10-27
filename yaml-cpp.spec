Name:		yaml-cpp
Version:	0.2.7
Release:	%mkrel 2
Summary:	A YAML parser and emitter for C++
Group:		Development/C++ 
License:	MIT 
URL:		http://code.google.com/p/yaml-cpp/
Source0:	http://yaml-cpp.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:	cmake

%description
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.


%package	devel
Summary:	Development files for %{name}
Group:		Development/C++
License:	MIT
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q 
# Fix eol 
sed -i 's/\r//' license.txt

%build
# ask cmake to not strip binaries
%cmake -DYAML_CPP_BUILD_TOOLS=0
%make VERBOSE=1

%install
rm -rf %{buildroot}

cd build/
%makeinstall DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%clean
rm -rf % {buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc license.txt
%{_libdir}/*.so.*


%files devel
%defattr(-,root,root,-)
%{_includedir}/yaml-cpp/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
