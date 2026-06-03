{
  description = "Python 3.11 development environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-23.11";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    utils,
  }:
    utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {
        inherit system;
        # Allow unfree packages if proprietary drivers/libraries is needed
        config.allowUnfree = true;
      };

      pythonEnv = pkgs.python311;

      pythonPackages = pythonEnv.withPackages (ps:
        with ps; [
          pip
          virtualenv
          setuptools
          wheel
        ]);
    in {
      devShells.default = pkgs.mkShell {
        name = "python311-env";

        nativeBuildInputs = with pkgs; [
          pyright
          black
          git
        ];

        buildInputs = with pkgs; [
          pythonPackages

          # Common native dependencies for building Python C-extensions
          stdenv.cc.cc
          zlib
          libffi
          openssl
        ];

        shellHook = ''
          # Fixes issues with dynamic libraries on Linux
          # export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib:$LD_LIBRARY_PATH"

          # Create a virtual environment automatically if it doesn't exist
          if [[ ! -d .venv ]]; then
            echo "Creating virtual environment..."
            python -m venv .venv
          fi

          # Activate the virtual environment
          source .venv/bin/activate
        '';
      };
    });
}
