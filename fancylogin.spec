Summary:	Themeable login program for Linux
Summary(pl.UTF-8):	Udziwniony program login dla Linuksa
Name:		fancylogin
Version:	0.99.7
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://fancylogin.sourceforge.net/data/%{name}-%{version}.tar.gz
# Source0-md5:	3d2810451e7936fb8c02eed0be53a12b
Patch0:		%{name}-DESTDIR.patch
URL:		http://fancylogin.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fancylogin is one of the most powerful login programs available for
Linux. fancylogin can do everything your old login program can do,
e.g. handling shadowed passwd files, user-time-terminal/
network-verification as done with HP-UX login, etc. It adds a lot of
capabilities for logging logins and support for themes to control the
login's look.

%description -l pl.UTF-8
fancylogin jest jednym z wielu potężnych programów typu login
dostępnych dla Linuksa. Może wszystko co twój stary program login, to
znaczy obsługuje pliki shadow, sprawdzanie użytkownika, terminala i
czasu. Dodaje też kilka innych możliwości dla logowania logowań oraz
udostępnia motywy do kontrolowania wyglądu loginu.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/bin,/sbin,%{_bindir},%{_mandir}/man1}

%{__make} install sampleconf \
	DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/compiling.html doc/configuration.html doc/credits.html doc/docbook.css doc/faq.html doc/index.html doc/license.html doc/obtaining.html doc/stylesheet-images/caution.gif doc/stylesheet-images/home.gif doc/stylesheet-images/important.gif doc/stylesheet-images/next.gif doc/stylesheet-images/note.gif doc/stylesheet-images/prev.gif doc/stylesheet-images/tip.gif doc/stylesheet-images/toc-blank.gif doc/stylesheet-images/toc-minus.gif doc/stylesheet-images/toc-plus.gif doc/stylesheet-images/up.gif doc/stylesheet-images/warning.gif
%attr(755,root,root) /bin/fancylogin
%attr(755,root,root) /sbin/mingetty.fancylogin
%{_sysconfdir}/default.flt
%{_mandir}/man1/fancylogin.1*

%clean
rm -rf $RPM_BUILD_ROOT
