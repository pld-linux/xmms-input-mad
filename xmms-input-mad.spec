Summary:	MP3 input plugin for xmms using MAD library
Summary(pl):	Wtyczka odtwarzaj±ca pliki MP3 dla xmms z u¿yciem bilioteki MAD
Name:		xmms-input-mad
Version:	0.0.9
Release:	5
License:	GPL
Group:		X11/Applications/Sound
Source0:	xmms-mad-%{version}.tar.gz
# Source0-md5:	6f969da20017514c6ebbcf0acd0b84f2
Patch0:		%{name}-no-configure.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	libmad-devel
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmms-mad is an input plugin for xmms that uses libmad to decode MPEG
layer 1/2/3 files and streams. It is not as configurable as mpg123
plugin, however it handles some evil mp3 files better.

%description -l pl
xmms-mad jest wtyczk± wej¶ciow± dla xmms-a u¿ywaj±c± libmad do
dekodowania plików i strumieni MPEG layer 1/2/3. Nie jest ona tak
konfigurowalna jak konkurencja (mpg123), jednak lepiej radzi sobie z
niektórymi uszkodzonymi plikami mp3.

%prep
%setup -q -n xmms-mad-%{version}
%patch0 -p1

%build
rm -f config/missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{xmms_input_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{xmms_input_plugindir}/*
