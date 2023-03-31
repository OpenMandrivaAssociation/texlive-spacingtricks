Name:		texlive-spacingtricks
Version:	60559
Release:	2
Summary:	Dealing with some spacing issues
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/spacingtricks
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spacingtricks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spacingtricks.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spacingtricks.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides macros for dealing with some spacing
issues, e.g. centering a single line, making a variable strut,
indenting a block, typesetting a compact list, placing two
boxes side by side with vertical adjustment.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/spacingtricks
%{_texmfdistdir}/tex/latex/spacingtricks
%doc %{_texmfdistdir}/doc/latex/spacingtricks

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
