%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-mesh-controller
Version:        1.0.0
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS mesh_controller package

License:        BSD-3
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-dynamic-reconfigure
Requires:       ros-noetic-mbf-mesh-core
Requires:       ros-noetic-mbf-msgs
Requires:       ros-noetic-mbf-utility
Requires:       ros-noetic-mesh-map
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-tf2-geometry-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-dynamic-reconfigure
BuildRequires:  ros-noetic-mbf-mesh-core
BuildRequires:  ros-noetic-mbf-msgs
BuildRequires:  ros-noetic-mbf-utility
BuildRequires:  ros-noetic-mesh-map
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-tf2-geometry-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The mesh_controller package

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Sat Jan 02 2021 Sebastian Pütz <spuetz@uos.de> - 1.0.0-2
- Autogenerated by Bloom

* Sun Dec 20 2020 Sebastian Pütz <spuetz@uos.de> - 1.0.0-1
- Autogenerated by Bloom

