%global tl_name calculation
%global tl_revision 35973

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Typesetting reasoned calculations, also called calculational proofs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/calculation
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/calculation.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/calculation.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/calculation.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The calculation environment formats reasoned calculations, also called
calculational proofs. The notion of reasoned calculations or
calculational proofs was originally advocated by Wim Feijen and Edsger
Dijkstra. The package accepts options fleqn and leqno (with the same
effect as the LaTeX options fleqn and leqno, or may inherit the options
from the document class). It allows steps and expressions to be numbered
(by LaTeX equation numbers, obeying the LaTeX \label command to refer to
these numbers), and a step doesn't take vertical space if its hint is
empty. An expression in a calculation can be given a comment; it is
placed at the side opposite to the equation numbers. Calculations are
allowed inside hints although numbering and commenting is then disabled.

