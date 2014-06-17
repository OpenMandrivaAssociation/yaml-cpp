%define major 0.5
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Name:		yaml-cpp
Version:	0.5.1
Release:	1
Summary:	A YAML parser and emitter for C++
Group:		Development/C++
License:	MIT
URL:		http://code.google.com/p/yaml-cpp/
Source0:	http://yaml-cpp.googlecode.com/files/%{name}-%{version}.tar.gz
Source100:	yaml-cpp.rpmlintrc
BuildRequires:	cmake
BuildRequires:	boost-devel

%description
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.

%package	-n %{libname}
Summary:	A YAML parser and emitter for C++
Group:		System/Libraries
License:	MIT
Obsoletes:	%{name} < 0.3.0

%description	-n %{libname}
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.

%package	-n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
License:	MIT
Obsoletes:	%{name}-devel < 0.3.0
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description	-n %{devname}
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
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/yaml-cpp/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu Oct 27 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.2.7-2mdv2012.0
+ Revision: 707635
- added macroses insteed of build scripts

* Thu Oct 27 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.2.7-1
+ Revision: 707561
- imported package yaml-cpp

