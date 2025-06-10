{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "jglossator-env";

  buildInputs = [
    pkgs.python313
    pkgs.python313Packages.pyqt6
  ];

  shellHook = ''
    echo "Environment ready for JGlossator"
    echo "Run the application with: python app_dictionary.py"
  '';
}
