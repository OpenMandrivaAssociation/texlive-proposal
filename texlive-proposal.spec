# revision 29174
# category Package
# catalog-ctan /macros/latex/contrib/proposal
# catalog-date 2013-02-19 13:34:37 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-proposal
Version:	20130219
Release:	8
Summary:	A class for preparing proposals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/proposal
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proposal.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proposal.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proposal.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The process of preparing a collaborative proposal, to a major
funding body, involves integration of contributions of a many
people at many sites. It is therefore an ideal application for
a text-based document preparation system such as LaTeX, in
concert with a distributed version control system such as SVN.
The proposal class itself provides a basis for such an
enterprise. The dfgproposal and dfgproposal classes provide two
specialisations of the base class for (respectively) German and
European research proposals. The packages depend on the
author's stex bundle.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/proposal/base/pdata.sty
%{_texmfdistdir}/tex/latex/proposal/base/proposal.cls
%{_texmfdistdir}/tex/latex/proposal/base/reporting.cls
%{_texmfdistdir}/tex/latex/proposal/dfg/dfgpdata.sty
%{_texmfdistdir}/tex/latex/proposal/dfg/dfgproposal.cls
%{_texmfdistdir}/tex/latex/proposal/dfg/dfgreporting.cls
%{_texmfdistdir}/tex/latex/proposal/eu/eupdata.sty
%{_texmfdistdir}/tex/latex/proposal/eu/euproposal.cls
%{_texmfdistdir}/tex/latex/proposal/eu/eureporting.cls
%doc %{_texmfdistdir}/doc/latex/proposal/README
%doc %{_texmfdistdir}/doc/latex/proposal/base/README
%doc %{_texmfdistdir}/doc/latex/proposal/base/proposal.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/dfg/README
%doc %{_texmfdistdir}/doc/latex/proposal/dfg/dfgproposal.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/eu/README
%doc %{_texmfdistdir}/doc/latex/proposal/eu/euproposal.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/examples/Makefile
%doc %{_texmfdistdir}/doc/latex/proposal/examples/README
%doc %{_texmfdistdir}/doc/latex/proposal/examples/dfgdocs/1_02.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/examples/dfgdocs/1_02e.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/examples/dfgdocs/2_01.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/examples/dfgdocs/2_010.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/examples/dfgdocs/2_012e.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/examples/dfgdocs/54_01_de.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/examples/dfgdocs/54_01_en.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/Makefile
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/README
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/breakthrough.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/impact.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/implementation.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/methodology.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/novelty.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/propB-blx.bib
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/propB.bbl
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/propB.deliverables
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/propB.delivs
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/propB.pdata
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/propB.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/propB.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/propB1-blx.bbl
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/propB2-blx.bbl
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/propB3-blx.bbl
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/propB4-blx.bbl
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/quality.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/fetopenstrep/workplan.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/lib/WApersons.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/lib/dummy.bib
%doc %{_texmfdistdir}/doc/latex/proposal/examples/lib/jacobs-logo.png
%doc %{_texmfdistdir}/doc/latex/proposal/examples/proposal/Makefile
%doc %{_texmfdistdir}/doc/latex/proposal/examples/proposal/funds.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/proposal/preconditions.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/proposal/proposal-blx.bib
%doc %{_texmfdistdir}/doc/latex/proposal/examples/proposal/proposal.pdata
%doc %{_texmfdistdir}/doc/latex/proposal/examples/proposal/proposal.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/examples/proposal/proposal.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/proposal/state.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/proposal/workplan.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/proposal/zusammenfassung.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/report/Makefile
%doc %{_texmfdistdir}/doc/latex/proposal/examples/report/README
%doc %{_texmfdistdir}/doc/latex/proposal/examples/report/finalreport-blx.bib
%doc %{_texmfdistdir}/doc/latex/proposal/examples/report/finalreport.bbl
%doc %{_texmfdistdir}/doc/latex/proposal/examples/report/finalreport.pdata
%doc %{_texmfdistdir}/doc/latex/proposal/examples/report/finalreport.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/examples/report/finalreport.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/report/letter_submission.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/examples/report/letter_submission.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/report/progressreport.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/report/progresssummary.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/simple-proposal/Makefile
%doc %{_texmfdistdir}/doc/latex/proposal/examples/simple-proposal/README
%doc %{_texmfdistdir}/doc/latex/proposal/examples/simple-proposal/jacobs-logo.png
%doc %{_texmfdistdir}/doc/latex/proposal/examples/simple-proposal/letter_submission.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/examples/simple-proposal/letter_submission.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/simple-proposal/preconditions.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/simple-proposal/proposal-blx.bib
%doc %{_texmfdistdir}/doc/latex/proposal/examples/simple-proposal/proposal.bbl
%doc %{_texmfdistdir}/doc/latex/proposal/examples/simple-proposal/proposal.pdata
%doc %{_texmfdistdir}/doc/latex/proposal/examples/simple-proposal/proposal.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/examples/simple-proposal/proposal.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/simple-proposal/proposal1-blx.bbl
%doc %{_texmfdistdir}/doc/latex/proposal/examples/simple-proposal/workplan.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/Makefile
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/README
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/deliverables.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/impact.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/implementation.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/issues.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/methodology.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/milestones.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/objectives.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/progress.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/propB-blx.bib
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/propB.bbl
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/propB.deliverables
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/propB.delivs
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/propB.pdata
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/propB.pdf
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/propB.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/propB1-blx.bbl
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/propB2-blx.bbl
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/propB3-blx.bbl
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/propB4-blx.bbl
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/quality.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/risks.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/site-bar.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/site-baz.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/site-efo.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/site-jacu.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/site-templatex.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/workplan.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/wp-class.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/wp-dissem.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/wp-management.tex
%doc %{_texmfdistdir}/doc/latex/proposal/examples/strep/wp-temple.tex
#- source
%doc %{_texmfdistdir}/source/latex/proposal/base/proposal.dtx
%doc %{_texmfdistdir}/source/latex/proposal/base/proposal.ins
%doc %{_texmfdistdir}/source/latex/proposal/dfg/dfgproposal.dtx
%doc %{_texmfdistdir}/source/latex/proposal/dfg/dfgproposal.ins
%doc %{_texmfdistdir}/source/latex/proposal/eu/euproposal.dtx
%doc %{_texmfdistdir}/source/latex/proposal/eu/euproposal.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
