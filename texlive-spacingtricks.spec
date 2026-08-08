%global tl_name spacingtricks
%global tl_revision 79865

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9
Release:	%{tl_revision}.1
Summary:	Addressing various spacing issues
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/spacingtricks
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spacingtricks.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spacingtricks.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spacingtricks.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides macros for addressing various spacing issues,
including: centering a single line creating a variable strut indenting a
block typesetting a compact list placing two boxes side by side with
vertical adjustment

