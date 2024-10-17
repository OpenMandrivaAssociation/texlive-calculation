Name:		texlive-calculation
Version:	35973
Release:	2
Summary:	Typesetting reasoned calculations, also called calculational proofs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/calculation
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calculation.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calculation.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calculation.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The calculation environment formats reasoned calculations, also
called calculational proofs. The notion of reasoned
calculations or calculational proofs was originally advocated
by Wim Feijen and Edsger Dijkstra. The package accepts options
fleqn and leqno (with the same effect as the LaTeX options
fleqn and leqno, or may inherit the options from the document
class). It allows steps and expressions to be numbered (by
LaTeX equation numbers, obeying the LaTeX \label command to
refer to these numbers), and a step doesn't take vertical space
if its hint is empty. An expression in a calculation can be
given a comment; it is placed at the side opposite to the
equation numbers. Calculations are allowed inside hints
although numbering and commenting is then disabled.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/calculation
%{_texmfdistdir}/tex/latex/calculation
%doc %{_texmfdistdir}/doc/latex/calculation

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
