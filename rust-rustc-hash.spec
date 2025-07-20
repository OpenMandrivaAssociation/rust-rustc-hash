# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_without check
%global debug_package %{nil}

%global crate rustc-hash

Name:           rust-rustc-hash
Version:        2.1.1
Release:        1
Summary:        Speedy, non-cryptographic hashing algorithm used by rustc
Group:          Development/Rust

License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/rustc-hash
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A speedy, non-cryptographic hashing algorithm used by rustc.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(rustc-hash) = 2.1.1
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CODE_OF_CONDUCT.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(rustc-hash/default) = 2.1.1
Requires:       cargo
Requires:       crate(rustc-hash) = 2.1.1
Requires:       crate(rustc-hash/std) = 2.1.1

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(rustc-hash/nightly) = 2.1.1
Requires:       cargo
Requires:       crate(rustc-hash) = 2.1.1

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rand-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(rustc-hash/rand) = 2.1.1
Requires:       (crate(rand/default) >= 0.8.0 with crate(rand/default) < 0.9.0~)
Requires:       cargo
Requires:       crate(rustc-hash) = 2.1.1
Requires:       crate(rustc-hash/std) = 2.1.1

%description -n %{name}+rand-devel %{_description}

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%files       -n %{name}+rand-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(rustc-hash/std) = 2.1.1
Requires:       cargo
Requires:       crate(rustc-hash) = 2.1.1

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
