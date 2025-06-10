{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "python-env";

  buildInputs = [
    pkgs.python313
    pkgs.python313Packages.pyperclip
  ];

  shellHook = ''
  '';
}
