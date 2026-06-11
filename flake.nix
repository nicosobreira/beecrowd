{
  description = "Python 3.11 development environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-25.11";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    utils,
  }:
    utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {inherit system;};
    in {
      devShells.default = pkgs.mkShell {
        nativeBuildInputs = with pkgs; [
          python311

          pyright
          black
        ];

        shellHook = ''
          if [[ ! -d .venv ]]; then
            echo "Creating virtual environment..."
            python -m venv .venv
          fi

          source .venv/bin/activate
        '';
      };
    });
}
