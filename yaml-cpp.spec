%define major 0.9
%define libname %mklibname %{name}
%define devname %mklibname %{name} -d

Name:		yaml-cpp
Version:	0.9.0
Release:	1
Summary:	A YAML parser and emitter for C++
Group:		Development/C++
License:	MIT
URL:		https://github.com/jbeder/yaml-cpp
# The tag is yaml-cpp-0.9.0; the lookaside file keeps the short name.
Source0:	https://github.com/jbeder/yaml-cpp/archive/refs/tags/%{name}-%{version}.tar.gz#/%{version}.tar.gz
Source100:	yaml-cpp.rpmlintrc
BuildRequires:	cmake ninja
BuildRequires:	boost-devel
BuildRequires:	gtest-devel

%patchlist
# dropped (no longer applies): yaml-cpp-0.9.0-clang-21.patch

%description
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.

%package -n %{libname}
Summary:	A YAML parser and emitter for C++
Group:		System/Libraries
License:	MIT
Obsoletes:	%{name} < 0.3.0
# The ELF generator only provides the real SONAME, libyaml-cpp.so.0.9.
# Unrebuilt binaries still require the 0.8 name; %%install ships that symlink.
%if "%{_lib}" == "lib64"
Provides:	libyaml-cpp.so.0.8()(64bit)
%else
Provides:	libyaml-cpp.so.0.8
%endif

%description	-n %{libname}
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
License:	MIT
Obsoletes:	%{name}-devel < 0.3.0
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{EVRD}

%description	-n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n yaml-cpp-yaml-cpp-0.9.0

%build
# ask cmake to not strip binaries
%cmake \
	-DYAML_CPP_BUILD_TESTS=OFF \
	-DYAML_CPP_BUILD_TOOLS=OFF \
	-DYAML_BUILD_SHARED_LIBS=ON \
	-DBUILD_GMOCK:BOOL=OFF \
	-DBUILD_GTEST:BOOL=OFF \
	-G Ninja

%ninja_build

%install
%ninja_install -C build
# Binaries built against 0.8 record SONAME libyaml-cpp.so.0.8.
ln -s libyaml-cpp.so.0.9 %{buildroot}%{_libdir}/libyaml-cpp.so.0.8

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/libyaml-cpp.so.0.8

%files -n %{devname}
%{_includedir}/yaml-cpp/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/yaml-cpp/
