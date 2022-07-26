%define major 0.6
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Name:		yaml-cpp
Version:	0.7.0
Release:	1
Summary:	A YAML parser and emitter for C++
Group:		Development/C++
License:	MIT
URL:		https://github.com/jbeder/yaml-cpp
Source0:	https://github.com/jbeder/yaml-cpp/archive/%{name}-%{version}.tar.gz
Source100:	yaml-cpp.rpmlintrc
BuildRequires:	cmake ninja
BuildRequires:	boost-devel
BuildRequires:	gtest-devel

%description
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.

%package -n %{libname}
Summary:	A YAML parser and emitter for C++
Group:		System/Libraries
License:	MIT
Obsoletes:	%{name} < 0.3.0

%description	-n %{libname}
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.

%package -n %{devname}
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
%autosetup -p1 -n %{name}-%{name}-%{version}

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

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/yaml-cpp/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/yaml-cpp
