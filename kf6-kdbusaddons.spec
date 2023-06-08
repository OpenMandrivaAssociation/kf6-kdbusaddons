%define libname %mklibname KF6DBusAddons
%define devname %mklibname KF6DBusAddons -d
%define git 20230608

Name: kf6-kdbusaddons
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kdbusaddons/-/archive/master/kdbusaddons-master.tar.bz2#/kdbusaddons-%{git}.tar.bz2
Summary: Qt addon library with a collection of D-Bus utilities
URL: https://invent.kde.org/frameworks/kdbusaddons
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
Requires: %{libname} = %{EVRD}

%description
Qt addon library with a collection of D-Bus utilities

%package -n %{libname}
Summary: Qt addon library with a collection of D-Bus utilities
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Qt addon library with a collection of D-Bus utilities

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Qt addon library with a collection of D-Bus utilities

%prep
%autosetup -p1 -n kdbusaddons-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_bindir}/kquitapp6
%{_datadir}/qlogging-categories6/kdbusaddons.*

%files -n %{devname}
%{_includedir}/KF6/KDBusAddons
%{_libdir}/cmake/KF6DBusAddons
%{_qtdir}/mkspecs/modules/qt_KDBusAddons.pri
%{_qtdir}/doc/KF6DBusAddons.*

%files -n %{libname}
%{_libdir}/libKF6DBusAddons.so*
