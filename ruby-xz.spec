#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	ruby-xz
Summary:	XZ compression via liblzma for Ruby, using FFI
Name:		ruby-xz
Version:	0.2.3
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	6930d427894a786e714b1dcca9addbf1
URL:		http://quintus.github.io/ruby-xz
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-archive-tar-minitar < 1
BuildRequires:	ruby-archive-tar-minitar >= 0.5
%endif
Requires:	xz-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are simple Ruby bindings for the liblzma library, which is best
known for the extreme compression ratio its native XZ format achieves.
Since FFI is used to implement the bindings, no compilation is needed
and they should work with JRuby as well.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/xz.rb
%{ruby_vendorlibdir}/xz
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
