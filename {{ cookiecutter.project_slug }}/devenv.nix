{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/packages/
  packages = [ 
    pkgs.git
    pkgs.gum
  ];

  {% if cookiecutter.python == 'y' %}
  languages.python = {
    enable = true;
    package = pkgs.python312;
    uv = {
      enable = true;
      sync.enable = true;
    };
    venv.enable = true;
  };
  {% endif %}
}
